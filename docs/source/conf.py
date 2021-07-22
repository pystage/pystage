# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import shutil
import sys
from tempfile import TemporaryFile
from urllib.request import urlopen
from zipfile import ZipFile
import inspect
from docutils.transforms import Transform
from docutils import nodes

sys.path.insert(0, os.path.abspath("../../src"))


# -- Project information -----------------------------------------------------

project = 'PyStage'
copyright = '2021, The Pystage Developing Team'
author = 'The Pystage Developing Team'

# The full version, including alpha/beta/rc tags
release = '0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon', "sphinx_rtd_theme", "m2r2", "sphinx_panels"]
# 'sphinx.ext.coverage', 'sphinx.ext.napoleon'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# alabaster
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# doing this as example for en
PATH_BLOCK_IMAGES = "/".join(["_static", "images", "blocks"])
LOADED_LANG = []


# download block img
def download_pngs(lang):
    if lang not in LOADED_LANG:
        # first cleanup
        extract_path = "/".join(["source", PATH_BLOCK_IMAGES, lang])
        if os.path.exists(extract_path):
            return
            # shutil.rmtree(extract_path)

        block_img_url = f"http://img.pystage.org/blocks/zip/png/300/{lang}_png300.zip"

        with urlopen(block_img_url) as url:
            print(f"Downloading block imgs for {lang}.")
            html = url.read()

            with TemporaryFile() as tmp:
                tmp.write(html)
                with ZipFile(tmp) as f:
                    f.extractall(extract_path)

                    # rename all files: add lang name in file name to avoid same file names. Sphinx will pack all pngs
                    # in one directory
                    for file in os.listdir(extract_path):
                        try:
                            os.rename("/".join([extract_path, file]), "/".join([extract_path, f"{lang}_{file}"]))
                        except WindowsError as e:
                            continue

        LOADED_LANG.append(lang)


# insert rst block with correct image
def autodoc_process_docstring(app, what, name, obj, options, lines):
    def get_block_png(lang_, opcode_):
        if "readthedocs" in os.getcwd():
            return "/".join(["source", PATH_BLOCK_IMAGES, lang_, f"{lang_}_{opcode_}.png"])
        else:
            # use this path for local build
            return "/".join([PATH_BLOCK_IMAGES, lang_, f"{lang_}_{opcode_}.png"])

    try:
        # only insert blocks for methods
        if what == "method":
            lang = name.split(".")[1]
            if len(lang) == 2:
                download_pngs(lang)

                # get opcode from wrapped function
                opcode = inspect.getsourcelines(obj)[0][-1].strip(" ").split("(")[0].split(".")[-1]
                # opcode = opcode.replace("pystage_", "")
                if "pystage_" in opcode:
                    return lines
                path = get_block_png(lang, opcode)

                # insert rst figure block, care to put in empty lines above and below.
                for i in range(3):
                    lines.insert(1, "")
                lines.insert(4, f".. figure:: {path}")
                lines.insert(5, "    :height: 50")
                for i in range(3):
                    lines.insert(6, "")

                # add warning if png not found. This may have several reasons.
                # if not os.path.exists("/".join(["source", path])) and \
                #         not os.path.exists("/".join(["source", "source", path])):
                #     lines.insert(7, r'Image not found. Maybe function is not yet implemented for this language. '
                #                     r'Also the naming of the block may not the same as the corresponding function.\n If '
                #                     r'this error keeps existing check if this function is really a scratch block.')

    except IndexError:
        return lines

    return lines


def setup(app):
    app.connect('autodoc-process-docstring', autodoc_process_docstring)

