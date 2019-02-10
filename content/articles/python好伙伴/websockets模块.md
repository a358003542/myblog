Title: websockets模块
Slug: websockets-module
Date: 2018-11-22
Modified: 2018-11-22
Tags:  python,



[TOC]


## 简介

python和websokets相关的模块在github得星差不多的大概有三个，一个autobahn在使用上更偏向twisted，而且个人使用的时候在连接上会报websocket upgrade error这样的错误，可能是我的问题，而另外一个更偏向javascript那边websocket的使用风格，因为个人没有使用过，不做点评，本文重点关注的是这个模块：

[https://github.com/aaugustin/websockets](https://github.com/aaugustin/websockets)

这个模块使用还是很简单的，不过需要读者对asyncio那块异步编程要有所熟悉。

## 全局websocket

首先你的应用启动的时候和服务器建立websocket连接，最好让这个websocket成为一个全局变量，后续的发送和监听消息需求都根据这个websocket来。



## 和其他GUI框架的继承问题

这个websockets模块和GUI框架的继承问题更多的是在于该GUI框架如何和asyncio的事件循环集成起来。这个在目标GUI框架的时候会有所讨论，就不在这里讨论了。

简单来说就是asyncio的事件循环里面你将添加一个或者多个任务，在目标任务中，完成websoket的相关工作。



## 常驻监听模式

请读者看下面代码，下面建立了一种常驻监听模式，由于可能存在各种原因websocket服务器那边可能会强制把websocket连接关闭，所以你需要捕捉这个异常，然后试着重新建立一个全局websocket连接。

```python
    async def create_websocket(self):
        """
        主面板初始化新建一个全局的websocket
        然后开始websocket监听
        :return:
        """
        ws_url = create_ws_url()

        while True:
            try:
                async with websockets.connect(ws_url) as websocket:
                    g_var.websocket = websocket

                    ws_message = await websocket.recv()
                    logger.info(f'websoket got message {ws_message}')

                    res = json.loads(ws_message)
                    # 先将听到的信息放入Queue中，后续统一处理
                    g_var.ws_message_queue.put_nowait(res)

            except websockets.ConnectionClosed as e:
                logger.error('websocket closed error')
```

这里我先把请到的消息放到一个队列里面，然后后续再慢慢处理队列里面的消息，这个并没有什么特别的考虑，只是觉得这样写逻辑会更清晰一些。



## 发送消息

发送消息就是简单的send，但你可能是在其他程序中，所以其他程序中更完整的表述是 在时间循环中添加一个任务，然后等着事件循环去完成目标任务。

```python
import asyncio
eventloop = asyncio.get_event_loop()
eventloop.create_task(hello(1))
        
async def hello(count):
    websocket = g_var.websocket
    
    name = {'name': f'wanze{count}'}

    name_obj = json.dumps(name)
    await websocket.send(name_obj)
    print(f"> {name}")
```

