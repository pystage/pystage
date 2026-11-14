import random
import math

from pystage.core.values import to_number, to_string, Text, compare, equals, divide, modulo

class _Operators():
    def __init__(self):
        super().__init__()

    def operator_random(self, start, end):
        # Like in Scratch: Whole numbers lead to a whole number,
        # otherwise the result is a decimal number.
        whole = all(float(to_number(v)).is_integer() and "." not in str(v) for v in (start, end))
        low, high = sorted((to_number(start), to_number(end)))
        if whole:
            return random.randint(int(low), int(high))
        return random.uniform(low, high)

    def operator_divide(self, a, b):
        return divide(a, b)

    def operator_mod(self, a, b):
        return modulo(a, b)

    def operator_join(self, string1, string2):
        return Text(to_string(string1) + to_string(string2))

    def operator_letter_of(self, letter, string):
        string = to_string(string)
        index = to_number(letter)
        if math.isinf(index) or index < 1 or index > len(string):
            return Text("")
        return Text(string[index - 1])

    def operator_length(self, string):
        return len(to_string(string))

    def operator_gt(self, a, b):
        return compare(a, b) > 0

    def operator_lt(self, a, b):
        return compare(a, b) < 0

    def operator_equals(self, a, b):
        return equals(a, b)

    def operator_contains(self, string1, string2):
        # Not case sensitive, like in Scratch
        return to_string(string2).lower() in to_string(string1).lower()

    def operator_round(self, number):
        # Scratch always rounds .5 up, Python rounds to the even number.
        number = to_number(number)
        if math.isinf(number):
            return number
        return math.floor(number + 0.5)

    def operator_mathop(self, operator, number): 
        ops = {
                'abs': abs,
                'floor': math.floor,
                'ceiling': math.ceil,
                'sqrt': math.sqrt,
                'sin': lambda n: math.sin((math.pi * n) / 180),
                'cos': lambda n: math.cos((math.pi * n) / 180),
                'tan': lambda n: math.tan((math.pi * n) / 180) if not n == 90 else float("inf"),
                'asin': lambda n: (math.asin(n) * 180) / math.pi,
                'acos': lambda n: (math.acos(n) * 180) / math.pi,
                'atan': lambda n: (math.atan(n) * 180) / math.pi,
                'ln': lambda n : math.log(n) if not n == 0 else -float("inf"),
                'log': lambda n: math.log10(n) if not n == 0 else -float("inf"),
                'e ^': math.exp,
                '10 ^': lambda n: math.pow(10, n),
                }
        if operator not in ops:
            raise ValueError(f"Operator {operator} not supported.")
        
        try:
            value = ops[operator](to_number(number))
            if value == float("inf"):
                return "Infinity"
            elif value == -float("inf"):
                return "-Infinity"
            # avoid for situations like sin(30) == 0.49999999999999994
            return round(value, 10)
        except ValueError:
            # print(f"ValueError: math domain error: {operator}({number})")
            return "NaN"
        except OverflowError:
            return "Infinity"
