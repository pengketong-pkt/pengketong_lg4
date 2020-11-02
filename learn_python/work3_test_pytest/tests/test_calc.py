"""
完善Calc的用例，增加更多用例（浮点数相乘bug）
"""
import pytest
import allure

from learn_python.work3_test_pytest.core.calc import Calc


class TestCalc:
    def setup_class(self):
        self.calc = Calc()

    def setup(self):
        pass

    # 乘法用例
    @pytest.mark.parametrize('a, b, c', [
        [1, 2, 2],
        [-1, -1, 1],
        [1, -1, 1]
    ])
    def test_mul(self, a, b, c):
        assert self.calc.mul(a, b) == c
        # assert calc.mul(-1, -1) == 1
        # assert calc.mul(1, -1) == 1

    # 除法用例
    @pytest.mark.parametrize('a, b, c', [
        [2, 2, 1],
        [0.2, 0.1, 2],
        [0, 2, 0]
    ])
    def test_div(self, a, b, c):
        assert self.calc.div(a, b) == c

    # 异常值例子
    @pytest.mark.parametrize('a, b', [
        [2, 0],
        [0.2, 0],
        [0, 0]
    ])
    def test_div(self, a, b):
        with pytest.raises(Exception):
            assert self.calc.div(a, b)

    # 流程示例，先乘后除
    def test_process1(self):
        r1 = self.calc.mul(1, 2)
        r2 = self.calc.div(2, 1)
        assert r1 == 2
        assert r2 == 2

    # 流程示例，先乘后除
    def test_process2(self):
        r1 = self.calc.div(2, 1)
        r2 = self.calc.mul(1, 2)
        assert r1 == 2
        assert r2 == 2
