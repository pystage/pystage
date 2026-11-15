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


## Scratch blocks

The block images are not files: the facade docstrings in `src/pystage/en` and `src/pystage/de` contain a
line `Scratch block: <scratchblocks syntax>` (German: `Scratch-Block: ...`). The `autodoc-process-docstring`
hook in `source/conf.py` turns it into `<pre class="blocks">`, and the vendored
[scratchblocks](https://scratchblocks.github.io/) 3.7.1 (`source/_static/scratchblocks/`) renders it in the browser
(`init.js` calls `renderMatching`, languages `en` and `de`). Nothing is downloaded during the build.

To check that scratchblocks recognises all block lines of the docstrings (needs Node and, on first use, network
access for `npm pack`; not part of the pytest suite):

```
python check_blocks.py          # lists the lines that scratchblocks does not parse cleanly
python check_blocks.py --dump   # only dump the lines as JSON
```

## Read the Docs

`../.readthedocs.yaml` builds with Python 3.12 and `requirements.txt`. The version is read from `../setup.cfg`.
To build locally in a clean environment: `pip install -r requirements.txt && sphinx-build -W -b html source build/html`.
