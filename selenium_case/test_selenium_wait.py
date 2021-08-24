# from selenium_case.base import Base
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

"""
本文件主要说明selenium的三种等待方式
1.强制等待
time.sleep(10)
强制等待10秒
2.隐式等待
主要用于初始化driver时设置,全局生效,
是设置的全局等待。设置等待时间，是对页面中的所有元素设置加载时间，如果超出了设置时间的则抛出异常。
隐式等待可以理解成在规定的时间范围内，浏览器在不停的刷新页面，直到找到相关元素或者时间结束。
3.显示等待
是针对于某个特定的元素设置的等待时间，在设置时间内，
默认每隔一段时间检测一次当前页面某个元素是否存在，如果在规定的时间内找到了元素，则直接执行，即找到元素就执行相关操作，如果超过设置时间检测不到则抛出异常。默认检测频率为0.5s，默认抛出

"""
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

    def test_search(self):

        # self.driver.find_element_by_id("kw").send_keys("selenium")
        ele=self.driver.find_element(By.XPATH,"//*[@id='kw']")
        print(ele)
        ele.click()
        self.driver.find_element_by_id("su").click()
        # 强制等待
        time.sleep(5)

    def test_Display_wait(self):
        """
        显示等待
        1.lambda方式
        wait.until(lambda diver:driver.find_element_by_id('kw'))
        2.基本的传入方法
        3.元素是否可见 可点击
        WebDriverWait(5).until()
        """
        #
        # WebDriverWait(5).until(lambda self.driver)
        ele = self.driver.find_element(By.XPATH, "//*[@id='kw']")
        print(ele)
        ele.click()
        self.driver.find_element_by_id("su").click()
        WebDriverWait(5).until(lambda diver: self.driver.find_element(By.XPATH,'//*[@id="u"]/a[1]'))
        self.driver.find_element(By.XPATH, '//*[@id="u"]/a[1]').click()
        pass