import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict

import jinja2
import requests
import yaml


def get_repo_stats(repo_url: str) -> Dict:
    """Get repository statistics from GitHub API"""
    if not repo_url.startswith('https://github.com/'):
        return {'stars': 0, 'forks': 0, 'last_commit': 'N/A', 'active': 'N/A'}

    try:
        # Extract owner and repo from URL, handling various formats
        parts = repo_url.rstrip('/').split('/')
        if len(parts) > 5:  # Handle deep paths like tree/master/etc
            owner = parts[3]
            repo = parts[4]
        else:
            owner = parts[-2]
            repo = parts[-1]

        api_url = f"https://api.github.com/repos/{owner}/{repo}"
        headers = {
            'Accept': 'application/vnd.github.v3+json',
            'Authorization': f"token {os.getenv('GITHUB_TOKEN')}" if os.getenv('GITHUB_TOKEN') else ''
        }

        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            data = response.json()

            # Get last commit date
            last_commit = data.get('pushed_at')
            if last_commit:
                last_commit_date = datetime.strptime(last_commit, '%Y-%m-%dT%H:%M:%SZ')
                months_since_commit = (datetime.now(timezone.utc) - last_commit_date.replace(
                    tzinfo=timezone.utc)).days / 30
                # Consider a repo active if it was updated in the last 12 months
                active = "Yes" if months_since_commit < 12 else "No"
            else:
                active = "Unknown"

            return {
                'stars': int(data.get('stargazers_count', 0)),
                'forks': int(data.get('forks_count', 0)),
                'last_commit': last_commit,
                'active': active
            }
    except Exception as e:
        print(f"Error fetching stats for {repo_url}: {e}")

    return {'stars': 0, 'forks': 0, 'last_commit': 'N/A', 'active': 'N/A'}

def generate_readme():
    """Generate README.md from template and YAML data"""
    script_dir = Path(__file__).parent
    parent_dir = script_dir.parent  # Get parent directory
    
    # Load template engines data
    yaml_path = script_dir / 'template-engines.yaml'
    with open(yaml_path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
        template_engines = data['template_engines']

    # Calculate statistics
    total_engines = sum(len(engines) for engines in template_engines.values())
    total_languages = len(template_engines)

    # Create Jinja environment
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(script_dir),
        trim_blocks=True,
        lstrip_blocks=True,
        autoescape=True
    )

    # Add custom filters if needed
    env.filters['int'] = lambda x: int(x) if str(x).isdigit() else 0

    # Load and render template
    template = env.get_template('README.md.jinja')
    readme_content = template.render(
        template_engines=template_engines,
        get_repo_stats=get_repo_stats,
        current_date=datetime.now().strftime('%Y-%m-%d'),
        total_engines=total_engines,
        total_languages=total_languages
    )
    
    # Write to README.md in parent directory
    readme_path = parent_dir / 'README.md'
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(readme_content)

    print(f"Successfully generated {readme_path}")
    print(f"Total template engines: {total_engines}")
    print(f"Total languages: {total_languages}")

if __name__ == "__main__":
    generate_readme()
