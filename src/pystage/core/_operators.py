import random
import math

class _Operators():
    def __init__(self):
        super().__init__()

    def operator_random(self, start, end):
        return random.randint(start, end)

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
            value = ops[operator](number)
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
