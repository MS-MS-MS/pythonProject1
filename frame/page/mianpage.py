#!/usr/bin/python3.8.4 (python版本)
# -*- coding: utf-8 -*-
# @Author  : MS
# @Software: PyCharm
# @Time    : 2021/9/11 18:03
# @File    : mianpage.py
from appium.webdriver.common.mobileby import MobileBy

from frame.page.basepage import BasePage
from frame.page.quotationpage import QuotationPage


class MainPage(BasePage):
    """
    雪球主页
    """
    def goto_quotation(self):
        # 伪造一个弹框
        self.find(MobileBy.ID,"com.xueqiu.android:id/post_status").click()
        # 点击行情
        self.find(MobileBy.XPATH,"//*[@resource-id='android:id/tabs']//*[@text='行情']").click()
        return QuotationPage(self.driver)