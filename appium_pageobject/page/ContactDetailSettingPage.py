# -*- coding: utf-8 -*-
""" 
@Time    : 2021/9/8 17:19
@Author  : MaSai
@FileName: ContactDetailSettingPage.py.py
@SoftWare: PyCharm
"""
from appium.webdriver.common.mobileby import MobileBy

from appium_pageobject.page.basepage import BasePage
from appium_pageobject.page.del_member_page import DelMemberPage


class ContactDetailSettingPage(BasePage):
    """
    个人信息设置界面
    """
    def goto_contactedit(self):
        #点击编辑成员
        self.find(MobileBy.XPATH,"//*[@text='编辑成员']").click()
        return DelMemberPage(self.driver)
