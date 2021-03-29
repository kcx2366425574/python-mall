# -*- encoding : utf-8 -*-
"""
@File       : __init__.py.py
@Time       :2021/3/29 18:46
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""

from mimesis import Person
from pprint import pprint

person = Person("zh")

pprint("{}[age:{}, sex:{}, university:{}]".format(person.name(), person.age(), person.sex(), person.university()))
