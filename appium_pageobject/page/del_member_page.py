# -*- coding: utf-8 -*-
""" 
@Time    : 2021/9/8 17:23
@Author  : MaSai
@FileName: del_member_page.py.py
@SoftWare: PyCharm
"""
from appium.webdriver.common.mobileby import MobileBy

from appium_pageobject.page.basepage import BasePage


class DelMemberPage(BasePage):
    """
    删除操作
    """
    def del_member(self):
        # 点击删除成员
        self.uiautomator("删除成员").click()
        # 点击确定
        self.find(MobileBy.XPATH,"//*[@text='确定']").click()
