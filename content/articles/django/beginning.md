Title: django后台api编写之-beginning
Date: 2018-05-26

[TOC]

# Beginning

一开始先介绍下Djanog项目的基本文件夹结构，还有一些基本的命令操作和一些基本的常识性东西。

首先是新建一个项目：

## 新建项目
```
django-admin startproject project-name
```

这个命令将创建一个文件夹，文件夹的名字就是这里设置的project-name，然后文件夹里面有一个manage.py文件，这个文件的主要作用就是挂载django的配置（一般是settings.py这个文件，当然你也可以修改为其他比如dev_settings.py文件）。

然后还有一个文件夹，里面有settings.py 、 urls.py 和 wsgi.py 文件。

settings.py 控制django的全部配置管理；

urls.py 控制django的路径分发主入口，这个在配置中可以修改的。

wsgi.py 是你用apache或者uwsgi挂载的时候的控制入口。


这样最简单的初始项目就是可以运行的了：


## 开启服务器

```
python manage.py runserver localhost:8080
```

后面控制服务器监听的localhost或者外网0.0.0.0，然后就是端口号。



## 新建一个app

```
python manage.py startapp app_name
```

这里顺便说一下，有一些项目你可能找不到 manager.py 这个文件了，其实这个文件就是一个便捷入口罢了，所有的命令一样都可以通过 django-admin 命令来运行的。



## 数据库操作

定义模型之后，你需要运行:

```
python manage.py makemigrations app_name
```

这个过程就是创建每个app下的migrations文件夹下面的一些迁移python脚本文件，有的时候某些情况你可能需要手工修改这些迁移文件。

```
python manage.py migrate
```
这个命令就是实际执行那些迁移python脚本。




## 交互式环境

进入python交互环境，这个和纯python交互环境的区别就是里面可以直接使用django里面的一些东西了，比如你定义的模型对象就可以直接使用了。这个对你开发进行测试工作非常有用！

```
python manage.py shell
```


或者进入sql实现的交互环境:

```
python manage.py dbshell
```



## 创建超级用户
最开始创建的项目就把admin url挂上去了，你可以去 \verb+/admin+ 这个url下看一下，但要登录除了做一下上面的数据库表格创建工作外，还需要创建一个超级用户用于登录。

```
python manage.py createsuperuser
```


