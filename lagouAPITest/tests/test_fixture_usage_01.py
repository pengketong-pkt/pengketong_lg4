# -*- coding: utf-8 -*-
# @Time    : 2021/3/15 18:12
# @Author  : pengketong
# 在lagouAPITest项目下新建一个文件，命名为test_fixture_usage.py

import pytest


@pytest.fixture(params=['hello', 'iTesting'], autouse=True, ids=['test1', 'test2'], name='test')
def my_method(request):
    print(request.param)


def test_use_fixtures_01():
    print('\n this is the 1st test')


def test_use_fixtures_02():
    print('\n this is the 2nd test')


def test_use_fixtures_03(test):
    print('\n this is the 3nd test')
