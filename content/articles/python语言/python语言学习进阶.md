Title: python语言学习进阶
Slug: python-advanced
Date: 2019-06-24
Modified: 2019-06-24



[TOC]

## 前言

淘得好书 《深入理解python特性》和 《流畅的python》，来对自己的python语言知识继续进阶查漏补缺之。





### 最疯狂的字典表达式

```python
t = {True: 'yes', 1: 'no', 1.0: 'maybe'}
t
Out[3]: {True: 'maybe'}
```

造成这样的结果首先是python的字典的key相同的判断机制，比如是 值相同 而且是 hash 值相同 才认为是 key相同。

其次是认为key相同key就不做改变了，而值是取最新的。也正是因为这样，下面的字典更新语句写法是可行的：

```
x = {'a':1, 'b':2}
y = {'b':3}
z = {**x, **y}
```

```
z
Out[8]: {'a': 1, 'b': 3}
```

而且这也是最快的字典更新方式。









## 参考资料

1. 深入理解python特性 达恩·巴德尔 【德】
2. 流畅的python