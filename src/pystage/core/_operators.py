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
                'tan': math.tan,
                'asin': lambda n: (math.asin(n) * 180) / math.pi,
                'acos': lambda n: (math.acos(n) * 180) / math.pi,
                'atan': lambda n: (math.atan(n) * 180) / math.pi,
                'ln': math.log,
                'log': math.log,
                'e ^': math.exp,
                '10 ^': lambda n: math.pow(10, n),
                }
        if operator not in ops:
            raise ValueError(f"Operator {operator} not supported.")
        return ops[operator](number)
