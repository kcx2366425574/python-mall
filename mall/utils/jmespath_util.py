# -*- encoding : utf-8 -*-
"""
@File       : jmespath_util.py
@Time       :2021/4/1 14:22
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : 默认值为自己加的，源代码没有
"""

import jmespath

d = {"foo": {"bar": "baz"}}
# baz
print(jmespath.search('foo.bar', d))


a = {"foo": {"bar": [{"name": "aa"}, {"name": "bb"}]}}
# ['aa', 'bb']
print(jmespath.search('foo.bar[*].name', a, default_value=22))


b = {"foo": {"bar": "baz"}}
# 55
print(jmespath.search('foo.zz', b, default_value=55))


c = ["1", "2", "3", "4"]
# 2
print(jmespath.search('[1]', c))
