Category: html5_tutorial
Slug: html5-style-guide
Date: 20191018

[TOC]

## html5代码规范

本文参考了 [这篇文章](http://codeguide.bootcss.com) 和 [这篇文章](http://alloyteam.github.io/CodeGuide/)  。

需要指出的是这些都是一些代码建议，其中有一些有点大头开蛋还是小头开蛋的意思，比如到底是空四个空格还是两个空格，这些有分歧的我就不写出来了，读者自行决定吧。



## 总的原则

1.  无论团队人数多少，代码应该看起来就好像一个人写的。——这个原则为大家所公认。
2.  文件名推荐是小写字母加下划线。（小写字母加连字符也是可以的，但是绝对不推荐带上空格）



## html

1.  缩进，这个一个好的编辑器会提供这个自动缩进功能的。
2.  属性名全部小写，用 `-` 隔开。
3.  属性的定义用 **双引号** 包围起来。
4.  `<hr>` `<img src=...>` 这样的不用后面加个 `/` 号了。
5.  关闭标签不要省略 `<li>...</li>`  这是没有疑问的。
6.  开头格式都是： `<!DOCTYPE html>` 
7.  语言指定遵循规范 ，`<html lang="zh-cn">` 
8.  字符编码推荐指定utf8，`<meta charset="utf-8">` 
9.  IE兼容模式，推荐加上这样一行：

```html
<meta http-equiv="X-UA-Compatible" content="IE=Edge">
```

10.  引用css和javascript，如下所示（不要再像以前加上一些杂七杂八的东西，尽可能保持代码简洁。）：

```html
<!-- External CSS -->
<link rel="stylesheet" href="code_guide.css">

<!-- In-document CSS -->
<style>
...
</style>

<!-- External JS -->
<script src="code_guide.js"></script>

<!-- In-document JS -->
<script>
...
</script>
```

11.  属性的顺序：
    1)  class
    2)  id name
    3)  data-*
    4)  src for type href value
    5)  title alt 
    6)  role aria-*

12.  布尔属性，html规范原文就是：

>   The values "true" and "false" are not allowed on boolean attributes. To represent a false value, the attribute has to be omitted altogether.
>
>   布尔属性存在就表示true，不存在就取值false。


```html
<input type="text" disabled>

<input type="checkbox" value="1" checked>

<select>
<option value="1" selected>1</option>
</select>
```

13. 代码简洁简洁，尽可能减少标签数量。这是没有疑问的。




## css

css代码规范有兴趣的请参看前面提到过的参考文章，这个我不太感兴趣，老实说css本来就可读性偏低吧，当然了基本的代码规范可以做一下。



