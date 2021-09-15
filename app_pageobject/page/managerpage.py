# -*- coding: utf-8 -*-
""" 
@Time    : 2021/9/15 15:12
@Author  : MaSai
@FileName: managerpage.py
@SoftWare: PyCharm
"""
from appium.webdriver.common.mobileby import MobileBy

from app_pageobject.page.basepage import BasePage
from app_pageobject.page.enterprisecontactpage import EnterpriseContactPage


class ManagerPage(BasePage):
    """
    企业管理设置界面
    """
    def goto_enterprisecontact(self):
        # 点击成员与部门管理
        self.find_and_click(MobileBy.XPATH,"//*[@text='成员与部门管理']")
        return EnterpriseContactPage(self.driver)