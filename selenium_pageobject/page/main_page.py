from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium_pageobject.page.add_member_page import AddMemberPage
from selenium_pageobject.page.base_page import  Base_Page
from selenium_pageobject.page.mail_list_page import MailList_Page


class Main_Page(Base_Page):
    base_url = "https://work.weixin.qq.com/wework_admin/frame#index"
    # def __init__(self):
    #     """
    #     初始化driver复用浏览器
    #     https://work.weixin.qq.com/
    #     """
    #     options=webdriver.ChromeOptions()
    #     options.debugger_address='127.0.0.1:9222'
    #     self.driver=webdriver.Chrome(options=options)
    #     self.driver.implicitly_wait(5)
    #     self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

    def goto_add_member(self):
        """
        点击添加成员操作
        """
        # self.driver.find_element(By.CSS_SELECTOR,'.index_service_cnt_itemWrap:nth-child(1)').click()
        self.find(By.CSS_SELECTOR,'.index_service_cnt_itemWrap:nth-child(1)').click()
        #跳转页面,传入self.driver
        return AddMemberPage()

    def goto_menu_contacts(self):
        """
        点击导航栏通讯录
        """
        # self.driver.find_element_by_id("menu_contacts").click()
        self.find(By.ID,"menu_contacts").click()
        # return MailList_Page(self.driver)
        return MailList_Page()