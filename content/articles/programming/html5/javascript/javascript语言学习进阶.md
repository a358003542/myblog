Category: javascript
Slug: javascript-language-learning-advanced
Date: 20201125

[TOC]

## 前言

本文是笔者在学习了javascript语言基本知识的基础上继续学习的整理总结。





## 字符串

### 字符串的match方法

字符串的match方法可以跟上RegExp 对象来继续正则表达式匹配操作。

## 对象

### 获取对象的keys数组

```
attrs = attrs || {};
Object.keys(attrs);
```





## 函数

### 立即执行的匿名函数

我们常见到某个js脚本一整段都被这样一种写法包围着：

```
(function($){…})(jQuery)
```

这是定义了一个匿名函数，其将立即执行，接受了一个jQuery参数，并传递给了匿名函数。





## document

### createElement

```
var e = document.createElement(name);
```

创建一个标签，返回的是一个 `Element` 对象。

### createTextNode

```
child = document.createTextNode(child);
```

创建一个文本节点。

```javascript
var e = document.createElement('li');
var t = document.createTextNode('this is text.')
e.appendChild(t);
```

上面的例子创建了一个li标签，然后创建了一个文本节点，然后将这个文本节点附加到该li标签上，最后该li标签内容如下：

```
<li>this is text.</li>
```

## Element对象

### querySelector

之前接触到的`document.querySelector` 是因为Document对象继承自Element对象，该方法实际来自Element对象。具体就是在本Element下继续进行搜索动作。

### setAttribute

`Element` 对象可以调用这个 `setAttribute` 方法来设置标签内的属性值。

```
element.setAttribute(name, value);
```



## Node对象

之前提到querySelector查到某个Element之后想要取出其文本内容可以调用 `textContent` 属性，document和Element都能这样做只是因为它们继承自Node对象，具体textContent这个属性的定义是在Node对象这里。

## 事件

Element对象继承自EventTarget从而获得了这些方法： `addEventListener` ， `removeEventListener` 和 `dispatchEvent` ，这几个方法都是和事件处理相关的。

熟悉GUI桌面程序的话会对事件有个大致的理解，大体类似于QT里面的信号。



### CustomEvent

自定义一个事件，第二个参数可以是任意的信息。

```
  new CustomEvent(name, { bubbles: true, cancelable: false })
```

### dispatchEvent

程序触发某个Element元素上监听的事件

```javascript
target.dispatchEvent(
      new CustomEvent(name, { bubbles: true, cancelable: false })
);
```

### addEventListener

给某个元素增加一个事件监听

### removeEventListener

移除某个元素上的事件监听



## 其他

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



### setInterval

```
setInterval(func, 1000)
```

启动一个计时器，第二个参数是时间间隔，每个那个时间间隔将会执行一次目标函数，默认单位是ms。









## 参考资料

1. Javascript权威指南 David Flanagan著.
2. [mozilla docs](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript)
3. [现代javascript教程](https://zh.javascript.info/)
4. [you donot need jquery](https://github.com/nefe/You-Dont-Need-jQuery/blob/master/README.zh-CN.md)