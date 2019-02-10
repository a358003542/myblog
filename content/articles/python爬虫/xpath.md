Title: xpath
Date: 2018-07-25
Slug: xpath
Tags: 爬虫,
[TOC]

## 前言

基本东西简单了解下即可，然后多看例子吧。

```
/what   基本路径表达，下个节点
//what  基本路径表达，任意位置的下个节点
```

这里 `/` 表示在下个节点中匹配， `//` 下个或所有子节点匹配。 

```
//div[@id='what']   根据id定位
//div[@id='what']/a[1] 根据id定位后找下面的第一个a标签
//div[@id='what']/a[*] 根据id定位后找下面的所有a标签
```

这里 `*` 表示所有的意思。

```
//div[@name]   找具有name属性的div标签

//div[@name='what'] 找name属性等于what的div标签 

//*[contains(@class,'what')] 找某个标签class属性有 what NOTICE: 这里的意思是有，多个class属性也是可以匹配的 class="what what_what"
//div[@class='what'] 那个目标标签的class属性就是what，也就是匹配的是 class="what"

//*[@id="list"]//dd[*]/a[@href and @title] 找id=list的标签下面的所有dd标签下面的a标签，a标签必须有href和title属性。
```



```
//title[@*]  选择title，随意属性，但title标签必须有属性
```





## 选择具体的内容

### 选择属性

```
//*[@id="list"]//dd[*]/a[@href and @title]/@href  
```

### 选择文本

```
//title/text()
```



## string

对于选择的节点（注意如果返回的是节点集 nodeset将只取第一个），将所有的节点（也就是包括子节点）的文本抽取出来并合并。

```
string(//div[@class="lemma-summary"])
```











## 参考资料

1. [阮一峰写的xpath入门教程](http://www.ruanyifeng.com/blog/2009/07/xpath_path_expressions.html)
2. [w3school的xpath教程](http://www.w3school.com.cn/xpath/)
3. [一篇关于xpath写的不错的博文](http://www.cnblogs.com/ziyunfei/archive/2012/10/05/2710631.html)