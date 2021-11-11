# -*- coding: utf-8 -*-
""" 
@Time    : 2021/11/10 16:05
@Author  : MaSai
@FileName: file_tools.py
@SoftWare: PyCharm
"""
import json
import os
import os.path
import uuid

import yaml


class FileTools:

    @classmethod
    def get_interface_dir(cls):
        # 返回interface的文件夹的绝对路径
        return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    @classmethod
    def read_yaml(cls, file_name):
        # 获取interface处于的目录
        _path = cls.get_interface_dir()

        print(_path)
        # 根据文件名拼装出来当前文件的绝对路径
        yaml_file = os.sep.join([_path, "data", file_name + ".yaml"])
        # 打开文件流
        with open(yaml_file, encoding="utf-8") as f:
            # 使用yaml把文件流转换成python对象返回回去
            return yaml.safe_load(f)





# if __name__ == '__main__':
#     print(FileTools.read_yaml("tag"))
#     data=FileTools.read_yaml("tag")
#     group_name=data["tag"]["add"]["group_name"]
#     print(group_name)
#     name=data["tag"]["add"]["name"]
#     print(name)
