import allure
import pytest
import yaml

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
        add_data_float=date["add_float"]["data"]
        add_data_ids=date["add_float"]["ids"]
        div_data_zero=date["div_zero"]["data"]
        div_data_ids=date["div_zero"]["ids"]
    return [add_data, add_ids, sub_data, sub_ids,mul_data,mul_ids,div_data,\
           div_ids,add_data_float,add_data_ids,div_data_zero,div_data_ids]


# def test_s():
#     getyaml()

@pytest.fixture(params=getyaml()[0],ids=getyaml()[1])
def get_fixture(request):
    """
    pytest.fixture参数化
    使用requrest 接受参数
    :param request:
    :return:request.param
    """
    return request.param
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
    @pytest.mark.run(order=6)
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
    @pytest.mark.run(order=5)
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
    @pytest.mark.run(order=4)
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
    @pytest.mark.run(order=3)
    def test_div(self, a, b, expect,getcacl):
        """
        除法的测试用例
        :return:
        """
        result=getcacl.div(a,b)
        assert result == expect

    @allure.story("加法浮点数的测试方法")
    @pytest.mark.parametrize("a,b,expect", getyaml()[8], ids=getyaml()[9])
    @pytest.mark.run(order=2)
    def test_add_float(self, a, b, expect, getcacl):
        # 以二进制的方式打开图片
        with open("../yaml/erro.png", "rb") as f:
            content = f.read()
        # 将图片传送给allure
        allure.attach(content, attachment_type=allure.attachment_type.PNG)
        """
        加法浮点数的测试方法
        :return:
        """
        result = getcacl.add(a, b)
        assert round(result,2) == expect

    @allure.story("除法除数为零的情况")
    @pytest.mark.parametrize("a,b,expect", getyaml()[10], ids=getyaml()[11])
    @pytest.mark.run(order=1)
    def test_div_zero(self, a, b, expect, getcacl):
        """
        除法除数为零的情况
        :return:
        """

        with pytest.raises(ZeroDivisionError):
            print("除法除数为零的情况")
            getcacl.div(a, b)



    # @allure.story("fixture测试方法")
    # # @pytest.mark.parametrize("a,b,expect", getyaml()[0], ids=getyaml()[1])
    # @pytest.mark.run(order=7)
    # def test_add1(self, getcacl,get_fixture):
    #     """
    #     加法的测试用例r
    #     :return:
    #     """
    #     # print(get_fixture)
    #     # rseult = self.calc.add(a, b)
    #     result = getcacl.add(get_fixture[0][0], get_fixture[0][1])
    #     assert result == get_fixture[0][2]
