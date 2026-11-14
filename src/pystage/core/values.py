"""Scratch value semantics.

Scratch has no types: every value is a number, a string or a boolean and is
converted on demand. The helpers here implement these conversions so that
blocks behave like in Scratch when they get "wrong" types, e.g. a text
where a number is expected.
"""
import math


def to_number(value):
    """Convert a value to a number like Scratch does (not a number: 0)."""
    if isinstance(value, bool):
        return int(value)
    if isinstance(value, (int, float)):
        if isinstance(value, float) and math.isnan(value):
            return 0
        return value
    try:
        text = str(value).strip()
        if text == "":
            return 0
        number = float(text)
    except (TypeError, ValueError):
        return 0
    if math.isnan(number):
        return 0
    if number == math.floor(number) and abs(number) < 1e15 and not math.isinf(number):
        return int(number)
    return number


def is_number(value):
    """True if the value is a number or a text that looks like one."""
    if isinstance(value, bool):
        return False
    if isinstance(value, (int, float)):
        return True
    try:
        text = str(value).strip()
        if text == "":
            return False
        float(text)
        return True
    except (TypeError, ValueError):
        return False


def to_string(value):
    """Convert a value to a text like Scratch does."""
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, float):
        if math.isnan(value):
            return "NaN"
        if math.isinf(value):
            return "Infinity" if value > 0 else "-Infinity"
        if value == math.floor(value) and abs(value) < 1e15:
            return str(int(value))
    return str(value)


def equals(a, b):
    """Scratch equality: numeric if both are numbers, else case-insensitive text."""
    if is_number(a) and is_number(b):
        return to_number(a) == to_number(b)
    return to_string(a).lower() == to_string(b).lower()


def compare(a, b):
    """Scratch comparison: negative, zero or positive, like a - b."""
    if is_number(a) and is_number(b):
        a, b = to_number(a), to_number(b)
    else:
        a, b = to_string(a).lower(), to_string(b).lower()
    return (a > b) - (a < b)


class Text(str):
    """A text that comes from Scratch-like sources: variables, lists, answers.

    It is a normal Python string, but it can be used like in Scratch where
    a number is expected:

    - In calculations, it is the number it looks like, 0 otherwise.
      Only adding a normal string appends it, as usual in Python.
    - Comparisons with numbers work. Texts are compared ignoring the case.

    This way, code that was converted from Scratch works without type
    conversions, e.g. if the answer to a question is used as number.
    """
    __slots__ = ()

    def __add__(self, other):
        if isinstance(other, str) and not isinstance(other, Text):
            return str(self) + other
        return to_number(self) + to_number(other)

    def __radd__(self, other):
        if isinstance(other, str):
            return other + str(self)
        return to_number(other) + to_number(self)

    def __sub__(self, other):
        return to_number(self) - to_number(other)

    def __rsub__(self, other):
        return to_number(other) - to_number(self)

    def __mul__(self, other):
        return to_number(self) * to_number(other)

    def __rmul__(self, other):
        return to_number(other) * to_number(self)

    def __truediv__(self, other):
        return to_number(self) / to_number(other)

    def __rtruediv__(self, other):
        return to_number(other) / to_number(self)

    def __mod__(self, other):
        return to_number(self) % to_number(other)

    def __rmod__(self, other):
        return to_number(other) % to_number(self)

    def __neg__(self):
        return -to_number(self)

    def __pos__(self):
        return to_number(self)

    def __abs__(self):
        return abs(to_number(self))

    def __int__(self):
        return int(to_number(self))

    def __float__(self):
        return float(to_number(self))

    def __round__(self, ndigits=None):
        return round(to_number(self), ndigits)

    def __eq__(self, other):
        if isinstance(other, (str, int, float)):
            return equals(self, other)
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, (str, int, float)):
            return not equals(self, other)
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, (str, int, float)):
            return compare(self, other) < 0
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, (str, int, float)):
            return compare(self, other) <= 0
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, (str, int, float)):
            return compare(self, other) > 0
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, (str, int, float)):
            return compare(self, other) >= 0
        return NotImplemented

    def __hash__(self):
        # Has to fit to __eq__
        if is_number(self):
            return hash(to_number(self))
        return hash(str(self).lower())


def wrap(value):
    """Texts become Scratch-like texts, everything else is unchanged."""
    if type(value) is str:
        return Text(value)
    return value
