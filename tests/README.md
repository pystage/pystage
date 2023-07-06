### Usage
Download scratch files for test into `src/scratch_projects`, and run `python generate.py -a` to convert all the scratch files into .py files.

`python generate.py -s` to select and convert a single file, and this will print out the path of sb3 file.
E.g. Converting "tests/show var.sb3"

You can copy this path and run `python generate.py -f <path>` to convert a single file.

Go to root directory, `pytest` to run all tests which will compare the output of the scratch file and the output of the generated .py file.
