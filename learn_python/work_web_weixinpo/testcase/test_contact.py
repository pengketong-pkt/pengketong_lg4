import time

from learn_python.work_web_weixinpo.page.index_page import IndexPage

import random


class TestContact:
    def setup(self):
        self.index = IndexPage()

    def test_addcontact(self):
        account = str(int(time.time()))
        name = "zz_" + account

        suffix = random.randint(10000000, 99999999)
        #拼接电话号码
        phone = (f"136{suffix}")
        phonenum = phone
        addmemberpage = self.index.click_add_member()
        addmemberpage.add_member(name, account, phonenum)
        result = addmemberpage.get_member(name)
        assert result
