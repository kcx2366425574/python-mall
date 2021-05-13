# -*- encoding : utf-8 -*-
"""
@File       : __init__.py.py
@Time       :2021/3/4 19:56
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""
from mall.utils.common_decoration import timethis, timethis_with_data, type_assert


@timethis("打印1000次")
def run():
    """
    print 1000 time
    :return:
    """
    for i in range(1000):
        print(i)
    print("-----------------")


@timethis_with_data(func_desc="打印1000次")
def run_with_data():
    """
    print 1000 time
    :return:
    """
    for i in range(1000):
        print(i)
    print("-----------------")


@type_assert(int, z=int)
def add(x, y, z=22):
    print(x+y+z)


if __name__ == '__main__':
    # run()
    # print(run.__doc__)
    #
    # run_with_data()
    # print(run_with_data.__doc__)
    add(1, 2, 11)

