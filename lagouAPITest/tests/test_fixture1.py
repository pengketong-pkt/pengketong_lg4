# -*- coding: utf-8 -*-
# @Time    : 2021/3/15 18:28
# @Author  : pengketong
# test_fixture1.py

import pytest


class TestClass:

    def test_use_fixtures_01(self, login):
        print('\nI am data:{}'.format(login))
