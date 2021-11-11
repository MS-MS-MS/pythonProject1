# -*- coding: utf-8 -*-
""" 
@Time    : 2021/11/9 16:38
@Author  : MaSai
@FileName: BaseApi_Tag.py
@SoftWare: PyCharm
"""
import requests


class BaseApi_Tag:
    """
    基类 封装公共方法
    """
    def send(self, method, url, **kwargs):
        """
        请求方法
        :param method: 请求方式
        :param url: url
        :param kwargs: 附加数据
        :return: 请求返回结果
        """
        data = {
            "method": method,
            "url": url
        }
        data.update(**kwargs)
        r = requests.request(**data)
        return r