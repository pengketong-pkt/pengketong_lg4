# -*- coding: utf-8 -*-
# @Time    : 2020/12/6 16:43
# @Author  : pengketong

# 存放 driver的初始化，或者存放一些最基本的方法， find,get_toast,....
import logging

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    # logging.basicConfig(level=logging.INFO,
    #                     filename='./myapptest.log',
    #                     filemode='w',
    #                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    #                     datefmt='%a, %d %b %Y %H:%M:%S')
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename='pengketong_lg4/learn_python/work_appium/weixin_PO/page/myapp.log',
                        filemode='w')

    # logging.basicConfig(filename="config.log", filemode="w", format="%(asctime)s-%(name)s-%(levelname)s-%(message)s",
    #                     level=logging.INFO)
    # logging.basicConfig(level=logging.INFO,  # 控制台打印的日志级别
    #                     filename='new.log',
    #                     filemode='a',  ##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
    #                     # a是追加模式，默认如果不写的话，就是追加模式
    #                     format=
    #                     '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
    #                     # 日志格式
    #                     )

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, by, locator):
        logging.info("find:")
        logging.info(by)
        logging.info(locator)

        return self.driver.find_element(by, locator)

    def finds(self, by, locator):
        logging.info("finds:")
        logging.info(by)
        logging.info(locator)

        return self.driver.find_elements(by, locator)

    def find_by_scroll(self, text):
        logging.info("find_by_scroll")
        logging.info(text)
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        'new UiScrollable(new UiSelector()'
                                        '.scrollable(true).instance(0))'
                                        '.scrollIntoView(new UiSelector()'
                                        f'.text("{text}").instance(0));')

    def get_toast_text(self):
        logging.info("get toast:")
        result = self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        logging.info(result)
        return result
