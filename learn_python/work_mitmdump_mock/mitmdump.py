# -*- coding: utf-8 -*-
# @Time    : 2020/12/15 18:20
# @Author  : pengketong
import json
from mitmproxy import http


def response(flow: http.HTTPFlow):
    if "quote.json" in flow.request.pretty_url and "x=" in flow.request.pretty_url:
        data = json.loads(flow.response.content)
        data['data']['items'][1]['quote']['name'] *= 2
        data['data']['items'][2]['quote']['name'] = ""
        data['data']['items'][3]['quote']['name'] *= 3
        flow.response.text = json.dumps(data)
