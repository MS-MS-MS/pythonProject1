#!/usr/bin/python3.8.4 (python版本)
# -*- coding: utf-8 -*-
# @Author  : MS
# @Software: PyCharm
# @Time    : 2021/9/11 17:53
# @File    : basepage.py

"""
处理黑名单简单框架联系
"""
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from frame.page.blacklist import tmp
# from frame.page.blacklist import Decorator


class BasePage:
    # 黑名单列表
    blacklist=[(MobileBy.ID,"com.xueqiu.android:id/iv_close")]
    def __init__(self, driver: WebDriver = None):
        if driver == None:
            desired_caps = {}
            # 告诉Appium使用的那个移动平台
            desired_caps['platformName'] = 'Android'
            # 告诉Appium是当前平台的系统版本
            desired_caps['platformVersion'] = '7.1'
            # 使用的设备是什么 android 可以随便填写
            desired_caps['deviceName'] = '127.0.0.1:21503'
            # 当前启动的包名
            desired_caps['appPackage'] = 'com.xueqiu.android'
            # 当前启动的页面命
            desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
            # 保证操作的信息不被重置，时系统一致保持登陆状态
            desired_caps["noReset"] = 'true'
            # 连接服务 传入Desired Capabilities
            # localhost标识本机
            # 4723 标识端口
            # wd是webdriver缩写
            # hub 表示是指主节点、中心节点
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        else:
            self.driver = driver

    def goto_mainpage(self):
        # 前往雪球主页
        from frame.page.mianpage import MainPage
        return MainPage(self.driver)

    @tmp
    def find(self, by, value=None):
        """
        查找元素方法
        传入 定位类型，以及属性
        """
        if value == None:
            result = self.driver.find_element(*by)
        else:
            result = self.driver.find_element(by, value)
        return result
        # try:
        #     # 如果传入的vaule为空则需要进行解包操作
        #     if value == None:
        #         result = self.driver.find_element(*by)
        #     else:
        #         result = self.driver.find_element(by, value)
        #     return result
        # except Exception as e:
        #     #捕捉异常
        #     for blacklist in self.blacklist:
        #         #查找黑名单列表
        #         # 这里要使用find_elements
        #         ele=self.driver.find_elements(*blacklist)
        #         if len(ele)>0:
        #             # len(ele)>0 证明查找到黑名单
        #             ele[0].click()
        #             return self.find(by,value)
        #     # 没有查找到黑名单元素直接抛异常
        #     raise e




