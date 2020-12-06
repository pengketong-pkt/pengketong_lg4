# -*- coding: utf-8 -*-
# @Time    : 2020/12/6 21:44
# @Author  : pengketong
from time import sleep

from appium.webdriver.common.mobileby import MobileBy


from learn_python.work_appium.weixin_PO.page.base_page import BasePage


class SearcherContactResult(BasePage):

    def searcher_contact_result(self, name):
        self.find(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/i6n"]').click()
        self.find(MobileBy.XPATH, '//*[@text="搜索"]').send_keys(name)
        sleep(3)
        eles = self.finds(MobileBy.XPATH, f"//*[@text='{name}']")
        searchnum = len(eles)
        print(searchnum)
        return searchnum
