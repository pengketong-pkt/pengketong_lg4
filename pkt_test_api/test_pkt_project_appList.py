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


# def test_get():
#     data1 = json.dumps({"projectId": "542884705818062848"})
#     header1 = {
#         "authorization": "Bearer%eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ7XCJ1c2VySWRcIjpcIjQyNFwiLFwib3JnSWRcIjpcIjE1M1wiLFwiYWNjb3VudFwiOlwiMTM2ODA1ODYxOTNcIixcInVzZXJOYW1lXCI6XCLlsI_pgJpcIixcImF1dGhvcml0aWVzXCI6W1wiMzQ5MFwiLFwiMzQ4OVwiLFwiMzQ4N1wiLFwiMzQ5N1wiLFwiMzQ5OFwiLFwiMzUwMlwiLFwiMzYyMFwiLFwiMzY0M1wiXSxcInNraWxsc1wiOltcIjUwNzFcIixcIjUwNzNcIixcIjUwNzJcIixcIjUwNzZcIixcIjUwNzVcIixcIjUwODFcIixcIjUwODJcIixcIjUwODRcIixcIjUwODdcIixcIjUwNjVcIixcIjUwNjZcIixcIjUwNjdcIixcIjUwODZcIixcIjUwODhcIixcIjUwNTJcIixcIjUwNTNcIixcIjUwNTRcIixcIjUwNTVcIixcIjUwNTZcIixcIjUwNTdcIixcIjUwNThcIixcIjUwNTlcIixcIjUwNjBcIixcIjUwNjFcIixcIjUwNjJcIixcIjUwNjNcIixcIjUwNzhcIixcIjUwNzlcIixcIjUwNjRcIixcIjUwNjhcIixcIjUwNjlcIixcIjUwNzdcIixcIjUwODVcIixcIjUwOTBcIixcIjUwOTFcIixcIjUwOTJcIl0sXCJjbGllbnRUeXBlXCI6e1wiY29kZVwiOjEsXCJkZXNcIjpcIkFQUFwifSxcImdyYW50VHlwZVwiOlwiQmVhcmVyIFwiLFwic3lzdGVtSWRcIjpcInNhYXNcIixcImNhcHRjaGFUb2tlbkNhY2hlS2V5XCI6XCIxMzY4MDU4NjE5MzpBUFA6Q2FwdGNoYSBcIn0iLCJhdWQiOiJhbnlvbmUiLCJqdGkiOiJhN2ZjMjE1YS02ZjgzLTQ1MmMtOTEzNy1iNGQxOTQ5YzdlODAiLCJpc3MiOiJiZ3kiLCJuYmYiOjE2MjAyOTI5NjcsImlhdCI6MTYyMDI5Mjk2NywiZXhwIjozMjQwNTg1OTM0fQ.sKAEGbgGB2NGAZZhXqJCNFLxtD8_1A59i05CpZwWu5k"
#     }
#     r1 = requests.post("https://tsyy.hbzhsq.cn:9301/api/integration/api/type/project/appList",
#                        data=data1,
#                        headers=header1)
#     print(r1.text)


def test_post_order():
    data2 = json.dumps({
        "pageNo": 1,
        "pageSize": 10,
        "keyWord": "",
        "areaId": 314,
        "projectIds": [2583],
        "subSystemId": "-1",
        "subSystemName": "",
        "operatingType": "-1",
        "orderSource": "-1",
        "orderCategory": "-1",
        "isPay": "-1",
        "orderStatus": -1,
        "createTimeFrom": "2021-05-17 00:00:00",
        "createTimeTo": "2021-05-17 24:00:00",
        "isVerification": "-1",
        "isComplete": "-1",
        "isCompleteVerify": "-1",
        "serviceTypeId": "-1",
        "serviceClassify": "-1",
        "orders": {
            "createTime": "desc"
        }
    })
    header2 = {

        "authorization": "Bearer%eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ7XCJ1c2VySWRcIjpcIjU0OTRcIixcIm9yZ0lkXCI6XCIxXCIsXCJhY2NvdW50XCI6XCIxMzY4MDU4NjE5M1wiLFwidXNlck5hbWVcIjpcIuW9reWPr-mAmlwiLFwiYXV0aG9yaXRpZXNcIjpbXCIzXCIsXCI0XCIsXCIxXCIsXCIyXCIsXCI1XCIsXCI2XCIsXCIxNVwiLFwiMTRcIixcIjE2XCIsXCIxN1wiLFwiMTlcIixcIjE4XCIsXCIyMFwiLFwiMjFcIl0sXCJza2lsbHNcIjpbXCI1XCIsXCI2XCIsXCI3XCIsXCI5XCIsXCIxMFwiLFwiMTFcIixcIjEzXCJdLFwiY2xpZW50VHlwZVwiOntcImNvZGVcIjoyLFwiZGVzXCI6XCJQQ1wifSxcImdyYW50VHlwZVwiOlwiQmVhcmVyIFwiLFwic3lzdGVtSWRcIjpcInNhYXNcIixcImNhcHRjaGFUb2tlbkNhY2hlS2V5XCI6XCIxMzY4MDU4NjE5MzpQQzpDYXB0Y2hhIFwifSIsImF1ZCI6ImFueW9uZSIsImp0aSI6ImIyOTQzZDY5LWY0YTYtNGE2ZS05ZjM4LTUzOWU4YTBkYWVmNyIsImlzcyI6ImJneSIsIm5iZiI6MTYyMTIxNTc3OCwiaWF0IjoxNjIxMjE1Nzc4LCJleHAiOjMyNDI0MzE1NTZ9.e15ef-Yr2rwE3s5D4xnHMqkVxSzd7NWRpEFyju9R5YY"
    }
    r2 = requests.post("http://112.126.118.14:49301/api/so/order/page/pc?type=project",
                       data=data2,
                       headers=header2)
    print(r2.text)
