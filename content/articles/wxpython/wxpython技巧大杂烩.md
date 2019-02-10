Title: wxpython技巧大杂烩
Date: 2018-08-27
Modified: 2018-11-23
Slug: wxpython-cookbooks
Tags: wxpython,

[TOC]


## 只有一个程序实例在运行

利用 `wx.SingleInstanceChecker` 很方便就可以做到这点，更多信息请参看文档的 [这里](https://wxpython.org/Phoenix/docs/html/wx.SingleInstanceChecker.html) 。下面的做法是确保了操作系统某个用户只有一个程序实例在运行。

```python
import wx

class SingleAppFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(300, 300))
        self.Centre()


class SingleApp(wx.App):
    def OnInit(self):
        self.name = "SingleApp-%s" % wx.GetUserId()
        self.instance = wx.SingleInstanceChecker(self.name)
        if self.instance.IsAnotherRunning():
            wx.MessageBox("Another instance is running", "ERROR")
            return False
        frame = SingleAppFrame(None, "SingleApp")
        frame.Show()
        return True
    

app = SingleApp(redirect=False)
app.MainLoop()
```



## 欢迎页面

利用wx.adv.SplashScreen 就可以很方便地制作出一个欢迎页面，读者还可以看一下demo各个案例中提到的 `wx.lib.agw.advancedsplash as AS`  ，和 SplashScreen 类比起来又多了一些可定制的选项。



```python
    from gui.mainFrame import ChaoShengHuo

    class ChaoShengHuoApp(wx.App):
        img_base = g_var.img_base

        def OnInit(self):
            self.name = "SingleApp-%s" % wx.GetUserId()
            self.instance = wx.SingleInstanceChecker(self.name)

            if self.instance.IsAnotherRunning():
                wx.MessageBox("已经有一个潮生活发票助手程序在运行了！", "Do not Panic")
                return False
            else:
                # 欢迎页面
                bitmap = wx.Bitmap(self.img_base + 'welcome.png', wx.BITMAP_TYPE_PNG)

                wx.adv.SplashScreen(bitmap, wx.adv.SPLASH_CENTRE_ON_SCREEN | wx.adv.SPLASH_TIMEOUT,
                                    3000, None, -1, wx.DefaultPosition, wx.DefaultSize,
                                    wx.BORDER_SIMPLE | wx.STAY_ON_TOP)
                wx.Yield()

                the_frame = ChaoShengHuo(None, -1)
                the_frame.Show(True)
                return True

```

## 程序最小化到托盘
主界面那边关闭事件是：
```
    def MinimizeWindow(self, event):
        self.Iconize(True)

    def CloseWindow(self, event):
        self.Hide()
        event.Skip()
```
```python
import wx
import wx.adv

class TaskBarIcon(wx.adv.TaskBarIcon):
    ID_About = wx.NewId()
    ID_Minshow = wx.NewId()
    ID_Maxshow = wx.NewId()
    ID_Closeshow = wx.NewId()

    def __init__(self, frame):
        wx.adv.TaskBarIcon.__init__(self)
        self.frame = frame
        self.SetIcon(wx.Icon(name='favicon.ico', type=wx.BITMAP_TYPE_ICO), '潮生活发票助手')
        self.Bind(wx.adv.EVT_TASKBAR_LEFT_DCLICK, self.OnTaskBarLeftDClick)  # 定义左键双击
        self.Bind(wx.EVT_MENU, self.OnAbout, id=self.ID_About)
        self.Bind(wx.EVT_MENU, self.OnMinshow, id=self.ID_Minshow)
        self.Bind(wx.EVT_MENU, self.OnMaxshow, id=self.ID_Maxshow)
        self.Bind(wx.EVT_MENU, self.OnCloseshow, id=self.ID_Closeshow)

    def OnTaskBarLeftDClick(self, event):
        if self.frame.IsIconized():
            self.frame.Iconize(False)
        if not self.frame.IsShown():
            self.frame.Show(True)
        self.frame.Raise()

    def OnAbout(self, event):
        wx.MessageBox('潮生活发票助手V3.0', '关于')

    def OnMinshow(self, event):
        self.frame.Iconize(True)

    def OnMaxshow(self, event):
        if self.frame.IsIconized():
            self.frame.Iconize(False)
        if not self.frame.IsShown():
            self.frame.Show(True)
        self.frame.Raise()

    def OnCloseshow(self, event):
        self.RemoveIcon()
        self.Destroy()
        self.frame.Destroy()


    def CreatePopupMenu(self):
        menu = wx.Menu()
        menu.Append(self.ID_Minshow, '最小化')
        menu.Append(self.ID_Maxshow, '最大化')
        menu.Append(self.ID_About, '关于')
        menu.Append(self.ID_Closeshow, '退出')
        return menu
```



## 图片重画
一个抹去事件被发送，当窗体背景需要重画的时候。
An erase event is sent when a window’s background needs to be repainted.

```
dc = event.GetDC()
```

```
wx.ClientDC：用于在一个窗口对象上绘画。当你想在窗口部件的主区域上（不包括
边框或别的装饰）绘画时使用它。主区域有时也称为客户区。wx.ClientDC类也应临
时创建。该类仅适用于wx.PaintEvent的处理之外。
```



[参考网页](https://blog.csdn.net/cassiepython/article/details/43103143)

```
import wx
 
class Frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,"My Frame",size=(400,300),
                          style = wx.DEFAULT_FRAME_STYLE)
        self.panel = wx.Panel(self)
        self.panel.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
    def OnEraseBack(self,event):
        dc = event.GetDC()
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        bmp = wx.Bitmap("background.jpg")
        dc.DrawBitmap(bmp, 0, 0)
if __name__ == '__main__':
    app = wx.App()
    frame = Frame()
    frame.Show()
    app.MainLoop()

```





## 让窗体可以拖动

你想要的那部分窗体可以拖动，就将事件绑定一下，但拖动事件实际执行方法应该在主窗体上，然后主窗体应该也进行一次绑定。具体原因还不是很明白。

```python
        self.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)  # 左键点击按下
        self.Bind(wx.EVT_LEFT_UP, self.OnLeftUp)  # 左键释放
        self.Bind(wx.EVT_MOTION, self.OnMouseMove)  # 鼠标移动

    # 拖动相关
    def OnLeftDown(self, event):
        logger.debug(f'GUI事件: {event} - OnLeftDown')
        self.CaptureMouse()  # 捕获鼠标
        pos = self.ClientToScreen(event.GetPosition())
        origin = self.GetPosition()
        self.delta = wx.Point(pos.x - origin.x, pos.y - origin.y)

    def OnLeftUp(self, event):
        logger.debug(f'GUI事件: {event} - OnLeftUp')
        if self.HasCapture():
            self.ReleaseMouse()  # 释放鼠标

    def OnMouseMove(self, event):
        logger.debug(f'GUI事件: {event} - OnMouseMove')

        if event.Dragging() and event.LeftIsDown():
            pos = self.ClientToScreen(event.GetPosition())
            newPos = (pos.x - self.delta.x, pos.y - self.delta.y)
            self.Move(newPos)
```





## 扩充你的颜色定义

wxpython有自己内部一套颜色定义库，然后你还可以利用进一步扩充自己的颜色定义库：

aquamarine：海蓝色 
black：黑色 
blue：蓝色 
brown：褐色 
coral：珊瑚色 
cyan：青色 
firebrick：火砖色 
gold：金色 
gray：灰色 
green：绿色 
khaki：土黄色 
magenta：绛红色 
maroon：栗色 
navy：藏青色
orange：橙色 
orchid：淡紫色 
pink：粉红色 
plum：梅红色 
purple：紫色 
red：红色
salmon：鲜肉色 
sienna：红褐色
tan：浅棕色
thistle：蓟色 
turquoise：青绿色 
violet：紫罗兰色 
wheat：浅黄色 
white：白色 
yellow：黄色 

更多颜色请参看 demo 那边的 ColourDB 。

你需要在你的app `OnInit` 的时候加载你自己定义的颜色，请看官方代码的这个片段，这样你就知道自己该怎么做了：

```python
def updateColourDB():
    """
    Updates the :class:`wx.ColourDatabase` by adding new colour names and RGB values.
    """

    global _haveUpdated
    if not _haveUpdated:
        import wx
        assert wx.GetApp() is not None, "You must have a wx.App object before you can use the colour database."
        cl = getColourInfoList()

        for info in cl:
            name, colour = info[0], wx.Colour(*info[1:])
            wx.TheColourDatabase.AddColour(name, colour)

        _haveUpdated = True
```





