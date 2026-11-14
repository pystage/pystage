### Usage
`pytest` in the root directory runs all tests. No window is opened.

`tests/tests/test_convert.py` converts all Scratch projects in `src/scratch_projects`, compares the code
with the expected results in `src/correct_results` and plays each converted project for a few seconds.

To add a project, put the sb3 file into a folder in `src/scratch_projects` and generate the expected result:

`python generate.py -a` (in this directory) converts all Scratch files into .py files.

`python generate.py -s` lets you select a single file, `python generate.py -f <folder>/<file>.sb3` converts
a single file directly.

After an intended change of the converter, generate all results and review the diff before you commit.
