# -*- coding: utf-8 -*-
# @Time    : 2020/12/6 18:09
# @Author  : pengketong
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from learn_python.work_appium.weixin_PO.page.base_page import BasePage
from learn_python.work_appium.weixin_PO.page.person_operation_page import PersonOperationPage


class PersonInfoPage(BasePage):

    def goto_person_operation_page(self):
        # self.find(MobileBy.ID, "com.tencent.wework:id/gq0").click()
        self.driver.find_element_by_id('com.tencent.wework:id/i6d').click()
        return PersonOperationPage(self.driver)