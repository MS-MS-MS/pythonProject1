# -*- coding: utf-8 -*-
""" 
@Time    : 2021/8/24 16:01
@Author  : MaSai
@FileName: test_Parameterization.py
@SoftWare: PyCharm
"""
import pytest

"""
pytest 参数化的使用
"""

@pytest.mark.parametrize("a,b,c",[[1,2,3],[2,2,4]])
def test_case1(a,b,c):
    assert c ==a+b

"""
参数化，标记数据
"""
@pytest.mark.parametrize("a,b",[
    ("3+5",8),
    ("3*5",15),
    pytest.param("6*9",42,marks=pytest.mark.xfail),
    pytest.param("6*6",42,marks=pytest.mark.skip)
])
def test_case2(a,b):
    assert eval(a)==b

"""
fixture 传参数
"""
@pytest.fixture()
def logins(request):
    name=request.param
    print(f"账号:{name}")
    return name

data = ["pyy1", "polo"]
ids = [f"login_test_name is:{name}" for name in data]

# @pytest.mark.parametrize("logins",data,ids=ids,indirect=True)
@pytest.mark.parametrize("logins",data,ids=ids)
# data数据中的值传入 到 logins 中
#  test_name 在获取到logins 的返回值
def test_name(logins):
    print(f" 测试用例的登录账号是：{logins} ")

@pytest.mark.parametrize("account_number",data,ids=ids)
# data数据中的值传入 到 logins 中
#  test_name 在获取到logins 的返回值
def test_name_1(account_number):
    print(f" 测试用例的登录账号是：{account_number} ")

"""
多个参数
"""
data = [
    {"username": "name1", "pwd": "pwd1"},
    {"username": "name2", "pwd": "pwd2"},
]

@pytest.fixture()
def logins(request):
    param=request.param
    print(f"账号:{param['username']},密码:{param['pwd']}")
    return param

@pytest.mark.parametrize("login_case",data,ids=ids)
# data数据中的值传入 到 logins 中
#  test_name 在获取到logins 的返回值
def test_name(login_case):
    print(f" 测试用例的登录账号是：{login_case['username']} ,密码:{login_case['pwd']} ")