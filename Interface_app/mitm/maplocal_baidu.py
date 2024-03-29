# -*- coding: utf-8 -*-
""" 
@Time    : 2021/10/9 15:18
@Author  : MaSai
@FileName: maplocal_baidu.py
@SoftWare: PyCharm
"""
from mitmproxy import http

"""
mitmproxy maplocal 使用
MapLocal （本地）是将指定的网络请求重定向到本地文件。
拦截指定的网络请求,返回本地请求结果
"""
from mitmproxy import http

def request(flow: http.HTTPFlow) -> None:
    # 发起请求,判断url 是不是预期的URL
    if flow.request.pretty_url == "https://www.baidu.com/":
        # 创造一个response
        flow.response = http.Response.make(
            200,  # (optional) status code
            b"Hello World",  # (optional) content
            {"Content-Type": "text/html"}  # (optional) headers
        )