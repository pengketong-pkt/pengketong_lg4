from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from learn_python.work_web_weixinpo.page.addmember_page import AddMemberPage
from learn_python.work_web_weixinpo.page.base_page import BasePage

#主页继承基类，会自动加载基类的初始化方法，传一个主页的URL过去即可
class IndexPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    # 定位到添加成员的元素，点击，然后return跳转到添加成员页面
    def click_add_member(self):


        self.find(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)").click()
        return AddMemberPage(self.driver)