# -*- coding: utf-8 -*-
""" 
@Time    : 2021/9/14 15:58
@Author  : MaSai
@FileName: memberinvitepage.py
@SoftWare: PyCharm
"""
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from app_pageobject.page.contactaddpage import ContactAddPage


class MemberInvitePage:
    """
    添加成员设置页面
    """

    def __init__(self, driver: WebDriver):
        # 构造函数接收参数
        # 实例化driver
        self.driver = driver

    def goto_contact(self):
        # 点击手动添加
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        # 前往添加成员界面ContactAdd
        return ContactAddPage(self.driver)
