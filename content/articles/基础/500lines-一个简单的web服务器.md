Title: 500lines-一个简单的web服务器
Date: 2018-05-28
Slug: 500lines-a-simple-web-server


[TOC]

## 前言

本文主要是对 [500lines](http://aosabook.org/en/500L/a-simple-web-server.html) 项目的这篇文章的学习和讨论，这篇文章写得是极好的，除了对如何编码有一些很好的借鉴参考价值，还主要能让读者对http web server 做的事情有了一个清楚的认识。这篇文章弄清楚了，对django或者flask在做一些什么事，就很胸有成竹了，甚至包括nginx等服务器在做一些什么事也有一个大致的了解了。

因为作者后端出身，所以对这篇文章的质量和价值是清楚的，以至于作者在强烈呼唤出现这样一篇类似的描述前端框架的文章，目前我对前端框架整个过程还没有一个很好的认识。



关于计算机网络和HTTP相关不在本文讨论了，笔者也自觉这一块有时间还需要再深入补一补。



我们的web服务器要做的工作如下：

- 占着个端口等着某个HTTP 请求包发过来
- 你知道的HTTP请求包有一定的格式，具体哪些信息进行parse操作
- 确定该请求要做点什么（分发GET POST）
- 程序做点什么
- 形成返回的数据格式，比如html等。
- 将返回的数据传回去

上面步骤的前两步和最后一步python的 `HTTPServer` 已经帮我们自动做了，更不用说django和flask这些框架，也早就帮我们做好了。我们只需要关注的是，请求过来的是GET还是POST等，然后当然是程序总要干点什么事，最后就是把要送回去的数据整理好，再一并发过去即可。

更高级的web server 如flask之类的，会提供很多额外的支持，比如请求参数，请求头等信息的整理，然后如果你希望实现restful风格api，只返回一个字典值，对应的一些响应头封装也帮你做好了，当然在返回数据上，比如html会引入jinja2模块引擎等，这些都是很好理解的。总的说来web server干的就是这些事。



## 第一个例子

针对python3版本代码稍作修改。

```python
from http.server import HTTPServer, BaseHTTPRequestHandler

class RequestHandler(BaseHTTPRequestHandler):
    '''Handle HTTP requests by returning a fixed 'page'.'''

    # Page to send back.
    Page = '''\
<html>
<body>
<p>Hello, web!</p>
</body>
</html>
'''

    # Handle a GET request.
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(self.Page)))
        self.end_headers()
        self.wfile.write(self.Page.encode())

#----------------------------------------------------------------------

if __name__ == '__main__':
    serverAddress = ('', 8080)
    server = HTTPServer(serverAddress, RequestHandler)
    server.serve_forever()
```

上面的 do_GET 方法内部作用原理如下：

```
    mname = 'do_' + self.command
    if not hasattr(self, mname):
        self.send_error(
            HTTPStatus.NOT_IMPLEMENTED,
            "Unsupported method (%r)" % self.command)
        return
    method = getattr(self, mname)
    method()
```

其中 self.command 就是http协议请求头传过来的GET或者POST等，然后 handler类会去找对应的方法，找到了再进行对应的操作。

这种根据函数名来进行行为分发的编程模式，很值得引起大家的注意，在web server里面一直都存在着这个需求。从url server_name 到对应的虚拟server分发，从path method 到对应的函数行为分发，再到后面高级的参数验证valide_what 等也有类似的行为分发需求。



## 简单的模板输出方案

这个就不码代码了，其实就是简单的python字符串format方法，更复杂的就使用jinja2模板系统来生成html内容，这是后话了。



## 挂载静态文件

静态文件就是找到对应的文件，然后返回就是了。当然对于 index.html 等特殊文件需要特别的处理。



500lines该文后来提到一种有趣的编码写法：

```
class case_no_file(object):
    '''File or directory does not exist.'''

    def test(self, handler):
        return not os.path.exists(handler.full_path)

    def act(self, handler):
        raise ServerException("'{0}' not found".format(handler.path))
```

```
    def do_GET(self):
        try:

            # Figure out what exactly is being requested.
            self.full_path = os.getcwd() + self.path

            # Figure out how to handle it.
            for case in self.Cases:
                cond= case()
                if cond.test(self):
                    cond.act(self)
                    break

        # Handle errors.
        except Exception as msg:
            self.handle_error(msg)
```

```
class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):

    Cases = [case_no_file,
             case_existing_file,
             case_always_fail]
```
针对多种情况，实现了行为分发，有点像switch语句但更python风格更优美的写法。



## 简单的cgi接口实现

接下来的cgi接口实现代码也是很简单的：

```python
class case_cgi_file(object):
    '''Something runnable.'''

    def test(self, handler):
        return os.path.isfile(handler.full_path) and \
               handler.full_path.endswith('.py')

    def act(self, handler):
        handler.run_cgi(handler.full_path)
        
    def run_cgi(self, full_path):
        cmd = "python " + full_path
        child_stdin, child_stdout = os.popen2(cmd)
        child_stdin.close()
        data = child_stdout.read()
        child_stdout.close()
        self.send_content(data)
```

其核心就是针对某个python脚本文件，启动cgi协议接口，简单来说就是启动一个python解释器运行一下目标脚本文件，然后获取其返回的内容，作为web server的返回内容返回即可。

然后下面有必要了解下cgi协议，所谓CGI协议，全称是（Common Gateway Interface）通用网关接口，说得再确切一点，是cgi程序和web server之间的接口标准，说得再简单粗糙点，一个web server，比如apache 或者 nginx 会把上面我们讨论的返回静态文件等做好，请读者进一步参看 [这篇文章](https://zhuanlan.zhihu.com/p/25181849) 。

然后有些请求，这些请求就是这里讨论的CGI协议，这里所谓的nginx就是web server，也是本例子中的大部分代码扮演的角色，而这里所谓的cgi程序，实际上就是那个python脚本，当然也可能是某个python框架，这个后面会讨论到。

路径上挂载的参数将作为环境变量传递进来，等等还有其他一些工作，就是CGI协议定义的内容。讲到cgi协议，到了python这边，就不可能不提到pep3333和wsgi标准了。



## WSGI

[PEP3333](https://www.python.org/dev/peps/pep-3333/) 定义了 Python Web Server Gateway Interface ，叫做python web server 网关协议，简称WSGI协议。从名字就看到出来，在python的世界里，推荐使用WSGI协议。所以我们可以猜到WSGI同样也要处理好，路径path里面挂载的参数，然后送入环境变量这个问题。继续深入的话还需要把服务器信息，客户端信息，本次请求信息都存入environ变量中，然后WSGI application（这个由python那边的程序或者框架提供），必须是可调用的，还有等等其他规范。

还有WSGI middleware 层，在django和flask（Werkzeug  ）里面，我们都将接触到 Middleware 类的概念。



总的说来nginx 扮演的是web server里面服务静态文件的角色，wsgi请求将发给gunicorn：gunicorn的官方介绍是：

>  Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX. 

简单来说在WSGI协议里面其扮演的也是web server的角色，而gunicorn挂载的另一边，就是django或者flask或者其他什么框架提供的wsgi脚本app，或者说application对象所在。

当然对于我们实际编码使用框架的人来说，不用太在意这些，记得在哪里调用path，path上面挂载的参数，怎么写行为，决定返回什么内容就是了。不过如果你是这些框架的编写人员，那么就要详细的研究WSGI协议了。