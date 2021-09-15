# -*- coding: utf-8 -*-
""" 
@Time    : 2021/9/14 16:51
@Author  : MaSai
@FileName: test_app.py
@SoftWare: PyCharm
"""
import pytest
import yaml

from app_pageobject.page.app import App


def get_yaml():
    """
    添加成员数据
    :return:
    """
    with open("../ymal/tx_add.yaml", encoding="utf-8") as f:
        date = yaml.safe_load(f)
        case = date["case"]
        ids = date["ids"]
    return case, ids


def get_del_yaml():
    with open("../ymal/tx_del.ymal", encoding="utf-8") as f:
        date = yaml.safe_load(f)
        name = date["name"]
        ids = date["ids"]
    return name, ids

class TestApp:
    def setup(self):
        self.main = App().start_app()

    @pytest.mark.parametrize("name,id,sex,phone", get_yaml()[0], ids=get_yaml()[1])
    def test_add(self, name, id, sex, phone):
        result=self.main.goto_main().goto_maillist().goto_addmember().goto_contact().goto_add(name, id, sex, phone).goto_Toast()
        print(result)
        assert result =="添加成功"

    @pytest.mark.parametrize("name", get_del_yaml()[0], ids=get_del_yaml()[1])
    def test_del(self, name):
        """
        通讯录删除
        删除成员测试用例
        :param name: 传入要删除的人员的姓名
        :return:
        """
        self.main.goto_main().goto_workbench().goto_manager().goto_enterprisecontact().goto_del(name).del_member()
