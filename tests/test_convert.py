from .diff import Diff
from pathlib import Path
from .generate import Converter, to_filename
from colored import fg, attr

def test_compare():
    BASE = Path(__file__).parent.parent
    source = BASE / "scratch_files"
    target = BASE / "generated_files"

    for file in source.iterdir():
        if file.is_dir():
            for f in file.iterdir():
                if f.is_file() and f.suffix == ".sb3":
                    proj_name = to_filename(f.stem)
                    dest = (target / file.stem / proj_name / proj_name).with_suffix(".py").as_posix()
                    
                    print(f"{fg('green')}Comparing {f.as_posix()}{attr('reset')}")
                    code = Converter.get_py_code(f.as_posix())
                    
                    assert Diff(dest, code).compare(True)
