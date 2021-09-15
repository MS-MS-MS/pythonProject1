# -*- coding: utf-8 -*-
""" 
@Time    : 2021/9/14 15:44
@Author  : MaSai
@FileName: mainpage.py
@SoftWare: PyCharm
"""
from appium.webdriver.common.mobileby import MobileBy
from app_pageobject.page.basepage import BasePage
from app_pageobject.page.maillistpage import MaillistPage
from app_pageobject.page.wwmainpage import WwMainPage


class MainPage(BasePage):
    """
    企业微信主页类
    继承BasePage
    """

    # def __init__(self, driver: WebDriver):
    #     # 构造函数接收参数
    #     # 实例化driver
    #     self.driver = driver

    def goto_maillist(self):
        """
        前往通讯录
        :return:
        """
        # 点击通讯录
        # self.driver.find_element(MobileBy.XPATH,"//*[@text='通讯录']").click()
        # 使用封装的find_and_click
        self.find_and_click(MobileBy.XPATH,"//*[@text='通讯录']")
        # 前往联系人列表界面
        return MaillistPage(self.driver)

    def goto_workbench(self):
        """
        点击前往工作台
        :return:
        """
        self.find_and_click(MobileBy.XPATH, "//*[@text='工作台']")
        return WwMainPage(self.driver)