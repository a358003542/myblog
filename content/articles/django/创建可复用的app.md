Title: django后台api编写之-创建可复用的app
Date: 2018-05-26

[TOC]

# 创建可复用的app
创建可复用的app会极大的降低你的目标django项目的复杂度，如果可能，将你的app打造成可复用的风格总是首选。

## 制作django-what的pypi包
有关pypi包的制作就不赘述了，下面主要在官方文档 [这里](https://docs.djangoproject.com/en/1.11/intro/reusable-apps/) 的基础上讨论一些问题。

## 测试问题
我试着如下安装测试过程：

```
python setup.py sdist
pip install dist/what.tar.gz
```
然后安装官方文档，在INSTALL_APPS那里设置好。app是可以正常使用的。但在安装测试过程中，这实在有点繁琐了。推荐还是将整个app文件夹复制到你的测试webapp那边去，然后一边修改一边看。测试好了再把内容同步到pypi安装包那边去。


## migrations问题
官方文档之所以选择制作sdist和用pip install tar包这种风格是有原因的，经测试egg包在访问上很成问题，只有用pip安装这种方法，在site-packages那边你安装才是文件夹风格而不是那种egg文件。这样你等下执行：
```
python manage.py makemigrations app_name
```
才会成功。

而且实际生成的迁移文件就放在site-packages那里的目标文件夹下的。所以你制作pypi包的时候不要把migrations文件夹里面的其他迁移文件包含进去了，要包含就包含 `__init__.py` 文件即可。

当然就算你不是制作django的目标pypi包，其他django项目在 `.gitignore` 文件上加上这一行总是不错的：

```
*/migrations/*
```
PS: 我知道stackoverflow那边都认为应该加上，还有人专门写了长篇大论认为应该加上。我确定的只有一点：早期测试开发过程，所有的migrations文件夹里面都只有 `__init__.py` 这个空白文件，保持代码整洁，在测试开发阶段不花精力在这上面，这是没有争议的。

