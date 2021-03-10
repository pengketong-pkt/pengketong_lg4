# -*- coding: utf-8 -*-
# @Time    : 2021/3/10 15:59
# @Author  : pengketong
# -*- coding: utf-8 -*-
# @Time    : 2021/3/10 15:05
# @Author  : pengketong
# coding=utf-8

import json

import unittest

import requests


class TestLaGou(unittest.TestCase):

    def setUp(self):
        self.s = requests.Session()

        self.url = 'https://www.lagou.com'

    def test_visit_lagou(self):
        result = self.s.get(self.url)

        assert result.status_code == 200

        unittest.TestCase.assertIn(self, '拉勾', result.text)

    def test_get_new_message(self):
        # 此处需要一个方法登录获取登录的cookie，但因我们无法知道拉勾登录真实的API，故采用此方式登录

        message_url = 'https://gate.lagou.com/v1/entry/message/newMessageList'

        cookie = {

            'cookie': '_gid=GA1.2.438589688.1601450871; gate_login_token=475844a837230240e1e73e4ecfa34102e65fa8e5384801cca67bbe983a142abb;'}

        headers = {'x-l-req-header': '{deviceType: 9}'}

        # 直接带登录态发送请求

        result = self.s.get(message_url, cookies=cookie, headers=headers)

        assert result.status_code == 200

        assert json.loads(result.content)['message'] == '成功'

    def tearDown(self):
        self.s.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
