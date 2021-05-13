1、当我们直接使用监控指标名称查询时，可以查询该指标下的所有时间序列。如：

```text
http_requests_total
```
等同于
```text
http_requests_total{}
```

2、PromQL还支持用户根据时间序列的标签匹配模式来对时间序列进行过滤，目前主要支持两种匹配模式：完全匹配和正则匹配。

2.1 完全匹配
例如，如果我们只需要查询所有http_requests_total时间序列中满足标签instance为localhost:9090的时间序列，则可以使用如下表达式：
```text
http_requests_total{instance="localhost:9090"}
```
反之使用instance!="localhost:9090"则可以排除这些时间序列：
```text
http_requests_total{instance!="localhost:9090"}
```

2.2 正则匹配
除了使用完全匹配的方式对时间序列进行过滤以外，PromQL还可以支持使用正则表达式作为匹配条件，多个表达式之间使用|进行分离.
例如，如果想查询多个环节下的时间序列序列可以使用如下表达式：
```text
http_requests_total{environment=~"staging|testing|development",method!="GET"}
```


### 范围查询

通过以下表达式可以选择最近5分钟内的所有样本数据
```text
http_requests_total{}[5m]
```

### 时间位移操作
在瞬时向量表达式或者区间向量表达式中，都是以当前时间为基准：
```text
# 瞬时向量表达式，选择当前最新的数据
http_request_total{} 
# 区间向量表达式，选择以当前时间为基准，5分钟内的数据
http_request_total{}[5m] 
```

而如果我们想查询，5分钟前的瞬时样本数据，或昨天一天的区间内的样本数据呢? 这个时候我们就可以使用位移操作，位移操作的关键字为offset。
```text
http_request_total{} offset 5m
http_request_total{}[1d] offset 1d
```

### 聚合操作
```text
# 查询系统所有http请求的总量
sum(http_request_total)

# 按照mode计算主机CPU的平均使用时间
avg(node_cpu) by (mode)

# 按照主机查询各个主机的CPU使用率
sum(sum(irate(node_cpu{mode!='idle'}[5m]))  / sum(irate(node_cpu[5m]))) by (instance)
```