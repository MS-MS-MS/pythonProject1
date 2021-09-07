# -*- coding: utf-8 -*-
""" 
@Time    : 2021/9/7 16:27
@Author  : MaSai
@FileName: mail_list_page.py
@SoftWare: PyCharm
"""
from appium_pageobject.page.add_member_page import Add_Member_Page
from appium_pageobject.page.basepage import BasePage


class MailListPage(BasePage):
    def goto_add_member(self):
        # 滑动查找到添加成员
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("添加成员").'
                                                        'instance(0));').click()
        return Add_Member_Page(self.driver)
