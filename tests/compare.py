import sys
from diff import Diff
from pathlib import Path
from generate import Converter, to_filename
import shutil
from colored import fg, bg, attr, stylize
import pytest

def valid_file(file: str):
    BASE = Path(__file__).parent / "src"
    source = BASE / "scratch_projects"
    target = source / file
    return target.is_file() and target.suffix == ".sb3"

def compare(fn: str):
    BASE = Path(__file__).parent / "src"
    source = BASE / "scratch_projects"
    target = BASE / "correct_results"

    results, files = [], []

    f = source / fn
    proj_name = to_filename(f.stem)
    dest = (target / f.parent.stem / proj_name / proj_name).with_suffix(".py").as_posix()
    
    print(f"{fg('green')}Comparing {f.as_posix()}{attr('reset')}")
    code = Converter.get_py_code(f.as_posix())
    
    result = Diff(dest, code).compare(True)
    results.append(result)
    files.append(f.as_posix())

    total = len(results)
    passed = len([r for r in results if r])
    failed = total - passed
    
    line = "=" * shutil.get_terminal_size().columns
    print(f"\n\n{line}")
    print(stylize(f"Total Files: {total}", styles=[fg("blue"), attr("bold")]))
    print(stylize(f"Passed Files: {passed}", styles=[fg("green"), attr("bold")]))
    print(stylize(f"Failed Files: {failed}", styles=[fg("red"), attr("bold")]))

    return all(results)

if __name__ == "__main__":
    if valid_file(sys.argv[-1]):
        compare(sys.argv[-1])
    else:
        print(stylize("Invalid file path", styles=[fg("red"), attr("bold")]))


