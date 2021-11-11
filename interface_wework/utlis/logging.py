# -*- coding: utf-8 -*-
""" 
@Time    : 2021/11/10 19:41
@Author  : MaSai
@FileName: logging.py
@SoftWare: PyCharm
"""
import logging
import os

from interface_wework.utlis.file_tools import FileTools

"""
日志文件
"""

# 创建logging对象
logger = logging.getLogger(__name__)
# 拼接log文件夹
file_path = os.sep.join([FileTools.get_interface_dir(), "logs"])
if not os.path.exists(file_path):
    # 判断文件是否存在，如果不存在则创建文件
    os.mkdir(file_path)
# 拼接log文件夹路径和句柄
fileHandler = logging.FileHandler(filename=file_path + "/apitest.log", encoding="utf-8")
# 日志格式 时间-文件名-方法名-报错行号-日志等级-日志信息
formatter = logging.Formatter('[%(asctime)s] %(filename)s - %(funcName)s line:%(lineno)d [%(levelname)s]: %(message)s')
# 句柄绑定日志格式
fileHandler.setFormatter(formatter)
# 控制台句柄定义
streamHandler = logging.StreamHandler()
# 控制台句柄绑定格式
streamHandler.setFormatter(formatter)
# 设置生效
logger.addHandler(fileHandler)
logger.addHandler(streamHandler)
# 设置日志的级别
logger.setLevel(logging.INFO)
