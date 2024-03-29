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

import pytest
import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait


def get_yaml():
    with open("tx_yaml/tx_add.yaml", encoding="utf-8") as f:
        date = yaml.safe_load(f)
        case = date["case"]
        ids = date["ids"]
        return case, ids


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
        self.driver.quit()

    def test_add(self):
        # 点击通讯录
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # 滑动查找到添加成员
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("添加成员").'
                                                        'instance(0));').click()
        # 点击手动添加
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        # # 填写姓名
        # time.sleep(2)
        self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.EditText' and @text='必填']").send_keys(
            "0001")
        # # 账号
        # self.driver.find_elements(MobileBy.ID,"com.tencent.wework:id/b09")[1].send_keys("0001")
        # # 选择性别
        # self.driver.find_elements(MobileBy.ID,"com.tencent.wework:id/b0h")[0].click()
        # #选择女
        # WebDriverWait(self.driver,5).until(lambda x:x.find_element(MobileBy.XPATH,"//*[@text='男']"))
        # self.driver.find_element(MobileBy.XPATH,"//*[@text='女']").click()
        # 填写手机号
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手机号']").send_keys("13500000001")
        # 保存
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("保存").'
                                                        'instance(0));').click()
        # print(self.driver.page_source)
        # print(self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'成功')]").text)
        # print(self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text)
        result = self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'成功')]").text
        assert result in "添加成功"

    @pytest.mark.parametrize("name,id,sex,phone", get_yaml()[0], ids=get_yaml()[1])
    def test_add_yaml(self, name, id, sex, phone):
        # 点击通讯录
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # 滑动查找到添加成员
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("添加成员").'
                                                        'instance(0));').click()
        # 点击手动添加
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        # # 填写姓名
        self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.EditText' and @text='必填']").send_keys(
            f"{name}")
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
        # print(self.driver.page_source)
        result = self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'成功')]").text
        assert result in "添加成功"
