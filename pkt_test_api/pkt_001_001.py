#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/5/6 15:59
# @Author : PengKeTong
# @Site : 
# @File : pkt_001_001.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
# @Author : feier
# @File : test_requests.py

# 发送 get 请求
import requests


def test_get():
    r = requests.get('https://httpbin.ceshiren.com/get')
    print(r)
    print(r.text)
    print(r.json())
    print(r.raw)
    print(r.content)
    print(r.status_code)
    assert r.status_code == 200


def test_res_header():
    r = requests.get('https://httpbin.ceshiren.com/get')
    print(r.headers)
    print(r.headers['Content-Type'])


def test_params():
    url = 'https://httpbin.ceshiren.com/get'
    params = {
        "para_key1": "para_value1",
        "para_key2:": "para_value2"
    }
    r = requests.get(url=url, params=params)
    print(r.text)
    assert r.status_code == 200


def test_headers():
    url = 'https://httpbin.ceshiren.com/get'
    header = {
        "myheader": "feier"
    }
    r = requests.get(url=url, headers=header)
    print(r.text)
    assert r.status_code == 200


def test_post():
    url = 'https://httpbin.ceshiren.com/post'
    form_data = {
        "key1": "value1",
        "key2": "value2"
    }
    r = requests.post(url, data=form_data)
    print(r.text)
    assert r.status_code == 200


def test_post_json():
    url = 'https://httpbin.ceshiren.com/post'
    json_data = {
        'json_key': "json_value"
    }
    r = requests.post(url, json=json_data)
    print(r.text)


def test_post_file():
    url = 'https://httpbin.ceshiren.com/post'
    filename = "file.txt"
    files = {
        'file': open(filename, 'rb')
    }
    r = requests.post(url, files=files)
    print(r.text)


def test_set_cookie():
    url = 'https://httpbin.ceshiren.com/cookies/set'
    cookies = {
        "mycookie": "class"
    }
    r = requests.get(url, cookies=cookies)
    print(r.text)


def test_get_cookie():
    url = "https://www.baidu.com"
    r = requests.get(url)
    print(r.cookies)
