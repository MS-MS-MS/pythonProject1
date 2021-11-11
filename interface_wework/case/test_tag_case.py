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
from interface_wework.utlis.file_tools import FileTools


def get_yaml():
    """
    读取yaml解析数据
    :return:
    """
    # 添加客户标签数据
    data = FileTools.read_yaml("tag")
    group_name = data["tag"]["add"]["group_name"]
    name = data["tag"]["add"]["name"]
    ids = data["tag"]["add"]["ids"]
    # 编辑客户标签数据
    edit_name = data["tag"]["edit_tag"]["name"]
    edit_ids = data["tag"]["edit_tag"]["ids"]
    #删除客户标签
    del_ids = data["tag"]["del_tag"]["ids"]

    return group_name, name, ids, edit_name, edit_ids,del_ids


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

    @pytest.mark.parametrize("group_name,name", [(get_yaml()[0], get_yaml()[1])], ids=[get_yaml()[2]])
    def test_add_tag(self, group_name, name):
        """
        测试添加客户标签
        :return:
        """
        # 获取id
        uid = self.get_uuid()
        Group_name = group_name + "_" + uid
        Name = name + "_" + uid
        r = self.tag.add_tag(Group_name, Name)
        # print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        assert r.json().get("errcode") == 0
        # 查询添加客户标签是否在企业标签库中
        r = self.tag.get_tag()
        assert Group_name in jsonpath(r.json(), "$.tag_group[*].group_name")

    @pytest.mark.parametrize("group_name,name,NewName", [(get_yaml()[0], get_yaml()[1], get_yaml()[3])],
                             ids=[get_yaml()[4]])
    def test_edit_tag(self, group_name, name, NewName):
        """
        编辑客户标签
        :return:
        """
        # 在编辑之前先创建客户标签
        uid = self.get_uuid()
        Group_name = group_name + "_" + uid
        Name = name + "_" + uid
        r = self.tag.add_tag(Group_name, Name)
        # 获取当前创建成功的tag_id_list
        tag_id_list = jsonpath(r.json(), "$..tag[*].id")[0]
        # 客户新标签
        new_name = NewName + "_" + uid
        # 进行编辑客户标签操作
        r_edit = self.tag.edit_tag(tag_id_list, new_name)
        # 断言是否编辑成功
        assert r_edit.json().get("errcode") == 0

    @pytest.mark.parametrize("group_name,name", [(get_yaml()[0], get_yaml()[1])], ids=[get_yaml()[5]])
    def test_delete_tag(self, group_name, name):
        """
        删除客户标签
        :return:
        """
        # 在编辑之前先创建客户标签
        uid = self.get_uuid()
        Group_name = group_name + "_" + uid
        Name = name + "_" + uid
        r = self.tag.add_tag(Group_name, Name)
        # 断言是否添加成功
        assert r.json().get("errcode") == 0
        # 获取当前创建成功的group_id_list
        group_id_list = (jsonpath(r.json(), "$..group_id"))
        # list 转str 类型转换
        group_id = "".join(group_id_list)
        del_r = self.tag.delete_tag(group_id)
        # 断言是否删除成功
        assert del_r.json().get("errcode") == 0
