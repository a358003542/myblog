Title: wxpython基础窗体一览
Date: 2018-09-21
Modified: 2018-11-23
Slug: wxpython-basic-window-gallery
Tags: wxpython,

[TOC]



## 简介

### 最基本的窗体

这些基本的窗体一般不会直接使用。

wx.Window wx.Control wx.ControlWithItem

### 顶层窗体

wx.PopupWindow wx.ScrolledWindow wx.Frame wx.MDIParentFrame wx.MDIChildFrame wx.Dialog

### 可以包含其他窗体的窗体

wx.ScrolledWindow wx.Panel wx.SplliterWindow wx.Notebook

### 一般动态窗体

动态窗体可被用户编辑。

wx.ToggleButton wx.CheckBox wx.TextCtrl wx.SpinCtrl ....

### 一般静态窗体

不可被用户编辑。

wx.StaticBox wx.StaticText wx.StaticLine wx.StaticBitmap wx.Gauge

### 其他窗体

wx.ToolBar wx.MenuBar wx.StatusBar



## 文本输入对话框

TextEntryDialog

一个小的弹出窗体，用户输入一行文本（其实也可以设为多行），然后程序获取用户输入的该行文本信息。

【图片】

- ShowModal 弹出窗体
- GetValue   获取文本内容



## 单选项对话框

SingleChoiceDialog

一个小的弹出窗体，用户进行一个单选动作。

- ShowModal 弹出窗体
- GetStringSelection 获取用户选择的字符串内容
- GetSelection 获取用户选择的索引位置



## 文件对话框

FileDialog

选择打开或保存文件的对话

```python
    def OnOpen(self,e):
        """ Open a file"""
        self.dirname = ''
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'r')
            self.control.SetValue(f.read())
            f.close()
        dlg.Destroy()
```



## 简单的信息弹窗

```
        dlg = wx.MessageDialog(self, "A small text editor", "About Sample Editor", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()
```

## 颜色选择对话框

ColourDialog



## 简单的About弹窗

AboutBox



## 文件夹选择对话框

DirDialog

## 字体选择对话框

FontDialog

## 多选对话框

MultiChoiceDialog

## 打印页面设置对话框

PageSetupDialog

## 打印对话框

PrintDialog

## 启动画面

- wx.adv.SplashScreen
- wx.adv.SplashScreen

## 添加菜单和菜单栏
```python
        filemenu = wx.Menu()

        aboutMenu = filemenu.Append(wx.ID_ABOUT, "&About", " Information about this program")

        filemenu.AppendSeparator()

        exitMenu = filemenu.Append(wx.ID_EXIT, "E&xit", " Terminate the program")

        menuBar = wx.MenuBar()

        menuBar.Append(filemenu, "&File")
        self.SetMenuBar(menuBar)
```

1. 你需要创建一个MenuBar对象，然后用Frame的 `SetMenuBar` 方法来设置，后面引用的时候可以使用 `GetMenuBar` 方法来获得对应的MenuBar对象
2. 你需要创建一个 Menu 对象，然后MenuBar菜单栏把这个菜单 `Append` 上去。
3. 具体某个菜单如上所示添加具体的一些选项
4. 菜单的点击事件绑定语句如下：

```python
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutMenu)
```





## 静态文本

StaticTex 

### 样式

- wx.ALIGN_CENTER 静态文本于静态文本控件的中心
- wx.ALIGN_LEFT 文本于控件中左对齐 默认
- wx.ALIGN_RIGHT 文本于控件中右对齐
- wx.ST_NO_AUTORESIZE 设置之后，通过SetLabel原来默认是要自动调整控件尺寸的，现在不调整了。

## 静态bitmap图片

StaticBitmap

## 文本输入

TextCtrl

### 样式

- wx.TE_CENTER 控件中文本居中
- wx.TE_LEFT 控件中文本左对齐
- wx.TE_RIGHT 右对齐
- wx.TE_PASSWORD 密码框
- wx.TE_PROCESS_ENTER 默认不处理Enter按键事件，设置后处理
- wx._TE_READONLY 只可读
- wx.TE_MULTILINE 可多行输入



### 方法

- Clear 输入文本重置为空字符串
- AppendText(text) 附加文本
- GetInsertionPoint
- SetInsertionPoint
- GetValue 获取输入文本
- SetValue 设置输入文本
- Remove 删除
- Replace 替换
- WriteText 在当前插入点插入某个文本

## 图片按钮

BitmapButton 

### 图片按钮更改图片

调用图片按钮的 `SetBitmapLabel` 方法，这个目前文档里面没提及。

## 开关按钮

ToggleButton

## 通用按钮

wx.lib.buttons 里面有很多通用按钮创建方法，上面提到的一般按钮，开关按钮，图片按钮都有，相比较之前的一般按钮，通用按钮提供了更多的可定制性。

## 滑块

Slider

## 微调控件

SpinCtrl

## 进度条

Gauge

## 复选框

CheckBox

## 单选按钮

RadioBox

- wx.RB_GROUP 重要！定义了一组单选按钮的开始

## 列表框

ListBox



## 滚动文字信息栏

一行滚动文字的信息栏，

```python
from wx.lib.ticker import Ticker
```

## 状态栏

状态栏
```
self.statusbar = self.CreateStatusBar()
```

这里的self只能是Frame，类似的还有 `CreateToolBar` 。这个根据需要来，不一定要添加的。




## 参考资料

1. [wxpython官方参考文档](https://docs.wxpython.org/)
2. wxpython in action , Author by Harri Pasanen and Robin Dunn