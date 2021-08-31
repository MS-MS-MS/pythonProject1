import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from selenium_pageobject.page.base_page import Base_Page


class AddMemberPage(Base_Page):
    """
    添加成员页面self.driver
    """

    # def __init__(self, driver:WebDriver):
    #     # 接受driver
    #     # driver:WebDriver 添加一个类型提示 方便语法联想
    #     self.driver = driver
    def addmember_msg(self, username, acctid, phonenumber):
        """
        填写成员信息操作
        """
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable((By.ID, "username")))
        self.find(By.ID, "username").send_keys(username)
        self.find(By.ID, "memberAdd_acctid").send_keys(acctid)
        self.find(By.ID, "memberAdd_phone").send_keys(phonenumber)
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()

    def get_number(self, vaule):
        """
        验证添加联系人
        """
        # 获取到当前页面联系人的信息
        # title 包含联系人的信息
        # contactlist = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        # titlelist = []
        # for element in contactlist:
        #     # 获取当前联系人的信息
        #     # getAttribute() 方法返回指定属性名的属性值。
        #     titlelist.append(element.get_attribute("title"))
        # return titlelist

        totallist = []
        titlelist = []
        while True:
            # 应对添加的联系人不在当前页面
            contactlist = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
            print(contactlist)
            # 拿到包含title元素
            titlelist = [element.get_attribute("title") for element in contactlist]
            if vaule in titlelist:
                # 添加的联系人的信息在此页面就返回True
                return True
            totallist = totallist + titlelist
            result: str = self.find(By.CSS_SELECTOR, ".ww_pageNav_info_text").text
            num, total = result.split("/", 1)
            if int(num) == int(total):
                # 翻到最后一页 没有找到添加的联系人的信息
                return False
            else:
                self.find(By.CSS_SELECTOR, ".js_next_page").click()
            # print(totallist)
        return totallist

    def addmember_msg_erro(self, username, acctid, phonenumber):
        """
        填写成员信息操作
        """
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable((By.ID, "username")))
        self.find(By.ID, "username").send_keys(username)
        self.find(By.ID, "memberAdd_acctid").send_keys(acctid)
        self.find(By.ID, "memberAdd_phone").send_keys(phonenumber)
        # CSS_SELECTOR 中大于号">"表示子节点的
        # 唯一节点.js_has_member
        # 唯一节点下div的子节点.js_has_member>div:nth-child(1)
        # 唯一节点下div的子节点下a标签的位置 .js_has_member>div:nth-child(1)>a:nth-child(2)
        time.sleep(3)
        ass=self.find(By.CSS_SELECTOR,'.member_edit_item_Account>div:nth-child(2)>div')
        return ass.text

