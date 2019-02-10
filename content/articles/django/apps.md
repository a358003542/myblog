Title: django后台api编写之-apps.py
Date: 2018-05-26

[TOC]


## apps.py

通过快捷命令创建的app模块是没有这个文件的，但是我看到某些例子里面其有这个文件，后来了解到这个文件是有特殊含义的：这是django项目用来存放app 一些相关配置信息的地方。

一个基本的例子如下：

```python
from django.apps import AppConfig

class RockNRollConfig(AppConfig):
    name = 'rock_n_roll'
    verbose_name = "Rock ’n’ roll"
```



其中name定义了本app的名字和完整名字，然后你需要在本app的 `__init__.py` 文件下加入：

```
default_app_config = 'rock_n_roll.apps.RockNRollConfig'
```

来引入这个配置文件。

有什么用？well，最简单的用处就是本app实际在 `INSTALLED_APPS ` 哪里不是默认的文件夹名字了，而是你这里定义的名字。

另外一个高级用法就是定制 `ready` 方法，来初始化本app的一些信号设置。



