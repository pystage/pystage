# PyStage Documentation

## How to

This documentation is generated with Sphinx (install it with pip e.g.).

The ```source``` directory contains the raw files for the documentation. Out of these files we can build
the documentation in html, pdf etc.

1. To generate the source files run from within this directory:

```sphinx-apidoc -f -o source ../src/pystage/ ```

2. Afterwards generate the html docu by running:

```make html```