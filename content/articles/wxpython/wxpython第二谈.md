Title: wxpython第二谈
Date: 2018-10-19
Modified: 2018-11-02
Slug: wxpython-talk-two
Tags: wxpython,


[TOC]

## 动态多组件切换

用boxsizer来挂载一些面板，然后隐藏一些面板，并显示初始你想要显示的那个panel。Add, Show Hide 等方法来操作，最后注意Layout一下，这是基本功了。

这里值得一提的是，如果你只是本panel基本的Layout，那么多个panel切换父panel给那些子panel的size都是一致的，因为你的子panel各个size大小不同，如果你动态切换需要更好的效果，那么应该调用父panel的Layout。

### 某个子Panel的重写

一些参数的变化，你的子panel需要重写，这个时候推荐使用box的Replace方法：

```python
        old_panel = self.category_sp2_panel
        new_panel = CategorySPInnerPanel(self, data_list=value)

        self.box.Replace(old_panel, new_panel)
        old_panel.Destroy()
        self.category_sp2_panel = new_panel
```

大体过程如上，实际切换推荐采用如下写法：

1. 首先隐藏box所包含的所有子面板：

```
    def hide_all_panel(self):
        for panel in self.box.GetChildren():
            self.box.Hide(panel.GetWindow())
```

2. 然后在决定显示那个子面板

   ```
   self.box.Show(self.category_sp1_panel)
   ```

当然了最后记得要调用父面板级别的Layout一下。



## 全局捕捉异常

```python

import sys

import traceback

import wx


class Panel(wx.Panel):
    def __init__(self, parent):
        super(Panel, self).__init__(parent)

        button = wx.Button(self, label='抛异常')
        button.Bind(wx.EVT_BUTTON, self.OnButton)

    def OnButton(self, event):
        1 / 0


def MyExceptionHook(etype, value, trace):
    """
    etype exception type
    value exception message
    trace traceback header
    :param etype:
    :param value:
    :param trace:
    :return:
    """
    frame = wx.GetApp().GetTopWindow()

    tmp = traceback.format_exception(etype, value, trace)

    exception = "".join(tmp)

    print(exception)


class DemoFrame(wx.Frame):
    def __init__(self):
        super(DemoFrame, self).__init__(None, -1, "test capture all excepiton", size=(600, 400))

        sys.excepthook = MyExceptionHook
        panel = Panel(self)


if __name__ == '__main__':
    app = wx.App()
    frame = DemoFrame()
    frame.Show()

    app.MainLoop()

```



实际过程很简单，就是把python的 sys.excepthook 重载为 MyExceptionHook 函数，一切异常交给它来处理。



##  验证器

验证器最开始是对于对话框的某些数据格式有限定要求，但后面发现验证器非常的有用，之前对话框管理 `self.data` 做的一些工作可以交给验证器来做，所以验证器这一块最好早接触。

一般使用验证器先自己定义一个验证器类，继承自 `wx.Validator` 。然后你自定义一个 `Clone` 方法，返回本验证器相同的副本。

验证器第一个功能是验证数据，你在本验证器类中定义的 `Validate` 方法就是做这个的。这个方法默认还将传递一个 win参数进来，这个win，比如说你的验证器类是挂载在某个TextCtrl上的，那么那个TextCtrl实例就是这个win，所以你可以方便引用这个win来获得数据。

如果 `Validate` 方法返回 True ，那么验证成功，如果返回 False，那么验证失败。再返回之前你还可以做一些其他的事情。

此外验证器类还需要定义 `TransferToWindow` 方法，表示验证器启动开始进行的动作；定义 `TransferFromWindow` 方法表示验证器验证结束后的动作。如果这两个函数都简单 `return True` ，那么将什么都不用做，此外你可以通过这两个方法一来一去来维护一个对话框维护的某个全局数据集。之前我还没接触验证器的时候，写了几十行代码为了维护一个类似的data数据集，而且是只要对话框各个控件稍有变动，就要触发一个事件进行数据同步动作。显然验证器的这种方案更加的优雅。

