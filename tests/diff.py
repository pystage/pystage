from colored import fg, attr
import difflib
import os


class Diff:
    def __init__(self, text1: str, text2: str):
        self.text1 = self.process(text1)
        self.text2 = self.process(text2)

    def color_diff(self, line: str):
        if line.startswith('-'):
            return fg('red') + line + attr('reset')
        elif line.startswith('+'):
            return fg('green') + line + attr('reset')
        elif line.startswith('?'):
            return fg('blue') + line + attr('reset')
        else:
            return None

    def compare(self, print_=False):
        text1 = self.text1.splitlines()
        text2 = self.text2.splitlines()
        differ = difflib.Differ()
        diff = differ.compare(text1, text2)

        diff = list(diff)

        if print_:
            for line in diff:
                colored_line = self.color_diff(line)
                colored_line and print(colored_line)
        return not any(line[0] in ('-', '+') for line in diff)

    def process(self, text: str):
        if os.path.exists(text):
            with open(text, 'r', encoding="utf-8") as f:
                return f.read()
        return text


if __name__ == '__main__':
    a = """\
    lyrics

    """
    b = """\
    lyrics

    """
    print(Diff(a, b).compare(True))
