# -*- coding: utf-8 -*-
""" 
@Time    : 2021/9/8 18:00
@Author  : MaSai
@FileName: wwmainpage.py.py
@SoftWare: PyCharm
"""
from appium.webdriver.common.mobileby import MobileBy
from appium_pageobject.page.basepage import BasePage
from appium_pageobject.page.manager_page import ManagerPage


class WwMainPage(BasePage):
    """
    工作台界面
    """
    def goto_manager(self):
        # 点击企业管理
        self.find(MobileBy.XPATH,"//*[@text='管理企业']").click()
        return ManagerPage(self.driver)