from selenium import webdriver

from selenium_case.base import Base



class Test_get_selenium():

    def setup(self):
        #初始化driver
        self.driver=webdriver.Chrome()
        # 隐式等待
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        # 关闭driver
        self.driver.quit()

    def test_get(self):
        # 打开百度
        self.driver.get("https://www.baidu.com")
        # print("打开浏览器")

