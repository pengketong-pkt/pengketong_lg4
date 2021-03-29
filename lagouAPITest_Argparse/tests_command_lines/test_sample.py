# -*- coding: utf-8 -*-
# @Time    : 2021/3/26 10:20
# @Author  : pengketong
import pytest


class TestDemo:

    def test_secret_auth(self, auth):
        print("\nmy auth are {}".format(auth))

        assert True
