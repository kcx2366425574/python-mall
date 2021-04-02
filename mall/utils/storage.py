# -*- encoding : utf-8 -*-
"""
@File       : storage.py
@Time       :2021/3/31 16:22
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : 扩展dict
"""


class Storage(dict):

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError as k:
            raise AttributeError(k)

    def __setattr__(self, key, value):
        self[key] = value

    def __delattr__(self, key):
        try:
            del self[key]
        except KeyError as k:
            raise AttributeError(k)

    def __repr__(self):
        return "<Storage " + dict.__repr__(self) + ">"


o = Storage()
o.b = 22
o.a = "aa"
print(o.b)
print(o["b"])
print(o)
