# -*- coding: utf-8 -*-
""" 
@Time    : 2021/9/14 15:44
@Author  : MaSai
@FileName: mainpage.py
@SoftWare: PyCharm
"""
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from app_pageobject.page.maillistpage import MaillistPage


class MainPage:
    """
    企业微信主页类
    """

    def __init__(self, driver: WebDriver):
        # 构造函数接收参数
        # 实例化driver
        self.driver = driver

    def goto_maillist(self):
        """
        前往通讯录
        :return:
        """
        # 点击通讯录
        self.driver.find_element(MobileBy.XPATH,"//*[@text='通讯录']").click()
        # 前往联系人列表界面
        return MaillistPage(self.driver)
