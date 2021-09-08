# -*- coding: utf-8 -*-
""" 
@Time    : 2021/9/7 16:09
@Author  : MaSai
@FileName: basepage.py
@SoftWare: PyCharm
"""
import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver



"""
1. 简答题
题目：
(1)添加联系人测试用例 实现PO封装
(2)【选做】删除联系人用例 实现PO封装
(3)将日志 保存到日志文件中，打印输出日志时间
(4)通过参数化实现多条用例自动生成，将测试数据保存到yaml 文件中。
"""


class BasePage:
    """
    基类用于封装基础的连接，查找方法封装 数据参数化的封装
    """

    def __init__(self, driver: WebDriver = None):
        """
        driver:WebDriver
        定义一个类型
        导入 from appium.webdriver.webdriver import WebDriver
        :param driver:
        """
        if driver == None:
            desired_caps = {}
            # 告诉Appium使用的那个移动平台
            desired_caps['platformName'] = 'Android'
            # 告诉Appium是当前平台的系统版本
            desired_caps['platformVersion'] = '7.1'
            # 使用的设备是什么 android 可以随便填写
            desired_caps['deviceName'] = '127.0.0.1:21503'
            # 当前启动的包名
            desired_caps['appPackage'] = 'com.tencent.wework'
            # 当前启动的页面命
            desired_caps['appActivity'] = 'com.tencent.wework.launch.WwMainActivity'
            # 保证操作的信息不被重置，时系统一致保持登陆状态
            desired_caps["noReset"] = 'true'
            # 连接服务 传入Desired Capabilities # localhost标识本机# 4723 标识端口# wd是webdriver缩写# hub 表示是指主节点、中心节点
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            self.driver.implicitly_wait(5)
        else:
            self.driver = driver



    def goto_main_page(self):
        from appium_pageobject.page.main_page import MainPage
        return MainPage(self.driver)

    def find(self, by, value):
        """
        查找元素方法
        :param by:
        :param value:
        :return:
        """
        print(by)
        print(value)
        return self.driver.find_element(by, value)

    def finds(self, by, value):
        """
        查找多个元素方法
        :param by:
        :param value:
        :return:
        """
        return self.driver.find_elements(by, value)

    def uiautomator(self, text):
        # 滑动查找
        return self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                               'scrollable(true).instance(0)).'
                                                               f'scrollIntoView(new UiSelector().text("{text}").'
                                                               'instance(0));')

    def step_ymal(self, path, funcname):
        """
        解析测试步骤的方法
        :param path: 需要传入测试步骤的yaml文件
        :param funcname: 传入当前函数名
        :return: 测试步骤数据
        """
        with open(path, encoding="utf-8") as f:
            date = yaml.safe_load(f)
            return self.step(date[funcname])

    def step(self, date):
        """
        按照测试步骤进行操作
        :param date:
        :return:
        """
        for step in date:
            if step["action"] == "click":
                self.find(step["by"], step["vaule"]).click()
            elif step["action"] == "send_keys":
                self.find(step["by"], step["vaule"]).send_keys(step["send_keys"])

# def step_ymal(path,funcname):
#         """
#         解析测试步骤的方法
#         :param path: 需要传入测试步骤的yaml文件
#         :return:
#         """
#         with open(path, encoding="utf-8") as f:
#             date = yaml.safe_load(f)
#             dates=date[funcname]
#             return step(dates)
# def step(date):
#         """
#         按照测试步骤进行操作
#         :param date:
#         :return:
#         """
#         for step in date:
#             print(step)
#             if step["action"] == "click":
#                 print(1)
#             elif step["action"] == "send_keys":
#                 print(2)
# def test_y():
#     print(step_ymal("../tx_yaml/main.ymal","goto_mail_list"))
