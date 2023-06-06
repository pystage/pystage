# 256 colors, id from 0 to 255
# FG: \u001b[38;5;${ID}m
# BG: \u001b[48;5;${ID}m


import inspect


class FG:
    BLACK = "\u001b[30m"
    RED = "\u001b[31m"
    GREEN = "\u001b[32m"
    YELLOW = "\u001b[33m"
    BLUE = "\u001b[34m"
    MAGENTA = "\u001b[35m"
    CYAN = "\u001b[36m"
    WHITE = "\u001b[37m"

    BRIGHT_BLACK = "\u001b[30;1m"
    BRIGHT_RED = "\u001b[31;1m"
    BRIGHT_GREEN = "\u001b[32;1m"
    BRIGHT_YELLOW = "\u001b[33;1m"
    BRIGHT_BLUE = "\u001b[34;1m"
    BRIGHT_MAGENTA = "\u001b[35;1m"
    BRIGHT_CYAN = "\u001b[36;1m"
    BRIGHT_WHITE = "\u001b[37;1m"

    RESET = "\u001b[0m"


class BG:
    BLACK = "\u001b[40m"
    RED = "\u001b[41m"
    GREEN = "\u001b[42m"
    YELLOW = "\u001b[43m"
    BLUE = "\u001b[44m"
    MAGENTA = "\u001b[45m"
    CYAN = "\u001b[46m"
    WHITE = "\u001b[47m"

    BRIGHT_BLACK = "\u001b[40;1m"
    BRIGHT_RED = "\u001b[41;1m"
    BRIGHT_GREEN = "\u001b[42;1m"
    BRIGHT_YELLOW = "\u001b[43;1m"
    BRIGHT_BLUE = "\u001b[44;1m"
    BRIGHT_MAGENTA = "\u001b[45;1m"
    BRIGHT_CYAN = "\u001b[46;1m"
    BRIGHT_WHITE = "\u001b[47;1m"

    RESET = "\u001b[0m"


class Style:
    BOLD = "\u001b[1m"
    UNDERLINE = "\u001b[4m"


def __print(*args):
    func_name = inspect.currentframe().f_back.f_code.co_name
    print(getattr(FG, func_name.upper()), *args, BG.RESET)


def red(*args): __print(*args)
def green(*args): __print(*args)
def yellow(*args): __print(*args)
def blue(*args): __print(*args)
def magenta(*args): __print(*args)
def cyan(*args): __print(*args)
def white(*args): __print(*args)
def black(*args): __print(*args)
