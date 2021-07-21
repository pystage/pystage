# PyStage

[![Documentation Status](https://readthedocs.org/projects/pystage/badge/?version=latest)](https://pystage.readthedocs.io/en/latest/?badge=latest)

Scratch-like Python programming.

PyStage bridges the gap between [Scratch](https://scratch.mit.edu/) and Python. This module implements all code blocks
as available in scratch. With the PyStage command line converter Scratch projects can be easily
transferred to Python executable Code. To run your game in Python, PyStage uses [PyGame](https://www.pygame.org/news).

![test](docs/pystage.png)

## Goals
* Export your Scratch project to real executable Python code!
* Helping coding beginners to learn Python "by Scratch".
* Implementation of scratch blocks in several languages (ideal for kids). As of now en and de.

# Installation
```pip install pystage```

---
**NOTE**

Please note this is a pre alpha version. Not all things may work as expected. If so, please contact us or open an issue.
Also, not all blocks are documented in a suitable manner.

---

# Usage
Converting a Scratch project to Python code:
1. Export your Scratch project on the Scratch page. You will get an .sb3 file.
2. Use the PyStage converter script (src/pystage/sb3.py). Yes, it's unhandy, we will work on it to make things easier.

The base usage is ```python -m pystage.convert.sb3 <SB3 File> -l en -d <DIRECTORY>```
The parameters are:
* ```-l``` language of generated python "scratch blocks". In the moment of writing, ```en``` and ```de``` are available.
* ```-d``` the output directory, defaults to current directory
* ```-i``` print intermediate code representation
* ```-s``` print sb3 project.json
* ```-p``` print python code
* ```-v``` verbose
* ```-vv``` debug mode


# Contributors

Special thanks to
* Kai Eckert
* Florian Rupp
