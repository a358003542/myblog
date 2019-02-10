Title: pelican模块
Slug: pelican-module
Date: 2016-09-25 21:51
Modified: 2016-10-03 18:50 
Tags: pelican, 静态网站生成, python
[TOC]

# 简介
pelican是一个静态网站生成工具，其是用python编写实现的，所以对于pythoner来说显得格外的亲切。

首先按照官方的quickstart简单的刷一遍吧，下面就一些问题作出一些讨论。


## 项目基本说明
python的虚拟环境控制这里就不多说了，下面主要讨论 `pelicanconf.py` 和 `publishconf.py` 和 `Makefile` 这个文件作出一些说明，然后项目文档的基本结构相关作出一些说明。

首先说明下 `publishconf.py` 和 `pelicanconf.py` 的区别， `publishconf.py` 文件里面有这样一句话：
```python
import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *
```

也就是其将继承所有来自 `pelicanconf.py` 里面的配置参量，不同的是 `publishconf.py` 是对阵发布到那边服务器上的，而 `pelicanconf.py` 的配置只是用于本机调试的。

所以 `pelicanconf.py` 里面的 `SITEURL` 变量是空值，而在 `publishconf.py` 里面是要赋一个具体的值的，该值随你的模板里面的用法不同而不同，具体就是 `{{ SITEURL }}` 这样的调用。

然后发布到远程机器pulish还会有其他一些额外的东西，比如 `DISQUS_SITENAME` 这个值，很多模板会根据这个值来决定是否开启disqus的javascript引用，而DISQUS系统在本机调试的时候是没有意义的，一般会不设置这个值从而自动关闭它。

`publishconf.py` 也许还有其他一些考虑，这里就略过了，下面将集中将 `pelicanconf.py` 里面的配置。

然后我们看到 `Makefile` 这个文件，这个脚本很好用，下面这些命令是很经常用到的：

```
make html
make serve
make github
...
```
其中make github会把你的output里面的内容刷到github pages对应的项目上去，其依赖于生成目标 `publish` ，而make publish和make html的惟一区别就是上面讨论的调用的那个具体的配置文件的不同。

这个Makefile文件我做了一些精简，这些都是无关紧要的，惟一值得一提的就是github目标的生成命令我参考官方文档做了一些更改（请 [参看这里](http://docs.getpelican.com/en/3.6.3/tips.html#publishing-to-github) ）：

```makefile
github: publish
	ghp-import -m "Generate Pelican site" $(OUTPUTDIR)
	git push develop $(GITHUB_PAGES_BRANCH):master
```

这里git的remote我加了一个develop指向目标地，是因为整个项目就是venv大环境作为一个项目是github上的另外一个项目，其已经使用origin这个目标地了，而github pages默认的那个目标地只好用develop这个名字了。

然后 `ghp-import` 是个命令行工具，在ubuntu下可以直接用 `apt` 安装之， 老实说这个工具在干嘛我还不太清楚。


## content和output文件夹说明
content 文件夹里面放着静态网站生成的源文件，接下来的讨论有些纯粹只是个人的设置偏好了，但都统一一并讲解了，具体DIY看读者自己的个人喜好了。

articles里面放着markdown或者html的源文件，其中articles文件夹下还有一层子文件夹，这些文件夹的名字最后会成为 `Category` 。而这在设置有： 

```
USE_FOLDER_AS_CATEGORY = True
```

然后html文件需要额外说一下，原网页的body里面的内容都会完整传过去，但是原html网页head部分里面除了必要的meta标签和title标签之外，其他多余的内容是传不过去的。那么css或者js的设置怎么弄呢，这个请参看后面的相关讨论，到时候设置好相关的meta标签即可。


images和pdfs和data和extra文件夹其实名字都是随意的，只是一般这样写罢了，pdfs里面放pdf，images里面放图片等。这几个文件夹都是所谓的静态资源文件夹，等下生成output文件夹的时候，里面的内容都放送入到output文件夹里面去。你需要如下设置：

```
STATIC_PATHS = ['images',
                'pdfs',
                'data',
                'extra',]
```

## 引用静态资源
比如在markdown里面引入图片如下所示：

```md
![img]({filename}/images/chemistry/Naphthalene.png)
```

这里 `{filename}` 是pelican特有的写法，表示引用某个文件。然后后面就是具体要引用的文件路径。其他引用类似，这里就不多说了。下面对extra这个文件夹多做一些说明，其是为了让网页加入favicon.ico静态文件的，你还需要如下设置：

```
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'}
}
```

这里参考了 [这个网页](http://stackoverflow.com/questions/31270373/how-to-add-a-favicon-to-a-pelican-blog) 。


## 引用js和css
js和css也是静态资源，但和上面的处理有有所不同，前面也提及了html源文件如果在head部分有css引用语句，都是会丢失的。你需要如下加上这样的meta标签语句：
```
<meta name="javascripts" content="周易之摇卦.js" />

```

然后你还需要安装pelican-plugins里面的 `pelican_javascript` 如下所示：

```
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['pelican_javascript', 'tipue_search', 'extract_toc']
```

更多信息请参看项目的 [github地址](https://github.com/mortada/pelican_javascript) 。


## output输出控制
```
ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = PAGE_URL
CATEGORY_URL = '{slug}/index.html'
CATEGORY_SAVE_AS = CATEGORY_URL
TAG_URL = 'tag/{slug}.html'
TAG_SAVE_AS = TAG_URL
```

- `ARTICLE_URL` 定义了文章的URL显示，其中slug你可以在文件头属性那边自定义。
- `ARTICLE_SAVE_AS` 定义了该文件在output文件夹那边如何的存储路径
- 后面类似的有控制 CATEGORY TAG PAGE 页面的URL和具体网页在output文件夹里面的存储路径。




# 其他技巧

## THEME设置或自定义THEME
```
THEME = 'mytheme'
```
具体自定义THEME其实就是copy一下别人的THEME，然后根据自己的jinja2知识等适当做一些修改。



## 目录自动生成
你需要安装 `extract_toc` 插件，然后你的virtuaenv环境里面需要安装了beautifulsoup4, 然后python-markdown那边你需要设置好 `toc` 插件开启。

```
MARKDOWN = ['toc']
```

然后在markdown那边加上这么一行即可：
```
[TOC]
```

## github markdown语法支持
在python-markdown那边开启 `fenced_code` 插件。


```
MARKDOWN = ['toc', 'fenced_code','codehilite(css_class=highlight, linenums=True)']
```

上面还设置了语法高亮类和显示行数。
