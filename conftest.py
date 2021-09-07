import time
from typing import List

import allure
import pytest
from pytestcode.cacl.calculator import Calculator


# @pytest.fixture(scope="class", autouse=True)
# def getcacl():
#     """
#     使用 pytest.fixture 初始化 计算器类
#     :return: cacl
#     """
#     # print("计算开始")
#     cacl = Calculator()
#     yield cacl
#     # print("计算结束")


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    """
    hock 函数
    :param session:
    :param config:
    :param items:
    :return:
    """
    print(items)
    # 反转用例
    items.reverse()
    for item in items:
        # 转换编码格式
        item.name = item.name.encode("utf-8").decode('unicode-escape')
        item._nodeid = item.nodeid.encode("utf-8").decode('unicode-escape')
        # 添加标签
        if "add" in item._nodeid:
            item.add_marker(pytest.mark.add)
        elif "div" in item._nodeid:
            item.add_marker(pytest.mark.div)


# 按照时间自动生成日志
@pytest.fixture(scope="session", autouse=True)
def manage_logs(request):
    """Set log file name same as test name"""
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    # roordir 根目录
    # 优先级1:先找pytest.ini
    # 优先级2: conftest.py
    # pytest.ini和conftest.py 文件不存在 就会报错
    rootdir = request.config.rootdir
    # print(f"文件位置{rootdir}")
    log_name = rootdir + '/output/log/' + now + '.logs'
    request.config.pluginmanager.get_plugin("logging-plugin") \
        .set_log_path(log_name)

