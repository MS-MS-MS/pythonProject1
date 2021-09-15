# -*- coding: utf-8 -*-
""" 
@Time    : 2021/9/14 15:58
@Author  : MaSai
@FileName: memberinvitepage.py
@SoftWare: PyCharm
"""
import time

from appium.webdriver.common.mobileby import MobileBy
from app_pageobject.page.basepage import BasePage
from app_pageobject.page.contactaddpage import ContactAddPage


class MemberInvitePage(BasePage):
    """
    添加成员设置页面
    继承BasePage类
    """

    # def __init__(self, driver: WebDriver):
    #     # 构造函数接收参数
    #     # 实例化driver
    #     self.driver = driver

    def goto_contact(self):
        # 点击手动添加
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.find_and_click(MobileBy.XPATH, "//*[@text='手动输入添加']")
        # 前往添加成员界面ContactAdd
        return ContactAddPage(self.driver)

    def goto_Toast(self):
        """
        获取toast提示
        :return:
        """
        time.sleep(1)
        result=self.goto_toast_text()
        return result

