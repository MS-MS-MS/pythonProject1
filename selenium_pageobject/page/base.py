# -*- coding: utf-8 -*-
""" 
@Time    : 2021/8/27 16:04
@Author  : MaSai
@FileName: base.py
@SoftWare: PyCharm
"""
from selenium import webdriver


class Base:
    def setup(self):
        #初始化driver
        self.driver=webdriver.Chrome()
        # 隐式等待
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        # 关闭driver
        self.driver.quit()