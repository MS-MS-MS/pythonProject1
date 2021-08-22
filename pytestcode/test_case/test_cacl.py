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
    with open("../yaml/caclyaml.yaml", encoding="utf-8") as f:
        date = yaml.safe_load(f)
        add_data=date["add"]["data"]
        add_ids=date["add"]["ids"]
        sub_data=date["sub"]["data"]
        sub_ids=date["sub"]["ids"]
        mul_data=date["mul"]["data"]
        mul_ids=date["mul"]["ids"]
        div_data=date["div"]["data"]
        div_ids=date["div"]["ids"]
    return add_data, add_ids, sub_data, sub_ids,mul_data,mul_ids,div_data,div_ids


# def test_s():
#     getyaml()

# @pytest.fixture(scope="class")
# def get_cacl():
#     print("开始计算")
#     cacl = Calculator()
#     yield cacl
#     print("结束计算")


class Test_cacl():
    # def setup_class(self):
    #     """
    #     实例化 计算器类
    #     :return:
    #     """
    #     self.calc = Calculator()
    #
    # def treadown_class(self):
    #     pass

    # @pytest.mark.parametrize("a,b,expect",[(1,2,3),(2,3,5)])
    @allure.story("加法测试方法")
    @pytest.mark.parametrize("a,b,expect", getyaml()[0], ids=getyaml()[1])
    @pytest.mark.run(order=4)
    def test_add(self, a, b, expect,getcacl):
        """
        加法的测试用例r
        :return:
        """
        # rseult = self.calc.add(a, b)
        result = getcacl.add(a, b)
        assert result == expect

    # @pytest.mark.parametrize("a,b,expect",[(3,2,1),(6,5,1)])
    @allure.story("减法测试方法")
    @pytest.mark.parametrize(["a", "b", "expect"], getyaml()[2], ids=getyaml()[3])
    @pytest.mark.run(order=3)
    def test_sub(self, a, b, expect,getcacl):
        """
        减法的测试用例
        :return:
        """
        result =getcacl.sub(a, b)
        assert result == expect

    # @pytest.mark.parametrize("a,b,expect", [(3, 2, 6), (6, 5, 10)])
    # @allure.story("乘法测试方法")
    @pytest.mark.parametrize("a,b,expect", getyaml()[4], ids=getyaml()[5])
    @pytest.mark.run(order=2)
    def test_mul(self, a, b, expect,getcacl):
        """
        乘法的测试用例
        :return:
        """
        # rseult = self.calc.mul(a, b)
        # result=get_cacl.mul(a,b)
        result = getcacl.mul(a, b)
        assert result == expect

    # @pytest.mark.parametrize("a,b,expect", [(3, 0, 0), (6, 2, 3)])
    @allure.story("除法的测试方法")
    @pytest.mark.parametrize("a,b,expect", getyaml()[6], ids=getyaml()[7])
    @pytest.mark.run(order=1)
    def test_div(self, a, b, expect,getcacl):
        """
        除法的测试用例
        :return:
        """
        result=getcacl.div(a,b)
        assert result == expect

