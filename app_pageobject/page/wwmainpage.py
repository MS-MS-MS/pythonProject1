# -*- coding: utf-8 -*-
""" 
@Time    : 2021/9/15 15:11
@Author  : MaSai
@FileName: wwmainpage.py
@SoftWare: PyCharm
"""
from appium.webdriver.common.mobileby import MobileBy

from app_pageobject.page.basepage import BasePage
from app_pageobject.page.managerpage import ManagerPage


class WwMainPage(BasePage):
    """
    工作台界面
    """
    def goto_manager(self):
        # 点击企业管理
        self.find_and_click(MobileBy.XPATH,"//*[@text='管理企业']")
        return ManagerPage(self.driver)