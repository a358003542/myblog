Title: html5基础
Date: 2018-05-26
Modified: 2018-08-16


[TOC]

# html5基础


## 第一个模板

```html
<!DOCTYPE html>
<html lang="zh-cn">
    <head>
    <meta charset="utf-8">
    <title>your awesome title</title>

    </head>

    <body>

    </body>
</html>
```

### doctype声明

现在html5的doctype声明非常简单了，开头加入如下简单一行即可:

    <!DOCTYPE html>

然后进入 **html** 标签，然后进入 **head** 标签，在head标签里面的内容不会显示在网页上，主要是一些关于本网页的配置信息。

### 字符集设置为utf-8

现在html5使用如下更简洁的语法了:

    <meta charset="utf-8">

然后 **body** 标签里面存放这实际要显示的网页内容。

## 第二个例子

```html
<!DOCTYPE html>
<html lang="zh-cn">
    <head>
    <meta charset="utf-8">
    <title>basic html</title>
    </head>

    <body>
        <nav>
            <ul>
                <li><a href="#">Home</a></li>
                <li><a href="#">About</a></li>
                <li><a href="#">Products</a></li>
                <li><a href="#">Contact Us</a></li>
            </ul>
        </nav>

    <header>
        <h1><a href="#">Very Basic Document</a></h1>
        <h2>A tag line might go here</h2>
    </header>

    <section>
        <article>
            <h3><a href="#">First Article Title</a></h3>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. </p>
        </article>

        <article>
            <h3><a href="#">Second Article Title</a></h3>
            <p>Praesent libero. Sed cursus ante dapibus diam.</p>
            </article>
        </section>

        <aside>
            <h4>Connect With Us</h4>
            <ul>
                <li><a href="#">Twitter</a></li>
                <li><a href="#">Facebook</a></li>
            </ul>
        </aside>

        <footer>
            <p>All rights reserved.</p>
        </footer>
    </body>
</html>
```

html5新加入了很多关于文档结构的标签，这些标签并没有任何布局含义，相当于一个自带名字的div，也就是默认标签的意思。其主要作用就是html内容分组(group)。

下面是常用的这些标签含义，在实际使用中，应该尽量规范使用这些标签。

-   **header:** 一个网页总要有个头，推荐都使用这个标签。
-   **nav:** 一般是目录或者导航菜单。
-   **section:** 一般是本网页的主体信息部分或者主页面——类似于GUI的主要显示窗口。
-   **article:** section下面的某一独立内容部分。
-   **aside:** 和网页主体信息不太相关的其他信息。
-   **footer:** 一般是关于作者，版权或者其他比如脚注等信息。

这些都可以通过div然后class或者id写法来取代，在实际使用中如果上面的默认标签能够满足需求，那么就应该使用html5的这些默认标签。

上面的例子已经出现了一些标签，然后还有一些很常用的标签，下面承接上面所将的继续补充写一个常用html标签清单。

## 常用html标签清单

-   **ul:** 不编号列表，也叫无序列表（Unordered list）。里面的item用 **li** 标签封装。
-   **ol:** 编号列表，也叫有序列表（Ordered list）。里面的item用 **li** 标签封装。
-   **h1,h2,h3 ...** 标题标签，数字表示各个标题的层级。
-   **p:** 段落标签。
-   **b:** 文字加粗
-   **i:** 文字斜体
-   **br** 换行
-   **hr** 水平线
-   **img** 加入图片，其中最常用的属性是 **src** ，指明具体图片引用地址。


### 建立一个链接

**a:** 引用链接标签，其中常用的属性是 `href` ，指明具体的引用地址，`title` 是悬浮的提示文字。

```
<a href="/where" title="go to where">show</a>
```

有的时候一个链接是用来下载文件的，你可以使用 `download`  属性来指定默认的保存文件名。

```
<a href="https://download.mozilla.org/?product=firefox-39.0-SSL&os=win&lang=en-US"
   download="firefox-39-installer.exe">
  Download Firefox 39 for Windows
</a>
```

如果连接有 `target="_blank" ` 属性，那么目标连接将会在浏览器新标签页打开。

创建一个电子邮箱链接：

```
<a href="mailto:nowhere@mozilla.org">Send email to nowhere</a>
```



## 文字强调的html5规范

