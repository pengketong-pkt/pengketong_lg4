# -*- coding: utf-8 -*-
# @Time    : 2021/3/11 9:46
# @Author  : pengketong
import pytest

if __name__ == '__main__':
    # 运行当前目录下所有（test_*.py  和 *_test.py）
    # pytest.main(['./tests/'])
    # pytest.main(['-v','-m',"lagou or baidu"])
    pytest.main(["-v",
                 "--alluredir=./allure_reports"])