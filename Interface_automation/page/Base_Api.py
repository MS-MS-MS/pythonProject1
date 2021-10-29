# -*- coding: utf-8 -*-
""" 
@Time    : 2021/10/25 21:04
@Author  : MaSai
@FileName: Base_Api.py
@SoftWare: PyCharm
"""
import requests


class Base_API:
    """
    基类
    """
    def __init__(self):
        pass

    def request(self,method,url,tool,**kwargs):
        """
        构造请求方法
        :param method:请求方法
        :param url: 请求url
        :param args:
        :param kwargs:
        :return: r
        """
        if tool == "requests":
            data={
                "method":method,
                "url":url

            }
            data.update(**kwargs)
            print(data)
            r=requests.request(**data)
            return r
        else:
            return True




