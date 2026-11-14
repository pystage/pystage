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
