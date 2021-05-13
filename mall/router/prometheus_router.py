# -*- encoding : utf-8 -*-
"""
@File       : prometheus_router.py
@Time       :2021/5/7 9:39
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""

from flask import Blueprint, request

from mall.db.engines.promethuesEngine import PromethuesUtil

app_prometheus = Blueprint('prometheus', __name__)


@app_prometheus.route('/get_promql', methods=['GET'])
def get_promql_return():
    params = request.args.to_dict()
    metric_name = params.pop("metric_name")
    time_qujian = params.pop("time_qujian", None)
    offset = params.pop("offset")
    result = PromethuesUtil().get_promql(metric_name, time_qujian=time_qujian, offset=offset, **params)
    return result
