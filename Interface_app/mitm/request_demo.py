# -*- coding: utf-8 -*-
""" 
@Time    : 2021/10/9 14:42
@Author  : MaSai
@FileName: request_demo.py
@SoftWare: PyCharm
"""
from mitmproxy import http


# request 方法名不可被改变
# 修改方法名 mitmproxy 不识别
def request(flow:http.HTTPFlow):
    # 增加请求头的头信息
    flow.request.headers["myheader"]="ms"
