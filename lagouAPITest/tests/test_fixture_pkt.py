# -*- coding: utf-8 -*-
# @Time    : 2021/3/15 18:04
# @Author  : pengketong
import pytest


@pytest.fixture(params=['hello', 'iTesting'])
def my_method(request):
    return request.param


def test_use_fixtures_01(my_method):
    print('\n this is the 1st test')

    print(my_method)


@pytest.mark.usefixtures('my_method')
def test_use_fixtures_02():
    print('\n this is the 2nd test')

    # 注意，如果我在这里想通过print(my_mthod)来打印出fixuture提供的参数，是不行的， 因为使用usefixtures无法获取fixture的返回值，如需要fixture的返回值，则需用test_use_fixtures_01那样的调用方式
