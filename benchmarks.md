# Benchmarks

## JavaScript

### [Marko-templating-benchmark](https://github.com/marko-js/templating-benchmarks)
This repo provides a framework for running benchmarks against multiple templating engines under Node.js. The following templating engine are compared:

| Template                                              | Syntax            | Streaming | Asynchronous | Auto-escape |
|-------------------------------------------------------|-------------------|-----------|--------------|-------------|
| [dustjs](https://github.com/linkedin/dustjs)          | Text              | ✔         | ✔            | ✔           |
| [doT](https://github.com/olado/doT)                   | Text              | ✖         | ✖            | ✖           |
| [handlebars](https://github.com/wycats/handlebars.js) | Text              | ✖         | ✖            | ✔           |
| [pug](https://github.com/pugjs/pug)                   | Short-hand HTML   | ✖         | ✖            | ✔           |
| [marko](https://github.com/marko-js/marko)            | HTML/Concise HTML | ✔         | ✔            | ✔           |
| [nunjucks](http://mozilla.github.io/nunjucks/)        | Text              | ✖         | ✔            | ✖           |
| [swig](http://mozilla.github.io/nunjucks/)            | Text              | ✖         | ✖            | ✔           |

### [Node.js template engine](https://github.com/baryshev/template-benchmark)

### [node](https://github.com/paularmstrong/node-templates)
old benchmark

## Go

1. [goTemplateBenchmark](https://github.com/slinso/goTemplateBenchmark)

This repo compares template engines in golang. It includes [Ace](https://github.com/yosssi/ace), [Amber](https://github.com/eknkc/amber), [Mustache.go](https://github.com/hoisie/mustache), [Raymond](https://github.com/aymerick/raymond), [Pongo2](https://github.com/flosch/pongo2), [Jet](https://github.com/CloudyKit/jet), [Soy](https://github.com/robfig/soy).


## Java

### [Java Template Benchmark](https://github.com/mbosecke/template-benchmark)
JMH benchmark

### [](https://github.com/casid/template-benchmark)
forked above 

### [](https://github.com/agentgt/template-benchmark)
Forked Above

## [spring-comparing-template-engines](https://github.com/jreijn/spring-comparing-template-engines)

## [](https://github.com/xmlet/template-benchmark)
forked from [Java Template Benchmark](https://github.com/mbosecke/template-benchmark)

## Rust

### [Rust template benchmark](https://github.com/rosetta-rs/template-benchmarks-rs)

## .Net

### [Fluid vs Liquid implementations](https://github.com/sebastienros/fluid?#benchmarks)
THe benchmark compares time taken for template engines implemented in C#. The template engines include - Fluid, Scriban, DotLiquid, Liquid.NET and Handlebars.NET repository.
Fluid is faster and allocates less memory than these .NET Liquid implementation. Fluid is 19% faster than the second in parsing while Scriban allocates nearly 3 times less memory than second. In rendering, Fluid is 26% faster than the second while Handlebars is 5 times faster than Scriban.

## PHP

### [Twig vs Smarty vs Fenom](https://github.com/fenom-template/benchmark)
[Comparison Details](https://github.com/fenom-template/fenom/blob/master/docs/en/benchmark.md) for three PHP templates engines-Twig, Smarty and Fenom is done.
The comparison templates invlve forEach, variable reference and template inheritance. [Script file](https://github.com/fenom-template/benchmark/blob/master/bin/fenom-benchmark.php) 
