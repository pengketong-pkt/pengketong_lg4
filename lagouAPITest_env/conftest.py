# -*- coding: utf-8 -*-
# @Time    : 2021/3/26 14:40
# @Author  : pengketong
import codecs

import json

import os

import pytest

import yaml


def pytest_addoption(parser):
    parser.addoption(

        "--env", action="store", default='dev', help="set env"

    )


@pytest.fixture(scope='session')
def get_env(request):
    return request.config.getoption('--env')


@pytest.fixture(scope='session')
def load_data_from_json_yaml(request):
    # 获取解析到的test_data所在的目录，以及调用test_data的文件

    data_folder, function_file = request.param

    # 根据传入的环境变量参数，计算出应该用那个环境下的数据文件

    data_file_name = function_file.replace('.py', '.%s.yaml' % request.getfixturevalue('get_env'))

    data_file = os.path.join(data_folder, data_file_name)

    _is_yaml_file = data_file.endswith((".yml", ".yaml"))

    with codecs.open(data_file, 'r', 'utf-8') as f:

        # Load the data from YAML or JSON

        if _is_yaml_file:

            data = yaml.safe_load(f)

        else:

            data = json.load(f)

    # 这里你可能需要根据业务需要，把数据解析以下再返回

    return data
