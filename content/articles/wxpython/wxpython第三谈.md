Title: wxpython第三谈
Date: 2018-12-13
Modified: 2018-12-24
Slug: wxpython-talk-three
Tags: wxpython,


[TOC]

## TextCtrl用代码改变文本

TextCtrl用代码直接改变文本的方法有：

- AppendText 尾部添加文本
- Clear 
- EmulateKeyPress 产生一个按键事件
- SetInsertionPoint 设置插入点
- SetValue
- WriteText 在当前插入点插入文本
- Remove 删除指定范围文本
- Replace 替换指定范围文本

## 对接系统的剪贴板

### 将文本放入剪贴板

```python
data = wx.TextDataObject()
text = "your text"
data.SetText(text)
if wx.TheClipboard.Open():
	wx.TheClipboard.SetData(data) #将数据放置到剪贴板上
	wx.TheClipboard.Close()
else:
	print('剪贴板打不开..')
```

### 从剪贴板中取内容

```python
data = wx.TextDataObject()
if wx.TheClipboard.Open():
    success = wx.TheClipboard.GetData(data)
    wx.TheClipboard.Close()
if success:
    return data.GetText()
```

此外还有清空剪贴板的动作： `Clear` 方法。



## ScrolledPanel

带滚动条的面板，下面是一些值得额外一提的东西：

### SetupScrolling

```python
SetupScrolling(self, scroll_x=True, scroll_y=True, rate_x=20, rate_y=20,
                       scrollToTop=True, scrollIntoView=True)
```

这个方法很重要，前面谈到，带滚动条的面板如果内容发生变动，除了 Layout 之外，还需要加上 `SetupScrolling` 这一句。

然后后面的这些选项也很重要：

- scroll_x 如果设置为False 则横向滚动条不显示
- scroll_y 如果设置为False 则竖向滚动条不显示
- rate_x 最小一步滚动的距离 
- rate_y 最小一步竖向滚动距离，
- scroolIntoView 滚动是尽可能让子面板合适的显示



此外你可以通过 `Scroll` 方法来程序进行滚动。



## wxpython里面的鼠标图案

一般面板，也就是继承自Window的类都有 `SetCursor` 方法来设置当前的鼠标图形

```
self.SetCursor(wx.Cursor(wx.CURSOR_HAND))
```

默认的是： `wx.CURSOR_ARROW` ，常用的显示要点击的手型是 `wx.CURSOR_HAND` ，此外还有：

- wx.CURSOR_ARROWWAIT 只能在windows下有效，表示繁忙的光标
- wx.CURSOR_BLANK 不可见的光标
- wx.CURSOR_WAIT 沙漏等待光标
- wx.CURSOR_WATCH 手表等待光标
- wx.CURSOR_SPRAYCAN 绘图用光标
- wx.CURSOR_SIZING 尺寸调整时光标，四个指向
- wx.CURSOR_SIZEWE 水平尺寸调整光标，左右指向
- wx.CURSOR_SIZENS 垂直尺寸调整光标，上下指向
- wx.CURSOR_RIGHT_BUTTON 右按键按下光标
- wx.CURSOR_PENCIL 钢笔样光标
- wx.CURSOR_PAINT_BRUSH 画刷样光标，同样在绘图程序中
- wx.CURSOR_MAGNIFIER 放大镜，表示缩放
- wx.CURSOR_MIDDLE_BUTTON 一个中间按键按下的鼠标

此外你还可以自定义光标图案： `wx.CursorFromImage(image)` 



## ComboBox内容的修改

