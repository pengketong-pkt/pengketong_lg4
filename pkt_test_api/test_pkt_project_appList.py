#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/5/7 9:21
# @Author : PengKeTong
# @Site : 
# @File : test_pkt_project_appList.py
# @Software: PyCharm
import json

import pytest
import requests


def test_get():
    data1 = json.dumps({"projectId": "542884705818062848"})
    header1 = {
        "authorization": "Bearer%eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ7XCJ1c2VySWRcIjpcIjQyNFwiLFwib3JnSWRcIjpcIjE1M1wiLFwiYWNjb3VudFwiOlwiMTM2ODA1ODYxOTNcIixcInVzZXJOYW1lXCI6XCLlsI_pgJpcIixcImF1dGhvcml0aWVzXCI6W1wiMzQ5MFwiLFwiMzQ4OVwiLFwiMzQ4N1wiLFwiMzQ5N1wiLFwiMzQ5OFwiLFwiMzUwMlwiLFwiMzYyMFwiLFwiMzY0M1wiXSxcInNraWxsc1wiOltcIjUwNzFcIixcIjUwNzNcIixcIjUwNzJcIixcIjUwNzZcIixcIjUwNzVcIixcIjUwODFcIixcIjUwODJcIixcIjUwODRcIixcIjUwODdcIixcIjUwNjVcIixcIjUwNjZcIixcIjUwNjdcIixcIjUwODZcIixcIjUwODhcIixcIjUwNTJcIixcIjUwNTNcIixcIjUwNTRcIixcIjUwNTVcIixcIjUwNTZcIixcIjUwNTdcIixcIjUwNThcIixcIjUwNTlcIixcIjUwNjBcIixcIjUwNjFcIixcIjUwNjJcIixcIjUwNjNcIixcIjUwNzhcIixcIjUwNzlcIixcIjUwNjRcIixcIjUwNjhcIixcIjUwNjlcIixcIjUwNzdcIixcIjUwODVcIixcIjUwOTBcIixcIjUwOTFcIixcIjUwOTJcIl0sXCJjbGllbnRUeXBlXCI6e1wiY29kZVwiOjEsXCJkZXNcIjpcIkFQUFwifSxcImdyYW50VHlwZVwiOlwiQmVhcmVyIFwiLFwic3lzdGVtSWRcIjpcInNhYXNcIixcImNhcHRjaGFUb2tlbkNhY2hlS2V5XCI6XCIxMzY4MDU4NjE5MzpBUFA6Q2FwdGNoYSBcIn0iLCJhdWQiOiJhbnlvbmUiLCJqdGkiOiJhN2ZjMjE1YS02ZjgzLTQ1MmMtOTEzNy1iNGQxOTQ5YzdlODAiLCJpc3MiOiJiZ3kiLCJuYmYiOjE2MjAyOTI5NjcsImlhdCI6MTYyMDI5Mjk2NywiZXhwIjozMjQwNTg1OTM0fQ.sKAEGbgGB2NGAZZhXqJCNFLxtD8_1A59i05CpZwWu5k"
    }
    r1 = requests.post("https://tsyy.hbzhsq.cn:9301/api/integration/api/type/project/appList",
                       data=data1,
                       headers=header1)
    print(r1.text)
