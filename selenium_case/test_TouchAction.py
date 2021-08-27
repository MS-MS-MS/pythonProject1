# -*- coding: utf-8 -*-
""" 
@Time    : 2021/8/27 16:35
@Author  : MaSai
@FileName: test_TouchAction.py
@SoftWare: PyCharm
"""
"""
TouchAction 用于H5网页的操作
"""
from selenium import webdriver
from selenium.webdriver import  TouchActions


class Test_TouchAction():
    def setup(self):
        """
        什么是 chromeoptions
        chromeoptions 是一个方便控制 chrome 启动时属性的类。通过 selenium 的源码，可以看到，chromeoptions 主要提供如下的功能：
        （1）设置 chrome 二进制文件位置 (binary_location)
        （2）添加启动参数 (add_argument)
        （3）添加扩展应用 (add_extension, add_encoded_extension)
        （4）添加实验性质的设置参数 (add_experimental_option)
        （5）设置调试器地址 (debugger_address)
        :return:
        """
        option =webdriver.ChromeOptions()
        option.add_experimental_option("w3c",False)
        self.driver=webdriver.Chrome(options=option)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_touch(self):
        self.driver.get("https://www.baidu.com/")
        # 定位元素位置
        send=self.driver.find_element_by_xpath('//*[@id="kw"]')
        search=self.driver.find_element_by_xpath('//*[@id="su"]')
        # 输入
        send.send_keys("selenium测试")
        # 引入TouchActions
        actions=TouchActions(self.driver)
        # tap 点击
        actions.tap(search)
        # 模拟滑动  要传入初始滑动的位置  x的偏移量 y的偏移量
        actions.scroll_from_element(send,0,10000)
        actions.perform()