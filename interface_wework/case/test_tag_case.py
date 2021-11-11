# -*- coding: utf-8 -*-
""" 
@Time    : 2021/11/9 20:33
@Author  : MaSai
@FileName: test_tag_case.py
@SoftWare: PyCharm
"""
import json
import os
import uuid

import pytest
from jsonpath import jsonpath

from interface_wework.API.Customer_label import Customer_Label


class Test_case:
    def setup(self):
        # 初始化客户标签类
        self.tag = Customer_Label()

    def get_uuid(self):
        # 生产唯一id
        return str(uuid.uuid1()).split("-")[0]

    def test_get_tag(self):
        """
        测试获取企业标签库
        :return:
        """
        r = self.tag.get_tag()
        # print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        assert r.json().get("errcode") == 0

    @pytest.mark.parametrize("group_name,name,name1", [("GROUP_NAME1", 'name', 'name1')])
    def test_add_tag(self, group_name, name, name1):
        """
        测试添加客户标签
        :return:
        """
        # 获取id
        uid = self.get_uuid()
        Group_name = group_name + "_" + uid
        Name = name + "_" + uid
        Name1 = name1 + "_" + uid
        r = self.tag.add_tag(Group_name, Name, Name1)
        # print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        assert r.json().get("errcode") == 0
        # 查询添加客户标签是否在企业标签库中
        r = self.tag.get_tag()
        assert Group_name in jsonpath(r.json(), "$.tag_group[*].group_name")

    @pytest.mark.parametrize("group_name,name,name1,NewName", [("GROUP_NAME1", 'name', 'name1', "NewName")])
    def test_edit_tag(self, group_name, name, name1, NewName):
        """
        编辑客户标签
        :return:
        """
        # 在编辑之前先创建客户标签
        uid = self.get_uuid()
        Group_name = group_name + "_" + uid
        Name = name + "_" + uid
        Name1 = name1 + "_" + uid
        r = self.tag.add_tag(Group_name, Name, Name1)
        # 获取当前创建成功的tag_id_list
        tag_id_list = jsonpath(r.json(), "$..tag[*].id")[0]
        # 客户新标签
        new_name = NewName + "_" + uid
        # 进行编辑客户标签操作
        r_edit = self.tag.edit_tag(tag_id_list, new_name)
        # 断言是否编辑成功
        assert r_edit.json().get("errcode") == 0

    @pytest.mark.parametrize("group_name,name,name1", [("GROUP_NAME1", 'name', 'name1')])
    def test_delete_tag(self, group_name, name, name1):
        """
        删除客户标签
        :return:
        """
        # 在编辑之前先创建客户标签
        uid = self.get_uuid()
        Group_name = group_name + "_" + uid
        Name = name + "_" + uid
        Name1 = name1 + "_" + uid
        r = self.tag.add_tag(Group_name, Name, Name1)
        # 断言是否添加成功
        assert r.json().get("errcode") == 0
        # 获取当前创建成功的group_id_list
        group_id_list = (jsonpath(r.json(), "$..group_id"))
        # list 转str 类型转换
        group_id="".join(group_id_list)
        del_r = self.tag.delete_tag(group_id)
        # 断言是否删除成功
        assert del_r.json().get("errcode") == 0
