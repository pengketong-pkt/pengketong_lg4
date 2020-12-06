# -*- coding: utf-8 -*-
# @Time    : 2020/12/6 18:23
# @Author  : pengketong
from appium.webdriver.common.mobileby import MobileBy

from learn_python.work_appium.weixin_PO.page.base_page import BasePage
from learn_python.work_appium.weixin_PO.page.edit_contact_page import EditContactPage


class PersonOperationPage(BasePage):


    def goto_edit_contact_page(self):
        # self.find(MobileBy.XPATH, "//*[@text='编辑成员']").click()
        self.find(MobileBy.XPATH, f"//*[@text='编辑成员']").click()

        return EditContactPage(self.driver)