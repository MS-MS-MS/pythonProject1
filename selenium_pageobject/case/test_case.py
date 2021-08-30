from selenium_pageobject.page.main_page import Main_Page


class Test_case:
    def setup(self):
        # 实例化Base_page
        self.main = Main_Page()

    def test_add(self):
        username = "97"
        acctid = "97"
        phonenumber = "13400000097"
        add_member=self.main.goto_add_member()
        #传入要添加联系人的信息
        add_member.addmember_msg(username,acctid,phonenumber)
        # 断言判断联系人的名字是否在当前所有联系人的列表中
        result=add_member.get_number(username)
        assert result==True

    def test_add1(self):
        username = "99"
        acctid = "99"
        phonenumber = "13400000099"
        get_add=self.main.goto_menu_contacts()
        #传入要添加联系人的信息
        get_add.add_member().addmember_msg(username,acctid,phonenumber)
        # 断言判断联系人的名字是否在当前所有联系人的列表中
        # assert username in get_add.add_member().get_number(username)
        result=get_add.add_member().get_number(username)
        print(result)
        assert result == True

