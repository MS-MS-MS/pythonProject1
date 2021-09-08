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
    def __init__(self,driver:webdriver=None):
        if driver==None:
            desired_caps={}
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
            self.driver=driver

    def goto_mail_list(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        from appium_pageobject.page.mail_list_page import MailListPage
        return MailListPage(self.driver)

    def get_yaml(self):
        with open("../tx_yaml/tx_add.yaml", encoding="utf-8") as f:
            date=yaml.safe_load(f)
            case=date["case"]
            ids=date["ids"]
        return case,ids



