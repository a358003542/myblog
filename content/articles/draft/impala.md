Title: impala
Slug: impala
Date: 2019-05-21
Modified: 2019-05-21
Tags: impala
Status: draft

[TOC]

## impala



impala是用于处理Hadoop集群上的大量数据的SQL处理引擎。

impala可以让你使用传统的SQL知识以极快的速度处理存储在HDFS上的数据。

impala和传统SQL关系数据库还是有一些区别的：

- impala无法更新或删除单个记录
- impala不支持事务
- impala不支持索引



## python连接impala

[impyla](https://github.com/cloudera/impyla) 模块可以让python连接impala，简单的连接下面的README简单的说了一下。

具体各个使用语法就是符合python通用的db api 2，如果读者使用过sqlite3，python的官方模块，那么大概该怎么使用它心里已经有个数了。

不熟悉也没关系，简单的连接下看看输出结果，大概情况也就了解了。这一块主要是SQL语法。



## 导出到DataFrame对象

这个还是需要说一下，cursor对象executor某个语句之后，其可以如下转成pandas的DataFrame对象，有时这样转了之后，后面很多数据处理工作会很方便的。

```python
from impala.util import as_pandas
df = as_pandas(cur)
```







## 参考资料

1. [w3cschool 的impala教程](https://www.w3cschool.cn/impala/)