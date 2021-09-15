# -*- coding: utf-8 -*-
""" 
@Time    : 2021/9/14 16:01
@Author  : MaSai
@FileName: contactaddpage.py
@SoftWare: PyCharm
"""
from appium.webdriver.common.mobileby import MobileBy
from faker import Faker
from selenium.webdriver.support.wait import WebDriverWait
from app_pageobject.page.basepage import BasePage



class ContactAddPage(BasePage):
    """
    添加成员页面
    """

    # def __init__(self, driver: WebDriver):
    #     # 构造函数接收参数
    #     # 实例化driver
    #     self.driver = driver

    def goto_add(self, name, id, sex, phone):
        """
        模拟手动输入添加联系人操作
        :return:
        """
        # fake = Faker("zh_CN")
        # name=fake.name()
        # phone=fake.phone_number()
        # # 填写姓名
        self.find_and_send(MobileBy.XPATH, "//*[@class='android.widget.EditText' and @text='必填']",name)
        # # 账号
        self.find_and_send(MobileBy.XPATH, "//*[contains(@text,'帐号')]/..//*[@text='选填']",id)
        # 选择性别
        self.find_and_click(MobileBy.XPATH, "//*[@text='性别']/..//*[@class='android.widget.ImageView']")
        # 选择女
        WebDriverWait(self.driver, 5).until(lambda x: x.find_element(MobileBy.XPATH, "//*[@text='男']"))
        if sex == "男":
            self.find_and_click(MobileBy.XPATH, "//*[@text='男']")
        else:
            self.find_and_click(MobileBy.XPATH, "//*[@text='女']")
        # 填写手机号
        self.find_and_send(MobileBy.XPATH, "//*[@text='手机号']",phone)
        # 保存
        self.slide_click("保存")
        from app_pageobject.page.memberinvitepage import MemberInvitePage
        return MemberInvitePage(self.driver)
