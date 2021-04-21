# -*- encoding : utf-8 -*-
"""
@File       : promethues_test.py
@Time       :2021/4/13 15:18
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""
import datetime
import time

from mall.common.load_config import load_config
from mall.db.engines.promethuesEngine import PromethuesUtil

load_config()

ps = PromethuesUtil()

now = time.time()
params = {
    "query": "up",

    # 区间数据
    "end": now,
    "start": now - 60,
    "step": "15s"
}

result = ps.get_Instantaneous_data(params=params, method="query")
"""
{
   "status" : "success",
   "data" : {
      "resultType" : "vector",
      "result" : [
         {
            "metric" : {
               "__name__" : "up",
               "job" : "prometheus",
               "instance" : "localhost:9090"
            },
            "value": [ 1435781451.781, "1" ]
         },
         {
            "metric" : {
               "__name__" : "up",
               "job" : "node",
               "instance" : "localhost:9100"
            },
            "value" : [ 1435781451.781, "0" ]
         }
      ]
   }
}
"""
print(result)

result = ps.get_Instantaneous_data(method="query_range", params=params)
"""
{
   "status" : "success",
   "data" : {
      "resultType" : "matrix",
      "result" : [
         {
            "metric" : {
               "__name__" : "up",
               "job" : "prometheus",
               "instance" : "localhost:9090"
            },
            "values" : [
               [ 1435781430.781, "1" ],
               [ 1435781445.781, "1" ],
               [ 1435781460.781, "1" ]
            ]
         },
         {
            "metric" : {
               "__name__" : "up",
               "job" : "node",
               "instance" : "localhost:9091"
            },
            "values" : [
               [ 1435781430.781, "0" ],
               [ 1435781445.781, "0" ],
               [ 1435781460.781, "1" ]
            ]
         }
      ]
   }
}
"""
print(result)

params = {
    "query": "prometheus_http_requests_total"
}
result = ps.get_Instantaneous_data(params=params)
print(result)

params = {
    "match[]": "process_start_time_seconds{job='prometheus'}"
}
result = ps.get_Instantaneous_data(method="series", params=params)
print(result)
