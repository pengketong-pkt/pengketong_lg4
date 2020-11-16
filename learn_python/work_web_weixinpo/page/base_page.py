# 基类，用来完成一些初始化操作，存放最基本的方法，比如实例化driver, find....
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    #初始化_base_url
    _base_url = ""

    # 定义一个构造函数，用来启动driver,默认为none，意味着只在第一次生成driver，后面就可以复用同一个driver，不用每个po都启动一个新的driver
    def __init__(self, driver: WebDriver = None):
        #如果driver为None，则新配置一个
        if driver == None:
            option = Options()
            option.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=option)
            self.driver.implicitly_wait(5)
        #如果driver不为None，沿用当前的driver
        else:
            self.driver = driver
        #如果_base_url不等于空，则将_base_url传给driver
        if self._base_url != "":
            self.driver.get(self._base_url)
    #定义找元素的方法
    def find(self, by, locator):
        return self.driver.find_element(by, locator)
    #定义找多个元素的方法
    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)
    #定义点击方法，默认10s,10s如果没有完成点击事件，跳过此操作
    def wait_for_click(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator))