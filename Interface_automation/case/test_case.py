# -*- coding: utf-8 -*-
""" 
@Time    : 2021/10/26 14:27
@Author  : MaSai
@FileName: test_case.py
@SoftWare: PyCharm
"""
from Interface_automation.page.deparment import Deparment


class Test_case:
    """
    测试企业微信部门类
    """

    def setup(self):
        self.deparment = Deparment()
        pass

    def test_deparment_list(self):
        """
        获取部门列表
        :return:
        """
        print(self.deparment.department_list().json())
        assert self.deparment.department_list().json().get("errcode") == 0

    def test_establish_department(self):
        """
        创建部门
        :return:
        """
        assert self.deparment.establish_department().json().get("errcode") == 0


    def test_updata_department(self):
        """
        更新部门
        :return:
        """
        assert self.deparment.updata_department().json().get("errcode") == 0

    def test_delete_department(self):
        """
        删除部门方法
        :return:
        """
        assert self.deparment.delete_department().json().get("errcode") == 0
