# -*- coding: utf-8 -*-
""" 
@Time    : 2021/9/7 16:27
@Author  : MaSai
@FileName: mail_list_page.py
@SoftWare: PyCharm
"""
from appium.webdriver.common.mobileby import MobileBy

from appium_pageobject.page.add_member_page import Add_Member_Page
from appium_pageobject.page.basepage import BasePage
from appium_pageobject.page.contactdetailbrief_page import ContactDetailBriefPage


class MailListPage(BasePage):
    """
    通讯录页面
    """
    def goto_add_member(self):
        """
        添加成员操作
        :return:
        """
        self.uiautomator("添加成员").click()
        return Add_Member_Page(self.driver)

    def goto_del(self,name):
        """
        删除成员操作
        :param name:传入要删除的人员名称
        :return:
        """
        self.find(MobileBy.XPATH,f"//*[@text='{name}']").click()
        return ContactDetailBriefPage(self.driver)

