from typing import List

import pytest
from pytestcode.cacl.calculator import Calculator


@pytest.fixture(scope="class",autouse=True)
def getcacl():
    """
    使用 pytest.fixture 初始化 计算器类
    :return: cacl
    """
    print("计算开始")
    cacl=Calculator()
    yield cacl
    print("计算结束")

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
        #转换编码格式
        item.name=item.name.encode("utf-8").decode('unicode-escape')
        item._nodeid = item.nodeid.encode("utf-8").decode('unicode-escape')
        # 添加标签
        if "add" in item._nodeid:
            item.add_marker(pytest.mark.add)
        elif "div" in item._nodeid:
            item.add_marker(pytest.mark.div)