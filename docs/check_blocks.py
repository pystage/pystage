"""Dump all 'Scratch block:' docstring lines of the en/de facades and check them with scratchblocks.

Usage (needs Node):  python check_blocks.py [--dump blocks.json]

scratchblocks is taken from the directory in SCRATCHBLOCKS_DIR (an unpacked `npm pack scratchblocks@3.7.1`),
or from `npm install` in this directory; if neither exists, it is fetched with `npm pack` into a temp dir.
"""
import ast
import json
import os
import re
import subprocess
import sys
import tarfile
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "src", "pystage")
LINE = re.compile(r"^\s*Scratch(?: block|-Block):\s*(.*\S)\s*$")
LANGS = {"en": "en", "de": "de"}


def collect():
    entries = []
    for lang in LANGS:
        folder = os.path.join(SRC, lang)
        for filename in sorted(os.listdir(folder)):
            if not filename.endswith(".py"):
                continue
            path = os.path.join(folder, filename)
            with open(path, encoding="utf-8") as f:
                tree = ast.parse(f.read())
            for cls in (n for n in ast.walk(tree) if isinstance(n, ast.ClassDef)):
                for func in (n for n in cls.body if isinstance(n, ast.FunctionDef)):
                    doc = ast.get_docstring(func, clean=False)
                    if not doc:
                        continue
                    for offset, line in enumerate(doc.splitlines()):
                        match = LINE.match(line)
                        if match:
                            entries.append({
                                "lang": lang,
                                "file": os.path.relpath(path, os.path.join(HERE, "..")),
                                "line": func.body[0].lineno + offset,
                                "name": f"{cls.name}.{func.name}",
                                "text": match.group(1),
                            })
    return entries


def main():
    entries = collect()
    with tempfile.TemporaryDirectory() as tmp:
        data = os.path.join(tmp, "blocks.json")
        with open(data, "w", encoding="utf-8") as f:
            json.dump(entries, f, ensure_ascii=False, indent=1)
        if "--dump" in sys.argv:
            print(open(data, encoding="utf-8").read())
            return 0
        env = dict(os.environ)
        if "SCRATCHBLOCKS_DIR" not in env and not os.path.isdir(os.path.join(HERE, "node_modules", "scratchblocks")):
            subprocess.run(["npm", "pack", "scratchblocks@3.7.1", "--silent"], cwd=tmp, check=True)
            with tarfile.open(os.path.join(tmp, "scratchblocks-3.7.1.tgz")) as tar:
                tar.extractall(tmp, filter="data")
            env["SCRATCHBLOCKS_DIR"] = os.path.join(tmp, "package")
        return subprocess.run(["node", os.path.join(HERE, "check_blocks.js"), data], env=env, cwd=HERE).returncode


if __name__ == "__main__":
    sys.exit(main())
