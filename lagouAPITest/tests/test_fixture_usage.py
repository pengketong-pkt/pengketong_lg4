# -*- coding: utf-8 -*-
# @Time    : 2021/3/15 17:53
# @Author  : pengketong
# 在lagouAPITest项目下新建一个文件，命名为 test_fixture_usage.py

# 在lagouAPITest项目下新建一个文件，命名为test_fixture_usage.py

import pytest


@pytest.fixture()
def my_method():
    print('This is iTesting Speaking')


# 函数直接使用fixture

@pytest.mark.usefixtures('my_method')
def test_use_fixtures():
    print('Please follow iTesting from wechat')


class TestClass1:

    # 类方法使用fixture

    @pytest.mark.usefixtures('my_method')
    def test_class_method_usage(self):
        print('[classMethod]Please follow iTesting from wechat')


# 类直接使用fixture

@pytest.mark.usefixtures('my_method')
class TestClass2:

    def test_method_usage_01(self):
        pass

    def test_method_usage_02(self):
        pass
