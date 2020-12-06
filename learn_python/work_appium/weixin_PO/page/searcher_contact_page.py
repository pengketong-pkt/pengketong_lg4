# -*- coding: utf-8 -*-
# @Time    : 2020/12/6 17:50
# @Author  : pengketong
from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from learn_python.work_appium.weixin_PO.page.base_page import BasePage
from learn_python.work_appium.weixin_PO.page.person_info_page import PersonInfoPage


class SearcherContactPage(BasePage):

    def goto_person_info_page(self, name):
        # self.find(MobileBy.XPATH,
        #                          "//android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout[1]/android.widget.TextView").click()
        self.find(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/i6n"]').click()
        self.find(MobileBy.XPATH, '//*[@text="搜索"]').send_keys(name)
        sleep(2)
        eles = self.finds(MobileBy.XPATH, f"//*[@text='{name}']")
        beforenum = len(eles)
        if beforenum < 2:
            print("没有可删除的人员")
            return
        eles[1].click()

        return PersonInfoPage(self.driver)
