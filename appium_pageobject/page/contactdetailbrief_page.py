# -*- coding: utf-8 -*-
""" 
@Time    : 2021/9/8 17:06
@Author  : MaSai
@FileName: contactdetailbrief_page.py
@SoftWare: PyCharm
"""
from appium.webdriver.common.mobileby import MobileBy

from appium_pageobject.page.ContactDetailSettingPage import ContactDetailSettingPage
from appium_pageobject.page.basepage import BasePage


class ContactDetailBriefPage(BasePage):
    """
    个人信息界面
    """
    def goto_setting(self):
        #点击三个点按钮
        self.find(MobileBy.ID,"com.tencent.wework:id/hc9").click()
        return ContactDetailSettingPage(self.driver)