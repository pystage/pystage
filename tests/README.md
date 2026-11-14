### Usage
`pytest` in the root directory runs all tests. No window is opened.

`tests/tests/test_convert.py` converts all Scratch projects in `src/scratch_projects`, compares the code
with the expected results in `src/correct_results` and plays each converted project for a few seconds.

To add a project, put the sb3 file into a folder in `src/scratch_projects` and generate the expected result:

`python generate.py -a` (in this directory) converts all Scratch files into .py files.

`python generate.py -s` lets you select a single file, `python generate.py -f <folder>/<file>.sb3` converts
a single file directly.

After an intended change of the converter, generate all results and review the diff before you commit.

### Generated projects

Projects cannot be created with Scratch automatically, so `make_projects.py` writes minimal but valid sb3 files
(project.json structured like Scratch 3 saves it, a tiny PNG per costume, a tiny WAV per sound) for the blocks
that no real test project uses: pen, timer, stage scripts, custom blocks, lists and monitors and so on.

`python make_projects.py` (in this directory) writes them into `src/scratch_projects/generated`, which
`test_convert.py` picks up like any other category, and the project with deliberately unsupported things into
`src/special_projects` (it is tested by `tests/test_convert_warnings.py`). The output is reproducible; a test
fails if the files in the repository differ from what the script writes. Run `python generate.py -a` afterwards.

`tests/test_coverage.py` makes sure that every block the converter supports is used by at least one project.
If you add a block to the library, add it to `make_projects.py` as well, or the test tells you.
