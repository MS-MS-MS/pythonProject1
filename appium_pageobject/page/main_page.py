# -*- coding: utf-8 -*-
""" 
@Time    : 2021/9/8 17:49
@Author  : MaSai
@FileName: main_page.py
@SoftWare: PyCharm
"""
from appium.webdriver.common.mobileby import MobileBy

from appium_pageobject.page.basepage import BasePage
from appium_pageobject.page.wwmainpage import WwMainPage


class MainPage(BasePage):
    """
    企业微信主页
    """
    def goto_mail_list(self):
        """
        点击前往通讯录界面
        :return:
        """
        # 点击通讯录
        # self.find(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.step_ymal("../tx_yaml/main.ymal", "goto_mail_list")
        from appium_pageobject.page.mail_list_page import MailListPage
        return MailListPage(self.driver)

    def goto_workbench(self):
        """
        点击前往工作台
        :return:
        """
        self.find(MobileBy.XPATH, "//*[@text='工作台']").click()
        return WwMainPage(self.driver)