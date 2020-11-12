import allure
import pytest
import yaml

from learn_python.work3_test_pytest.core.calc import Calc


class TestCalcYaml:
    def setup_class(self):
        self.calc = Calc()

    def setup(self):
        pass

    @allure.story("正常整数")
    @pytest.mark.parametrize("a, b, exp", yaml.safe_load(open("./data.yaml")))
    def test_mul_01(self, a, b, exp):
        assert self.calc.mul(a, b) == exp
