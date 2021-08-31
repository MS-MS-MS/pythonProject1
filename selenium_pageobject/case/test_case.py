from selenium_pageobject.page.main_page import Main_Page


class Test_case:
    username = "97"
    acctid = "97"
    phonenumber = "13400000097"
    def setup(self):
        # 实例化Base_page
        self.main = Main_Page()

    def test_add(self):

        add_member=self.main.goto_add_member()
        #传入要添加联系人的信息
        add_member.addmember_msg(self.username,self.acctid,self.phonenumber)
        # 断言判断联系人的名字是否在当前所有联系人的列表中
        result=add_member.get_number(self.username)
        assert result==True

    def test_add1(self):
        get_add=self.main.goto_menu_contacts()
        #传入要添加联系人的信息
        get_add.add_member().addmember_msg(self.username,self.acctid,self.phonenumber)
        # 断言判断联系人的名字是否在当前所有联系人的列表中
        # assert username in get_add.add_member().get_number(username)
        result=get_add.add_member().get_number(self.username)
        print(result)
        assert result == True

    def test_addfail(self):
        """
        添加联系人失败用例
        :return:
        """
        username = "97"
        acctid = "97"
        phonenumber = "13400000097"
        add_member = self.main.goto_add_member()
        # 传入要添加联系人的信息
        result=add_member.addmember_msg_erro(username, acctid, phonenumber)
        assert username in result

