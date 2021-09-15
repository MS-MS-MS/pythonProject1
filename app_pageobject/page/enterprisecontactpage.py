# -*- coding: utf-8 -*-
""" 
@Time    : 2021/9/15 15:14
@Author  : MaSai
@FileName: enterprisecontactpage.py
@SoftWare: PyCharm
"""
from appium.webdriver.common.mobileby import MobileBy

from app_pageobject.page.basepage import BasePage
from app_pageobject.page.delmemberpage import DelMemberPage


class EnterpriseContactPage(BasePage):
    """
    管理通讯录界面
    """
    def goto_del(self, name):
        """
        删除成员操作
        :param name:传入要删除的人员名称
        :return:
        """
        self.find_and_click(MobileBy.XPATH, f"//*[@text='{name}']")
        return DelMemberPage(self.driver)