# -*- coding: utf-8 -*-
""" 
@Time    : 2021/10/9 17:27
@Author  : MaSai
@FileName: maplocal_xuqiu.py
@SoftWare: PyCharm
"""
import json

from mitmproxy import http

"""
对第一个股票保持原样
对第二个股票名字加长一倍
对第三个股票名字变成空
"""


def response(flow: http.HTTPFlow):
    # 设置过滤条件,修改特点的请求
    if "quote.json" in flow.request.pretty_url and "x=" in flow.request.pretty_url:
        # 取到响应返回的数据,保存到python 对象中
        print(flow.response.content)
        data = json.loads(flow.response.content)
        print(data)
        # 修改一支股票的名字
        # data["data"]["items"][0]['quote']['name']="456"
        name = data["data"]["items"][1]['quote']['name']
        data["data"]["items"][1]['quote']['name'] = name * 2
        data["data"]["items"][2]['quote']['name'] = ""
        # 把修改的数据赋值给response原始数据中
        flow.response.text = json.dumps(data)
