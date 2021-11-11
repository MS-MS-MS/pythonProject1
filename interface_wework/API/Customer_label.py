# -*- coding: utf-8 -*-
""" 
@Time    : 2021/11/9 17:43
@Author  : MaSai
@FileName: Customer_label.py
@SoftWare: PyCharm
"""
import uuid

import yaml

from interface_wework.API.WeWork_Tag import WeWrok_Tag
from interface_wework.utlis.file_tools import FileTools


class Customer_Label(WeWrok_Tag):
    """
    客户标签类
    """

    def __init__(self):
        """
        初始化获取token
        """
        data = FileTools.read_yaml("token")
        corpid = data["access_token"]['corpid']['ceshiren']
        corpsecret = data["access_token"]['corpsecret']['customer_tag']
        self.access_token = self.get_access_token(corpid, corpsecret)



    def get_tag(self):
        # 获取企业标签库
        url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list"
        params = {
            "access_token": self.access_token
        }
        r = self.send("POST", url, params=params)
        return r

    def add_tag(self,group_name,name,name1):
        """
        添加企业标签
        """
        url = f'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag'
        # data = {
        #     "group_name": f"GROUP_NAME1_{uid}",
        #     "tag": [{
        #         "name": f"TAG_NAME_1_{uid}",
        #     },
        #         {
        #             "name": f"TAG_NAME_2_{uid}",
        #         }
        #     ]
        # }
        data = {
            "group_name": f"{group_name}",
            "tag": [{
                "name": f"{name}",
            },
                {
                    "name": f"{name1}",
                }
            ]
        }
        params = {
            "access_token": self.access_token
        }
        r = self.send("POST", url, params=params, json=data)
        return r

    def edit_tag(self,tag_id,new_name):
        """
        编辑客户
        """
        data = {
            "id":tag_id,
            "name":new_name,
        }
        url = f'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag'
        params = {
            "access_token": self.access_token
        }
        r = self.send("POST", url, params=params, json=data)
        return r

    def delete_tag(self,group_id):
        "删除客户标签"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag"
        # data = {
        #     "tag_id": [
        #         "etvTLHBwAAO65S3qCJDYXZ4PajFnCBtw",
        #     ],
        #     "group_id": [
        #         "etvTLHBwAAfFgAHj8Hp6G5o5yPQwbh8g",
        #     ],
        # }

        data = {
            "group_id": [
                f"{group_id}",
            ]
        }

        params = {
            "access_token": self.access_token
        }
        r = self.send("POST", url, params=params, json=data)
        return r
