from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class Base_Page:
    """
    基类用于封装driver
    """
    base_url=""
    def __init__(self,driver:WebDriver=None):
        """
        初始化driver复用浏览器
        https://work.weixin.qq.com/
        """
        if driver==None:
            """
            第一次创建dirver 判断driver是否为None
            """
            options = webdriver.ChromeOptions()
            options.debugger_address = '127.0.0.1:9222'
            self.driver = webdriver.Chrome(options=options)
            self.driver.implicitly_wait(5)
        else:
            self.driver=driver
        if self.base_url!="":
            # 判断界面是否打开
            self.driver.get(self.base_url)

    def find(self,by,locator):
        """
        封装find方法返回查找到的元素
        """
        return  self.driver.find_element(by,locator)

    def finds(self,by,locator):
        """
        封装finds方法返回查找到的所有元素
        """
        return self.driver.find_elements(by,locator)
