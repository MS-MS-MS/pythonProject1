# -*- coding: utf-8 -*-
""" 
@Time    : 2021/8/24 11:09
@Author  : MaSai
@FileName: test_fixture.py
@SoftWare: PyCharm
"""
import pytest

"""
fixture 模拟setup treadown 方法使用
"""
@pytest.fixture(scope="session")
def open():
    "会话前置setup操作"
    print("打开浏览器")
    test = "测试变量是否返回"
    yield test
    # "会话后置treadown 操作"
    print("关闭浏览器")


@pytest.fixture
def login(open):
    "会话前置setup操作"
    print(f"输入账号请先登陆:{open}")
    name = "姓名"
    pwd = "密码"
    age = "年龄"
    yield name, pwd, age
    # "会话后置treadown 操作"
    print("登陆成功")


def test_1(login):
    print("用例1")
    print(login)
    name, pwd, age = login
    print(name, pwd, age)
    assert name in "姓名"
    assert pwd in "密码"
    assert age in "年龄"


def test_2(login):
    print("用例2")
    print(login)
