# -*- coding: utf-8 -*-
# @Time    : 2021/3/26 10:11
# @Author  : pengketong
import pytest


def pytest_addoption(parser):
    parser.addoption(

        "--auth", action="store", default=None, help="Your own auth key pair"

    )


@pytest.fixture(scope='session')
def auth(request):
    return request.config.getoption('--auth')
