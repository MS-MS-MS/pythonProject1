# -*- coding: utf-8 -*-
""" 
@Time    : 2021/8/26 17:45
@Author  : MaSai
@FileName: test_ActionChains.py.py
@SoftWare: PyCharm
"""
"""
主要是描述ActionChains用法
模拟鼠标的操作
"""
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class Test_Actionschains():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip()
    def test_case(self):
        self.driver.get("https://sahitest.com/demo/clicks.htm")
        # elemenet_click=self.driver.find_element_by_xpath("/h   tml/body/form/input[3]")
        elemenet_click = self.driver.find_element_by_xpath('//*[@value = "click me"]')
        elemenet_doubleclick = self.driver.find_element_by_xpath('//*[@value = "dbl click me"]')
        elemenet_rightclick = self.driver.find_element_by_xpath('//*[@value = "right click me"]')
        action = ActionChains(self.driver)
        # 鼠标单击
        action.click(elemenet_click)
        # 双击
        action.double_click(elemenet_doubleclick)
        # 右键
        action.context_click(elemenet_rightclick)
        sleep(3)
        # 执行用例
        action.perform()
        sleep(3)

    @pytest.mark.skip
    def test_moves(self):
        self.driver.get("https://www.baidu.com")
        # move=self.driver.find_element_by_link_text("设置")
        move = self.driver.find_element_by_xpath('//*[@id="s-usersetting-top"]')
        action = ActionChains(self.driver)
        # 光标的移动
        action.move_to_element(move)
        # 执行
        action.perform()
        sleep(5)

    @pytest.mark.skip()
    def test_drog(self):
        self.driver.get("https://sahitest.com/demo/dragDropMooTools.htm")
        stear = self.driver.find_element_by_xpath('//*[@id="dragger"]')
        end = self.driver.find_element_by_xpath('/html/body/div[2]')
        action = ActionChains(self.driver)
        #  方法1元素的拖拽 将A元素拖拽到B元素的位置在释放
        # action.drag_and_drop(stear, end)
        # 方法2元素的拖拽 将A元素拖拽到B元素的位置在释放
        # action.click_and_hold(stear).release(end)
        #3将A 元素按住不释放，移动到B元素 在释放
        action.click_and_hold(stear).move_to_element(end).release()
        # 执行操作
        action.perform()
        sleep(5)


    def test_send(self):
        self.driver.get("https://sahitest.com/demo/label.htm")
        # 定位到输入框
        send=self.driver.find_element_by_xpath('/html/body/label[1]/input')
        # 将光标移动到输入框，以便输入
        send.click()
        action=ActionChains(self.driver)
        #
        action.send_keys("username").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("tom").pause(1)
        action.send_keys(Keys.BACK_SPACE)
        action.perform()
if __name__ == '__main__':
    pytest.main(['-v', 's', 'test_ActionChains.py'])