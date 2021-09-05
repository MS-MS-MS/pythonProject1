#!/usr/bin/python3.8.4 (python版本)
# -*- coding: utf-8 -*-
# @Author  : MS
# @Software: PyCharm
# @Time    : 2021/9/5 9:46
# @File    : test_tx_add.py
"""
1.简答题
题目：
（1）实现添加联系人测试用例 （灵活使用元素定位，并添加断言）
（2）实现添加多条联系人测试用例
"""

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy



class Test_Tx:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1'
        desired_caps['deviceName'] = '127.0.0.1:21503'
        # com.android.settings/com.android.settings.Settings
        desired_caps['appPackage'] = 'com.tencent.wework'
        desired_caps['appActivity'] = 'com.tencent.wework.launch.WwMainActivity'
        desired_caps["noReset"] = 'true'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)
    def teardown(self):
        # self.driver.quit()
        pass

    def test_add(self):
        self.driver.find_element(MobileBy.XPATH,"//*[@text='通讯录']").click()
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("添加成员").'
                                                        'instance(0));').click()



