### Usage
Download scratch files for test into `/scratch_files`, and run `generate.py` to convert all the scratch files into .py files.

`python generate.py -f <filename>` to convert a single file.

`pytest tests` to run all tests which will compare the output of the scratch file and the output of the generated .py file.
