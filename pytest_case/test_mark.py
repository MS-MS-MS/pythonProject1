# -*- coding: utf-8 -*-
"""
@Time    : 2021/8/24 15:28
@Author  : MaSai
@FileName: test_mark.py
@SoftWare: PyCharm
"""

"""
标记测试用例
pytest.mark
提示警告配置pytest.ini 文件
markers=
        smoke:说明(不能使用中文)
@pytest.mark.xfail
期望测试用例是失败的，但是不会影响测试用例的的执行。
如果测试用例执行失败的则结果是xfail（不会额外显示出错误信息）；如果测试用例执行成功的则结果是xpass。
"""
import pytest


@pytest.fixture()
def get_fix():
    print("get_fix")


class TestClass():
    @pytest.mark.smoke
    def test_one(self):
        print("test_one方法执行")
        assert 2 == 1

    @pytest.mark.tagname
    def test_two(self):
        print("test_two方法执行")
        assert 'o' in 'love'

    @pytest.mark.xfail
    def test_xfail(self):
        print("xfail:期望用例是失败用例")

    @pytest.mark.skip(reason="跳过此用例")
    def test_skip(self):
        print("skip:不执行此用例")

    @pytest.mark.usefixtures("get_fix")
    def test_usefixtures(self):
        print("xc")

    @pytest.mark.flaky(reruns=3, reruns_delay=1)
    def test_flaky(self):
        print("标记重跑次数及延时时间")
        assert 1 == 2
#
#
# @pytest.mark.tagnames
# def test_there():
#     print("test_there方法执行")
#     assert 'o' in 'love'
#
#
# def login():
#     print("登录")
#
#
# @pytest.mark.usefictures("login")
# def test_case1():
#     print("case1")
    # 标记
# import sys
# skipmark = pytest.mark.skip(reason="不能在window上运行=====")
# skipifmark = pytest.mark.skipif(sys.platform == 'win32', reason="不能在window上运行啦啦啦=====")
#
# @skipmark
# class TestSkip_Mark(object):
#     """
#     跳过标记
#     """
#
#     @skipifmark
#     def test_function(self):
#         print("测试标记")
#
#     def test_def(self):
#         print("测试标记")
#
# @skipmark
# def test_skip():
#     print("测试标记")
#
#
#
#
# if sys.platform.startswith("IOS"):
#     pytest.skip("skipping windows-only tests", allow_module_level=True)
#
#
# @pytest.fixture(autouse=True)
# def login():
#     print("====登录====")
#
#
# def test_case01():
#     print("我是测试用例11111")
#
#
# import pytest
# @pytest.fixture()
# def demo_fixture(request):
#     test_input = request.param
#     if test_input == 3:
#         pytest.skip("传入的值等于3就跳过执行")
# @pytest.mark.parametrize("demo_fixture", [1, 3], indirect=True,ids=["正常","跳过"])
# def test_the_unknown3(demo_fixture):
#     print("a")
#     ...
# # if __name__ == "__main__":
# #     pytest.main(["-s", '-r' "test_skipif.py"])
#
# @pytest.mark.xfail(raises=AssertionError)
# def test_01():
#     assert 1 == 2
#
#
# @pytest.mark.xfail(raises=ValueError)
# def test_02():
#     if isinstance('1234', int) is not True:
#         raise TypeError("传入参数非整数")
#
# @pytest.mark.xfail(strict=True)
# def test_01():
#     assert 1 == 1
#
#
#
# def test_xfail():
# 	print("xfail方法")
# 	pytest.xfail(reason="不行执行")
# 	assert 1==1
#
# @pytest.mark.xfail
# def test_02():
#     assert 1 == 2
#
# import pytest
# class TestClass():
#
#     def test_one(self):
#         print("test_one方法执行")
#         pytest.xfail(reason='该功能尚未完善')
#         assert  1==1
#
#     def test_two(self):
#         print("test_two方法执行")
#         assert  'o' in 'love'
#
#     def test_three(self):
#         print("test_three方法执行")
#         assert 3-2==1