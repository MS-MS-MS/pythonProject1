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


"""
1. 简答题
题目：
（1）计算机器（加法和除法）测试用例，使用fixture 实现setup/teardown 功能
（2）使用第三方插件完成测试用例顺序的控制
（3）编写的用例使用Allure工具生成测试（添加日志，截图）

使用@pytest.fixture进行参数化
@pytest.fixture(params=getyaml()[0],ids=getyaml()[1])
# params 接受一个列表，列表中每个数据都可以作为用例的输入。也就说有多少数据，就会形成多少用例
# 不能接受字典或者元组 
# 当前只能在传入数据的时候进行解析,加法的数据取出来,写加法的fixture参数化 , 减法的数据,写减法的参数化
# 想的是写一个fixture参数化的方法，每个测试方法调用该方法，但是params 只能接受列表:list[],不能解析出值  
# 当前这个问题先挂起,在深入学习以后在解决
"""
def getyaml():
    """
    解析ymal 文件
    :return:
    """
    with open("../yaml/caclfix.yaml", encoding="utf-8") as f:
        date = yaml.safe_load(f)
        add_data = date["add"]["adddata"]
        add_ids = date["add"]["addids"]
        sub_data = date["sub"]["subdata"]
        sub_ids = date["sub"]["subids"]
    return [add_data, add_ids,sub_data,sub_ids]

@pytest.fixture(params=getyaml()[0],ids=getyaml()[1])
def get_fix_add(request):
    """
    加法参数
    request 默认接受参数
    使用request.param 返回参数
    :param request:
    :return: request.param
    """
    return request.param

@pytest.fixture(params=getyaml()[2],ids=getyaml()[3])
def get_fix_sub(request):
    """
      减法参数
      request 默认接受参数
      使用request.param 返回参数
      :param request:
      :return: request.param
      """
    return request.param

class Test_cacl():
    """
    使用fixtrue 参数化
    """
    def test_add(self,getcacl,get_fix_add):
        result=getcacl.add(get_fix_add[0],get_fix_add[1])
        assert result== get_fix_add[2]

    def test_sub(self,getcacl,get_fix_sub):
        result=getcacl.sub(get_fix_sub[0],get_fix_sub[1])
        assert result== get_fix_sub[2]



# def test_fix(get_fix_add):
#     print(get_fix_add)
#     print(type(get_fix_add))

# def getyaml():
#     """
#     解析ymal 文件
#     :return:
#     """
#     with open("../yaml/caclfix.yaml", encoding="utf-8") as f:
#         date = yaml.safe_load(f)
#         add_data = date["add"]["adddata"]
#         add_ids = date["add"]["addids"]
#         sub_data = date["sub"]["subdata"]
#         sub_ids = date["sub"]["subids"]
#     return [add_data, add_ids,sub_data,sub_ids]
#     #     add_data = date["add"]
#     #     sub_data = date["sub"]
#     # return add_data,sub_data
#
# # dict={'adddata': [[2, 2, 4], [100, 100, 100], [-1, -2, -3], [0, 0, 0]],
# #       'addids': ['整型', '大数', '负数', 'zero']}, \
# #      {'subdata': [[1, 1, 0], [0.5, 0.2, 0.3], [200, 100, 100], [-5, -2, -3], [0, 0, 0]],
# #      'subids': ['整型', '浮点', '大数', '负数', 'zero']}
# @pytest.fixture(params=getyaml()[0],ids=getyaml()[1])
# @pytest.fixture(params=list(getyaml()))
# def get_fixture(request):
#     """
#     pytest.fixture参数化
#     使用requrest 接受参数
#     :param request:
#     :return:request.param
#     """
#     # print(f"request.param{request.param}")
#     return request.param
#     # return add_data,add_ids
#
# def test_fix(get_fixture):
#     print(type(get_fixture))
    print(get_fixture)
    # a=get_fixture['adddata']
    # b=get_fixture['addids']
    # print(a)
#
# def test_getyaml():
#     print(type(getyaml()))
#
#
#
#
# class Test_cacl():
#
#     @allure.story("加法测试方法")
#     # @pytest.mark.parametrize("a,b,expect", getyaml()[0], ids=getyaml()[1])
#     def test_add1(self, getcacl, get_fixture):
#         """
#         加法的测试用例r
#         :return:
#         """
#         # print(get_fixture)
#         # print(get_fixture['adddata'][0])
#         # print(get_fixture['adddata'][1])
#         # print(get_fixture['adddata'][2])
#         # print(get_fixture['addids'])
#         # for i in get_fixture['adddata']:
#         #    a= get_fixture['adddata'][i][0]
#         #    b= get_fixture['adddata'][i][1]
#         #    c= get_fixture['adddata'][i][2]
#             # result = getcacl.add(get_fixture['adddata'][i][0], get_fixture['adddata'][i][1])
#             # assert result == get_fixture['adddata'][2]
#         #
#         # pass
# # {'subdata': [[1, 1, 0], [0.5, 0.2, 0.3], [200, 100, 100], [-5, -2, -3], [0, 0, 0]], 'subids': ['整型', '浮点', '大数', '负数', 'zero']}
# # {'subdata': [[1, 1, 0], [0.5, 0.2, 0.3], [200, 100, 100], [-5, -2, -3], [0, 0, 0]], 'subids': ['整型', '浮点', '大数', '负数', 'zero']}
# # {'adddata': [[2, 2, 4], [100, 100, 100], [-1, -2, -3], [0, 0, 0]], 'addids': ['整型', '大数', '负数', 'zero']}
# # {'adddata': [[2, 2, 4], [100, 100, 100], [-1, -2, -3], [0, 0, 0]], 'addids': ['整型', '大数', '负数', 'zero']}
#
#
#
# # @pytest.fixture(scope="class")
# # def get_cacl():
# #     print("开始计算")
# #     cacl = Calculator()
# #     yield cacl
# #     print("结束计算")
#
# # @pytest.mark.parametrize("a,b,c",[(1,2,3),(1,5,6)],ids=["int","int1"])
# # def test_case(a ,b,c):
# #     result=a+b
# #     assert result==c