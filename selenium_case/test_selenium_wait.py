# from selenium_case.base import Base
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
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
显示等待
1.lambda方式
wait.until(lambda x:x.find_element_by_id('kw'))
2.基本的传入方法
3.元素是否可见 可点击
WebDriverWait(5).until()
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
        ele = self.driver.find_element(By.XPATH, "//*[@id='kw']")
        print(ele)
        ele.click()
        self.driver.find_element_by_id("su").click()
        # 强制等待
        time.sleep(5)

    def test_Display_wait_func(self):
        # 第一种方式  until 需要接受一个方法
        # 创建一个方法 在页面是查找该元素,
        # 返回 查找元素的长度 返回的长度大于等于1 证明该元素在页面上已经被查找到
        # 重要 自定义的方法需要一个默认参数 until 需要进行传参
        def wait(x):
            return len(self.driver.find_elements(By.XPATH, '//*[@id="s-usersetting-top"]')) >= 1

        WebDriverWait(self.driver, 5).until(wait)
        self.driver.find_element_by_id("kw").send_keys("selenium")
        self.driver.find_element_by_id("su").click()
        time.sleep(5)
        # self.driver.find_element_by_id("su").click()

    def test_Display_wait_excpted(self):
        """
        expected_conditions
        对网页的元素是否可点击,可见进行判断
        配合WebDriverWait().until 使用
        """
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="s-usersetting-top"]')))
        self.driver.find_element_by_id("kw").send_keys("selenium")
        self.driver.find_element_by_id("su").click()
        time.sleep(5)

    def test_Display_wait_lambda(self):
        """
        使用lambda 匿名函数
        lambda X  接受的是 self.driver  x引用的域变量就是WebDriverWait的self._driver类变量
        lambda x:x.find_element(loc)表达式就被替换成为了self.driver.find_element就可以正常的使用driver使用一样
        """
        WebDriverWait(self.driver, 5).until(lambda x: x.find_element(By.XPATH, '//*[@id="s-usersetting-top"]'))
        self.driver.find_element_by_id("kw").send_keys("selenium")
        self.driver.find_element_by_id("su").click()
        time.sleep(5)






# $x("//*[@id='s-usersetting-top']")
# 在console 使用xpath 定位方式 $x("元素的xpth")
#  $x("//*[@id='content_left']//*[@class='result c-container new-pmd']//*[@class='t c-title-en']")