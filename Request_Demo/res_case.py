# -*- coding: utf-8 -*-
""" 
@Time    : 2021/10/27 14:36
@Author  : MaSai
@FileName: res_case.py
@SoftWare: PyCharm
"""
import requests
from jsonpath import jsonpath


class Test_demo():
    def test_get(self):
        # get请求
        r = requests.get('http://httpbin.org/get')
        print(r.json())
        print(jsonpath(r.json(), "$.headers.Accept"))


    def test_get_params(self):
        # get请求添加参数
        params={
            "leave":"asd"
        }
        r = requests.get('http://httpbin.org/get',params=params)
        print(r.json())

    def test_get_header(self):
        """
        定制请求头
        :return:
        """
        heards = {
            "name": "ms"
        }

        url = 'http://httpbin.org/get'
        r=requests.get(url,headers=heards)
        print(r.text)

    def test_get_Cookies(self):
        """
        定制cookies
        :return:
        """
        # header = {
        #     "cookie": "hogwarts:school"
        # }
        #
        # url = 'http://httpbin.org/get'
        # r=requests.get(url,headers=header)
        # print(r.text)
        url = 'https://httpbin.testing-studio.com/cookies'
        r=requests.get(url)
        print(r.text)

    def test_psot(self):
        "post请求"
        url="http://httpbin.org/post"
        r=requests.post(url)
        print(r.text)
        print(r.json())

    def test_psot_data(self):
        "post请求 data表单格式"
        data={
            "a":"aaaa"
        }
        url="http://httpbin.org/post"
        r=requests.post(url,data=data)
        print(r.text)

    def test_psot_json(self):
        "post 请求 json"
        data = {
            "b": "bbbbbb"
        }
        url = "http://httpbin.org/post"
        r = requests.post(url, json=data)
        print(r.text)

    def test_delete(self):
        #删除请求
        url="https://httpbin.testing-studio.com/delete"
        r = requests.delete(url)
        print(r.text)

    def test_heard(self):
        r = requests.head('http://httpbin.org/get')
        print(r.text)

    def test_heard(self):
        r = requests.options('http://httpbin.org/get')
        print(r.text)

    def test_file(self):
        # 上传文件的的接口参数的类型为content - type: multipart / form - data，
        # 那么我们使用requests来发送请求的时候，接口中文件上传的参数需要使用files来传递。files参数格式如下
        # fiels为字典类型数据，上传的文件为键值对的形式，参数名作为键，
        # 参数值是一个元组，内容为以下格式（文件名，打开的文件流，文件类型）
        # files = {
        #     "pic": ("test01.gif", open("test01.gif", "rb"), "images/git")
        # }
        # # 注意点：除了上传的文件，接口其他参数不能放入files中
        url = 'http://httpbin.org/post'
        multiple_files = [
            ('images', ('foo.png', open('foo.png', 'rb'), 'image/png')),
            ('images', ('bar.png', open('bar.png', 'rb'), 'image/png'))
        ]
        r = requests.post(url, files=multiple_files)
        print(r.text)
