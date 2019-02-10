Title: wxpython绘图和自定义窗体
Date: 2018-11-23
Modified: 2018-11-23
Slug: wxpython-drawing-custom-widget
Tags: wxpython,

[TOC]

## 前言

本文重点讨论wxpython较为底层的绘图知识和利用这些知识来建立自定义的一些窗体。



## GDI

wxpython底层绘图有个GDI（Graphics Device Interface）的概念，可以理解为通用绘图接口，利用这个通用绘图接口，一套绘图方法，就可以向显示器，打印机等绘图。这样程序员可以不用考虑硬件底层来进行绘图编程了。

这个GDI具体来说就是一些绘图的类和方法。

## DC

在开始绘图前，你需要创建一个设备上下文DC（device context），这个DC具体来说就是wx.DC类。实际使用中不应该使用wx.DC类，而应该选择更具体的设备向的DC子类。这些子类具体分为三类：

- 用于绘制到屏幕的上下文
- 用于绘制到另外地方而非屏幕
- 用于缓冲一个设备上下文

### 用于绘制到屏幕

- wx.ClientDC 
- wx.PaintDC 如果你是在EVT_PAINT事件中，那么你应该使用这个设备上下文，其他时候必须使用wx.ClientDC 。
- wx.WindowDC 如果你不光希望在客户区绘制，窗体的边框，标题栏等你都想绘制，那么就使用这个。
- wx.ScreenDC 如果你希望在整个屏幕上绘制，那么就使用这个。

### 非屏幕设备上下文

- wx.MemoryDC 用于内存中的位图bitmap上绘制
- wx.MetafileDC 这个只在windows下有效，将绘制并写入到文件中
- wx.PostScriptDC 这个是跨平台的，将写入eps文件中
- wx.PrinterDC 这个只在windows下有效，将写入打印机中

### 缓冲设备上下文

- wx.BufferedDC 
- wx.BufferedPaintDC 缓冲一个设备上下文，当你做几个重绘的时候，防止屏幕闪烁，缓冲是个选择。复杂的绘制防止屏幕闪烁，推荐使用 `dc = wx.BufferedPaintDC(self)`





## 带颜色的线条

wxpython里的StaticLine是不可以定制颜色的，请看下面这个类实现了一个可以定义颜色的线条功能。这个例子基本演示了如何自定义窗体，具体就是在OnPaint上画上窗体图形，然后Bind好你想要的事件和动作。

绘图变得也来越复杂和更多的定制需求，你的窗体可能需要加入更多的方法来支持这些特性。

```python

import wx


class ColorStaticLine(wx.Panel):
    """
    带颜色的线段
    """
    def __init__(self, parent, color='black', mode='hline', **kwargs):
        super(ColorStaticLine, self).__init__(parent=parent, **kwargs)
        self.parent = parent

        self.color = color
        self.mode = mode

        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def OnPaint(self, event):
        dc = wx.PaintDC(self)

        width, height = self.GetClientSize()

        dc.SetPen(wx.Pen(wx.Colour(self.color)))

        if self.mode == 'hline':
            dc.DrawLine(0, 0, width, 0)
        elif self.mode == 'vline':
            dc.DrawLine(0, 0, 0, height)

```



虽然这是一个很简单的例子，但我们可以学到很多东西：

- 定义重画事件，然后使用 wx.PaintDC 。
- 具体绘画区域x,y的计算是重新开始的，即 (0,0)
- 具体本面板的绘画区域可以由 self.GetClientSize() 方法获得。
- 通过 dc.SetPen 来设置画笔，这是可以设置颜色，然后dc.DrawLine画一条直线，这就是整个绘画过程了。



这样我们就定义了一个自己个性化的可复用小面板组件了。



TODO ： 一个问题，为什么这里要继承自 wx.Panel 才行，这其中的道理暂时还没想明白。

## 基本形状绘制

### 带颜色的方块

```
dc.SetBrush(wx.Brush('#1ac500'))
dc.DrawRectangle(130, 15, 90, 60)
```

设置画刷，然后画一个矩形。

### 绘制圆弧

```
DrawArc(x1, y1, x2, y2, xc, yc)
```

绘制一个圆弧，起点 x1 y1 终点 x2 y2 中心点 xc yc 弧线逆时针绘制，如果设置了画刷，而会填充圆弧区域。

### 画一个圆

```
DrawCircle(x, y, radius)
```

以x y 为中心， radius为半径，画一个圆。

### 画一直线

```
DrawLine(x1, y1, x2, y2)
```

起点 x1 y1 终点 x2 y2 画一直线

### 画多边形

```
DrawPolygon(points)
```

定义一系列的点，画一多边形，起点和终点自动相连

### 画圆角矩形

```
DrawRoundedRectangle(x, y, width, height, radius)
```

radius控制曲率



### 绘制文本

```
DrawText(text, x, y)
```



