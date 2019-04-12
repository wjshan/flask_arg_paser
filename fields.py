# !/usr/bin/python3
# @File: fields.py
# --coding:utf-8--
# @Author:daniel
# @Time: 2019年04月12日 10:17
from flask import request


class Field(object):
    def __init__(self, key=None, methods=None, validators=None):
        self.key = key
        self.value = None
        self.validators = validators or []
        self.methods = methods

    @property
    def valid_method(self):
        meth = request.method.lower()
        return not self.methods or meth in self.methods
