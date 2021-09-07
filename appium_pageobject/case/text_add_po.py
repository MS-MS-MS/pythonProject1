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

# def test_yaml():
#     print(get_yaml())

class Test_Tx:
    def setup(self):
        # 实例化基类
        self.mian = BasePage()

    @pytest.mark.parametrize("name,id,sex,phone", get_yaml()[0], ids=get_yaml()[1])
    def test_add(self, name, id, sex, phone):
        addmember = self.mian
        result = addmember.goto_mail_list().goto_add_member().goto_membernvitemenu().goto_contact(name, id, sex, phone).goto_toast()
        assert result in "添加成功"
