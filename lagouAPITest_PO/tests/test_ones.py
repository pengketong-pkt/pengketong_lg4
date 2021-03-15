# -*- coding: utf-8 -*-
# @Time    : 2021/3/15 15:52
# @Author  : pengketong
# -*- coding: utf-8 -*-

import pytest

from lagouAPITest_PO.pages.ones import OneAI


class TestOneAI:

    # 注意，需要email和密码需要更改成你自己的账户密码

    @pytest.mark.parametrize('login_data, project_name, target_page', [({"password": "iTestingIsGood",
                                                                         "email": "pleasefollowiTesting@outlook.com"},
                                                                        {"project_name": "VIPTEST"}, {
                                                                            "target_page": "https://ones.ai/project/#/home/project"})])
    def test_project_name_txt(self, login_data, project_name, target_page):
        print(login_data)

        one_page = OneAI(login_data, target_page)

        actual_project_name = one_page.get_project_name()

        assert actual_project_name == project_name["project_name"]
