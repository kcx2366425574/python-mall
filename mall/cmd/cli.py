# -*- encoding : utf-8 -*-
"""
@File       : cli.py
@Time       :2021/2/26 8:50
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""
import fire
from mall.db.models.product import product_inner_func as ProductIN


CONST_NAME = {
    "product": ProductIN
}


def list(name):
    if name not in CONST_NAME:
        return "please input correct args, {}".format(CONST_NAME.keys())
    result = CONST_NAME.get(name).get_product()
    return [i.to_dict() for i in result]


fire.Fire()
