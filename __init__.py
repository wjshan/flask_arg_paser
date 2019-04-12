# !/usr/bin/python3
# @File: __init__.py.py
# --coding:utf-8--
# @Author:daniel
# @Time: 2019年04月12日 10:17
from flask_restful import Resource
from .fields import Field
from flask import request
import copy


class PaserResource(Resource):
    def dispatch_request(self, *args, **kwargs):
        super().dispatch_request(*args, **kwargs)

    def get_all_field(self):
        return [(name, field) for name, field in self.__dict__ if isinstance(field, Field) and field.valid_method]

    def get_value(self, key):
        return request.get_data(key) or request.get_json(key)

    def valid_and_submit(self):
        for name, field in self.get_all_field():
            key = field.key or name
            value = self.get_value(key)
            _field = copy.deepcopy(field)
            _field.value = value
            self.__setattr__(name, copy.deepcopy(_field))
            for rule in field.validators:
                _v = rule(value)
                if _v is False:
                    return False
            validate_func = getattr(self, "validate_{}".format(key))
            if validate_func:
                return validate_func(value)
            return True
