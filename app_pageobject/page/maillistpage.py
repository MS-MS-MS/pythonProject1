# -*- coding: utf-8 -*-
""" 
@Time    : 2021/9/14 15:53
@Author  : MaSai
@FileName: maillistpage.py
@SoftWare: PyCharm
"""

from app_pageobject.page.basepage import BasePage
from app_pageobject.page.memberinvitepage import MemberInvitePage


class MaillistPage(BasePage):
    """
    通讯录界面
    继承BasePage类
    """

    # def __init__(self, driver: WebDriver):
    #     # 构造函数接收参数
    #     # 实例化driver
    #     self.driver = driver

    def goto_addmember(self):
        # 点击添加成员
        # self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
        #                                                        'scrollable(true).instance(0)).'
        #                                                        'scrollIntoView(new UiSelector().text("添加成员").'
        #                                                        'instance(0));').click()
        #使用封装滑动查找方法
        self.slide_click("添加成员")
        # 前往添加成员设置界面
        return MemberInvitePage(self.driver)
