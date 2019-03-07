Title: wxpython第一谈
Date: 2018-08-27
Modified: 2018-09-20
Slug: wxpython-talk-one
Tags: wxpython,


[TOC]

## 前言

本文假设读者已经熟悉某一种桌面图形开发了，比如说PyQt之类的，也就是基本的图形桌面开发概念读者是熟悉了，下面将言简意赅地就wxpython相关的特色核心概念说明之，然后后面就针对某些专门的问题专门讨论了。

首先说下安装，现在wxpython和pyqt5一样都已经进步了，都可以直接用pip安装了，而且linux下和windows都可以直接安装。



## Sizer.Add参数详解

- `Sizer.Add(item, 0 , wx.ALIGN_RIGHT, 0)`    右对齐布局，第一个参数proportion详细讨论在后面，第三个参数是设置border的宽度的。
- Sizer.Add(item, 0, wx.ALIGN_CENTER, 0)  居中布局
- Sizer.Add(item, 0, wx.EXPAND, 0) 扩展布局，（在vertical sizer里面水平扩展；在horizontal sizer里面垂直扩展）

### proportion参数

默认是0，0表示不缩放，我估计这样设置之后父窗体Layout，而子窗体将不会自动Layout。然后设置其他整数则是某种缩放比的意思。参考资料谈了一些缩放比的问题，暂时不是很关心这个。下面是讨论的原文：

> proportion参数是被wx.BoxSizer用作因数去决定当sizer的大小改变时，sizer应该如何调整它的孩子的尺寸。我们这里使用的是水平方向调整的sizer，stretch因数决定每个孩子的水平尺寸如何改变（坚直方向的改变由box sizer基于第三个参数来决定）。

一般的0表示不缩放，1表示随着父窗体缩放而缩放。

### Flag参数

这块东西经常遇到，虽然Flag较多，还是建议沉下心来学一下，这些后面会频繁用到的：

####  控制那边有border
```
wx.TOP
wx.BOTTOM
wx.LEFT
wx.RIGHT
wx.ALL
```

#### 扩展

```
wx.EXPAND  周围有空间就扩展
wx.SHAPED  扩展同时保持宽高比
```

#### 对齐

```
wx.ALIGN_CENTER or wx.ALIGN_CENTRE
wx.ALIGN_LEFT
wx.ALIGN_RIGHT
wx.ALIGN_RIGHT
wx.ALIGN_TOP
wx.ALIGN_BOTTOM
wx.ALIGN_CENTER_VERTICAL or wx.ALIGN_CENTRE_VERTICAL
wx.ALIGN_CENTER_HORIZONTAL or wx.ALIGN_CENTRE_HORIZONTAL
```

下面举一些组合的例子：

```
 wx.EXPAND | wx.LEFT  有空间就扩展，border在左边，这样你会看到左边有空白
```

```
 wx.EXPAND | wx.LEFT | wx.RIGHT  有空间就扩展，border在左边和右边，这样你会看到左边和右边有空白
```

```
wx.EXPAND | wx.ALL 有空间就扩展，上下左右border都有
```

## Frame样式
- `wx.FRAME_NO_TASKBAR` 没有任务栏

- `wx.FRAME_SHAPED` 非矩形框架

- `wx.FRAME_TOOL_WINDOW` 

- `wx.FRAME_FLOAT_ON_PARENT` 框架将漂浮在父窗体之上

- `wx.STAY_ON_TOP` 总在最上

- `wx.SIMPLE_BORDER` 没有装饰的边框


## 布局的太布局的

一般手写布局代码的话，肯定是使用各个Sizer，其中BoxSizer最常用，对于不是特别复杂的布局BoxSizer，横竖拼接加上Add的参数调配，基本上都是调出来的。以至于每个panel类里面我现在都写上了一个 `self.box` 成为惯例了，虽然后面某些情况下会使用到其他Sizer，比如GridSizer等，但GridSizer是可以放在BoxSizer里面的，所以问题不大。这样形成惯例之后，后面引用该面板，想到主Sizer，就直接panel.box即可，这是题外话了。

### FlexGridSizer

FlexGridSizer布局将页面分成二维的表格，各个表格元素高度一定是一样的，但宽度可以不一样（GridSizer则要求一定一样）。

```
wx.FlexGridSizer(int rows=1, int cols=0, int vgap=0, int hgap=0)
```

- rows 多少行
- cols 多少列
- vgap 垂直向加点空间
- hgap 水平向加点空间





## wxpython里面的ID



window identifiers 是一些整数 决定了窗体在系统中的唯一性，wxpython中可以如下定义窗体的ID：

### 窗体ID的定义
- 明确赋值一个正整数，不推荐
- 使用wx.NewID()
- 传递wx.ID_ANY 或 -1 给窗体构造器
```
frame = wx.Frame.__init__(None, -1)
id = frame.GetId()
```



然后笔者强烈推荐读者使用名字来定义和定位窗体，这样你的代码具有更具有良好的可读性。

### 标准ID

