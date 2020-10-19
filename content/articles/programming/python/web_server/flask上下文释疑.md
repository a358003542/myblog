Category: web_server
Slug: flask-context-faq
Tags: flask
Date: 20190405

[TOC]

### 问题一 gunicorn多进程模式是怎样和flask作用的

参考 [这个问题](https://stackoverflow.com/questions/670891/is-there-a-way-for-multiple-processes-to-share-a-listening-socket#) 的解答：

```python
import socket
import os

def main():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind(("127.0.0.1", 8888))
    serversocket.listen(0)

    # Child Process
    if os.fork() == 0:
        accept_conn("child", serversocket)

    accept_conn("parent", serversocket)

def accept_conn(message, s):
    while True:
        c, addr = s.accept()
        print 'Got connection from in %s' % message
        c.send('Thank you for your connecting to %s\n' % message)
        c.close()

if __name__ == "__main__":
    main()
```

gunicorn 采用的是 pre-fork work 模式，大概作业模式如上代码所示，不同点是 gunicorn 起的主进程不负责消息处理，只负责端口监听和消息分发给子进程。

多进程的情况我们大体是熟悉的，基本上都是独立运行的内部变量类之间完全不相同的程序了。flask wsgi源码中有如下代码：

```python

    def wsgi_app(self, environ, start_response):
        ctx = self.request_context(environ)
        error = None
        try:
            try:
                ctx.push()
                response = self.full_dispatch_request()
            except Exception as e:
                error = e
                response = self.handle_exception(e)
            except:  # noqa: B001
                error = sys.exc_info()[1]
                raise
            return response(environ, start_response)
        finally:
            if self.should_ignore_error(error):
                error = None
            ctx.auto_pop(error)
```

其中environ环境中大概有本进程的 app类，然后ctx就是所谓的请求环境，简单了解下这个对后面的讨论有帮助。



### 问题二 flask如何应对多线程

这个就要从 flask 源码的 globals 里面的这两行代码说起：

```python
_request_ctx_stack = LocalStack()
_app_ctx_stack = LocalStack()
```

后面代码使用的 请求环境栈和应用环境栈都是这里定义的，这个LocalStack 参考了 [这片文章](https://cizixs.com/2017/01/13/flask-insight-context/) 的讨论，借鉴了python threading 模块的 local，其是一个线程本地变量，简单来说就是其是一个字典按照线程不同id的索引，不同的id各自取各自的值，互不干扰。

所以flask在多线程下，请求环境栈和应用环境栈你可以将其看做各自不同的堆栈，互不干扰。

### 问题三 flask如何应对多协程

原则上如果flask使用的python的threading的local，那么对于协程问题是不能很好地应对的，这个python3.7似乎新增了一个 `contextvars` 模块就是为了解决这个问题的。那么问题就来了，我们知道gunicorn 可以开始多个进程的worker，而且多个进程worker之下还可以开启多个线程，除了默认的线程之外，gunicorn是还可以开启gevent之类的异步线程的。gevent之类的就是在开启多协程，那么flask能够应对这种情况吗？

flask使用的是 werkzeug定义的Local类，而在源码中我们看到这个：

```python
try:
    from greenlet import getcurrent as get_ident
except ImportError:
    try:
        from thread import get_ident
    except ImportError:
        from _thread import get_ident
```

也就是werkzeug会试着先加载greenlet的get_ident 函数，我想这个函数应该是支持不同的greenlet协程的，而gevent底层似乎开启的就是greenlet协程。

这就说明清楚了，也就是说flask的请求环境栈和应用环境栈不仅是线程独立的，而且还有额外对于greenlet的支持。

那么这里就提出一个问题，我估计现在flask现在应该对于python内部的asyncio协程模式是不能支持的。

### 问题四 请求环境栈到底做了什么工作

在请求没有到来之前，请求环境栈和应用环境栈都是空的。你要使用app类除了在代码里面直接引用之没有其他办法。

当一个请求过来了之后，请求环境栈会执行push动作，收集好当前环境的很多变量之后，比如 `request`  `session` ，还有其他变量，然后将这个请求环境上下文压入堆栈，然后检查应用环境堆栈，如果为空，则会自动创建；或者默认top应用不同当前的，也会自动创建压入。

因为前面讨论过在flask能够应对的多线程多协程默认下，【下面为了讨论方便，只说线程了】，在最小的线程单元中，每个请求环境栈和应用环境栈都是不同的，都会默默记录下当前的请求环境和应用环境，都是一个请求一个请求顺序处理的。于是一个请求来，push，处理完，pop。这是很简单的模式。

具体应用环境存储做了一些优化，比如当前top的和当前一致的话就直接存储None，到时候需要的话，直接调用 `current_app` 来取就是了。

在取的时候采用了如下代码使用了一种惰性的动态代理机制：

```python
def _lookup_req_object(name):
    top = _request_ctx_stack.top
    if top is None:
        raise RuntimeError(_request_ctx_err_msg)
    return getattr(top, name)

request = LocalProxy(partial(_lookup_req_object, "request"))
session = LocalProxy(partial(_lookup_req_object, "session"))

g = LocalProxy(partial(_lookup_app_object, "g"))
```

然后request 和session的生存期就是本请求期，这是没有问题的。不过对于g这个变量还需要讨论下。第一个这个g最小粒度在线程这是没有问题的，各个线程之间g彼此完全不相干。而在线程内部接受的不同请求，由于他们都是引用的默认的那个相同的应用上下文环境，那么这个g是可以为多个请求公用的。但正如上面讨论的，不仅不同线程之间g不通用，而且就算某个线程内部，虽然可以应付多个请求，但对于多个应用情况来说g是和应用上下文绑定的，这些请求彼此并不公用g。

flask推荐请求之间要记住某个值，推荐使用数据库或者session这个变量，session虽然是挂在请求上下文中的，但实际在请求上下文创建的时候其是直接接受session参数的：

```
def __init__(self, app, environ, request=None, session=None):
```

这个session具体怎么传递的还不是清楚，应该在werkzeug那边。

flask推荐g的一种使用方式，是比如管理数据库的连接等，虽然g可能会为空，但只要如下，确保引用的时候，检查一下即可：

```python
from flask import g

def get_db():
    if 'db' not in g:
        g.db = connect_to_database()

    return g.db

@app.teardown_appcontext
def teardown_db():
    db = g.pop('db', None)

    if db is not None:
        db.close()
```



### 问题五 多应用的情况是怎么回事

参考了 [这篇文章](https://cizixs.com/2017/01/13/flask-insight-context/) 的讨论 ，flask是支持多应用的编码风格的：

```python
from werkzeug.wsgi import DispatcherMiddleware
from frontend_app import application as frontend
from backend_app import application as backend

application = DispatcherMiddleware(frontend, {
    '/backend':     backend
})
```

也就是单一线程接受不同的请求，这个请求是哪个app负责的，这个请求是哪个app负责的，依靠应用上下文环境栈是支持这种情况的。



最后一般教程都会提到应用上下文环境可用于单元测试：

```
with app.app_context():
    pass
```

```
from hello import app
from flask import current_app
app_ctx = app.app_context()
app_ctx.push()
print(current_app.name)
```

### 问题六 session到底是个什么东西

前面提到flask在创建请求上下文的时候session这个参数是不知道从哪里直接传进来的，那个flask的这个session到底是个什么东西？

首先说下背景知识：我们知道服务器那么响应内容可以设置这样的响应头： `Set-Cookie` ，对应flask里面的：

```
r = Response('test')
r.set_cookie('a','1')
```

客服端client或者说浏览器在接收到这样的响应之后，下次对目标服务器的请求会在请求头上加上对应的Cookie。

如下图所示：

![img]({static}/images/python_third_party/session_and_cookie.png)

说明： 上面是第二次刷新的结果，如果用浏览器的无痕模式测试，第一次request的请求头没有Cookie的。

然后我们在上图的Cookie中看到了 `session` 这个字段，只是内容含义不明。这个就是对应flask里面的session：

```
from flask import session
```

只是经过了flask的加密。