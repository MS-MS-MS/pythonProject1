# -*- coding: utf-8 -*-
""" 
@Time    : 2021/9/14 16:51
@Author  : MaSai
@FileName: test_app.py
@SoftWare: PyCharm
"""
from app_pageobject.page.app import App


class TestApp:
    def setup(self):
        self.main=App().start_app()

    def test_add(self):
        self.main.goto_main().goto_maillist().goto_addmember().goto_contact().goto_add()
