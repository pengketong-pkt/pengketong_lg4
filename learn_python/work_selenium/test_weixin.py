from selenium import webdriver
from selenium.webdriver.common.by import By


class TestTestcase():
    def setup_method(self):
        # 复用浏览器
        from selenium.webdriver.chrome.options import Options
        option = Options()
        option.debugger_address = "127.0.0.1:9222"

        # 未安装chromedriver插件时指定driver路径
        # self.driver = webdriver.Chrome(executable_path="./chromedriver", options=option)

        # 通过brew cask install chromedriver安装webdriver后，不再需要指定路径
        # （如果浏览器版本和chromedriver不匹配，在网上下载对应版本替换就好了）
        self.driver = webdriver.Chrome(options=option)
        # 隐式等待
        self.driver.implicitly_wait(3)

    def teardown_method(self, method):
        self.driver.quit()

    # def test_testcase(self):
    #     self.driver.get("https://ceshiren.com/")
    #     self.driver.find_element(By.LINK_TEXT, "所有分类").click()
    #     element = self.driver.find_element(By.LINK_TEXT, "所有分类")
    #     result = element.get_attribute("class")
    #     assert 'active' == result
    def test_wechat(self):
        """需求：使用 cookie 登录企业微信，完成添加联系人，加上断言验证"""

        # 打开企业微信通讯录
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")

        # 获取cookies
        cookies = self.driver.get_cookies()
        # print(cookies)

        # shelve 模块， python 自带的对象持久化存储
        # db = shelve.open('cookies')
        # 保存当前cookie
        # db['cookie'] = cookies
        # 获取db中的cookie
        # cookies = db['cookie']
        # db.close()

        # cookie中的expiry可能是浮点型，为避免报错需要转换一下或者删除
        for cookie in cookies:
            if "expiry" in cookie:
                # cookie.pop('expiry')
                cookie['expiry'] = int(cookie['expiry'])
                self.driver.add_cookie(cookie)

        # 让cookie生效，刷新页面
        self.driver.refresh()

    def test_wx_01(self):
        # self.driver.find_element(By.XPATH, '//*[@id="menu_contacts"]/span').click()
        # sleep(5)

        self.driver.find_elements(By.CSS_SELECTOR, ".qui_btn.ww_btn.js_add_member")[1].click()
        self.driver.find_element_by_id('username').send_keys('pxy_009')
        self.driver.find_element_by_id('memberAdd_acctid').send_keys('00099')
        self.driver.find_element_by_id('memberAdd_phone').send_keys('13680586119')
        self.driver.find_elements(By.CSS_SELECTOR, ".qui_btn.ww_btn.js_btn_save")[0].click()
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        titles = [element.get_attribute("title") for element in elements]
        for pxy_009 in titles:
         assert "成功"