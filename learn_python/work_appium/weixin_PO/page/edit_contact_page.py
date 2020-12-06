# -*- coding: utf-8 -*-
# @Time    : 2020/12/6 18:26
# @Author  : pengketong
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from learn_python.work_appium.weixin_PO.page.base_page import BasePage



class EditContactPage(BasePage):


    def goto_searcher_contact_page(self):
        self.find(MobileBy.XPATH, "//*[@text='删除成员']").click()
        self.find(MobileBy.XPATH, "//*[@text='确定']").click()
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        #                          'new UiScrollable(new UiSelector()'
        #                          '.scrollable(true).instance(0))'
        #                          '.scrollIntoView(new UiSelector()'
        #                          '.text("删除成员").instance(0));').click()
        # self.driver.find_element(MobileBy.XPATH, f"//*[@text='确定']").click()
        from learn_python.work_appium.weixin_PO.page.searcher_contact_page import SearcherContactPage
        return SearcherContactPage(self.driver)