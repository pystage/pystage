import json
import sys
from pathlib import Path
import zipfile

try:
    path = Path(__file__).resolve().parent.parent / "src"
    sys.path.insert(0, path.as_posix())

    from pystage.convert.sb3 import get_intermediate, get_python, to_filename
    import chalk
except ImportError as e:
    print("Import Error")
    print(e)


class Converter:
    def __init__(self, path: str, dest: str, language: str = "en"):
        self.path = path
        self.dest = dest
        self.language = language

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
            chalk.red(f"Failed to convert {self.path}")
            chalk.red(e)

    def __convert(self):
        archive = zipfile.ZipFile(self.path, 'r')
        with archive.open("project.json") as f:
            project_name = to_filename(Path(self.path).stem)
            data = json.loads(f.read())
            project = get_intermediate(data, project_name)
            # print(f"Creating project: {project_name}")
            dp = Path(self.dest) / project_name
            print(f"Exporting to: {dp}")
            self.delete_directory(dp)
            # print(f"Creating directory: {dp}")
            dp.mkdir(parents=True)
            self.write_json(dp / "project.json", data)
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


BASE: Path = Path(__file__).resolve().parent.parent


def convert():
    source = BASE / "scratch_files"
    target = BASE / "generated_files"
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

if __name__ == "__main__":
    convert()
