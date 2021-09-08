# -*- coding: utf-8 -*-
""" 
@Time    : 2021/9/8 18:11
@Author  : MaSai
@FileName: enterprisecontact_page.py
@SoftWare: PyCharm
"""
from appium.webdriver.common.mobileby import MobileBy

from appium_pageobject.page.basepage import BasePage
from appium_pageobject.page.del_member_page import DelMemberPage


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
        self.find(MobileBy.XPATH, f"//*[@text='{name}']").click()
        return DelMemberPage(self.driver)