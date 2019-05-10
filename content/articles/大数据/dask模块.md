Title: dask模块
Slug: dask-module
Date: 2019-05-06
Modified: 2019-05-06
Tags: dask

[TOC]

## 前言

总的说来对于python生态圈来说，大数据解决方案我是推荐dask多于pyspark。接触pyspark之后最大的痛苦就是，之前学习机器学习积累下来的numpy，pandas，sklearn的知识，全部不能继续使用了。而dask作为python的大数据解决方案，不说完全无缝对接，这也是不现实的，毕竟到了大数据那块，不说其他东西，就是你要应对的变量，也必然是惰性加载和惰性求值的，这也是一个区别点。但总的给我的感觉就是，作为python爱好者，之于大数据解决方案，dask真的用的很爽。

dask的官方文档写的很厚实，主要是这块东西也多。本文作者尽我所知简要地说下个人使用经验吧。其他深入研究还是要读者去研究 [官方文档](https://docs.dask.org/en/latest/) 的。



## 大数据hadoop简介

现在的hadoop2的架构大概如下所示：

![img]({static}/images/大数据/HADOOP.png)

底层是hadoop分布式文件系统作为大数据的文件存储支持。HDFS的基本架构如下图所示：

![img](http://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-hdfs/images/hdfsarchitecture.png)

然后中层是YARN对计算资源进行调度分配。YARN的基本架构如下图所示：

![img](http://hadoop.apache.org/docs/stable/hadoop-yarn/hadoop-yarn-site/yarn_architecture.gif)

如上图所示，Yarn有一个Scheduler，也就是Resource Manager 进行资源调度，然后还有很多 个worker，也就是Node Manager进行实际的应用计算任务。

而最高层MapReduce框架是分布式应用程序的一个支持性框架，现在Hadoop2可扩展性很好，dask，spark等这些框架都是可以运行在Yarn之上的。

## dask-yarn

dask连接yarn集群

```python
from dask_yarn import YarnCluster
from dask.distributed import Client

# Create a cluster where each worker has two cores and eight GiB of memory
cluster = YarnCluster(environment = 'environment.tar.gz',
                      worker_vcores=w_cores,
                      worker_memory=w_mem,
                      scheduler_vcores=s_cores,
                      scheduler_memory=s_mem,
                      name=app_name,
                      worker_env={'ARROW_LIBHDFS_DIR': libhdfs_env})
# Scale out to ten such workers
cluster.scale(10)

# Connect to the cluster
client = Client(cluster)
```

基本的连接过程如上所示，你需要安装 `dask-yarn` 模块，然后连接的时候参数

- environment 你的分布式应用程序的python环境包，你可以激活虚拟环境下运行 `venv-pack` 命令来打包之。
- worker_vcores 申请分配应用资源worker cpu 核数
- worker_memory 申请分配应用资源worker 内存数
- scheduler_vcores 申请分配应用资源scheduler cpu 核数
- scheduler_memory 申请分配应用资源scheduler 内存数
- name 申请分配资源的应用名字
- work_env 这里是大数据组配置好了hadoop的环境变量



### 实际调整worker资源

最开始是没有实际开启worker资源的。

```
cluster.scale()
```

然后可以跟个数字，其会自动决定是 `scale_up` 还是 `scale_down` 。

### 关闭应用释放资源

似乎cluster的关闭动作会申请自动释放你在hadoop集群上申请的资源，但任何非正常推荐都可能导致申请的应用资源仍占在哪里的。更保险起见是确保异常之后总能够执行:

```
cluster.shutdown()
```

### 强制关闭某个应用

```
 dask-yarn kill application_1538148161343_0051
```



## dask单机版

dask单机版在熟悉dask命令和基本调试代码上还是很有用的，不需要做任何配置就是dask单机版。

按照官方文档，单机版也分为单机调度或分布式调度两种，官方文档推荐如下采用分布式调度，说有更好的诊断功能等。

```
from dask.distributed import Client, LocalCluster
cluster = LocalCluster()
client = Client(cluster)
```

似乎现在只能在linux上运行了。











单机版的线程调度中还是有所区别的：

- 相同的进程中用多个线程 【】 默认是dask.array dask.dataframe dask.delayed

scheduler="threads"

- 分开的进程处理 默认是dask.bag

scheduler="processes"

- 单线程式

scheduler="single-threaded"





## 参考资料

1. [dask官方文档](https://docs.dask.org/en/latest/)