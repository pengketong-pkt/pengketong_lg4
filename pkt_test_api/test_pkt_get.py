#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/4/15 15:19
# @Author : PengKeTong
# @Site : 
# @File : test_pkt_get.py
# @Software: PyCharm
# coding:utf-8

import requests

# 请求url
url = "http://httpbin.org/get"

# 请求头
headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "User-Agent": "python-requests/2.9.1",
}

# 查询字符串
params = {'name': 'Jack', 'age': '24'}

r = requests.get(url=url, headers=headers, params=params)

print(r.status_code)  # 获取响应状态码
print(r.content)  # 获取响应消息

if __name__ == "__main__":
    pass