参考了 [这个问题](https://stackoverflow.com/questions/682923/dynamically-change-the-choices-in-a-wx-combobox) 。

ComboBox的官方手册上找不到相关方法，原来ComboBox继承自 `ItemContainer` ，调用这里的方法，就可以动态修改ComboBox里面的内容。

- Clear 清空
- Append 附加
- Delete(self, n) 删除
- Insert 插入
- `Set(self, items)`  整个替换 



## 自定义对话框

某些情况下直接继承自 `SizedDialog`  会很方便：

```python
import wx.lib.sized_controls as sc

class Dialog(sc.SizedDialog):
    def __init__(self, parent, *args, data=None, type='simple', **kwargs):
        sc.SizedDialog.__init__(self, parent, *args, size=(400, 300), **kwargs)
        self.parent = parent
        
        pane = self.GetContentsPane()
        pane.SetSizerType("form")

        # 科目名称
        wx.StaticText(pane, -1, "科目名称")
        self.nameText = wx.StaticText(pane, -1, label=self.name)

        self.Fit()
        self.SetMinSize(self.GetSize())

        self.Layout()
        self.Center()
```

或者直接继承自 `wx.Dialog` ，然后就像自定义panel一样做，除了里面添加button推荐使用一些标准ID，这样可以类似下面关闭对话框之后判断具体点击了那个按钮：

```
val = dlg.ShowModal()
if val == wx.ID_DELETE ...
```



## 列表控件

列表控件支持三种模式：

1. style=wx.LC_ICON 图标模式，大概看上去像windows上的文件浏览的样子
2. style=wx.LC_SMALL_ICON 小图标模式
3. style=wx.LC_LIST 列表模式 有点类似于小图标模式，不同的是按列排列的
4. style=wx.LC_REPORT 报告模式 类似于excel表单的那种

具体更详尽的使用还是需要查阅文档的，此外如果你需要在某个item里面添加Panel或者其他控件，那么建议读者了解下 `wx.lib.agw.ultimatelistctrl.UltimateListCtrl` ，如果读者需要某一列可排序，了解下 `wx.lib.mixins.listctrl.ColumnSorterMixin` 如果需要item成为 textctrl 可以输入，了解下 `wx.lib.mixins.listctrl.TextEditMixin` ，还有其他的mixin，不过在使用 ultimatelistctrl的时候就没必要使用那些mixin了。



## 网格控件

网格控件 `wx.grid.Grid` 感觉比列表控件更加复杂，具体涉及到的方法很多，建议根据需要查阅文档之。



## 树型控件

TreeCtrl 显示复杂的层次数据，比如目录结构时可以用到。

## HTMLWindow

对于某些复杂的文本显示需求，可以使用HTMLWindow用一种类html标记语言来渲染而成，其底层并不是用的浏览器渲染，而是wxpython自己完成了的渲染，简单来说这只是wxpython通过一种类html标记语言完成的一种快速定义文本显示界面的功能。

此外wxpython还提供了html2包，其是利用浏览器底层渲染，然后显示的，这样更接近浏览器显示效果。

## wxpython的打印支持

这一块暂时略过



## DateTime和python的datetime对象互转

这一节参考了 python cook book 的 #12 recipe。这里记录下，后面有时候应该会用到的：

```python
import datetime
import wx

def pydate2wxdate(date):
    assert isinstance(date, (datetime.datetime, datetime.date))

    tt = date.timetuple()
    dmy = (tt[2], tt[1]-1, tt[0])
    return wx.DateTimeFromDMY(*dmy)

def wxdate2pydate(date):
    assert isinstance(date, wx.DateTime)
    if date.IsValid():
        ymd = map(int, date.FormatISODate().split('-'))
        return datetime.date(*ymd)
    else:
        return None
```



## boxsizer两个值得注意的方法

### AddSpacer

作用就是增加一段固定的空白距离，boxsizer覆写了sizer的AddSpacer方法，横向竖向不能混淆的。

```python
def add_vspace(box, size):
    """
    boxsizer竖向增加空白距离，如果不是VERTICAL则将抛异常
    :param box:
    :param size:
    :return:
    """
    if box.GetOrientation() == wx.VERTICAL:
        box.AddSpacer(size)
    else:
        raise NotVerticalSizer


def add_hspace(box, size):
    """
    boxsizer横向增加空白距离，如果不是HORIZONTAL则将抛异常
    :param box:
    :param size:
    :return:
    """
    if box.GetOrientation() == wx.HORIZONTAL:
        box.AddSpacer(size)
    else:
        raise NotHorizontalSizer
```



### AddStretchSpacer

这个方法是sizer里面的，boxsizer也可以调用，一开始我还没注意到。这个方法和上面方法的区别就是增加了一段可缩放的空白距离，其在Qt里面就是一段弹簧样的东西。利用这个缩放器很方便实现某个空间的居中或者某个比例的位置调整。




## 参考资料

1. [zetcode 的wxpython教程](http://zetcode.com/wxpython)
2. [wxpython官方参考文档](https://docs.wxpython.org/)
3. wxpython in action , Author by Harri Pasanen and Robin Dunn

