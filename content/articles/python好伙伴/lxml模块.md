Title: lxml模块
Slug: lxml-module
Date: 2019-11-05
Modified: 2019-11-05
Tags:  xml, lxml, html

[TOC]

## 简介

lxml模块最先接触是在爬虫那块，因为Beautifulsoup很好用，所有lxml模块基本上也就处于一个被调用阶段，并没有深入了解。但随着你对爬虫框架的研究深入，你就会发现xpath语句才是正确的从xml或html中抽取信息的标准流程化语言，而即使是功能还算强大的css selector选择器，其实也不过是xpath语句的精简版。这样lxml模块开始受到我的重视了，因为lxml对xpath语句有着很好的支持。

```python
from lxml import etree
selector = etree.HTML(html)
html_e = selector.xpath('//title')
```

此外lxml还可以很方便的去构建一个xml或者lxml文本：

```python
from lxml import etree

root = etree.Element('root')
child_1 = etree.SubElement(root, 'child_1')
child_1.set('a', '1')
child_1.text = 'this is a text'
child_2 = etree.SubElement(root, 'child_2')
print(etree.tostring(root, pretty_print=True))
```

实际上xml几乎是可以表达任何结构信息的，从简单的html到复杂的语法树。而基于xpath我们可以实现对于非常复杂的结构信息的精准信息搜索定位等操作。

关于xml谁是element谁是属性并没有特别的标准了，很可能实际上完全是两个相同的结构信息会有不同的xml结构表达，这方面各个具体实现领域有不同的考量，但在实践上还是有很多参考指导建议的，这个感兴趣的可以看下[这个网页](https://www.ibm.com/developerworks/library/x-eleatt/) 。

lxml类似于beautifulsoup也提供了find和find_all方法，但还是推荐读者使用xpath方法，实际上据说lxml里面的find和find_all方法也是基于lxml的xpath方法的，推荐读者多多使用xpath方法，熟悉xpath语法。

xpath方法一般会返回一个列表，不过如果你xpath语句使用 `string` 包装了的话，就会返回一个字符串，这个要注意下。

关于具体的使用下面有时间慢慢写上一些。