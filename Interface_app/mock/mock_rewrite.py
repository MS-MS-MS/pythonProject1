# -*- coding: utf-8 -*-
""" 
@Time    : 2021/10/12 15:20
@Author  : MaSai
@FileName: mock_rewrite.py
@SoftWare: PyCharm
"""
'''
1. 简答题
题目：
（1）实现 MapLocal 修改雪球行情页的股票名称改为自己的名字（使用charles 和 mitmproxy 分别实现）
（2）实现 Rewrite 实现股票颜色变换的的边界值测试（使用charles 和 mitmproxy 分别实现）
（3）提交源码以及设置界面和效果的截图
'''
import json
from mitmproxy import http


# （1）实现 Rewrite 实现股票颜色变换的的边界值测试（使用charles 和 mitmproxy 分别实现）
def response(flow: http.HTTPFlow):
    # 设置过滤条件,修改特点的请求
    if "quote.json" in flow.request.pretty_url and "x=" in flow.request.pretty_url:
        # 取到响应返回的数据,保存到python 对象中
        print(flow.response.content)
        data = json.loads(flow.response.content)
        print(data)
        # 修改股票的名字以及股票颜色
        data["data"]["items"][0]['quote']['name']="MA"
        data["data"]["items"][0]['quote']['percent']="+5.0"
        data["data"]["items"][1]['quote']['name']="MA1"
        data["data"]["items"][1]['quote']['percent'] = "+6.0"
        data["data"]["items"][2]['quote']['name']="MA2"
        data["data"]["items"][2]['quote']['percent']="+0.0"
        # 把修改的数据赋值给response原始数据中
        flow.response.text = json.dumps(data)