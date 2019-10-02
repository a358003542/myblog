Title: hadoop文件系统
Slug: hadoop-file-system
Date: 2019-05-10
Modified: 2019-05-10
Tags: hdfs
Status: draft

[TOC]

## 前言

hdfs的全称是hadoop分布式文件系统。

HDFS采用master/slave架构。一个HDFS集群是由一个Namenode和一定数目的Datanode组成的。

hdfs的设计主要针对那些只写入一次，多次读取的数据。





## pyarrow连接hdfs

```python
import pyarrow as pa
fs = pa.hdfs.connect(host, port, user=user)
```

连接之后返回的是HDFS文件对象，该文件对象可以继续调用如下命令：

- cat

- chmod

- chown

- delete

- df

- exists

- get_capacity

- get_space_used

- info

- ls

- rm

- rename

- upload