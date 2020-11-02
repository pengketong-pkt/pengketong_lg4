"""
<<<<<<< HEAD
完善你的Calc的用例，增加更多用例（浮点数相乘bug）
- 提交你的github测试文件地址
- 把allure的首页截图到回帖中


"""
import pytest
import allure
from learn_python.work3_test_pytest.core.calc import Calc


@allure.feature("测试用例")
=======
完善Calc的用例，增加更多用例（浮点数相乘bug）
"""
import pytest
import allure

from learn_python.work3_test_pytest.core.calc import Calc


>>>>>>> origin/master
class TestCalc:
    def setup_class(self):
        self.calc = Calc()

    def setup(self):
        pass

<<<<<<< HEAD
    # 正常整数相乘
    @allure.story("正常整数相乘")
    @pytest.mark.parametrize('a, b, c', [
        [1, 2, 2],
        [-1, -1, 1],
        [1, -1, 1],
        [-1, 1, -1]
    ])
    def test_mul_01(self, a, b, c):
=======
    # 乘法用例
    @pytest.mark.parametrize('a, b, c', [
        [1, 2, 2],
        [-1, -1, 1],
        [1, -1, 1]
    ])
    def test_mul(self, a, b, c):
>>>>>>> origin/master
        assert self.calc.mul(a, b) == c
        # assert calc.mul(-1, -1) == 1
        # assert calc.mul(1, -1) == 1

<<<<<<< HEAD
    # 浮点数相乘
    @allure.story("浮点数相乘")
    @pytest.mark.parametrize('a, b, c', [
        [0.01, 0.01, 0.0001],
        [0.01, -0.01, -0.0001],
        [-0.01, 0.01, -0.0001],
        [9.9, 9.9, 98.01]
    ])
    def test_mul_02(self, a, b, c):
        assert self.calc.mul(a, b) == c

    # 整数与浮点数相乘
    @allure.story("整数与浮点数相乘")
    @pytest.mark.parametrize('a, b, c', [
        [1, 0.01, 0.01],
        [1, -0.01, -0.01],
        [0.01, 1, 0.01],
        [-0.01, 1, -0.01]
    ])
    def test_mul_03(self, a, b, c):
        assert self.calc.mul(a, b) == c

    # 整数、浮点数与0相乘
    @allure.story("整数、浮点数与0相乘")
    @pytest.mark.parametrize('a, b, c', [
        [1, 0, 0],
        [-1, 0, 0],
        [0.01, 0, 0],
        [-0.01, 0, 0],
        [0, 1, 0],
        [0, -1, 0],
        [0, 0.01, 0],
        [0, -0.01, 0],
        [0, 0, 0]
    ])
    def test_mul_04(self, a, b, c):
        assert self.calc.mul(a, b) == c

    # 异常值相乘
    @allure.story("异常值")
    @pytest.mark.parametrize('a, b', [
        ['a', 'b'],
        ['@', '!'],
        ['中文', '中文'],
        [0, 0],
    ])
    def test_mul_05(self, a, b):
        with pytest.raises(Exception):
            assert self.calc.div(a, b)

    # 整数相除
    @allure.story("整数相除")
    @pytest.mark.parametrize('a, b, c', [
        [2, 2, 1],
        [-2, -2, 1],
        [2, -2, 1],
        [-2, 2, 1]
    ])
    def test_div_01(self, a, b, c):
        assert self.calc.div(a, b) == c

    # 浮点数相除
    @allure.story("浮点数相除")
    @pytest.mark.parametrize('a, b, c', [
        [0.02, 0.02, 1],
        [-0.02, -0.02, 1],
        [0.02, -0.02, 1],
        [-0.02, 0.02, 1]
    ])
    def test_div_02(self, a, b, c):
        assert self.calc.div(a, b) == c

    # 整数与浮点数相除
    @allure.story("整数与浮点数相除")
    @pytest.mark.parametrize('a, b, c', [
        [2, 0.02, 100],
        [-2, 0.02, -100],
        [2, -0.02, -100],
        [-2, -0.02, 100],
    ])
    def test_div_03(self, a, b, c):
        assert self.calc.div(a, b) == c

    # 0为被除数
    @allure.story("0为被除数")
    @pytest.mark.parametrize('a, b, c', [
        [0, 2, 0],
        [0, -2, 0],
        [0, 0.02, 0],
        [0, -0.02, 0]
    ])
    def test_div_04(self, a, b, c):
        assert self.calc.div(a, b) == c

    # 异常值相除
    @allure.story("异常值")
    @pytest.mark.parametrize('a, b', [
        [2, 0],
        [0.2, 0],
        [-2, 0],
        [-0.2, 0],
        ['a', 'b'],
        ['@', '!'],
        ['中文', '中文'],
        [0, 0],
    ])
    def test_div_05(self, a, b):
        with pytest.raises(Exception):
            assert self.calc.div(a, b)

    # 流程示例1
    @allure.story("先乘后除")
    def test_process_01(self):
=======
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
>>>>>>> origin/master
        r1 = self.calc.mul(1, 2)
        r2 = self.calc.div(2, 1)
        assert r1 == 2
        assert r2 == 2

<<<<<<< HEAD
    # 流程示例2
    @allure.story("先除后乘")
    def test_process_02(self):
=======
    # 流程示例，先乘后除
    def test_process2(self):
>>>>>>> origin/master
        r1 = self.calc.div(2, 1)
        r2 = self.calc.mul(1, 2)
        assert r1 == 2
        assert r2 == 2
