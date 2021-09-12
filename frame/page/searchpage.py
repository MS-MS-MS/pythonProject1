#!/usr/bin/python3.8.4 (python版本)
# -*- coding: utf-8 -*-
# @Author  : MS
# @Software: PyCharm
# @Time    : 2021/9/11 18:17
# @File    : searchpage.py
from frame.page.basepage import BasePage


class SearchPage(BasePage):
    """
    搜索界面
    """
    def goto_usearch(self):
        result="搜索成功"
        return result