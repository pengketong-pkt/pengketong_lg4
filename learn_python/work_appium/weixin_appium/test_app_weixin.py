# -*- coding: utf-8 -*-
# @Time    : 2020/11/20 17:03
# @Author  : pengketong
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class Test_App:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "true"
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_delete(self):
        name = 'pxy_1604583411'
        # 点击通讯录
        self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        # 点击搜索按钮
        self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/i6n"]').click()
        # 输入需要搜索的名字
        self.driver.find_element(MobileBy.XPATH, '//*[@text="搜索"]').send_keys(name)
        # 点击搜索出来的数据
        self.driver.find_element(MobileBy.XPATH, '//*[@text="彭新洋企业"]').click()
        # 点击右上角三个点按钮
        self.driver.find_element_by_id('com.tencent.wework:id/i6d').click()
        # 点击编辑成员按钮
        self.driver.find_element(MobileBy.XPATH, '//*[@text="编辑成员"]').click()
        # 点击删除成员按钮
        self.driver.find_element(MobileBy.XPATH, '//*[@text="删除成员"]').click()
        # 点击删除弹框的确定按钮
        self.driver.find_element(MobileBy.XPATH, '//*[@text="确定"]').click()
        # 点击左上角返回按钮，返回到通讯录页面
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/i63').click()
        # 点击搜索按钮
        self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/i6n"]').click()
        # 搜索刚才被删除的名字，确认是否已被删除
        self.driver.find_element(MobileBy.XPATH, '//*[@text="搜索"]').send_keys(name)
        result = self.driver.find_element(MobileBy.XPATH, '//*[@text="无搜索结果"]').text
        assert result == "无搜索结果"