你的Dialog可能有几个控件，几个控件使用各自的validator是独立的，虽然你在写验证器类的时候可以统一为一个类，但实际运行时有好几个验证器各自起作用的。具体请看下面这个例子：

```python

import wx



class CategorySPAddValidator(wx.Validator):
    def __init__(self, data, key):
        super(CategorySPAddValidator, self).__init__()
        self.data = data
        self.key = key

    def Clone(self):
        return CategorySPAddValidator(self.data, self.key)

    def handle_targetCtrl_state(self, targetCtrl, state):
        """
        成功和失败的动作通用动作
        :param state:
        :return:
        """
        if state:
            targetCtrl.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
            targetCtrl.Refresh()
        else:
            targetCtrl.SetBackgroundColour("pink")
            targetCtrl.SetFocus()
            targetCtrl.Refresh()

    def Validate(self, win):
        targetCtrl = self.GetWindow()
        value = targetCtrl.GetValue()

        state = True

        if self.key == 'name':
            if len(value) == 0:
                dlg = wx.MessageDialog(win, "科目名称不能为空", '输入有误')
                dlg.ShowModal()
                state = False
        elif self.key == 'code':
            if len(value) == 0:
                dlg = wx.MessageDialog(win, "税收分类编码不能为空.", '输入有误')
                dlg.ShowModal()
                state = False
            elif len(value) != 19:
                dlg = wx.MessageDialog(win, "税收分类编码必须是19位.", '输入有误')
                dlg.ShowModal()
                state = False
        elif self.key == 'unit':
            pass
        elif self.key == 'price':
            pass

        self.handle_targetCtrl_state(targetCtrl, state)

        return state

    def TransferToWindow(self):
        """
        对话框打开是，读取数据到窗体
        :return:
        """
        targetCtrl = self.GetWindow()

        state = True
        value = None

        if self.key == 'name':
            value = self.data.get('spmc', '')
        elif self.key == 'code':
            value = self.data.get('spbm', '')
        elif self.key == 'unit':
            value = self.data.get('jldw', '')
        elif self.key == 'price':
            value = self.data.get('dj', '')

        targetCtrl.SetValue(value)
        return state

    def TransferFromWindow(self):
        """
        对话框关闭
        :return:
        """
        targetCtrl = self.GetWindow()
        value = targetCtrl.GetValue()

        state = True

        if self.key == 'name':
            self.data['spmc'] = value
        elif self.key == 'code':
            self.data['spbm'] = value
        elif self.key == 'unit':
            self.data['jldw'] = value
        elif self.key == 'price':
            self.data['dj'] = value

        return state

```



这个例子我是跟着wxpython in action 一书上的例子进行了一些优化，一开始我以为书上的例子并没有很好地解决dialog那边数据传输问题，但最神奇的是，原对话框的 self.data 属性已经发生更改了，而且我确认 `TransferFromWindow` 哪里 self.data 指的的本验证器，当然。但问题是后面我调用dlg里面的data数据，没想到就是修改好的数据。所以现在的问题是，Why it works . 一个初步的猜测是wxpython的验证器非常聪明地将我之前传输 `self.data` 数据进来的时候就把它记住了，只能做这个解释。

经过试验发现上面如果面板层次稍微复杂点，上面的self.data直接操作风格就不行了，而如果你的验证器要管理多个数据也不能这样做的。总之关于验证器基本该了解的就是这么多了，具体数据传输，到母面板的哪里，或者从哪里提取数据，这些都是小细节了。

上面的代码只是一个演示功能，读者具体自己写代码还是不要寄托这些神奇的魔法，应该更加明晰的指定数据从哪里来，到哪里去。

## wxpython和asyncio的集成

