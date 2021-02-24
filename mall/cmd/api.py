# -*- encoding : utf-8 -*-
"""
@File       : api.py
@Time       :2021/1/22 15:42
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""
from mall import app
from mall.common.load_config import load_config


if __name__ == '__main__':
    load_config()
    app.run(host="0.0.0.0", port=8081, threaded=True)
