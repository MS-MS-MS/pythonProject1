import yaml
"""
测试步骤使用
"""

def get_yaml():
    with open("../yaml/step.yaml")as f:
        date=yaml.safe_load(f)
        step=date["steps"]
    return step

def test_yaml():
    print(get_yaml())
    for step in get_yaml():
        print(step)
        if "add" in step:
            test_add()
        elif "sub" in step:
            test_sub()

def test_add():
    print("case1")

def test_sub():
    print("case2")


