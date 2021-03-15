# -*- coding: utf-8 -*-
# @Time    : 2021/3/15 18:43
# @Author  : pengketong
# test_sample.py

import pytest


@pytest.fixture()
def is_odd(request):
    print('Now the parameter are:--{}\n'.format(request.param))

    if int(request.param) % 2 == 0:

        return False

    else:

        return True


@pytest.mark.parametrize("is_odd", [1, 0], indirect=True)
def test_is_odd(is_odd):
    if is_odd:

        print("is odd number")

    else:

        print("not odd number")


if __name__ == "__main__":
    pytest.main([])
