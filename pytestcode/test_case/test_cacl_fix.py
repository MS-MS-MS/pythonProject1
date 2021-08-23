# -*- coding: utf-8 -*-
""" 
@Time    : 2021/8/23 15:45
@Author  : MaSai
@FileName: test_cacl_fix.py
@SoftWare: PyCharm
"""
import allure
import pytest
import yaml

from pytestcode.cacl.calculator import Calculator

"""
1. 简答题
题目：
（1）计算机器（加法和除法）测试用例，使用fixture 实现setup/teardown 功能
（2）使用第三方插件完成测试用例顺序的控制
（3）编写的用例使用Allure工具生成测试（添加日志，截图）
"""


def getyaml():
    """
    解析ymal 文件
    :return:
    """
    with open("../yaml/caclfix.yaml", encoding="utf-8") as f:
        date = yaml.safe_load(f)
        add_data = date["add"]["data"]
        add_ids = date["add"]["ids"]
        sub_data = date["sub"]["data"]
        sub_ids = date["sub"]["ids"]
    return add_data, add_ids,sub_data,sub_ids


# @pytest.fixture(params=getyaml()[0],ids=getyaml()[1])
@pytest.fixture(params=getyaml())
def get_fixture(request):
    """
    pytest.fixture参数化
    使用requrest 接受参数
    :param request:
    :return:request.param
    """
    print(f"request.param{request.param}")
    return request.param
    # return add_data,add_ids

def test_fix(get_fixture):
    print(get_fixture)




class Test_cacl():

    @allure.story("加法测试方法")
    # @pytest.mark.parametrize("a,b,expect", getyaml()[0], ids=getyaml()[1])
    def test_add1(self, getcacl, get_fixture):
        """
        加法的测试用例r
        :return:
        """
        # print(get_fixture)
        # for i in get_fixture[0]:
        #     print(i)
        # result = getcacl.add(get_fixture[1][0], get_fixture[1][1])
        # assert result == get_fixture[1][2]
        # pass



# @pytest.fixture(scope="class")
# def get_cacl():
#     print("开始计算")
#     cacl = Calculator()
#     yield cacl
#     print("结束计算")