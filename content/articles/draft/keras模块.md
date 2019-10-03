Title: keras模块
Slug: keras-module
Date: 2018-11-05
Modified: 2018-11-05
Tags: keras
Status: draft

[TOC]

## 前言

本文档记录关于keras模块学习中的一些东西。



## to_categorical

把一个向量变成二元数字(即0 1 )的矩阵，实际上就是one-hot编码。

```python
import numpy as np
labels = np.array([1,2,3,1,2,3,1,2,3])
labels
array([1, 2, 3, 1, 2, 3, 1, 2, 3])
to_categorical(labels)
array([[0., 1., 0., 0.],
       [0., 0., 1., 0.],
       [0., 0., 0., 1.],
       [0., 1., 0., 0.],
       [0., 0., 1., 0.],
       [0., 0., 0., 1.],
       [0., 1., 0., 0.],
       [0., 0., 1., 0.],
       [0., 0., 0., 1.]], dtype=float32)
```

默认输出的dtype是 float32，然后你可以用 `num_classes=None` 来指定种类数，或者让程序自己判断。

这个one-hot编码通常用于标签数据的预处理。

