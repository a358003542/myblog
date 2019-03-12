Title: spark学习笔记
Slug: spark-learning-note
Date: 2019-03-07
Modified: 2019-03-07
Tags: spark

[TOC]

## 前言

总的说来数据挖掘，数据处理，机器学习直到深度学习等，实际上其骨子里面的很多东西都是相通的。而从实践的角度出发，我们可以把这个领域看做更多的矩阵或者张量运算的领域，虽然大数据这个词概念不是很清晰，到底何种程度上才算得上大数据，我的一个总的看法是，如果你面对的计算，矩阵的维度数是非常大的，至少是上万的级别，而且随着你的项目程序运行，这个矩阵的大小还会进一步膨胀，这个时候就算得上大数据了吧。

现在单机的运算能力比以前又提升了不少，假设你面临一个算法问题，虽然暂时能够在单机上运算，但如果你面临的这个问题在一个很合理的时间范围内矩阵大小还会膨胀，直到超过你的单机承受能力，而你的算法代码，整个都是建立在矩阵这个思维之上的，这个时候我觉得你面对的就是一个大数据问题。

大数据问题是这样一个问题，可能我这样说不太确切，但大体也可以这样说，大数据问题就是矩阵过大的问题。

而现在似乎比较前沿的人工智能芯片问题实际上就是如何更好地设计芯片来加速矩阵运算的问题。

也就是大数据问题并不讨论算法细节，机器学习细节等。原则上你应该写一套非大数据工具下的测试代码小规模测试下你的算法代码，再移植到大数据工具上，而一个设计得很好的大数据工具，就是要让你从部署，维护到移植都感觉非常的舒适。

基于上面的讨论，这就引来了第一个问题，spark自带的机器学习包可能并不是很推荐使用，首先不得不承认spark精力有限，其自带的机器学习包功能很有限，更不用说新出来的神经网络等技术层出不穷，spark是不可能照顾得过来的。而keras那边对于这个领域是越做越好了，要让算法开发人员放弃这些模块，这是不可能的。所以我们在学习spark的时候必须要有这个底线，这个底线就是简单的根据spark做些简单的运算这是可以接受的，但复杂的算法实现不应该用spark那边提供的语言来写。如果不行，那更多是spark或者目前的大数据工具还不是很好用。

比如Apache arrow这个项目，似乎正在试图对接好spark的RDD和pandas的DataFrame等。这个是后面再说。笔者在大数据领域也是个人研究摸索性质，我们继续看吧。



## 安装

spark的安装还是很简单的，在windows下如果你已经配置好了JAVA环境，设置好了 `JAVA_HOME` 这个环境变量，然后下载下来的安装包解压出来即可。

以python来说，假设你安装了 

```
pip install pyspark
```

似乎就可以启用pyspark的shell环境了。这个还是挺让我困惑的，pyspark应该还不知道我的spark解压在哪里的吧，也可能是pyspark安装的时候自带的有？

但如果你想更加顺滑地在jupyter notebook下使用pyspark的语句的话，还是要把 `SPARK_HOME` 这个环境变量安装好，然后安装: 

```
pip install findspark
```

然后再jupyter notebook 下运行：

```python
import findspark
findspark.init()
import pyspark
from pyspark import SparkConf, SparkContext
conf = (SparkConf()
         .setMaster("local")
         .setAppName("My spark app")
         .set("spark.executor.memory", "1g"))
sc = SparkContext(conf = conf)
```

这里你也可以不设置 `SPARK_HOME` 环境变量，而是在上面代码的 `init` 方法哪里指定 `spark_home` 参数。

这里 `SparkConf` 是关于spark的一些配置，后面有时间再了解吧，按照spark最简单的教程，正常调出sc变量就算是在jupyter notebook环境下，当然，如果你运行的是python脚本的话，也就是python脚本下，成功对接好spark环境了。

这里的一些细节问题后面有时间翻文档，查资料吧，这里继续上面的讨论，这也是我们要用spark的核心原因，为什么spark能够很好地应对矩阵过大问题，当然spark的矩阵并行运算速度提升，能够发挥多台机器的潜力也是很重要的。

`SparkContext` 接受 `SparkConf` 指定的一些配置信息，然后与Spark集群进行连接，通过 `SparkContext` 可以进行创建RDD ，集群中广播变量等工作。

