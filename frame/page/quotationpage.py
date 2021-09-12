#!/usr/bin/python3.8.4 (python版本)
# -*- coding: utf-8 -*-
# @Author  : MS
# @Software: PyCharm
# @Time    : 2021/9/11 18:14
# @File    : quotationpage.py
from appium.webdriver.common.mobileby import MobileBy

from frame.page.basepage import BasePage
from frame.page.searchpage import SearchPage


class QuotationPage(BasePage):
    """
    行情界面
    """
    def goto_search(self):
        # 点击搜索操作
        self.find(MobileBy.ID,"com.xueqiu.android:id/action_search").click()
        return SearchPage(self.driver)