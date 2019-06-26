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

### ChainMap

将多个字典组合成为一个map字典，想到的一个应用就是配置字典流，利用ChainMap定义搜索路径流，先搜索到的配置优先取用。

```python
from collections import ChainMap
d1 = {'a':1,'b':2}
d2 = {'a':2,'d':3}
d3 = ChainMap(d1, d2)
```



### typing.NamedTuple

这个类添加于python3.6，与 collections.namedtuple 非常类似。

```python
from typing import NamedTuple
class Car(NamedTuple):
    color: str
    mileage: float
    automatic: bool
car1 = Car(color='red',mileage=3512.5, automatic=True)
car1.color
```

总的说来我不赞同达恩·巴德尔的观点——推荐使用typing.NamedTuple ，因为namedtuple有比较优势和区分的是相对于字典，其有两个特点：一，key不可变；二，轻量级。在某些情况下使用namedtuple优于字典。但是如果采用类的写法，那么就换了一个情景了，我认为在这个情境下，NamedTuple和dict都不太合适，而类应该成为第一公民。

### queue.PriorityQueue

queue.PriorityQueue 内部实现是基于heapq堆排序的，只是额外做了一些处理，从而保证操作是线程安全的。一般来说如果要实现一个优先级队列，推荐使用 PriorityQueue：

```python
from queue import PriorityQueue
q = PriorityQueue()
q.put((2, 'code'))
q.put((1, 'eat'))
q.put((3, 'sleep')) 
while not q.empty():
    print(q.get())
```

```
(1, 'eat')
(2, 'code')
(3, 'sleep')
```

### queue.Queue

这个是线程安全的先进先出【队列操作】数据结构。

```
from queue import Queue
q = Queue()
q.put('a')
q.put('c')
print(q.get())
print(q.get())
```

```
a
c
```



### queue.LifoQueue

这个是线程安全的后进先出【栈操作】的数据结构。

```
from queue import LifoQueue
q = LifoQueue()
q.put('a')
q.put('c')
print(q.get())
print(q.get())
```

```
c
a
```

### multiprocessing.Queue

跨进程的先进先出队列数据结构：

```
from multiprocessing import Queue
q = Queue()
q.put('a')
q.put('c')
print(q.get())
print(q.get())
```

```
a
c
```



## 参考资料

1. 深入理解python特性 达恩·巴德尔 【德】
2. 流畅的python