### centos7上安装spark

参考了参考资料3，感觉类似windows下的绿色安装方式，关键是findspark指向正确的位置，或者设置好 `SPARK_HOME` 环境变量。唯一值得一提的就是需要安装好java

```
sudo yum install java
```



## 什么时候用pyspark那边的东西

在初步接触之后正如前面讨论的，pyspark那边情况复杂而相关运算python支持模块少，不是动不动就把数据处理的任务转成pyspark那边的东西然后再从头开始写代码，这有时只是在浪费精力。

我对这块也在摸索讨论阶段，但也看到，对于某些问题【我是说代码中的某部分任务】，纯python单机版完全可以应付的来，可以做的又快又好，那么我们应该马上将pyspark的比如说DataFrame对象转成pandas的DataFrame对象，然后调用你之前写好的python代码完成工作即可。

只有那些不可避免要用到pyspark那边的东西，或者使用pyspark那边的东西能更好地完成工作时，才考虑用pyspark那边的东西。

我对这块还需要进一步学习研究，这里只是简单提下，比如说一个问题，pyspark那边读取的日志流，进入处理环节，数据最后精简整合为一个数据矩阵的，而这个数据矩阵相比较原来很庞大的日志流数据来说，是已经和很精简版本的了，而且在单机上是能够很好地应付了，那么就应该将这个数据矩阵转成pandas的Dataframe对象，然后完成任务即可。



## RDD是什么

似乎Spark的主打牌就是RDD，弹性分布式数据集（Resilient Distributed Dataset）。Spark关注的工作就是创建RDD，转化RDD，计算RDD。

一个简单的说法就是spark的RDD是分成不同的区的，然后每个区的RDD交给不同的机器（或者说执行器）来运算。这个分区动作就解决了矩阵维度过大的问题，但具体设计到计算，实际上就不那么简单了。简单的矩阵加减法问题不大，但矩阵乘法spark是怎么做的？不管怎么说spark这个功能因为引入RDD这个概念，或者说矩阵分区动作，是能够通过扩充机器应对矩阵过大的问题的。

spark工具还额外提供了大数据要对应的某个节点丢失之类的数据备份等等问题，这个算是大数据工具都要做的基本功了。

新建一个RDD:

```
x = sc.parallelize([1,2,3,4,5])
y = sc.parallelize([[1,2,3],[4,5,6]])
```

如果我运行：

```
x2 = x.map(lambda x: x+1)
```

然后试着打印RDD：

```
x.collect()
x2.collect()
```

似乎没什么问题，map每个元素执行了某个lambda算式，还好。

但如果是：

```
y2 = y.map(lambda y: y+1)
y2.collect()
```

程序就会抛出异常。

这里有两点，map的时候还没有实际计算，这叫做spark的惰性求值机制，第二点RDD在计算的面对的是原数据的一个一个——即第一层级，原始状态是不考虑矩阵这样的数据结构，而更接近于列表这种数据结构。

我们试着这样写：

```python
y2 = y.map(lambda y: list(map(lambda x: x+1, y)))
y2.collect()
```

这样矩阵的每个元素就都加一了，所以我们看到spark不是不可以应付矩阵这种数据结构，只是需要一些额外的工作。

如果spark只有RDD这个接口开放出来的话，那spark会非常非常的难用，有点类似于LISP语言的那种。不过才刚开始学习spark，还是不要太着急，似乎spark后面会提供其他结构形式的支持。





### RDD的cache方法

将目标RDD对象缓存到内存里面，





## 广播变量

```
x = sc.broadcase([1,2,3])
```

广播变量可以被工作节点访问，访问就是调用目标变量的 `value` 方法。暂时对这个广播变量还不是很懂，TODO



## 自定义UDF函数对象





## DataFrame对象

pyspark的DataFrame对象







## 参考资料

1. [using pyspark first](https://www.analyticsvidhya.com/blog/2016/10/using-pyspark-to-perform-transformations-and-actions-on-rdd/)
2. [pyspark dataframe operations](https://www.analyticsvidhya.com/blog/2016/10/spark-dataframe-and-operations/)
3. [install spark centos7](https://idroot.us/linux/install-apache-spark-centos-7/)