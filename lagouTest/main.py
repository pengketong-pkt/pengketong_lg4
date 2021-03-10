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
from lagouTest.common.html_reporter import GenerateReport

__author__ = 'iTesting'

import unittest, os

if __name__ == "__main__":
    suite = unittest.defaultTestLoader.discover(os.path.join(os.path.dirname(__file__), "tests"), \
 \
                                                pattern='*.py', top_level_dir=os.path.dirname(__file__))

    html_report = GenerateReport()

    html_report.generate_report(suite)
