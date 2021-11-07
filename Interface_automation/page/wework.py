# -*- coding: utf-8 -*-
""" 
@Time    : 2021/10/26 11:24
@Author  : MaSai
@FileName: test_wework.py
@SoftWare: PyCharm
"""
from Interface_automation.page.Base_Api import Base_API


class WeWork(Base_API):
    """
    企业微信获取token
    """

    def __init__(self):
        super().__init__()

    def get_token(self):
        """
        获取企业微信 access_token
        :return:  self.token
        """
        ID = "ww5c96fef453a0de4d"
        SECRE = "4sWLvMEwtn686Y3nNJmuUOgInUuiSyzcOD4TpsNNMdU"
        # 定义请求参数
        params = {
            "corpid": ID,
            "corpsecret": SECRE
        }

        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        r = self.request("GET", url, tool="requests", params=params)
        return r.json().get("access_token")
