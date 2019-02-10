Title: jinja2模板
Slug: jinja2-template
Date: 2017-10-12 
Modified: 2018-12-26
Tags: python, template,

[TOC]


## 前言

jinja2模板在flask和pelican中都有使用，而且就是在django框架中，模版语法也大体类似，所以jinja2模板还是很值得一学的。



## 注释

这里面的内容是模板文件的注释内容。

    {# ... #}

## 变量

这里算是jinja2模板的主体内容了，里面的变量可以直接使用，在render的时候传进去即可。然后 `object.a` 这样的dot法引用，或者 `object['a']` 这样的利用对象 `__getitem__` 内置方法来调用值的形式也支持。

    {{ ... }}

变量的值在jinja2模板系统中调用之后将会变成字符串然后插入在文档中，这就不多说了。

## for语句

for语句结构如下所示:

```jinja2
<ul>
{% for user in users %}
  <li>{{ user.username }}</li>
{% endfor %}
</ul>
```



## 条件分支

条件分支主要用于有条件的显示某些内容。

```jinja2
{% if user %}
 Hello, {{ user }}!
 {% else %}
 Hello , stranger!
 {% endif %}
```



## html特殊符号问题

如果你的变量有这些html的特殊符号:

```html
<  >  &  "
```

假设你没有在flask中使用jinja2模板系统，那么这些字符是没有经过特殊处理的，那么比如说 `<b>test</b>` 这段字符串到了html文档中就将以粗体的形式显示。如果你希望显示这些符号，那么可以使用 **escape** 过滤器来做到这点:

    {{ test|escape }}

或者:

    {{ test|e }}

都是一样的。

这里的过滤器有点类似bash的管道的意思，意思是将输出的字符串经过额外的操作。

但一般推荐的风格是html标签都放在jinja2模板系统的外面，jinja2模板系统只处理最核心的那些字符串。所以flask是设置为全局auto escape的，这是正确的思路。如果你确实有某些html标签就希望是html标签的形式显示出来，而不经过escape，那么可以采用 **safe** 过滤器<sup><a id="fnr.1" class="footref" href="#fn.1">1</a></sup> 。

```jinja2
{{ "<b>test</b>"|safe }}
```

## 模板文件继承机制

jinja2的模板文件有一种继承机制，可以让你基于某个模板文件来建构出另外一个模板文件，前面那个模板文件大概可以称作模板文件的模板文件吧。具体使用是在父模板（模板文件的模板文件）构建一些block区块，如下所示:

```jinja2
<title>{% block title %} {% endblock %}</title>
```

这里构建了一个title区块。

然后子模板首先继承父模板所有的内容:

    {% extends "base.html" %}

然后一些需要定制的部分，比如说这里的title部分，做成block之后，子模板文件可以重新定义这个title block:

    {% extends "base.html" %}
    {% block title}books - the classic books of  which you want to collected
    {% endblock %}

此外子模块在block重载的时候，你还可以用

    {{ super() }}

来加载父模块在该block中的一些定义。

上面title block的内容你可以如下引用之:

    {{ self.title() }}



## 过滤器filters

过滤器就是一些额外的字符串操作函数，一般推荐还是在python代码中把要输出显示的字符串处理好吧，下面列出一些函数简单了解下即可。



- safe 渲染值不转义
- capitalize 值首字母大写 其他字母小写
- lower 字母都小写
- upper 字母都大写
- title 值每个单词首字母大写
- trim 值首尾空格去除
- striptags 渲染之前把所有HTML标签去掉



## 宏

宏 和python的函数类似，遇到即将其展开。

```jinja2
{% macro render_comment(comment) %}
<li>{{ comment }}</li>
{% endmacro %}
<ul>
{% for comment in comments %}
{{ render_comment(comment) }}
{% endfor %}
</ul>
```

外部宏文件 引入

```jinja2
{% import 'macros.html' as macros %}

{% import 'macros.html' as macros %}
<ul>
{% for comment in comments %}
{{ macros.render_comment(comment) }}
{% endfor %}
</ul>
```

引入

    {% include 'common.html' %}





<div id="footnotes">
<h2 class="footnotes">Footnotes: </h2>
<div id="text-footnotes">

<div class="footdef"><sup><a id="fn.1" class="footnum" href="#fnr.1">1</a></sup> <div class="footpara">参考了 [这个网页](http://stackoverflow.com/questions/3206344/passing-html-to-template-using-flask-jinja2) 。</div></div>
