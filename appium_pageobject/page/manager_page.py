# -*- coding: utf-8 -*-
""" 
@Time    : 2021/9/8 18:07
@Author  : MaSai
@FileName: manager_page.py
@SoftWare: PyCharm
"""
from appium.webdriver.common.mobileby import MobileBy

from appium_pageobject.page.basepage import BasePage
from appium_pageobject.page.enterprisecontact_page import EnterpriseContactPage


class ManagerPage(BasePage):
    """
    企业管理设置界面
    """
    def goto_enterprisecontact(self):
        # 点击成员与部门管理
        self.find(MobileBy.XPATH,"//*[@text='成员与部门管理']").click()
        return EnterpriseContactPage(self.driver)