按照html5提出的规范，并不推荐用 `<b>` 标签作为文字的强调用途（我一般使用的文字加粗是那个词提醒读者这个词需要特别记忆）。其推荐的是 `<em>` 标签作为一级强调，然后 `<strong>` 标签作为更进一步的强调。在默认样式中，`<em>` 是斜体，然后`<strong>`是粗体。显然html5的意思是将表达文字的样式这样的标签`<b><i>`尽可能不用直到废弃，然后对于文字强调都推荐使用`<em>`和`<strong>`标签。其设计思路是html完全成为一个描述文档内容结构的标签系统，而不带有任何内容表现形式的东西。还是推荐按照html5规范来，少用`<b>`标签和`<i>`标签。请参看 [这个网页](http://stackoverflow.com/questions/271743/whats-the-difference-between-b-and-strong-i-and-em) 的讨论。



## 注释

```html
<!-- Make me into a comment. -->
```

## 有序列表里面带无序列表

就是把无序列表嵌套进去即可。

```html
<ol>
    <li>ol li1</li>
    <li>ol li2</li>
    <ul>
        <li>ul li1</li>
        <li>ul li2</li>
    </ul>
</ol>
```

## table

table表格有时也可用于布局，不过不推荐这种风格，因为html标签应该尽可能是文本结构层而非表现形式层。一个完整的table模板如下所示:

```html
<table>
<caption>表格的标题用caption标签</caption>
<thead>
<tr><th>标签</th><th>fullname</th><th>说明</th></tr>
</thead>
<tbody>
<tr><td>tr</td><td>table row</td><td>表格中的一行</td></tr>
<tr><td>th</td><td>table head</td><td>表格的列名</td></tr>
<tr><td>td</td><td>table data</td><td>表格具体要展示的数据</td></tr>
</tbody>
</table>
```

<table>
<caption>表格的标题用caption标签</caption>
<thead>
<tr><th>标签</th><th>fullname</th><th>说明</th></tr>
</thead>
<tbody>
<tr><td>tr</td><td>table row</td><td>表格中的一行</td></tr>
<tr><td>th</td><td>table head</td><td>表格的列名</td></tr>
<tr><td>td</td><td>table data</td><td>表格具体要展示的数据</td></tr>
</tbody>
</table>


大体在html上画表格就如上所示了，其他一些更漂亮的表格制作都是通过css来完成的，这里先略过了。

## div和span

div（division）在html标记语言中主要是区块的意思。我们知道html页面要显示的元素就好比一个个盒子逐步排布下来，而 `div` 可以看作一个这样自定义的盒子。html中有两种显示风格的盒子，一种是块状区块，比如p段落标签；还有一种是inline盒子，比如说em标签，其不会换行。

div标签更确切的表达是块状区块，可以看作其display属性是 `block` （但不一定，不过推荐接受这样的设定）；此外还有所谓的inline区块，用 `span` 标签来表示这样的元素，可以理解为改标签元素的display属性是 `inline` 。

## inline css

最基本的css属性可以通过inline css模式直接在html标签中通过 **style** 属性来加上。

### font-size

字体大小

```html
<p style="font-size:12pt">paragraph</p>
```

### color

字体颜色， 这是css支持的 [color关键词清单](http://www.w3.org/TR/css3-color/#svg-color) 。

```html
<h2 style="color:green">paragraph</h2>
```

### font-family

字族， 这是css一般支持的 [字族信息](http://www.w3.org/TR/CSS21/fonts.html#generic-font-families) 。

```html
<ol>
    <li style="font-family:Arial">Arial</li>
</ol>
```

一般有文字的标签都可以用上面的三个属性来控制其内文字的大小，颜色和字族。虽然现在都推荐用css来控制，但思路顺序应该是优先inline css，太过普遍多次出现的情况下才考虑单独css控制。

### background-color

背景颜色。如果读者熟悉LaTeX排版系统的，那么我们都清楚LaTeX排版很核心的一个概念就是盒子。在html这里，我们似乎也可以把一个个标签看作一个个排版用的盒子。然后这里的background-color就是控制这一个盒子的背景颜色。

```html
<body style="background-color:yellow">
</body>
```

### text-align

文字在标签盒子里的对齐方式。可选参数有: left, right, center。

```html
<h3 style="text-align:center">居中对齐的标题</h3>
```

## 外部css
有一种说法，是将放在html <head> 标签里面的css和具体外部的css文件引用区分开来，在我看来区别不大吧。然后网络上还有一种说法认为html <head> 标签里面应该多用id的css定义，而外部css文件应该只用class定义好做到普适性，在我看来也有点削足适履了。额，目前的国内网络环境大家都懂的，所以我喜欢少用css文件引用，尽量将一些css定义都放在 <head> 标签里面，就是为了加载快一点，至于其他，倒没什么特别好讲究的。不过在使用css定义前应该用class，只有觉得某些元素需要个别处理的时候才用id属性控制，我想这是没有问题的。

放在<head>标签里面的css大致如下格式引入进来:

```html
<style>
这里的格式和外部css文件格式完全一致
</style>
```

引入外部文件css如下:

```html
<link rel="stylesheet"  href="main.css" >
```

然后在外部css文件里面你还可以如下进一步引用其他的css文件:

```css
@import url("http://getbootstrap.com/dist/css/bootstrap.min.css");
```

这种引用语句后面的分号不太清楚是不是必须的，不太关心这个，没事就加上吧。参考了 [这个网页](http://stackoverflow.com/questions/147500/is-it-possible-to-include-one-css-file-in-another) 。



