# -*- coding: utf-8 -*-
# @Time    : 2020/12/6 16:45
# @Author  : pengketong

# 主页
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver

from learn_python.work_appium.weixin_PO.page.base_page import BasePage
from learn_python.work_appium.weixin_PO.page.contact_list_page import ContactListPage
from learn_python.work_appium.weixin_PO.page.searcher_contact_page import SearcherContactPage
from learn_python.work_appium.weixin_PO.page.searcher_contact_result import SearcherContactResult


class MainPage(BasePage):
    # def __init__(self, driver: WebDriver):
    #     self.driver = driver
    # 首页-通讯录
    _contact_list = (MobileBy.XPATH, "//*[@text='通讯录']")

    def goto_contactlist(self):
        '''
        进入到通讯录
        '''
        # 点击【通讯录】

        self.find(*self._contact_list).click()
        return ContactListPage(self.driver)

    def goto_searcher_contact_page(self):
        self.find(*self._contact_list).click()
        return SearcherContactPage(self.driver)

    def goto_searcher_contact_result(self):
        self.find(*self._contact_list).click()
        return SearcherContactResult(self.driver)
