# -*- coding: utf-8 -*-
# @Time    : 2020/12/6 16:44
# @Author  : pengketong

# 通讯录页面
# from app.page.member_invite_page import MemberInviteMenuPage
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver

from learn_python.work_appium.weixin_PO.page.base_page import BasePage


class ContactListPage(BasePage):
    # def __init__(self, driver:WebDriver):
    #     self.driver = driver

    def add_member(self):
        '''
        添加成员
        '''
        # 点击【添加成员】
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        #                          'new UiScrollable(new UiSelector()'
        #                          '.scrollable(true).instance(0))'
        #                          '.scrollIntoView(new UiSelector()'
        #                          '.text("添加成员").instance(0));').click()
        self.find_by_scroll("添加成员").click()
        from learn_python.work_appium.weixin_PO.page.member_invite_page import MemberInviteMenuPage
        return MemberInviteMenuPage(self.driver)
