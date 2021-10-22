# -*- coding: utf-8 -*-
""" 
@Time    : 2021/10/21 15:19
@Author  : MaSai
@FileName: request_case.py
@SoftWare: PyCharm
"""
from hamcrest import assert_that, equal_to
from jsonpath import jsonpath

"""
Pythoon requests库练习
"""
import requests


class Test_demo():
    def test_get(self):
        # get请求
        r = requests.get('http://httpbin.org/get')
        print(r.json())

    def test_post(self):
        # PSOT请求
        r = requests.post('http://httpbin.org/post', data={'key': 'value'})
        print(r.text)

    def test_params(self):
        param = {
            'name': 'ma',
            'password': '123'
        }
        r = requests.get('http://httpbin.org/get', params=param)
        print(r.status_code)
        # print(r.json())
        print(r.url)
        print(r.request.body)

    def test_post_json(self):
        param = {
            'name': 'ma',
            'password': '123'
        }
        r = requests.post('https://httpbin.testing-studio.com/post', json=param)
        # print(r.status_code)
        print(r.text)
        assert r.json()['json']['name'] == "ma"

    def test_howgort(self):
        r = requests.get("https://ceshiren.com/categories.json")
        print(r.json()['category_list']['categories'][0])
        print(r.json()['category_list']['categories'][0]['id'])
        print(r.json()['category_list']['categories'][0]['name'])
        assert r.json()['category_list']['categories'][0]['name'] == '开源项目'

    def test_jsonpath(self):
        r = requests.get("https://ceshiren.com/categories.json")
        # 使用jsonpath取值
        # $..name 取当前文件下所有name的值
        # assert jsonpath(r.json(),'$..name')[0]=='开源项目'
        print(jsonpath(r.json(), '$.category_list.categories[*].name'))
        # assert jsonpath(r.json(),'$.category_list.categories[*].name')[0]=='开源项目'

    def test_homcrest(self):
        r = requests.get("https://ceshiren.com/categories.json")
        # 使用jsonpath取值
        # $..name 取当前文件下所有name的值
        # assert jsonpath(r.json(),'$..name')[0]=='开源项目'
        # print(jsonpath(r.json(), '$.category_list.categories[*].name'))
        assert_that(jsonpath(r.json(), '$.category_list.categories[*].name')[0], equal_to('开源项目'))

    def test_Cookies(self):
        url = 'https://httpbin.testing-studio.com/cookies'
        # Cookie 首字母大写
        header = {
            "Cookie": "hogwarts:school"
        }
        r = requests.get(url=url, headers=header)
        # print(r.status_code)
        print(r.headers)

    def test_Cookies_1(self):
        url = 'https://httpbin.testing-studio.com/cookies'
        header={
            "User-Agent": "hogwarts"
        }
        cookie_date = {
            "hogwarts":"school",
            "name":"ma"
        }
        r = requests.get(url=url,headers=header, cookies=cookie_date)
        print(r.request.headers)





