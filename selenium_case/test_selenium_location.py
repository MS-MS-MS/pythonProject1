# -*- coding: utf-8 -*-
""" 
@Time    : 2021/8/26 17:08
@Author  : MaSai
@FileName: test_selenium_location.py
@SoftWare: PyCharm
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_wait():
    def setup(self):
        # 初始化driver
        self.driver = webdriver.Chrome()
        # 隐式等待
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.get("https://www.baidu.com")

    def teardown(self):
        # 关闭driver
        self.driver.quit()

    def test_location(self):
        self.driver.find_element_by_id("kw").send_keys("selenium")
        self.driver.find_element_by_id("su").click()
        self.driver.find_element(By.XPATH,"//*[@class='toindex']").click()
    def test_location_1(self):
        self.driver.find_element_by_id("kw").send_keys("dac")
        self.driver.find_element_by_id("su").click()
        # self.driver.find_element(By.XPATH,"//*[@id='1']").click()
        # self.driver.find_element(By.XPATH,"//*[@id='j-wgt-userbar']//li[1]").click()
        print(1)
