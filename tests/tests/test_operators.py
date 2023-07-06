from pystage.core._operators import _Operators

class TestOperators:
    def test_xx_of_n_block(self):
        calculate = _Operators().operator_mathop

        assert calculate('abs', -10) == 10
        assert calculate('floor', 10.5) == 10
        assert calculate('floor', -10.5) == -11
        assert calculate('ceiling', -10.5) == -10
        assert calculate('ceiling', 10.5) == 11
        assert calculate('sqrt', 100) == 10
        assert calculate('sqrt', -4) == "NaN"
        assert calculate('sin', 0) == 0
        assert calculate('sin', -30) == -0.5
        assert calculate('sin', 60) == 0.8660254038
        assert calculate('sin', 90) == 1
        assert calculate('cos', 0) == 1
        assert calculate('cos', -30) == 0.8660254038
        assert calculate('cos', 60) == 0.5
        assert calculate('cos', 90) == 0
        assert calculate('tan', 0) == 0
        assert calculate('tan', -30) == -0.5773502692
        assert calculate('tan', 45) == 1
        assert calculate('tan', 89) == 57.2899616308
        assert calculate('tan', 90) == "Infinity"
        assert calculate('asin', 0) == 0
        assert calculate('asin', 1) == 90
        assert calculate('asin', 1.1) == "NaN"
        assert calculate('asin', -0.9) == -64.1580672368
        assert calculate('acos', 0) == 90
        assert calculate('acos', -1) == 180
        assert calculate('acos', 1) == 0
        assert calculate('atan', 1) == 45
        assert calculate('atan', 0) == 0
        assert calculate('ln', 0) == "-Infinity"
        assert calculate('ln', 1) == 0
        assert calculate('ln', 10) == 2.302585093
        assert calculate('ln', -10) == "NaN"
        assert calculate('log', 10) == 1
        assert calculate('log', 100) == 2
        assert calculate('log', -100) == "NaN"
        assert calculate('log', 0) == "-Infinity"
        assert calculate('e ^', 0) == 1
        assert calculate('e ^', 1) == 2.7182818285
        assert calculate('e ^', -1) == 0.3678794412
        assert calculate('10 ^', 0) == 1
        assert calculate('10 ^', 2) == 100
        assert calculate('10 ^', -2) == 0.01
        assert calculate('10 ^', 1000) == "Infinity"
