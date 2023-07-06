import json
from pathlib import Path
import zipfile
import argparse
import colored
import curses
import sys

from pystage.convert.sb3 import get_intermediate, get_python, to_filename


"""
Code is very messy now, but it works. I will clean it up later.

Usage is in the README.md file.
"""

class Key1:
    UP = 450
    DOWN = 456
    ENTER = 10
    q = 113
    ESC = 27
    BACKSPACE = 8


class Key2:
    UP = 259
    DOWN = 258
    ENTER = 10
    q = 113
    ESC = 27
    BACKSPACE = 263


def get_files(path, folder=False, ext=None):
    path = Path(path) if not isinstance(path, Path) else path
    if folder:
        return [x for x in path.iterdir() if x.is_dir()]
    if ext is None:
        return [x for x in path.iterdir() if x.is_file()]
    else:
        return [x for x in path.iterdir() if x.is_file() and x.suffix == ext]


def lines(files, cur):
    results = []
    for i, file in enumerate(files):
        if i == cur:
            results.append(f">>> {file.stem}")
        else:
            results.append(f"    {file.stem}")

    return results


class Converter:
    def __init__(self, path: str, dest: str, language: str = "en", show_err: bool = False):
        self.path = path
        self.dest = dest
        self.language = language
        self.show_err = show_err

    def delete_directory(self, path: Path):
        if not path.exists():
            return
        for p in path.iterdir():
            if p.is_dir():
                self.delete_directory(p)
            else:
                p.unlink()
        path.rmdir()

    def write_json(self, path: Path, data):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def convert(self):
        try:
            self.__convert()
        except Exception as e:
            print(colored.stylize(
                f"Failed to convert {self.path}", colored.fg("red")))
            print(colored.stylize(e, colored.fg("red")))
            if self.show_err:
                raise e

    @staticmethod
    def get_py_code(path: str, language: str = "en"):
        archive = zipfile.ZipFile(path, 'r')
        with archive.open("project.json") as f:
            project_name = to_filename(Path(path).stem)
            data = json.loads(f.read())
            project = get_intermediate(data, project_name)
        return get_python(project, language=language)

    def __convert(self):
        archive = zipfile.ZipFile(self.path, 'r')
        with archive.open("project.json") as f:
            project_name = to_filename(Path(self.path).stem)
            data = json.loads(f.read())
            dp = Path(self.dest) / project_name
            print(f"Exporting to: {dp}")
            self.delete_directory(dp)
            dp.mkdir(parents=True)
            self.write_json(dp / "project.json", data)
            project = get_intermediate(data, project_name)
            self.write_json(dp / "project_intermediate.json", project)
            (dp / "images").mkdir(parents=True)
            (dp / "sounds").mkdir(parents=True)
            for key in project["costumes"]:
                c = project["costumes"][key]
                with archive.open(f'{key}.{c["extension"]}') as infile:
                    with open(dp / "images" / f'{c["global_name"]}.{c["extension"]}', "wb") as outfile:
                        outfile.write(infile.read())
            for key in project["sounds"]:
                s = project["sounds"][key]
                with archive.open(f'{key}.{s["extension"]}') as infile:
                    with open(dp / "sounds" / f'{s["global_name"]}.{s["extension"]}', "wb") as outfile:
                        outfile.write(infile.read())
            with open(dp / f'{project_name}.py', "w", encoding="utf-8") as pyfile:
                pyfile.write(get_python(project, language=self.language))


BASE: Path = Path(__file__).resolve().parent / "src"


def convert():
    source = BASE / "scratch_projects"
    target = BASE / "correct_results"
    for file in source.iterdir():
        if file.is_dir():
            for f in file.iterdir():
                if f.is_file() and f.suffix == ".sb3":
                    path = f.as_posix()
                    dest = (target / file.stem).as_posix()
                    converter = Converter(path, dest)
                    converter.convert()
        else:
            print(f"Skipping {file}")
    return True


def main(stdscr):
    ter_height, ter_width = stdscr.getmaxyx()
    column = int(ter_width)//30
    line_len = int(ter_width)//column - 3
    stdscr.nodelay(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLUE)

    files = get_files(BASE / "scratch_projects", folder=True)
    cur = 0
    cur_folder = files[cur]
    cur_file = None
    selecting_folder = True

    while True:
        if selecting_folder:
            cur_folder = files[cur]
        else:
            cur_file = files[cur]
        stdscr.clear()
        stdscr.addstr("q: quit, arrow keys: select, enter: choose, backspace: go back\n")
        for i, line in enumerate(lines(files, cur)):
            line = line[:line_len-3] + "..." if len(line) > line_len else line
            try:
                if i == cur:
                    stdscr.attron(curses.color_pair(1))
                    stdscr.addstr("{:<{}}".format(line, line_len))
                    stdscr.attroff(curses.color_pair(1))
                else:
                    stdscr.addstr("{:<{}}".format(line, line_len))
                if (i+1) % column == 0:
                    stdscr.addstr("\n")
            except curses.error:
                pass

        stdscr.refresh()
        key = stdscr.getch()
        curses.curs_set(0)

        if key in [Key1.UP, Key2.UP]:
            cur = (cur - 1) % len(files)
        elif key in [Key1.DOWN, Key2.DOWN]:
            cur = (cur + 1) % len(files)
        elif key in [Key1.ENTER, Key2.ENTER]:
            if not selecting_folder:
                source = cur_file.as_posix()
                target = (BASE / "correct_results" / cur_folder.stem).as_posix()
                fn = f"\"{cur_file.parent.stem}/{cur_file.stem}{cur_file.suffix}\""
                print("Converting", colored.stylize(fn, colored.fg("green")))
                Converter(source, target).convert()
                break
            files = get_files(cur_folder, ext='.sb3')
            cur = 0
            selecting_folder = False
        elif key in [Key1.BACKSPACE, Key2.BACKSPACE]:
            if not selecting_folder:
                selecting_folder = True
                files = get_files(BASE / "scratch_projects", folder=True)
                cur = files.index(cur_folder)
        elif key in [Key1.q, Key2.q]:
            break


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Convert Scratch 3.0 projects to Python')
    parser.add_argument("-s", "--select", action="store_true")
    parser.add_argument("-a", "--all", action="store_true")
    parser.add_argument("-f", "--file", type=str, help="Path to .sb3 file")
    args = parser.parse_args()

    # python tests\generate.py -s
    if args.select:
        try:
            curses.wrapper(main)
        except KeyboardInterrupt:
            curses.endwin()
            sys.exit(1)
        except Exception as e:
            curses.endwin()
            print(colored.stylize(e.args[0], colored.fg("red")))
            sys.exit(1)
    elif args.file:
        source = BASE / "scratch_projects"
        target = BASE / "correct_results"
        path = source / args.file
        dest = target / Path(args.file).parent
        converter = Converter(path.as_posix(), dest.as_posix(), show_err=True)
        converter.convert()
    elif args.all:
        convert()
    else:
        parser.print_help()
        print(colored.stylize("\nPlease specify -s (select) or -a (all)", [colored.fg("red"), colored.attr("bold")]))
