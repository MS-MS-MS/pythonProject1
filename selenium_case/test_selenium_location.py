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
        # self.driver.quit()
        pass

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

    def test_XPATH(self):
        # self.driver.find_element_by_id("kw").send_keys("ds")
        # self.driver.find_element_by_id("su").click()
        # xpath=self.driver.find_element(By.XPATH,"//sanp[text()='按图片搜索']")
        # print(xpath)
        self.driver.find_element_by_id("kw").send_keys("as")
        """
        定位百度一下位置
        在form标签id=form的字节点span的class=='bg s_btn_wr的子节点inputd的@id='su'元素
        from→span→input
        爷爷定位孙子元素
        form下的孙子节点input
        """
        self.driver.find_element(By.XPATH,"//form[@id='form']/span[@class='bg s_btn_wr']/input[@id='su']").click()
        self.driver.find_element(By.XPATH,"//form[@id='form']//input[@id='su']").click()
