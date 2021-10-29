# -*- coding: utf-8 -*-
""" 
@Time    : 2021/10/25 18:03
@Author  : MaSai
@FileName: test_department.py
@SoftWare: PyCharm
"""
import time
import requests

class Test_department:
    """
    企业微信接口测试 增删改查部门练习
    """
    def setup(self):
        """
        获取企业微信 access_token
        :return:  self.token
        """
        ID = "ww5c96fef453a0de4d"
        SECRE = "4sWLvMEwtn686Y3nNJmuUOgInUuiSyzcOD4TpsNNMdU"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={ID}&corpsecret={SECRE}"
        r = requests.get(url)
        # print(r.json().get("access_token"))
        self.token = r.json().get("access_token")

    def test_establish_department(self):
        """
        创建部门
        :return:
        """
        tim = int(time.time())
        data = {
            "name": f"广州研发中心_{tim}",
            "name_en": f"RDGZ_{tim}",
            "parentid": 1,
            "order": 1,
            "id": 2
        }

        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={self.token}"
        r = requests.post(url, json=data)
        assert r.json().get("errcode") == 0
        print(r.json())

    def test_department_list(self):
        """
        获取部门列表方法
        :return:
        """
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}&id={2}"
        r = requests.get(url)
        print(r.json())
        assert r.json().get("errcode") == 0

    def test_updata_department(self):
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
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.token}"
        r = requests.post(url, json=data)
        assert r.json().get("errcode") == 0

    def test_delete_department(self):
        """
        删除部门方法
        :return:
        """
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.token}&id={2}"
        r = requests.get(url)
        assert r.json().get("errcode") == 0