[官方文档标准ID列表](https://wxpython.org/Phoenix/docs/html/wx.StandardID.enumeration.html) 

### 根据ID来查找窗体
1、wx.FindWindowById(id, parent=None)
2、wx.FindWindowByName(name, parent=None)
3、wx.FindWindowByLabel(label, parent=None)

如果在某个窗体内调用 `self.FindWindowById` 则是本窗体内查找，找到的第一个。



## 根据名字来查找窗体

笔者强烈推荐读者在写大型GUI程序的时候给几个核心窗体都定义好唯一的名字（具体大部分窗体都可以接受一个name可选参数的），然后如下来查找之。这对于你后面的编程会带来很大的便利。

```python
import wx

def find_window_by_name(name):
    """
    根据窗体的名字来返回窗体，推荐风格
    :param name:
    :return:
    """
    window = wx.FindWindowByName(name)
    return window

def is_the_window_name(window, name):
    """
    根据名字来判断是否是这个窗体
    :param window:
    :param name:
    :return:
    """
    if window.SetName() == name:
        return True
    else:
        return False
```



## 深入理解wxpython中的事件

```
Bind(event, handler, source=None, id=wx.ID_ANY, id2=wx.ID_ANY)
```

- event 比如在wx.Button上鼠标单击一下将触发一个 wx.EVT_BUTTON 事件，event这里可以定义具体你想要绑定的事件。
- handler 处理器
- source 一般不需要指定，如果父窗口多个相同的触发源，比如说多个按钮，那么就需要指定下。
- id 根据id定义事件触发源，在某些情况下根据id来会更方便些，然后id2同id可以确定一串连续的窗体。

### wxpython事件处理过程



![img]({static}/images/wxpython/wxpython事件处理过程.png)



1. 事件触发--> 获取事件触发对象
2. 检查事件触发对象是否允许处理事件（可以通过 `SetEvtHandlerEnabled(boolean)` 来禁用窗体处理事件）【UI层面Disable Enable只是禁用了窗体和用户的交互，但它还是可以处理间接接受到的事件，比如通过PostEvent等】
3. `event.Skip()` 这个方法之前我以为是该事件的处理跳过了，理解错误了，更准确的说法是 **本事件处理完成** 了。 也就是如果在事件触发链中，没有看到这个方法，那么事件将会继续传播，否则事件处理终止。
4. 如果目标事件允许 传播propagate ， 那么还会继续向上去触发父容器的事件，直到App，也就是最顶层结束传播。【默认情况，只有wx.CommandEvent及其子类的实例向上展开至容器级。其它的所有事件都不传播。】【Button单击属于CommandEvent，鼠标移动和浮动在上和离开都是MouseEvent】

#### 习题1

请读者解释为什么是下面的写法，鼠标浮动在上和离开事件为什么只能定向self.button。

```
self.Bind(wx.EVT_BUTTON, self.OnButtonClick,  self.button)    #1 绑定按钮事件     
self.button.Bind(wx.EVT_ENTER_WINDOW,   self.OnEnterWindow)     #2 绑定鼠标位于其上事件 
self.button.Bind(wx.EVT_LEAVE_WINDOW, self.OnLeaveWindow)     #3 绑定鼠标离开事件
```

按钮点击行为可以传播，其首先在本窗体上触发按钮事件，然后在本窗体上找对应的方法 `OnButtonClick` ，如果找到这个方法了，那么执行，执行过程中如果遇到Skip方法，那么本事件处理到此结束；如果没有，则会试着向上传播，直到顶层窗体。向上传播的过程就是传播事件，也就是本窗体的父窗体也将触发本按钮事件，然后试着实行对应的 `OnButtonClick` 方法。

鼠标移动行为是不可以传播事件，必须指明那个按钮绑定的。 `self.button.Bind`  过程就是直接执行你初始挂在的那个方法，找不到就抛出异常了。

大体是这样的，如果读者还有不明白了，请阅读 wxpython in action 这本书的第三章，关于这部分问题，这本书讲的很好。

#### 习题2

如何一个按钮的点击事件会触发两个动作。

简单来说就是写两个 `self.button.Bind()` 语句绑定两个函数就可以了，按照前面说的，这两个函数每个都要跟上 `event.Skip()` 。



### 手动触发某个事件

有时直接手动触发一个事件会省下很多代码。

```
self.Close(True)
```



### 获取当前事件的触发对象

```
button = event.GetEventObject()
print(button.GetName())
```



### 常见的wx.Event子类

- wx.CloseEvent frame框架关闭时触发
- wx.CommandEvent 按钮单击 菜单选择 等
- wx.KeyEvent 按键事件
- wx.MouseEvent 鼠标事件
- wx.PaintEvent 窗体需要重画时触发
- wx.SizeEvent 窗体大小或布局改变时触发
- wx.TimerEvent wx.Timer类创建的定时事件



### 按钮三事件

按钮在GUI设计中是使用频率非常高的一个组件，其绑定的最常用的三个事件有：

- self.Bind(wx.EVT_BUTTON, self.OnButtonClick,  self.button)   绑定按钮事件  
- self.button.Bind(wx.EVT_ENTER_WINDOW,  self.OnEnterWindow)    绑定鼠标位于其上事件  
- self.button.Bind(wx.EVT_LEAVE_WINDOW, self.OnLeaveWindow)     绑定鼠标离开事件





## 什么时候调用Layout方法

动态调整GUI的各个元素，我们会看到网上各个例子经常会看到调用了 Layout方法，然后有的时候我发现不调用似乎影响不大，有的时候发现不调用页面会变形，那么到底什么时候应该调用Layout方法呢。请参看 [这篇文章](https://wiki.wxpython.org/WhenAndHowToCallLayout) 。

1. StaticText 进行 SetLable 操作之后，应该Layout下
2. 通过sizer显示或隐藏某个面板元素之后应该Layout 下。

如果窗体触发了 `EVT_SIZE` 事件，wxpython会自动进行Layout重排。重排的时候父窗体的sizer会自动进行Layout，然后父窗体的子窗体也会相应的进行重排操作，但如果某个子窗体不需要重排，那么它就不会接受 `EVT_SIZE` 事件了，也就不会调用Layout方法了。比如StaticText 更改Layout，你调用其父窗体的Layout，StaticText是不会自动调整的。

按照 [这个网页](https://stackoverflow.com/questions/6294726/setsizer-setsizerandfit-and-resizing-components) 的介绍，加上个人的一点实践经验，不推荐使用 `SetSizerAndFit` 方法了，个人的使用体验是使用 `SetSizer` 就能完成工作了，而加上Fit有的时候会给你的布局带来一些困扰，比如ScrolledPanel在Fit之后会发生截断问题。

总的原则经过试验确实是可行的：

1. SetSizer
2. 发现不对劲，Layout
3. Layout之后还不对劲，这通常不是布局的问题了，某些情况下你更改了一些数据，可能需要Refresh
4.  TODO Layout 和 Refresh 的区别是什么 目前我已经遇到一个问题，只有Refresh之后才有正常的行为，那就是重画的透明组件再设置标签之后，似乎只有Refresh之后才会再次进行重画动作，这值得引起读者的注意。然后有的时候我们看到子面板Layout之后会自动Refresh。

### ScrolledPanel

这里特别值得一提的是 `ScrolledPanel` 里面的内容在发生变动的时候，除了Layout之外还需要加上：

```
self.SetupScrolling()
```

实践发现是内容变动之后都需要加上这句，否则侧边滚动条会丢失，下面的内容也会被隐藏。

## 设置背景颜色和字体颜色

wxpython的任何窗体对象（是的这两个方法是挂在wx.Window上的），可以用 `SetBackgroundColour` 来设置其背景颜色，用 `SetForegroundColour`来设置前景颜色，前景颜色一般就是所谓的字体颜色吧。

如果你需要动态调成某个面板的背景颜色，那么记得调用Refresh方法来激活重画事件。

## 将图片转成python编码

首先是编写这样一个python脚本：

```python
#!/usr/bin/env python
# -*-coding:utf-8-*-


"""
将项目图片文件全部转成python文件，然后可以直接 import images 来引用图片了。
"""

import sys
from wx.tools import img2py

command_lines = [
    "   -F -i -n Favicon static/images/favicon.ico images.py",
    "-a -F -n ApplyTaiKa static/images/apply_tai_ka.png images.py",
    "-a -F -n Address static/images/address_img.png images.py",
]

if __name__ == "__main__":
    for line in command_lines:
        args = line.split()
        img2py.main(args)
```

其调用了wxpython提供的工具 img2py ，然后输出的images.py 里面的图片对象有如下方法：

```
    def GetBitmap(self):
        return wx.Bitmap(self.GetImage())
    def GetData(self):
        data = self.data
        if self.isBase64:
            data = b64decode(self.data)
        return data

    def GetIcon(self):
        icon = wx.Icon()
        icon.CopyFromBitmap(self.GetBitmap())
        return icon

    def GetImage(self):
        stream = BytesIO(self.GetData())
        return wx.Image(stream)
```

最常用的是 `GetBitmap` 直接获取Bitmap图片对象。

## 后台任务

wxpython的后台任务推荐用 `wx.CallAfter` 或者 `wx.CallLater` 来调用。用python内置的多线程可能会让你的界面有时出现一些奇怪的问题。

```
wx.CallAfter(callable, *args, **kwargs)
```

## Timer

wxpython里面的计时器某些任务挂上去还是很方便的。

        self.timer = wx.Timer(self)
        self.timer.Start(1000)
        self.Bind(wx.EVT_TIMER, self.update, self.timer)








## 参考资料

1. [zetcode 的wxpython教程](http://zetcode.com/wxpython)
2. [wxpython官方参考文档](https://docs.wxpython.org/)
3. wxpython in action , Author by Harri Pasanen and Robin Dunn

