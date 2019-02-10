Title: django后台api编写之-url分发
Date: 2018-05-26

[TOC]

## url分发

web框架的一个核心功能就是完成url分发工作，我们先来看下django的这块内容。

基本过程是在你的 project 的 `urls.py` 那里定义好整个项目的url分发规则。默认的内容如下:

```python
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
]
```

读者有兴趣可以先看下那个admin页，在 `/admin` 那边。请确认已经执行前面的数据库操作 `makemigrations` 和 `migrate` 了，然后已经创建超级用户了 `createsuperuser` 。这样你就可以看到django默认自动创建的admin支持页面了。

然后接下来就是类似这样的在这里插入你自己的 app的 各个 urls定义。一般如下简单写上即可:

```python
from django.urls import include, path
    ....
    path('app_name/', include('app_name.urls')),
    ....
```

在确定没有特殊url分发需求的情况下，都推荐如上使用django官方教程推荐的这种url分发写法。

在某个app下的 `urls.py` 将进一步定义url分发规则:

```python
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```



上面的讨论是根据django的官方教程来的，应该是推荐的写法风格。



## url上带参数

```python
from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^add/([\d]+)/([\d]+)$', views.add, name='add'),
]
```

这里参数将逐个传递个视图函数，唯一值得一提的是django的视图函数默认第一个函数是传递进去的 `request` 参量。在 `views.py` 里面的内容如下:

```python
from django.http import HttpResponse

def add(request, a, b):
    res = int(a) + int(b)
    return HttpResponse(str(res))
```

上面这种正则表达式的写法是老式的django的url写法，一般没有特别的需求的话，应该按照django官方教程，采用下面的推荐写法：

```python
from django.urls import path

from . import views

urlpatterns = [
    path('add/<int:a>/<int:b>', views.add, name='add'),
]
```





## url定义name

`name` 这个参量大体类似于flask的 `endpoint` 的概念，然后django还有的 `reverse` 函数，其大体类似于flask的 `url_for` 的概念。

比如上面视图函数的 add 对应的url我们可以如下获得:

    from django.core.urlresolvers import reverse
    reverse('add',args=(1,2))

然后在模板中有:

    <a href="{% url 'add' 1 2 %}">link</a>

## 获取full-url

上面提到的reverse函数返回的url字符串还不是完整的url，而只是相对url。如果我们要获取全站的完整url则可以使用 `request.build_absolute_uri(location)` ，如果不指定location则默认是当前的url。


