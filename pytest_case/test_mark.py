# -*- coding: utf-8 -*-
""" 
@Time    : 2021/8/24 15:28
@Author  : MaSai
@FileName: test_mark.py
@SoftWare: PyCharm
"""
import pytest

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

class TestClass():
    @pytest.mark.smoke
    def test_one(self):
        print("test_one方法执行")
        assert  2==1
    @pytest.mark.tagname
    def test_two(self):
        print("test_two方法执行")
        assert  'o' in 'love'

    @pytest.mark.xfail
    def test_four(self):
        print("test_four方法执行")

@pytest.mark.tagnames
def test_there():
   print("test_there方法执行")
   assert  'o' in 'love'

