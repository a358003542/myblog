Title: jupyter notebook
Slug: jupyter-notebook
Date: 2018-01-21 11:27
Modified:  2018-01-21 11:27
Tags: jupyter-notebook, ipython,
[TOC]

## magic function

### 运行某个python脚本
```
%run test.py
```
运行某个python脚本，里面的变量也会赋值在里面

### 运行系统的某个命令
```
!cat text.txt
```
在windows下是：
```
!type text.txt
```

### 脚本或命令运行计时
```
%timeit what
```



### 更好地集成matplotlib

```
%matplotlib inline
```

