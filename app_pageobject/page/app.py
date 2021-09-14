# -*- coding: utf-8 -*-
""" 
@Time    : 2021/9/14 15:38
@Author  : MaSai
@FileName: app.py
@SoftWare: PyCharm
"""
from appium import webdriver




class App:
    """
    App类
    用于封装APP启动 重启 关闭方法
    """
    def start_app(self):
        """
        启动App
        :return:
        """
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
        return self


    def restart_app(self):
        """
        重启app
        :return:
        """
        pass

    def goto_main(self):
        """
        前往主页方法
        :return:
        """
        from app_pageobject.page.mainpage import MainPage
        # 进行driver传递
        return MainPage(self.driver)