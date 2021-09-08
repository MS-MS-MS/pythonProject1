# -*- coding: utf-8 -*-
""" 
@Time    : 2021/9/7 16:50
@Author  : MaSai
@FileName: text_add_po.py
@SoftWare: PyCharm
"""
import pytest
import yaml

from appium_pageobject.page.basepage import BasePage


def get_yaml():
    with open("../tx_yaml/tx_add.yaml", encoding="utf-8") as f:
        date = yaml.safe_load(f)
        case = date["case"]
        ids = date["ids"]
    return case, ids

def get_del_yaml():
    with open("../tx_yaml/tx_del.ymal", encoding="utf-8") as f:
        date = yaml.safe_load(f)
        name = date["name"]
        ids = date["ids"]
    return name, ids


# def test_yaml():
#     print(get_yaml())

class Test_Tx:
    def setup(self):
        # 实例化基类
        self.mian = BasePage()

    @pytest.mark.parametrize("name,id,sex,phone", get_yaml()[0], ids=get_yaml()[1])
    def test_add(self, name, id, sex, phone):
        """
        添加成员测试用例
        :param name:姓名
        :param id:账号
        :param sex:性别
        :param phone:手机号
        :return:
        """
        addmember = self.mian.goto_main_page()
        result = addmember.goto_mail_list().goto_add_member().goto_membernvitemenu().goto_contact(name, id, sex,
                                                                                                  phone).goto_toast()
        assert result in "添加成功"


    @pytest.mark.parametrize("name",get_del_yaml()[0],ids=get_del_yaml()[1])
    def test_del(self, name):
        """
        通讯录删除
        删除成员测试用例
        :param name: 传入要删除的人员的姓名
        :return:
        """
        delmember = self.mian.goto_main_page()
        delmember.goto_mail_list().goto_del(name).goto_setting().goto_contactedit().del_member()

    @pytest.mark.parametrize("name", get_del_yaml()[0], ids=get_del_yaml()[1])
    def test_workbench_del(self, name):
        """
        工作台删除
        删除成员测试用例
        :param name: 传入要删除的人员的姓名
        :return:
        """
        delmember = self.mian.goto_main_page()
        delmember.goto_workbench().goto_manager().goto_enterprisecontact().goto_del(name).del_member()