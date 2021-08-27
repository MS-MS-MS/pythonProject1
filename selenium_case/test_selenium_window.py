# -*- coding: utf-8 -*-
""" 
@Time    : 2021/8/27 10:33
@Author  : MaSai
@FileName: test_selenium_window.py
@SoftWare: PyCharm
"""
from selenium_case.base import Base

"""
网页窗口切换的操作
获取当前窗口
self.driver.current_window_handle、
获取所有窗口
self.driver.window_handles
指定窗口跳转 要传入指定的窗口
self.driver.switch_to_window(window[0])
"""

from time import sleep




class Test_Window(Base):
    def test_window(self):
        self.driver.get("https://www.baidu.com/")
        # 点击登录按钮
        self.driver.find_element_by_xpath('//*[@id="s-top-loginbtn"]').click()
        # 获取当前窗户
        print("1 " + self.driver.current_window_handle)

        print("2 " + self.driver.current_window_handle)
        # 点击立即注册
        self.driver.find_element_by_xpath('//*[@id="passport-login-pop-dialog"]/div/div/div/div[3]/a').click()
        # self.driver.find_element_by_link_text("立即注册").click()
        sleep(5)
        # 获取当前窗口
        print("立即注册" + self.driver.current_window_handle)
        # 进行点击操作，页面进行跳转，在获取当前的所以窗口
        # print("立即注册" + self.driver.window_handles)
        # 创建一个变量，用于获取当前的所以窗口
        windows = self.driver.window_handles
        # 进行窗口跳转 指定的跳转窗口
        self.driver.switch_to_window(windows[-1])

        sleep(5)
        # 在注册的节目输入用户名和密码
        self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_4__userName"]').send_keys("username")
        self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_4__phone"]').send_keys("12111")
        # 强制等待
        sleep(3)
        # 在切换窗口到首页,进行用户名登录
        self.driver.switch_to_window(windows[0])
        self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_11__footerULoginBtn"]').click()
        self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_11__userName"]').send_keys("username")
        self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_11__password"]').send_keys("123456")
        self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_11__submit"]').click()
        sleep(5)