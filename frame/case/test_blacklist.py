#!/usr/bin/python3.8.4 (python版本)
# -*- coding: utf-8 -*-
# @Author  : MS
# @Software: PyCharm
# @Time    : 2021/9/11 18:19
# @File    : test_blacklist.py
from frame.page.basepage import BasePage


class TestFrame:
    """
    测试类方法
    """

    def setup(self):
        # 实例化BasePage类
        self.main = BasePage()

    def test_case(self):
        result=self.main.goto_mainpage().goto_quotation().goto_search().goto_usearch()
        assert result in "搜索成功"


#
# def tmp(func):
#     def wrapper(*args,**kwargs):
#         print("这是装饰的增强函数")
#         func(*args,**kwargs)
#         print("after")
#     return wrapper
#
#
# @tmp
# def a(a1):
#     print(a1)
#
# def test_a():
#     a(20)
