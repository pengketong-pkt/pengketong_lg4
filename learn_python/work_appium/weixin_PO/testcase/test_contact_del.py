# -*- coding: utf-8 -*-
# @Time    : 2020/12/6 18:38
# @Author  : pengketong
from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from learn_python.work_appium.weixin_PO.page.app import App
from learn_python.work_appium.weixin_PO.page.searcher_contact_result import SearcherContactResult


class TestWX:
    def setup_class(self):
        self.app = App()

    def setup(self):
        self.main = self.app.start().goto_main()

    def teardown_class(self):
        self.app.stop()

    def test_contact_del(self):
        beforenum=self.main.goto_searcher_contact_result().searcher_contact_result("pxy_160")

        sleep(5)

        self.main.goto_searcher_contact_page().goto_person_info_page(
            "pxy_160").goto_person_operation_page().goto_edit_contact_page().goto_searcher_contact_page()
        sleep(5)
        afternum = self.main.goto_searcher_contact_result().searcher_contact_result("pxy_160")
        assert afternum == beforenum - 1
