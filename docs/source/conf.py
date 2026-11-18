# Configuration file for the Sphinx documentation builder.
# Full list of options: https://www.sphinx-doc.org/en/master/usage/configuration.html

import configparser
import html
import os
import re
import sys

# autodoc imports pystage, which imports pygame: never open a window or audio device
os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")

_here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(_here, "..", "..", "src")))


# -- Project information -----------------------------------------------------

project = 'PyStage'
copyright = '2021-2026, The Pystage Developing Team'
author = 'The Pystage Developing Team'

# The version is maintained in setup.cfg only
_setup = configparser.ConfigParser()
_setup.read(os.path.join(_here, "..", "..", "setup.cfg"), encoding="utf-8")
release = _setup["metadata"]["version"]
version = ".".join(release.split(".")[:2])


# -- General configuration ---------------------------------------------------

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon', "sphinx_rtd_theme", "m2r2", "sphinx_design"]
templates_path = ['_templates']
exclude_patterns = ["modules.rst"]


# -- Options for HTML output -------------------------------------------------

html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']

# Scratch blocks are rendered in the browser by scratchblocks (vendored in _static/scratchblocks)
html_js_files = [
    "scratchblocks/scratchblocks.min.js",
    "scratchblocks/translations-de.js",
    "scratchblocks/translations-lt.js",
    "scratchblocks/init.js",
]


# -- Scratch block rendering -------------------------------------------------

# Docstring line of the facade methods, English, German or Lithuanian, e.g. "Scratch block: move (10) steps"
BLOCK_LINE = re.compile(r"^\s*Scratch(?: block|-Block| blokas):\s*(.*\S)\s*$")


def block_html_lines(text):
    """The rst lines that show one block as a pre.blocks element for scratchblocks."""
    return [".. raw:: html", "", f'   <pre class="blocks">{html.escape(text, quote=False)}</pre>']


def autodoc_process_docstring(app, what, name, obj, options, lines):
    """Replace the 'Scratch block: ...' line by a raw html element that scratchblocks renders."""
    escape_star_args(lines)
    for i, line in enumerate(lines):
        match = BLOCK_LINE.match(line)
        if match:
            lines[i:i + 1] = block_html_lines(match.group(1)) + [""]
            break


# Docstrings inherited from pygame mention *args, **kwargs, *groups, which docutils reads as emphasis
STAR_ARGS = re.compile(r"(?<![\w\\*])(\*{1,2})(args|kwargs|groups)\b")


def escape_star_args(lines):
    for i, line in enumerate(lines):
        lines[i] = STAR_ARGS.sub(lambda m: "\\" + m.group(1) + m.group(2), line)


def fix_readme_images(app, doctree):
    """README.md refers to docs/pystage.png (valid on GitHub); in the docs the file is one level up."""
    from docutils import nodes
    for node in doctree.findall(nodes.image):
        if node["uri"] == "docs/pystage.png":
            node["uri"] = "../pystage.png"


def setup(app):
    app.connect('autodoc-process-docstring', autodoc_process_docstring)
    app.connect('doctree-read', fix_readme_images, priority=100)
