Category: javascript
Slug: javascript-language-learning-advanced
Date: 2021

[TOC]

## 前言

本文是笔者在学习了javascript语言基本知识的基础上继续学习的整理总结。



## setInterval

```
setInterval(func, 1000)
```

启动一个计时器，第二个参数是时间间隔，每个那个时间间隔将会执行一次目标函数，默认单位是ms。



### 将JavaScript对象转成JSON字符串

如下所示，下面也演示了利用 `JSON.parse` 来将相应的JSON字符串转成JavaScript对象。

```javascript
> let x = JSON.stringify({ x: 5, y: 6 });
undefined
> x
'{"x":5,"y":6}'
> typeof x
'string'
> let y = JSON.parse(x)
undefined
> y
{ x: 5, y: 6 }
> typeof y
'object'
```





## 参考资料

1. Javascript权威指南 David Flanagan著.
2. [mozilla docs](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript)
3. [现代javascript教程](https://zh.javascript.info/)
4. [you donot need jquery](https://github.com/nefe/You-Dont-Need-jQuery/blob/master/README.zh-CN.md)