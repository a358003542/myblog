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



## JSON

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



## 函数

### 立即执行的匿名函数

我们常见到某个js脚本一整段都被这样一种写法包围着：

```
(function($){…})(jQuery)
```

这是定义了一个匿名函数，其将立即执行，接受了一个jQuery参数，并传递给了匿名函数。

之所以这种写法很常见是因为这样做可以将整个模块的代码都放在一个匿名函数里面，这样模块里面定义的全局变量就成了函数内的局部变量了，这样不会污染全局变量命名空间。

## window

window对象里面的属性都是全局变量，可以直接调用的。

### setInterval

```
setInterval(func, 1000)
```

启动一个计时器，第二个参数是时间间隔，每个那个时间间隔将会执行一次目标函数，默认单位是ms。

### setTimeout

类似setInterval，启动一次性任务。

### location

该窗口的Location对象

### history

该窗口的History对象

## document

### getElementById

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

### dataset

查询到的元素如果div则是更具体的HTMLdivElement等等，其继承自HTMLElement，HTMLElement有一些专门的方法。比如这个dataset，其是可以只读属性，对应html中的`data-*` 这样的属性值，比如说 `data-name` 将变成dataset的`{'name': 'what'}` 。

### classList

类似上面的讨论也是HTMLElement的一个属性，表示class属性数组。



## Node对象

### textContent

之前提到querySelector查到某个Element之后想要取出其文本内容可以调用 `textContent` 属性，document和Element都能这样做只是因为它们继承自Node对象，具体textContent这个属性的定义是在Node对象这里。

### parentElement

返回本节点的父节点

```
parentElement = node.parentElement
```

### removeChild

移除本节点的某个子节点

```
node.removeChild(child);
```



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

### event.target和event.currentTarget的区别

事件响应到调用函数那边，通过event.target或者event.currentTarget可以引用触发事件的浏览器对象，不过它们是有一点区别的。

首先说一下事件的冒泡机制，当某个元素触发了某个事件，其会触发本元素上事件响应处理程序，然后该事件会继续冒泡到本元素的父元素之上，再触发父元素的事件响应处理程序。

event.target是引用那个最开始触发事件的那个目标元素，而event.currentTarget是引用那个实际处理事件的元素。比如说某个div里面有一个button，你给div绑定了事件监听处理函数，然后那个事件监听处理函数里面调用 `event.currentTarget` 则会指向那个div，而如果你调用 `event.target` 则会引用最开始触发click事件的那个元素，也就是button。

在一个目标button里面处理click事件使用event.target或者event.currentTarget是没有区别的。

## 其他









## 参考资料

1. Javascript权威指南 David Flanagan著.
2. [mozilla docs](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript)
3. [现代javascript教程](https://zh.javascript.info/)
4. [you donot need jquery](https://github.com/nefe/You-Dont-Need-jQuery/blob/master/README.zh-CN.md)