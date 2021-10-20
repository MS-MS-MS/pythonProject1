# -*- coding: utf-8 -*-
""" 
@Time    : 2021/10/19 21:19
@Author  : MaSai
@FileName: mock_maplocal.py
@SoftWare: PyCharm
"""
# 实现 MapLocal 修改雪球行情页的股票名称改为自己的名字（使用charles 和 mitmproxy 分别实现）
from mitmproxy import http


def request(flow:http.HTTPFlow):
    # 判断是否是要修改的接口
    if "quote.json" in flow.request.pretty_url and "x=" in flow.request.pretty_url:
        # 读本地json文件
        with open("data.json") as f:
            # 创建一个接口返回
            flow.response=http.Response.make(
                200,
                f.read(),
                {"Content-Type": "application/json"}
            )



