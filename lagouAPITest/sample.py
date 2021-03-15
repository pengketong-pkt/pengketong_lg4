# -*- coding: utf-8 -*-
# @Time    : 2021/3/11 14:10
# @Author  : pengketong
import pytest


@pytest.mark.smoke
class Sample(object):

    def test_equal(self):
        # 在这里，我让这个case失败，来演示re-run

        assert 1 == 1

    def not_equal(self):
        assert 1 != 0
