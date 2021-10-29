# -*- coding: utf-8 -*-
""" 
@Time    : 2021/10/26 11:32
@Author  : MaSai
@FileName: deparment.py
@SoftWare: PyCharm
"""
import time

from Interface_automation.page.wework import WeWork


class Deparment(WeWork):
    def __init__(self):
        super().__init__()

    def department_list(self):
        """
        获取部门列表方法
        :return:
        """

        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.get_token()}&id={2}"
        r = self.request("GET", url,tool="requests")
        return r

    def establish_department(self):
        """
        创建部门
        :return:
        """
        tim = int(time.time())
        tim = int(time.time())
        data = {
            "name": f"广州研发中心_{tim}",
            "name_en": f"RDGZ_{tim}",
            "parentid": 1,
            "order": 1,
            "id": 2
        }
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={self.get_token()}"
        r = self.request("POST", url,tool="requests",json=data)
        return r


    def updata_department(self):
        """
        更新部门
        :return:
        """
        data = {
            "id": 2,
            "name": "广州研发中心_1",
            "name_en": "RDGZ_1",
            "parentid": 1,
            "order": 1
        }
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.get_token()}"
        r = self.request("POST", url, tool="requests", json=data)
        return r

    def delete_department(self):
        """
        删除部门方法
        :return:
        """
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.get_token()}&id={2}"
        r = self.request("GET", url, tool="requests")
        return r
