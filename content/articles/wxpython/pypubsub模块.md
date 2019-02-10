Title: pypubsub模块
Date: 2018-11-29
Modified: 2018-11-29
Slug: pypubsub-module
Tags: pypubsub,


[TOC]

## 前言

pypubsub模块的基本使用这里就不赘述了，简单的看下官方文档即可。这里我要说的是debug问题：

pypubsub引入之后程序经常出现问题之后是没有任何异常信息直接退出，这给日常编码带来了很多困扰，下面重点解决这个问题。

官方文档的高级使用部分有相关介绍，不过似乎有点杂乱，然后语焉不详。

搜索到 [这个页面](https://wxpython.org/Phoenix/docs/html/wx.lib.pubsub.core.listener.IListenerExcHandler.html) ，似乎是要这样配置就能捕捉到异常信息。

我试着跟着他写了一下，然后发现 listenerID 和 topicObj.getName() 只有消息的名字，具体程序捕捉到了什么异常并没有写明。

在简单了解Topic和Linstener对象之后发现也找不到存储异常信息的地方。

只好翻文档，在API的utils里面有个ExcPublisher引起来了我的兴趣，看了下源码，简单的使用哪个 ExcPublisher 发现能够打印出异常信息，但是还是有其他异常。然后发现其核心实际上就是这里：

```python
    def __call__(self, listenerID: str, topicObj):
        """
        Handle the exception raised by given listener. Send the
        Traceback to all subscribers of topic self.topicUncaughtExc.
        """
        tbInfo = TracebackInfo()
        self.__topicObj.publish(listenerStr=listenerID, excTraceback=tbInfo)
```

他有新建了topic发送了消息，而哪个tbInfo就是异常信息，然后看了下，发现其实际上是从python的traceback异常堆栈哪里搜索到的，这也是奇怪，因为python的全局异常信息在这里，但是程序却没有抛出异常，可能pypubsub已经中途拦截了吧。

这样我们简单写了这样一个东西：

```python

from pubsub.utils.exchandling import TracebackInfo, IListenerExcHandler


class MyExcPublisher(IListenerExcHandler):
    """
    Example exception handler that simply publishes the exception traceback.
    The messages will have topic name given by topicUncaughtExc.
    """

    def __call__(self, listenerID: str, topicObj):
        """
        Handle the exception raised by given listener. Send the
        Traceback to all subscribers of topic self.topicUncaughtExc.
        """
        tbInfo = TracebackInfo()
        logger.error(f'message {topicObj.getName()} caught a error:\n {tbInfo}')
```

然后定义：

```
pub.setListenerExcHandler(MyExcPublisher())
```

发现工作的还行。到这里我已经完事了，就基本的异常捕捉已经差不多了。不过下面有些东西建议读者稍微了解下，可能后面遇到某些情况debug就需要用于这些知识。



### 听所有的topic

```python
>>> def snoop(topicObj=pub.AUTO_TOPIC, **mesgData):
>>>     print 'topic "%s": %s' % (topicObj.getName(), mesgData)
>>>
>>> pub.subscribe(snoop, pub.ALL_TOPICS)
(<pubsub.core.listenerimpl.Listener instance at 0x01A040A8>, True)
>>> pub.sendMessage('some.topic.name', a=1, b=2)
topic "some.topic.name": {'a': 1, 'b': 2}
```

### 打印topic层级

如果你用到了topic的层级，可能需要这个。

```python
pubsub.utils.printTreeDocs()
```



### 消息缓冲再释放

我就遇到这样一个问题，那就是因为一种程序设计，模型层那边有数据更改会自动发送消息，大部分情况都没问题，就是GUI还没完全初始化的时候，出了问题。这里我们需要把消息先缓冲起来，然后再释放。

我写了这么一个简单的类：

```python

from pubsub import pub


class PreGUIController():
    """
    GUI初始化之前接受的信号缓冲起来
    GUI初始化之后再发送出去
    """

    def __init__(self):
        self.info_queue = []
        self.listener, _ = pub.subscribe(self.remember_it, pub.ALL_TOPICS)

    def stop_listen(self):
        pub.unsubscribe(self.listener, pub.ALL_TOPICS)

    def repeat_it(self):
        """
        再次发送那些信号
        :return:
        """
        for msg in self.info_queue:
            name = msg['name']
            kwargs = msg['kwargs']

            pub.sendMessage(f'{name}', **kwargs)

            import time
            time.sleep(0.1)

    def remember_it(self, topicObj=pub.AUTO_TOPIC, **kwargs):
        msg = {
            'name': topicObj.getName(),
            'kwargs': kwargs
        }

        self.info_queue.append(msg)

```

具体使用如下：

```
    pre_controller = PreGUIController()
    # GUI初始化
    pre_controller.stop_listen()
    pre_controller.repeat_it()
```

这里用到的知识实际上就是前面的听所有topic和一些的方法编写，唯一的一个新的知识点就是如何让某个listener取消监听某个topic。

