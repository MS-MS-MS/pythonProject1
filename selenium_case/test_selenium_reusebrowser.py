# -*- coding: utf-8 -*-
""" 
@Time    : 2021/8/27 14:48
@Author  : MaSai
@FileName: test_selenium_reusebrowser.py
@SoftWare: PyCharm
复用浏览器方法
"""
import time
from typing import List, Dict
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
import json


class TestChains():
    # def setup(self):
    #     # 创建一个选项options
    #     self.opt = webdriver.ChromeOptions()
    #     # 创建一个远程ip端口9222
    #     self.opt.debugger_address = "127.0.0.1:1222"

    def teardown(self):
        self.driver.quit()

    def test_login(self):
        # 调用options
        opt = Options()
        # 设置复用浏览器的端口，地址
        opt.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=opt)
        # 打开企业微信主页
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # 获取当前登录之后的微信页面的cookies
        cookies = self.driver.get_cookies()
        with open("cookies.txt", "w") as f:
        # dump方法把cookies存到文件cookies.txt中
            json.dump(cookies, f)
        print("ok")

    def test_weixin(self):
        self.driver = webdriver.Chrome()
        # 先打开企业微信的页面，才能传cookies进去
        self.driver.get("https://work.weixin.qq.com/")

        with open("cookies.txt", "r") as f:
            # 从文件获取cookies，并转化成list对象
            cookies: List[Dict] = json.load(f)
        # 遍历每一条cookies，把登录的cookies传入到企业微信中
        for cookie in cookies:
            # 由于selenium的cookies不支持expiry，所以需要去掉
            if "expiry" in cookie.keys():
                # dict支持pop的删除函数
                cookie.pop("expiry")
            # 添加cookies
            self.driver.add_cookie(cookie)
        # 再打开企业微信登录后的页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        sleep(5)