绘制文本之前你可以通过：

- `SetTextForeground` 来设置字体颜色 此外还有 `GetTextForeground`
- `dc.SetBackgroundMode(wx.SOLID)`  默认 `wx.SOLID` 文本有背景颜色，或者设置 `wx.TRANSPARENT` ，文本无背景颜色。
- `dc.SetTextBackground` 设置文本背景颜色
- `dc.SetFont` 设置字体



### 绘图图片

```
DrawBitmap
DrawIcon
```

## 设置画笔

上面提到的一些基本形状的绘制，填充区域由画刷控制，而那些形状的线条颜色，则是由画笔控制的。

```
SetPen
```

```
wx.Pen(wx.Colour, width=1, style=wx.PENSTYLE_SOLID)
```

### 画笔的样式

- wx.PENSTYLE_SOLID 默认的实线就是这个

- wx.PENSTYLE_DOT 小点

- wx.PENSTYLE_LONG_DASH 虚线

- wx.PENSTYLE_SHORT_DASH 短虚线

- wx.PENSTYLE_DOT_DASH 点划线

- wx.PENSTYLE_TRANSPARENT 没有笔线

- wx.PENSTYLE_STIPPLE 使用提供的位图作为笔触

- wx.PENSTYLE_BDIAGONAL_HATCH 反斜线

- wx.PENSTYLE_CROSSDIAG_HATCH  XXX 线

- wx.PENSTYLE_FDIAGONAL_HATCH 正斜线

- wx.PENSTYLE_CROSS_HATCH +++ 线

- wx.PENSTYLE_HORIZONTAL_HATCH 水平线

- wx.PENSTYLE_VERTICAL_HATCH 垂直线


## 设置画刷

```
SetBrush()
```

```
wx.Brush(colour, style=wx.SOLID)
```

### 画刷的样式

画刷的样式下面列举如下：

- wx.BRUSHSTYLE_SOLID 默认实心填充

- wx.BRUSHSTYLE_TRANSPARENT 透明，也就是没有填充

- wx.BRUSHSTYLE_STIPPLE_MASK_OPAQUE 用位图做笔触，the mask is used for blitting monochrome using text foreground and background colors.

- wx.BRUSHSTYLE_STIPPLE_MASK 用位图做笔触， mask is used for masking areas in the stipple bitmap.

- wx.BRUSHSTYLE_STIPPLE 用位图做笔触

- wx.BRUSHSTYLE_BDIAGONAL_HATCH 反斜线

- wx.BRUSHSTYLE_CROSSDIAG_HATCH XXX 线

- wx.BRUSHSTYLE_FDIAGONAL_HATCH 正斜线

- wx.BRUSHSTYLE_CROSS_HATCH +++ 线

- wx.BRUSHSTYLE_HORIZONTAL_HATCH 水平线

- wx.BRUSHSTYLE_VERTICAL_HATCH 垂直线


### 自定义画刷图案

```
brush1 = wx.Brush(wx.Bitmap('pattern1.png'))
dc.SetBrush(brush1)
dc.DrawRectangle(10, 15, 90, 60)
```

画刷可以指定某个图片来作为其刷出来的图案。

## 获取绘图区域尺寸

```
width, height = self.GetClientSize()
```

## 获取某个窗体的尺寸

wxpython内的窗体（继承自Window）都有 GetSize 这个方法，这样你可以得到某个窗体的尺寸：

```
width, height = self.GetSize()
```



## 获取文本的宽度和高度

```
w, h = self.GetTextExtent(line)
```

如果是空行的话可以写为：

```
w, h = self.GetTextExtent('M')
```

## 居中的定义

获取绘图区域的width，然后计算好你想要居中的对象的width（w），然后居中绘制起点x是：

```
start_x = (width - w)/2
```



## 居右的定义

获取绘图区域的width，然后计算好你想要居右的对象的window（w）,然后居右的绘制起点x是：

```
start_x = width -w
```

## dc.Clear

TODO 我对这个理解还不是很深，只知道这个可以用来清空背景画刷。

```python
brush = wx.Brush("white")  
dc.SetBackground(brush)  
dc.Clear() 
```

## style管理

一般常数状态不用多说，下面说下wxpython的style是如何管理的，其首先定义一些常数，比如说

A = 0b1

B = 0b10

C = 0b100

然后假如说你定义了一个状态：style = A | B ， 则执行逻辑或操作即可。加入你想要测试style是否包含B态则 `style & B` 即可。由于每个style态只占一个二进制位，则其和目标style进行逻辑与操作，包含就返回非0值，返回0值则说明不包含目标style态。






## 参考资料

1. [zetcode 的wxpython教程](http://zetcode.com/wxpython)
2. [wxpython官方参考文档](https://docs.wxpython.org/)
3. wxpython in action , Author by Harri Pasanen and Robin Dunn

