# -*- coding: utf-8 -*-
""" 
@Time    : 2021/9/7 16:41
@Author  : MaSai
@FileName: add_member_page.py
@SoftWare: PyCharm
"""
from appium.webdriver.common.mobileby import MobileBy

from appium_pageobject.page.basepage import BasePage
from appium_pageobject.page.contactadd_page import ContactAddPage


class Add_Member_Page(BasePage):
    def goto_membernvitemenu(self):
        # 点击手动添加
        # self.find(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.step_ymal("../tx_yaml/membernvitemenu.ymal","goto_membernvitemenu")
        return ContactAddPage(self.driver)

    def goto_toast(self):
        result = self.find(MobileBy.XPATH, "//*[contains(@text,'成功')]").text
        return result
