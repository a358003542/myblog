Title: logbook模块
Slug: logbook-module
Date: 2018-08-27
Modified: 2018-09-20
Tags:  logging,

[TOC]

## 前言

logbook似乎是个不错的模块可以改进我们的日志功能，可以看做系统logging模块的第三方升级版，但还是有很多地方不同的。

一开始我接触的最大的不同就是logbook官方文档并不推荐将某个handler注册在某个logger的那种做法，logbook的handler可以注册在整个线程或者整个进程上。或者我们看到官方文档的第一个例子是这种写法：



```python
from logbook import warn, StreamHandler
import sys
StreamHandler(sys.stdout).push_application()
warn('This is a warning')
```

或者写作：

```python
from logbook import warn, StreamHandler
import sys
log_handler = StreamHandler(sys.stdout)
with log_handler.applicationbound():
	warn('This is too cool for stdlib')
```



这是单个注册在整个程序上的，此外还有 `threadbound` 是注册在整个线程上的。一般桌面GUI程序推荐注册在整个程序上，web应用推荐注册在整个线程上。



这并不是说你不需要定义logger了，你还是如同你以前习惯的这样定义和使用。

```python
from logbook import Logger
logger = Logger(__name__)
logger.info('just log it.')
```

logbook更多的配置如下所示，就是配置不同的handler：

```python
import os
from logbook import NestedSetup, NullHandler, FileHandler, \
     MailHandler, Processor

def inject_information(record):
    record.extra['cwd'] = os.getcwd()

# a nested handler setup can be used to configure more complex setups
setup = NestedSetup([
    # make sure we never bubble up to the stderr handler
    # if we run out of setup handling
    NullHandler(),
    # then write messages that are at least warnings to a logfile
    FileHandler('application.log', level='WARNING'),
    # errors should then be delivered by mail and also be kept
    # in the application log, so we let them bubble up.
    MailHandler('servererrors@example.com',
                   ['admin@example.com'],
                   level='ERROR', bubble=True),
    # while we're at it we can push a processor on its own stack to
    # record additional information.  Because processors and handlers
    # go to different stacks it does not matter if the processor is
    # added here at the bottom or at the very beginning.  Same would
    # be true for flags.
    Processor(inject_information)
])
```



上面的Processor会自动在每条日志记录上打上额外的信息。logbook还提供了很强大的MailHandler等等。这些相关配置信息后面慢慢了解。

## 一些配置

### level

```
critical 导致程序终止的异常
error  还可以应付的error
warning 一些情况可能不是error
notice  no-error 但你可能希望看见
info  信息你不想看见
debug 信息给debug用
```

### handler

- StreamHandler 流handler，一般指 sys.stdout 
- FileHandler RotatingFileHandler TimedRotatingHandler 用于输出到文件
- MailHandler 用于输出到email

### bubble

bubble参数默认是False，某个日志记录被某个handler处理了其他的handler就不会处理了，而设置bubble=True之后，其他handler同样也可以处理。



### action_level

有了这个级别的记录才会输出日志，否则不输出。