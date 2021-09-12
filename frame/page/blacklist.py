#!/usr/bin/python3.8.4 (python版本)
# -*- coding: utf-8 -*-
# @Author  : MS
# @Software: PyCharm
# @Time    : 2021/9/12 11:19
# @File    : blacklist.py
"""
find 方法的增强函数
处理黑名单方法
"""
import allure


def tmp(func):
    def wrapper(*args,**kwargs):
        from frame.page.basepage import BasePage
        # 当前的所以参数都在args里面 args=(self, by, value)
        _inance:BasePage=args[0]
        try:
            # func=find查找元素的方法
            # 找到元素直接返回
            result=func(*args,**kwargs)
            return result
        except Exception as e:
            #截屏使用
            _inance.driver.save_screenshot("tmp.png")
            # 已二进制的方式将图片打开
            with open("tmp.png","rb") as f:
                connent=f.read()
            # 将图片上传到allure
            # 确定图片上传类型
            allure.attach(connent,attachment_type=allure.attachment_type.PNG)
            # 处理异常方法 循环便利查找黑名单的方法
            for black_ele in _inance.blacklist:
                # 元组解包操作
                ele=_inance.driver.find_elements(*black_ele)
                if len(ele)>0:
                    # 关闭黑名单节目
                    ele[0].click()
                    # 递归调用 再次查早要找的元素
                    return wrapper(*args,**kwargs)
            # 在黑名单列表中没有找到元素直接报异常
            raise e
    return wrapper





