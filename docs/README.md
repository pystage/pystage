# PyStage Documentation

## How to

This documentation is generated with Sphinx (install it with pip e.g.).

The ```source``` directory contains the raw files for the documentation. Out of these files we can build
the documentation in html, pdf etc.

1. To generate the source files run from within this directory:

```sphinx-apidoc -f -o source ../src/pystage/ -t source/_templates -E```
  * ```-t```: The path to the templates directory (optional)
  * ```-E```: Exclude submodule headings (optional)

2. Afterwards generate the html docu by running:

```make html```


## Include images

Images can be included using restructured Text:

```.. figure:: _static/image.png```

It is also possible to put the image directly in a function documentation. Therefore, put 
the image directly in the docstring of the function. Make sure to have a blank line above and below 
of the reST element. The path to the image must be relative to the place of the docstring.