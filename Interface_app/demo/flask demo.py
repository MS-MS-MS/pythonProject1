# -*- coding: utf-8 -*-
""" 
@Time    : 2021/9/23 16:16
@Author  : MaSai
@FileName: flask demo.py
@SoftWare: PyCharm
set FLASK_APP=flask demo.py
flask run
"""
from flask import Flask, session, request, Request, make_response

app = Flask(__name__)
request: Request
app.secret_key = "key"


@app.route("/request", methods=['POST', 'GET'])
def hello():
    query = request.args
    post = request.form
    return f"query: {query}\n" \
           f"post: {post}"


@app.route("/session")
def session_handle():
    for k, v in request.args.items():
        session[k] = v
    resp = make_response({k: v for k, v in session.items()})
    for k, v in request.args.items():
        resp.set_cookie(f"cookie_{k}", v)
    return resp