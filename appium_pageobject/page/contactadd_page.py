# -*- coding: utf-8 -*-
""" 
@Time    : 2021/9/7 16:46
@Author  : MaSai
@FileName: contactadd_page.py
@SoftWare: PyCharm
"""
import pytest
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from appium_pageobject.page.basepage import BasePage


class ContactAddPage(BasePage):
    """
    添加成员信息操作
    """

    def goto_contact(self, name, id, sex, phone):
        # # 填写姓名
        self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.EditText' and @text='必填']").send_keys(f"{name}")
        # # 账号
        self.driver.find_elements(MobileBy.ID, "com.tencent.wework:id/b09")[1].send_keys(f"{id}")
        # 选择性别
        self.driver.find_elements(MobileBy.ID, "com.tencent.wework:id/b0h")[0].click()
        # 选择女
        WebDriverWait(self.driver, 5).until(lambda x: x.find_element(MobileBy.XPATH, "//*[@text='男']"))
        if sex == "男":
            self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        else:
            self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
        # 填写手机号
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手机号']").send_keys(f"{phone}")
        # 保存
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("保存").'
                                                        'instance(0));').click()
        from appium_pageobject.page.add_member_page import Add_Member_Page
        return Add_Member_Page(self.driver)
