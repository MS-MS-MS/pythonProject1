from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from selenium_pageobject.page.base_page import Base_Page


class MailList_Page(Base_Page):
    # def __init__(self,driver:WebDriver):
    #     self.driver=driver
    """
    通讯录页面
    """

    def add_member(self):
        from selenium_pageobject.page.add_member_page import AddMemberPage
        # CSS_SELECTOR 中大于号">"表示子节点的
        # 唯一节点.js_has_member
        # 唯一节点下div的子节点.js_has_member>div:nth-child(1)
        # 唯一节点下div的子节点下a标签的位置 .js_has_member>div:nth-child(1)>a:nth-child(2)
        WebDriverWait(self.driver,5).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,".js_has_member>div:nth-child(1)>a:nth-child(2)")))
        self.find(By.CSS_SELECTOR,".js_has_member>div:nth-child(1)>a:nth-child(2)").click()
        return AddMemberPage(self.driver)
        # locator = (By.CSS_SELECTOR, ".js_has_member>div:nth-child(1)>a:nth-child(2)")
        # def wait_for_next(x: WebDriver):
        #     """
        #     自定义一个显示等待
        #     点击元素判断是否跳转到新节目
        #     没有跳转就再次点击
        #     跳转成功返回要定位的页面元素
        #     """
        #     try:
        #         self.find(*locator).click()
        #         return self.find(By.ID, "username")
        #     except:
        #         return False
        #
        # return AddMemberPage()
