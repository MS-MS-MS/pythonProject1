# -*- coding: utf-8 -*-
""" 
@Time    : 2021/9/15 15:16
@Author  : MaSai
@FileName: delmemberpage.py
@SoftWare: PyCharm
"""
from appium.webdriver.common.mobileby import MobileBy

from app_pageobject.page.basepage import BasePage


class DelMemberPage(BasePage):
    """
    删除操作
    """
    def del_member(self):
        # 点击删除成员
        self.slide_click("删除成员")
        # 点击确定
        self.find_and_click(MobileBy.XPATH,"//*[@text='确定']")