# -*- coding: utf-8 -*-
# @Time    : 2021/3/15 18:25
# @Author  : pengketong
import pytest


class TestClass:

    @pytest.fixture(params=['hello', 'iTesting'], autouse=True)
    def my_method1(self, request):
        print('\nthe param are:{}'.format(request.param))

        return request.param

    @pytest.fixture(params=['VIPTEST', 'is good'], autouse=True)
    def my_method2(self, request):
        print('\nthe param are:{}'.format(request.param))

        return request.param

    def test_use_fixtures_01(self):
        pass
