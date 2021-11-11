# -*- coding: utf-8 -*-
""" 
@Time    : 2021/11/9 16:38
@Author  : MaSai
@FileName: WeWork_Tag.py
@SoftWare: PyCharm
"""
from interface_wework.API.BaseApi_Tag import  BaseApi_Tag


class WeWrok_Tag(BaseApi_Tag):
    """
    测试产品基础方法
    """
    def get_access_token(self,corpid,corpsecret):
        """
        获取access_token方法
        :param corpid: 企业ID ww5c96fef453a0de4d
        :param corpsecret: 应用的凭证密钥  vL4X17X-26i7xujadEiHT4yakmdHu4FEmxDzMXySrtU
        :return:
        """

        url="https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        parmes={
            "corpid":corpid,
            "corpsecret":corpsecret
        }
        r=self.send("GET",url,params=parmes)
        return r.json().get("access_token")


