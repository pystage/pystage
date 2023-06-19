import sys
from pathlib import Path

path = Path(__file__).resolve().parent.parent / "src"
sys.path.insert(0, path.as_posix())
