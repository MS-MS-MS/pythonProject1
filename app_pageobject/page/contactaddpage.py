# -*- coding: utf-8 -*-
""" 
@Time    : 2021/9/14 16:01
@Author  : MaSai
@FileName: contactaddpage.py
@SoftWare: PyCharm
"""
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from faker import Faker


class ContactAddPage:
    """
    添加成员页面
    """
    def __init__(self, driver: WebDriver):
        # 构造函数接收参数
        # 实例化driver
        self.driver = driver

    def goto_add(self):
        """
        模拟手动输入添加联系人操作
        :return:
        """
        fake = Faker("zh_CN")
        name=fake.name()
        phone=fake.phone_number()
        # self.driver.find_element(MobileBy.XPATH,"//*[@class='android.widget.RelativeLayout']/[@text='必填']").send_keys(name)
        # self.driver.find_element(MobileBy.XPATH,"//*[@text='帐号']..//[@text='选填']").send_keys(name)

        # # 填写姓名
        self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.EditText' and @text='必填']").send_keys(f"{name}")
        # 填写手机号
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手机号']").send_keys(f"{phone}")