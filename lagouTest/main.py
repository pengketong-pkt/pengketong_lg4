# -*- coding: utf-8 -*-
# @Time    : 2021/3/10 15:57
# @Author  : pengketong
# -*- coding: utf-8 -*-
# @Time    : 2021/3/9 19:51
# @Author  : pengketong
# coding=utf-8


import os

import unittest

# if __name__ == "__main__":
#     suite = unittest.defaultTestLoader.discover(os.path.join(os.path.dirname(__file__), "tests_1"), pattern='*.py',
#                                                 top_level_dir=os.path.dirname(__file__))
#
#     runner = unittest.TextTestRunner(verbosity=2)
#
#     runner.run(suite)
# from lagouTest.common.html_reporter import GenerateReport
#
# __author__ = 'iTesting'
#
# import unittest, os
#
# if __name__ == "__main__":
#     suite = unittest.defaultTestLoader.discover(os.path.join(os.path.dirname(__file__), "tests"), \
#  \
#                                                 pattern='*.py', top_level_dir=os.path.dirname(__file__))
#
#     html_report = GenerateReport()
#
#     html_report.generate_report(suite)
# coding=utf-8

import pytest

import os

import glob


# 查找所有待执行的测试用例module，见《04|必知必会，打好Python基本功》

def find_modules_from_folder(folder):
    absolute_f = os.path.abspath(folder)

    md = glob.glob(os.path.join(absolute_f, "*.py"))

    return [f for f in md if os.path.isfile(f) and not f.endswith('__init__.py')]


if __name__ == "__main__":
    # 得出测试文件夹地址

    test_folder = os.path.join(os.path.dirname(__file__), 'tests')

    # 得出测试文件夹下的所有测试用例

    target_file = find_modules_from_folder(test_folder)

    # 直接运行所有的测试用例

    pytest.main([*target_file, '-v'])
