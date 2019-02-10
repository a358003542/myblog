Title: django后台api编写之-django和celery
Date: 2018-05-26

[TOC]

## django和celery

django-crontab这个模块我试过的，还是很便捷的，不过其还是基于系统的crontab，而如果我们将django和celery组合起来，celery灵活的消息分发机制，无疑将给未来开发带来更多的可能性。celery的官方文档在 [这里](http://docs.celeryproject.org/en/latest/index.html) ，本文主要讲一下celery的基本概念和django的集成问题，更多celery的知识请参阅官方文档。



### celery的核心概念

-   broker  任务队列服务提供者，celery推荐使用redis或者rabbitmq作为broker。
-   task 具体执行的任务，其实就是定义的一些函数。
-   backend 用来存储任务之后的输出结果
-   worker celery的启动就是开启一个worker。



### django内文件安排

本小节参考了 [这篇文章](https://medium.com/@yehandjoe/celery-4-periodic-task-in-django-9f6b5a8c21c7) 和 [这篇文章](http://geek.csdn.net/news/detail/128791) 。需要提醒读者的是，django和celery集成现在并不需要额外安装什么插件了，而且下面讲的配置实际上就是一个单独的celery app大部分都是类似的，只是多了一些细节上的处理和优化。

#### celeryconfig.py 

首先推荐在你的django app `settings.py` 旁新建个 `celeryconfig.py` 文件，有的教程让设置这个配置文件名字为 `celery.py` ，这样很不好，文件名和某个模块名字重复有时会出问题的。里面的内容如下：

```python

import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_name.settings')

app = Celery('project_name')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
```

这个下面新建的任务不过是方便测试罢了，然后上面几行配置基本上死的。最值得讲的就是这两行：

```
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
```

第一行是从django的配置对象中读取配置，特别注意的就是那个 `namespace='CELERY'` ，这样只有 `CELERY_` 开头的配置才会读取，而且对应原celery配置的关系是：

```
CELERY_BROKER_URL  -> BROKER_URL
```

我那次就是 `CELERY_BEAT_SCHEDULE` 写成了 `CELERYBEAT_SCHEDULE` 然后老实发现周期性程序启动不起来。

第二行也是一个优化细节，从函数名字也可以看到，就是自动发现任务。在你的django的其他app里面新建一个 `tasks.py` ，celery会自动发现你定义的任务。



#### `__init__.py` 

还是你的django项目的project `settings.py` 那个文件夹里面，`__init__.py` 推荐写上这几行内容：

```
from .celeryconfig import app as celery_app

__all__ = ('celery_app',)
```

#### settings.py

具体celery的一些配置就统一写在 `settings.py` 文件里面，上面也提到了，都要 `CELERY_` 开头，大体如下所示：

```

CELERY_BROKER_URL = 'redis://localhost:6379'
#CELERY_RESULT_BACKEND = 'redis://localhost:6379'
#CELERY_ACCEPT_CONTENT = ['application/json']
#CELERY_RESULT_SERIALIZER = 'json'
#CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Shanghai'
# schedules
from celery.schedules import crontab
CELERY_BEAT_SCHEDULE = {
    'crawl_juhe_every_one_hour': {
         'task': 'wxarticles.tasks.crawl_juhe',
         'schedule': crontab(minute=0, hour='*/3'),
    },
    'every_miniute_for_test': {
        'task': 'wxarticles.tasks.test_celery',
        'schedule': crontab(),
    },
}


```

#### 定义任务

好了，定义任务，实际上就是定义一个函数，比如下面这个简单的打印函数来确认celery周期程序是工作着的：

```
from celery import shared_task

@shared_task()
def test_celery():
    print('celery is working.')
```

celery的crontab功能很强大，比如上面的 `crontab()` 就是每分钟执行一次。具体请参看 [官方文档](http://docs.celeryproject.org/en/latest/userguide/periodic-tasks.html) 之。

#### 启动任务

和celery其他操作都是一样的，就是启动worker：

```
celery -A project_name worker -l info
```

`-A` 选项跟着 celery app的名字，在这里也就是django项目的名字。 `-l` 选项设置日志打印级别。

你还可以加上 `-B` 来同时启动周期性任务。

或者另外开个命令：

```
celery -A project_name beat -l info
```





---

其他制作脚本啊，制作后台程序，制作服务啊，使用supervisor啊，实际上和celery关系已经不大了，可以不在这里说了。



#### 手工启动一次任务

参考了 [这个网页](https://stackoverflow.com/questions/12900023/how-can-i-run-a-celery-periodic-task-from-the-shell-manually) 。

```
$ python manage.py shell
>>> from myapp.tasks import my_task
>>> eager_result = my_task.apply()
```