本小节主要参考了 [这个代码文件](https://github.com/BrendanSimon/micropython_experiments/blob/master/keypad_lcd/wx_asyncio_test_1.py) 。我看了一下，空闲事件和Timer事件都彼此触发，重复得很明显，就选择一个Timer触发即可。

然后看了一下asyncio的相关文档，stop是不会让事件循环中的任务丢失的，所以总的效果就是asyncio 的事件循环一直在后台运行就是了。

```python
        self.timer = wx.Timer(self)
        self.timer.Start(1)
        self.Bind(wx.EVT_TIMER, self.idle_handler)
        self.eventloop = asyncio.get_event_loop()
        
    def idle_handler(self, event):
        """
        Idle handler runs the asyncio event loop.
        """
        self.eventloop.call_soon(self.eventloop.stop)
        self.eventloop.run_forever()
```



## 利用进程间通信来实现多次启动应用只有一个应用

前面已经讲了wxpython如何实现确保只有一个程序实例在运行，就是利用 `wx.SingleInstanceChecker` 这个类，具体使用很简单。

但我们如何实现那种效果，就是下一次点击应用图标，还是弹出的原窗体应用，而第二次启动应用尝试悄然结束即可。

仔细分析问题和查了一些资料之后发现，这实际上就是一个简单的进程间通信问题。第二次启动应用的进程，只要发送一个简单的消息给原应用就可以实现这种效果了。

了解进程间通信原理之后发现这块还挺复杂的，尤其是windows的那些win32 API操作，我非常的不熟悉，然后看到套接字也可以做进程间通信，这说白了就是你的应用开了一些小的server监听端口和client请求。这种实现方式兼容性是最好的，但一开始我总感觉是不是有点杀鸡用牛刀了，因为我就想发个简单的信号即可，然后了解到python的signal模块在windows这边兼容性不好，其他windows的win32操作麻烦还不一定是个好方案，就决定写个简单的套接字。

好在应用asyncio事件循环上面提及的，已经挂载在应用上了，也就是说我们只需要利用asyncio模块照着教程写个最简单的套接字发送一个简单的消息即可。

```python
LOCAL_SOCKET_PORT = 10000
MSG_INSTANCE = 'instance'


async def handle_local_socket_server(reader, writer):
    data = await reader.read()
    message = data.decode()

    if message == MSG_INSTANCE:
        logger.info('another instance is calling.')
        mainFrame = get_mainFrame()
        mainFrame.taskBarIcon.max_show()


async def handle_local_socket_client(message, loop):
    reader, writer = await asyncio.open_connection('127.0.0.1', LOCAL_SOCKET_PORT, loop=loop)
    writer.write(message.encode())

    await writer.drain()
    writer.close()

    .....
    
    if self.instance.IsAnotherRunning():
            self.eventloop.run_until_complete(handle_local_socket_client(MSG_INSTANCE, loop=self.eventloop))
            logger.warning('已经有一个潮生活发票助手程序在运行了！')
            return False
        else:
            local_socket_server = asyncio.start_server(handle_local_socket_server, '127.0.0.1', port=LOCAL_SOCKET_PORT,
                                                       loop=self.eventloop)

            self.eventloop.run_until_complete(local_socket_server)

```

大概代码如上所示，最后效果还挺不错的。

这里基本上只用到了asyncio套接字编程最基础的那些知识，这里有个问题，我这边还没有试探：那就是按照道理只需要 `self.eventloop.create_task` 把任务挂上去即可，而不需要 `run_until_complete` 的，可能是前面提及的wxpython和asyncio集成，要稍后面一些asyncio的事件循环才启动，因为那个计时器也才刚开始创建，这个我没试过，也可能不是。



## 程序触发事件

wxpython里面如何通过程序来触发某个事件呢，如下所示：

```python
            homeButton = find_window_by_name('homeButton')
            evt = wx.PyCommandEvent(wx.EVT_BUTTON.typeId, homeButton.GetId())
            wx.PostEvent(homeButton, evt)
```

核心就是 `wx.PostEvent` 方法，值得一提的是，通过这种方法触发的事件不能调用
```
event.GetEventObject()
```
不过你可以通过
```
    button = find_window_by_id(event.GetId())
```
来找到那个目标button，也就是 `GetId` 方法还是可以用的。




## 参考资料

1. [zetcode 的wxpython教程](http://zetcode.com/wxpython)
2. [wxpython官方参考文档](https://docs.wxpython.org/)
3. wxpython in action , Author by Harri Pasanen and Robin Dunn

