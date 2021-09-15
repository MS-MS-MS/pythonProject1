# -*- coding: utf-8 -*-
""" 
@Time    : 2021/9/15 10:41
@Author  : MaSai
@FileName: basepage.py
@SoftWare: PyCharm
"""
import logging

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage:
    """
    基类 用于封装driver find方法
    """
    def __init__(self, driver: WebDriver=None):
        # driver 初始要设置成None
        # 实例化driver
        self.driver = driver

    def find(self,by,vaule):
        """
        查找元素
        :param by:
        :param vaule:
        :return:
        """
        self.log_info("find")
        self.log_info(by)
        self.log_info(vaule)
        if vaule==None:
            result=self.driver.find_element(*by)
        else:
            result=self.driver.find_element(by,vaule)
        return result


    def find_and_click(self,by,vaule):
        """
        查找元素并点击
        :param by:
        :param vaule:
        :return:
        """
        self.log_info("find_and_click")
        self.log_info(by)
        self.log_info(vaule)
        if vaule==None:
            self.driver.find_element(*by).click()
        else:
            self.driver.find_element(by,vaule).click()

    def find_and_send(self,by,vaule,text):
        """
        查找元素并填写
        :param by:
        :param vaule:
        :return:
        """
        self.log_info("find_and_send")
        self.log_info(by)
        self.log_info(vaule)
        self.log_info(text)
        if vaule==None:
            self.driver.find_element(*by).send_keys(text)
        else:
            self.driver.find_element(by,vaule).send_keys(text)

    def slide_click(self, text):
        # 滑动查找
        self.log_info("slide_click")
        self.log_info(text)
        return self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                               'scrollable(true).instance(0)).'
                                                               f'scrollIntoView(new UiSelector().text("{text}").'
                                                               'instance(0));').click()
    def goto_toast_text(self):
        # Toast消失提示框
        self.log_info("goto_toast_text")
        result=self.driver.find_element(MobileBy.XPATH,"//*[@class='android.widget.Toast']").get_attribute('text')
        return result

    def log_info(self, message):
        logging.info(message)

