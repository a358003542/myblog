Slug: html5-tutorial
Date: 20191018
Summary: 本文讨论了最基础的HTML知识，可作为学习html5的第一篇学习文章。


[TOC]

If you are a english reader, I recommend [this article](https://www.websiteplanet.com/blog/html-guide-beginners/ ) for your html5 starting point. 




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

这些都可以通过div来取代，在实际使用中如果上面的默认标签能够满足需求，那么就应该使用html5的这些默认标签。

上面的例子已经出现了一些标签，然后还有一些很常用的标签，下面承接上面所讲的继续补充说明一些常用html标签清单。

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

最基本的css属性可以通过inline css模式直接在html标签中通过 **style** 属性来加上。具体如下所示：

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
有一种说法，是将放在html `<head>` 标签里面的css和具体外部的css文件引用区分开来，在我看来区别不大吧。然后网络上还有一种说法认为html `<head>` 标签里面应该多用id的css定义，而外部css文件应该只用class定义好做到普适性，在我看来也有点削足适履了。

在具体使用的时候一个总的原则是一般推荐使用class，只有觉得某些元素需要个别处理的时候才用id属性控制。

放在`<head>` 标签里面的css大致如下格式引入进来:

```html
<style>
这里的格式和外部css文件格式完全一致
</style>
```

引入外部文件css如下:

```html
<link rel="stylesheet"  href="main.css" >
```

然后在外部css文件里面你还可以如下进一步引用其他的css文件【参考了 [这个网页](http://stackoverflow.com/questions/147500/is-it-possible-to-include-one-css-file-in-another) 。】:

```css
@import url("http://getbootstrap.com/dist/css/bootstrap.min.css");
```



## 设置背景图片
```
background-image:url("https://theurl/tothe/image.jpg");
```
### 设置背景图片位置

设置背景图片位置，可能的值有top，center，right，left，top，bottom等，如下所示:
```
top left
top center
top right
center left
center center
center right
bottom left
bottom center
bottom right
```
如果只给出一个值，则第二个值是默认值center。
```
background-position: center center;
```
### 设置背景图片是否重复

默认是repeat，如下设置为 `no-repeat` ，则背景图片不会重复以铺满整个背景了。

    background-repeat: no-repeat;

### 设置背景图片不随页面滚动

    background-attachment:fixed;

### 设置背景图片尺寸

如下设置为 `cover` ，则背景图片会拉伸到足够大，以覆盖整个区域，图片某些部位可能不会显示在背景中。

    background-size: cover;

如果设置为 `contain` ，则背景图片会拉伸至最大长度或最大宽度不超过背景为止。

此外还可以如下指定宽高比，下面是宽100px，高150px: 

    background-size:100px 150px;

## 设置背景颜色

这里是html各个标签盒子的背景颜色，而color设置的是里面字体的颜色。

    background-color:red;

## 控制文本大小写

如下所示，依次为: 大写，首字母大写，小写。
```
h1 {text-transform:uppercase}
h2 {text-transform:capitalize}
p {text-transform:lowercase}
```

## 边框画一个圆

这样边框就成为一个圆了。
```
<div style="border:1pt solid blue;border-radius:50%;width:100px;height:100px;margin:auto;"></div>
```

<div style="border:1pt solid blue;border-radius:50%;width:100px;height:100px;margin:auto;"></div>
## z-index属性

css中某个标签盒子设置z-index属性，将影响这些标签盒子的堆叠顺序。比如说如下将header标签的 `z-index` 属性设置为1，而其他的都不设置，则保证header网页头部分总是第一个先堆放。:
```
header{
z-index:1;
}
```

## 表单

之前并没有对html中的表单各个情况进行说明，这里详细说明之。这里所谓的表单是指 `form` 标签加上其内包含的 `input` 等元素。这些input元素构成了我们熟知的文本输入框，下拉列表，单选框，复选框等等。

```
<form>

<input> </input>

</form>

```

具体表单元素的类型由input标签的 `type` 元素定义，下面分别详细说明之:

### 单行文本输入

单行文本输入用input标签，type类型为 `text` ，然后具体说明文字推荐用 `label` 标签。

```html
<form>
<label>name:</label>
<input type="text" name="yourname"></input>
</form>
```

然后input的 `name` 属性很重要，其值具体对应该文本输入的值的变量名（比如python的wsgi机制就将其刷成 `form.yourname` 这样的引用）。

<form>
<label>name:</label>
<input type="text" name="yourname"></input>
</form>

### 多行文本输入

多行文本输入使用 `textarea` 标签生成的，现在先简单了解下即可。

```html
<textarea rows="5">
the textarea you say something
</textarea>
```

<textarea rows="5">
the textarea you say something
</textarea>

### 加上action

也就是表单form标签上加上action属性，然后表单内定义submit的按钮或者input元素，点击之后将会将数据发送给action那边去，具体方法由method属性定义，默认是GET。

```html
<form action="/where" method="POST">
  <input type="text">
  <button type="submit">submit</button>
</form>
```

### required

加上requird属性，该字段必须填上值。

```html
<input type="text" required>
```

### placeholder

预显示的文字

```html
<input type="text" placeholder="input your name" required>
```

### 按钮

html有好几种方法创建一个按钮，w3school不推荐button标签，而是推荐使用如下所示的input标签的形式:
```html
<form action="https://www.google.com" method="get">
<input type="submit" value="click to google"></input>
</form>
```

<form action="https://www.google.com" method="get">
<input type="submit" value="click to google"></input>
</form>

其 `value` 属性定义了具体按钮上显示的文字。然后具体跳转行为用form标签的 `action` 属性来定义，你还可以定义 `method` 属性来具体定义HTTP的method，比如下面是一个表单提交的例子:

```html
<form action="http://httpbin.org/post" method="post">
<label>name:</label>
<input type="text" name="name" />
<label>password:</label>
<input type="password" name="password" />
<input type="submit" value="提交" />
</form>
```

<form action="http://httpbin.org/post" method="post">
<label>name:</label>
<input type="text" name="name" />
<label>password:</label>
<input type="password" name="password" />
<input type="submit" value="提交" />
</form>

然后我们注意到上面还出现了一个新的type类型 `password` ，其类似单行文本输入，不同的是你是在输入密码，所以不会在屏幕上显示出来。



#### 重置按钮

```
   <input type="reset" value="重置"  />
```

这个按钮将会将表单所有内容清空。



#### 单选按钮

```html
<form action="http://httpbin.org/get" method="get">
<label>Male</label>
<input type="radio" name="Sex" value="Male" checked="checked" />
<label>Female</label>
<input type="radio" name="Sex" value="Female" />
<input type ="submit" value ="提交">
</form>
```

<form action="http://httpbin.org/get" method="get">
<label>Male</label>
<input type="radio" name="Sex" value="Male" checked="checked" />
<label>Female</label>
<input type="radio" name="Sex" value="Female" />
<input type ="submit" value ="提交">
</form>

上面新出现的 `checked` ，默认单选按钮和下面的复选按钮是没有选中的，而设置成为 "checked" 则默认为选中了。

#### 复选按钮

```html
<form action="http://httpbin.org/get" method="get">
<p>你喜欢吃的水果:</p>
<label>apple</label><input type="checkbox" name="fruits" value="apple"/>
<label>banana</label><input type="checkbox" name="fruits" value="banana" />
<label>pear</label><input type="checkbox" name="fruits" value="pear" />
<input type="submit" value="提交" />
</form>


```

<form action="http://httpbin.org/get" method="get">
<p>你喜欢吃的水果:</p>
<label>apple</label><input type="checkbox" name="fruits" value="apple"/>
<label>banana</label><input type="checkbox" name="fruits" value="banana" />
<label>pear</label><input type="checkbox" name="fruits" value="pear" />
<input type="submit" value="提交" />
</form>



### label标签

标签用户说明输入框的一些内容，但还有一个用途，改进鼠标用户的可用性，如果用户点击标签，那么将会聚焦到目标表单对象上，只需要我们如下设置：

```
<label for="控件id名称">
<input id="控件id名称"
```





## 响应式布局

提示：现在推荐使用bootstrap来进行响应式设计，下面的内容有助于我们来理解bootstrap内部是如何实现响应式布局的。

请读者先阅读 [这篇文章](http://www.ruanyifeng.com/blog/2012/05/responsive_web_design.html) 。这篇刚开始 Ethan Marccote 给出的那个例子有个非常重要的信息，那就是设备的像素分级:

- 大于1300像素
- 600到1300像素
- 400到600像素
- 小于400像素

这个像素分级可以为后面我们要根据不同的设备进行css进行设置提供了参考。

然后一般网页都要加上这一行:

```
<meta name="viewport" content="width=device-width, initial-scale=1" />
```

意思是网页默认宽度为设备宽度，原始缩放比为1。

然后就是各个元素宽度最好不要有 `width: xxx px` 这样写死了的css设置，而是 `%` 或者 `auto` 。字体的大小也都推荐使用 `em` 这样的相对大小。

h1 默认大小是 1.5em 。
```
h1 {
  font-size: 1.5em;
}
```
small 默认是 0.875em 。
```
small {
  font-size: 0.875em;
}
```
流动式布局，各个区块的位置都是浮动的，有些情况下会需要使用 `position: absolute` ，这会带来很多麻烦，尽量少用。

根据屏幕响应式多个css配置适应: 【因为css有很多通用配置是多设备皆适用的，下面这些根据屏幕响应的css应该放在css文件的最后面。】

参看 [这篇文章](http://learn.shayhowe.com/advanced-html-css/responsive-web-design/) ，其提到了现在流行的 mobile-first 设计思路，也就是有限照顾手机小屏幕设备的设计流程。先写好通用css配置，然后css文件最后面如下设置这些屏幕响应css设置。从最小的屏幕照顾起:

```css
@media screen and (min-width: 400px) {}
@media screen and (min-width:600px){}
@media screen and (min-width:1000px){}
@media screen and (min-width:1400px){}
```

这里 min-width 是指设备宽度至少要大于那个值，此外还有 max-width 是指设置宽度要小于那个值。上面的例子，假设设备750px，那么第一个第二个配置都满足，但因为css覆盖配置，后面如果你定制了那么将生效后面的，这就是先调手机端的mobile-first思路。

图片的自适应，如下设置最大宽度。

```
img { max-width: 100%;}
```


## no-js class
```
<html class="no-js" lang="zh">
```
他们说这个class可以用来设置某些情况下javascript被禁用之后的css。

## 基本写法

前面谈到的inline css因为肯定是作用于本标签，所以写法就简化了，style引入之后后面加入一些属性即可。然后前面谈到的外部css，其写法都是如下所示:

```css
p{
text-indent:2em;/*段落缩进*/
line-height:180%;/*行间距*/
}
```

第一个元素我们可以简单称之为css选择器，在网络抓取中也有类似的概念。然后花括号里面就是类似 inline css 一样的格式了，用分号隔开，换行不换行都是无所谓的，具体为了美观一般都一个属性占一行吧。

## css选择器

这里以html5为例，html5内置的标签都是可以直接引用的，比如body，article，video，table，figure等等。如果你在css中引用section，那么意思就是整个文档的section标签那些元素被选中了。

我们知道html5中可以通过 **class** 属性来将某个元素归于某一类，现在假设有:
```html
<p class="emph">hello</p>
```
那么我们使用 `p.emph` 其意思就是将选中p标签然后class属性为emph的那些标签。

我们在css中经常看到这样的形式：

```html
.hightlight
```

其完整形式为 `*.hightlight` ，也就是所有class属性为hightlight的元素都将被选中。

然后id属性可用来定义某个标签的唯一id，一般就用 `#idname` 选中那个标签即可。



### 子选择器

  `h1 > strong` ，其只严格选择h1标签下遇到的**第一个**strong标签，这里的下是严格意义上的父子标签包含关系的下，如果某个strong标签在em标签里面，然后这个em标签在h1标签里面，则该strong元素是不会被这里所谓的严格逐级选择选中的。

### 后代选择器

 `figure p` 其选择的就是所有figure标签元素里面的 **所有** p标签元素。前面谈及的那些标签元素表示方法你都可以用的，比如 `#footer .emph` 选择的就是id为footer的那个标签里面class属性为emph的标签。



更多css选择信息请参看w3school的 [css元素选择详解部分](http://www.w3school.com.cn/css/css_selector_type.asp) ，但这一块最好不要弄得太复杂。实际上这样的选择逻辑弄得越复杂后面css代码的维护就越困难，最好的实践还是用 **class** 和 **id** 来管理各个css属性。

### 带上其他属性选择

有href属性的a标签才应用样式:
```
a[href] {color:red;}
```
有href属性和title属性的a标签才应用样式:
```
a[href][title] {color:red;}
```
具体属性是什么值也指定了:
```
a[href="http://www.w3school.com.cn/about_us.asp"] {color: red;}
```
### 伪类选定

带个:冒号后面跟着该标签的伪类，主要是值该标签的某种特殊状态，最常见的是a标签的各个状态，如下所示:
```
a:link {color: #FF0000} /* 未访问的链接 */
a:visited {color: #00FF00} /* 已访问的链接 */
a:hover {color: #FF00FF} /* 鼠标移动到链接上 */
a:active {color: #0000FF} /* 选定的链接 */
```
#### first-child伪类
```
p:first-child {
color: red;
}
```
只有是父标签的第一个子标签元素才会被选定。

#### nth-child伪类
```
p:nth-child(2) {
color: red;
}
```
是父标签的第几个子标签元素才会被选定。

### css选择权值

如果某个标签被多个css语句选定，那么具体权值如下：

```
标签权值为1 子选择器和后代选择器两个标签的1+1=2 类选择器权值为10 id选择器权值为100
```

### css样式层叠优先级

内联样式 > 嵌入样式 > 外部样式

## !important 用法

css设置有时不可避免会发生样式重叠覆盖，当然一般是尽可能统一css设置，但有时嫌麻烦懒得弄了，你可以用 `!important` 来手工提高某个css设置的优先级(参考了 [这个网页](http://www.cnblogs.com/qieqing/articles/1224085.html) 。)。如下所示：

```css
table, th, td
{
margin:0 auto;
min-width:2em;
text-align:center !important ;
padding: 5px;
}
```

上面严格控制表格各项都居中对齐。

## css的长度单位

css有很多长度单位，这些单位如果你熟悉 \(\LaTeX\) 的话你就会对这些单位很眼熟。其中绝对长度单位有：1in = 2.54cm = 25.4mm = 72pt = 6pc ，这些并不推荐使用。[这篇网页](http://www.w3.org/Style/Examples/007/units.en.html) 推荐多使用 `px` ， `em` 和 `%` 这样的长度单位。其中"px"和"%"是css特有的，其会根据显示屏而变动，然后1em我们知道就是当前字体M的宽度（TeX里面的情况）。其中px值得引起我们的注意，其会根据显示设备而有很好的调整，更多信息请参看上面提到的那个参考网页。

## css的盒子模型

html的显示布局和 \(TeX\) 的显示布局一样也是采用的浮动盒子模型，从上到下，从左到右，一个个盒子排下来，只是 \(TeX\) 更复杂，还有一个分页算法。简言之就是每一个标签元素都是一个盒子(我还不太确定一个个字是不是一个盒子，在 \(TeX\) 里面一个个字都是一个盒子。) 。

下面这个图片来自 [这个网页](http://www.hicksdesign.co.uk/boxmodel/) 。

![img]({static}/images/前端开发/html_box_model.png "html_box_model")


[这篇文章](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Box_Model/Introduction_to_the_CSS_box_model) 讲解得很好，下面简要介绍之，下面放在短代码环境的都是可以用作css属性的。盒子最中心的是content区域，如果该盒子的 `box-sizing` 是默认值的话，那么 `width` 控制的就是content区域的宽度。如果将 `box-sizing` 设置为 `border-box` ，那么 `width` 对应的就是整个盒子的宽度。这个只是一点简单的数学加减法把戏罢了，没什么大不了的。

然后类似的 `height` 默认是控制content区域的高度，然后有 `min-width` , `min-height` 来控制盒子content区域的最小宽度和最小高度，然后有 `max-width` , `max-height` 来控制盒子content区域的最大宽度和最大高度，类似的这几个属性如果 `box-sizing` 设置为 `border-box` ，那么对应的都是整个盒子的宽度或高度。

content区域外围是padding区域，padding区域是透明的，如果整个盒子设置 `background-color` 或 `backgroud-image` ，这是你会看到他们。padding区域有如下属性来控制上面下面左边右边的长度: `padding-top` , `padding-bottom` , `padding-left` , `padding-right` 。 还有一个简便的写法 `padding` ，这种写法设置一个值控制上面四个量还是很方便的，但其还可以接多个值，有一定顺序，不太喜欢这种用法。

padding区域外面是border区域，通常我们在网页中看到的一条条边框线就是它了， 用 `border-width` 来控制边框线的宽度。这实际上是一个简写，类似上面的 `padding` ，可以跟四个值:

上，右，下，左:
```
border-width: 1px 2em 0 4rem;
```
或者三个值:

上，右和左，下:
```
border-width: 1px 2em 1.5cm;
```
或者两个值:

上下，左右:
```
border-width: 2px 1.5em;
```
此外还有: `border-top-width` 对应上宽度， `border-bottom-width` 等。

border区域外面就是margin边距区域。其有如下属性，含义大家一看应该就明白了: `margin-top` , `margin-bottom` , `margin-left` , `margin-right` , `margin` 。

### border属性

border属性可以跟上三个值，分别是: border-width border-style border-color
```
img {
border: 1px solid #4682b4
}
```
border-style情况比较多，常见的有 **solid** 实线 **dashed** 虚线 **double** 双线 **dotted** 点线等，更多请参看 [这个网页](http://www.w3school.com.cn/cssref/pr_border-style.asp) 。

## css布局

这个网站专门介绍 [css布局](http://zh.learnlayout.com/) ，深入浅出讲的还是很好的，css布局是css里面很重要的课题，建立认真学习一下。

### display属性

#### block

块级元素，占满自身右边所有行的行空间。 div元素和p默认就是所谓的block元素，display属性为 **block** 。
```css
display:block;
```
#### inline

span元素默认是 **inline** 。
```css
display:inline;
```
就占据我需要的宽度，其他盒子元素可以继续填满这一行。

比如:
```css
li{
    display:inline;
}
```
这样你的无序列表和有序列表的各个item不会另起一行了。其默认的是 `display:list-item;` 。

#### inline-block

inline-block的意思是块级元素还是块级元素，只是几个块级元素对外排布是 inline 模式排布的，这是css较新的一个特性。如果对块状元素设置display属性为 **inline** ，则这些块状元素都会失去自己内部的尺寸布局，这可能不是你想要的。

#### none
```css
display:none
```
该元素不会显示。和 `visibility:hidden` 的区别是其本该显示的空间不会保留了。

### float属性

元素居右放置
```
float:right;
```
### clear属性

两侧都不能出现浮动元素
```
clear:both;
```
### position属性

css布局控制中，positon是一个很关键的属性。参考了 [这个网页](http://zh.learnlayout.com/position.html) 和 [这个网页](http://www.cnblogs.com/polk6/p/3214847.html) 。position属性有如下四个值可以设置:

#### static

static是默认值，没有什么其他额外的位置调整行为，表示它不会被"positioned"。

#### relative

relative和static类似，除非你还有其他的属性设置。比如 `top` , `right` , `bottom` , `left` 这些属性来调整，具体相对的含义是相对于原本它应该在的地方。相对调整之后留下来的地方会被保留下来，没有后续处理动作了。

#### fixed

fixed的应用就是将某个元素总是显示在页面上，比如说某些弹窗广告。 `top` , `right` , `bottom` , `left` 这些属性可以辅助来调整这个弹窗具体的位置。

#### absolute

absolute类似于fixed，不过其不是相对于视窗固定，而是相对于页面固定。比如下面这个aside设置:

```html
aside {
margin-left: -200px;
width: 181px;
position: absolute;
background-color:#FDF6E3;
}
```

这个aside是个目录，就放在正文的左边的，如果不用absolute布局的话，右边空间就不会释放出来。请参看 [这个网页的那个nav标签元素](http://zh.learnlayout.com/position-example.html) 。



## bootstrap

本文点到为止讲解一下，读者简单了解即可，具体还是要自己练手来学习。

## 安装

本文是如下加载的：
```
<!-- 最新版本的 Bootstrap 核心 CSS 文件 -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

<!-- 可选的 Bootstrap 主题文件（一般不用引入） -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">

<!-- 最新的 Bootstrap 核心 JavaScript 文件 -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
```


<!-- 最新版本的 Bootstrap 核心 CSS 文件 -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

<!-- 可选的 Bootstrap 主题文件（一般不用引入） -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">

<!-- 最新的 Bootstrap 核心 JavaScript 文件 -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
## viewport元数据声明

为了确保适当的绘制和触屏缩放，需要加上如下viewport元数据声明:
```
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
```
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

## container类

通过container class的 `div` 来获得一个固定宽度的响应式容器。
```
<div class="container" style="background:#FFF0F5">
我在container类里面。
</div>
```
<div class="container" style="background:#FFF0F5">
我在container类里面。
</div>
## 栅格系统

栅格系统是bootstrap框架里面很有用的一个特性了，其基本思路如下:

1. 每一行 `row` 类都放在上面谈及的 `container` 类里面。
2. 然后在每一行row类里面（这里所谓的什么类实际上就是该类属性的div盒子）再添加行类。

具体行类有很多种，请参看 [这个网页](http://getbootstrap.com/examples/grid/) 和官方文档的 [这里](http://getbootstrap.com/css/#grid) 来具体设计之。

```html
<div class="container" style="background:#FFF0F5">
我在container类里面。
<div class="row" style="background-color:yellow">
<div class="col-md-8" style="background-color:red">
我在col-md-8盒子里面，黄色是row盒子。
</div>
<div class="col-md-4" style="background-color:blue">
我在col-md-4盒子里面，8+4=12，bootstrap最多12列。
</div>
</div>
</div>
```

<div class="container" style="background:#FFF0F5">
我在container类里面。
<div class="row" style="background-color:yellow">
<div class="col-md-8" style="background-color:red">
我在col-md-8盒子里面，黄色是row盒子。
</div>
<div class="col-md-4" style="background-color:blue">
我在col-md-4盒子里面，8+4=12，bootstrap最多12列。
</div>
</div>
</div>

## 其他常规css设置

其他常规css设置比如说h1-h6字体大小啊，等等其他常规标签的字体大小啊颜色啊代码背景的设置啊等等，这些都可以通过浏览器的开发者工具来查看具体的css代码设置，如果觉得默认设置不好则另外再弄个css文件重载也是可以的，这些就不多说了。


bootstrap提供了 `text-lowercase` , `text-uppercase` , `text-capitalize` class:
```
<p class="text-lowercase">HELLO world</p>
<p class="text-uppercase">hello world</p>
<p class="text-capitalize">hello world</p>
```

<p class="text-lowercase">HELLO world</p>
<p class="text-uppercase">hello world</p>
<p class="text-capitalize">hello world</p>
## 控制文本对齐方式
主要作用于p段落盒子的属性支持: <strong>text-left</strong> ,  <strong>text-center</strong> ,  <strong>text-right</strong> ,  <strong>text-justify</strong> , <strong>text-nowrap</strong> 。

具体这些css都很简单:
```
<pre class="pre-scrollable">
    .text-left {
  text-align: left;
}
.text-right {
  text-align: right;
}
.text-center {
  text-align: center;
}
.text-justify {
  text-align: justify;
}
.text-nowrap {
  white-space: nowrap;
}
</pre>
```





## lead盒子

后面都如此约定，所谓的 **lead盒子** 是指class属性为lead的div标签，即:
```html
<div class="lead" style="border:1px solid">
hi ，我在lead盒子里面，边框是额外加上去的。可以用来作为某个特别重要的话的强调。
</div>
```

<div class="lead" style="border:1px solid">
hi ，我在lead盒子里面，边框是额外加上去的。可以用来作为某个特别重要的话的强调。
</div>

## jumbotron盒子
bootstrap提供的jumbotron盒子一般在首页用于展示某个特别重要希望读者阅读的信息。

```html
<div class="jumbotron">
<p>大家好，我在jumbotron盒子里面。</p>
</div>
```

<div class="jumbotron">
<p>大家好，我在jumbotron盒子里面。</p>
</div>



## pull-left和pull-right

bootstrap用这个class属性来左对齐或右对齐某个标签元素。

## tabs的制作

利用bootstrap制作tabs，就是建立一个ul无序列表，然后class属性设置为 **nav nav-tabs** ，这样就制作了一个简单的tabs了。

```html
<ul class="nav nav-tabs">
<li class="active"><a href="#">Features</a></li>
<li><a href="#">Details</a></li>
</ul>
```

<ul class="nav nav-tabs">
<li class="active"><a href="#">Features</a></li>
<li><a href="#">Details</a></li>
</ul>

## pill形状tabs制作
```html
<ul class="nav nav-pills">
<li class="active"><a href="#">Features</a></li>
<li><a href="#">Details</a></li>
</ul>
```

<ul class="nav nav-pills">
<li class="active"><a href="#">Features</a></li>
<li><a href="#">Details</a></li>
</ul>

## list-inline

给ul或ol加上 <strong>list-inline</strong> 属性，来是li列表元素水平inline-block显示，如下所示:
<ul class="list-inline">
<li>第一个li</li>
<li>第二个li</li>
</ul>

## kbd标签

kbd标签用来显示按键组合: <kbd>Ctrl+X</kbd>



## 如何制作一个 `Bootstrap` 风格的带链接的按钮

bootstrap用默认的button来制作标签，如果你需要点击动作的还需要额外的onclick去定制，如果你需要的动作仅仅只是打开某个网页，那么使用a标签会更合适一些，只是我们还需要这个a标签看上去像一个按钮，这样会好看一些，参看 [这个网页](http://stackoverflow.com/questions/19981949/how-to-make-a-button-in-bootstrap-look-like-a-normal-link-in-nav-tabs) ，具体代码如下所示：

```
<a href="https://www.bing.com" target="_blank" role="button" class="btn btn-success btn-large">Click here!</a>
```
<a href="https://www.bing.com" target="_blank" role="button" class="btn btn-success btn-large">Click here!</a>

## 前言

本文在行文上是假设读者已经掌握了一门编程语言了的，所以一些基本的编程语言方面的概念不会做过多的讨论。

javascript就历史起源来说似乎并不是一个主角命，更像是编程语言世界里面一个注定跑跑龙套的。1995年某个公司开发了某个浏览器，然后该公司需要为这个浏览器开发一个脚本语言，就把这个任务丢给了 Brendan Eich ，Brendan Eich很不情愿地接受了这个不喜欢的任务，大概花了10天时间仓促完成了Javascript的设计，而且javascript最开始名字不叫javascript，叫livescript，就连javascript这个名字后面改也有点蹭Java语言的热度的嫌疑。

后面javascript的流行和大热可能是其创始人也料想不到的，实际上就是javascript后面刚发展起来的那几年，大家也只是觉得其主要作为一个前端脚本语言，对其仍然是一种轻视的态度，觉得这个语言也就写写浏览器界面的动态效果之类的。随着node.js的出现和相关生态圈的日益成熟壮大，人们才惊讶地发现javascript已经是编程世界里面最大热的几门语言之一了，继而近几年，随着javascript生态的不断成熟和壮大，再也没有人去质疑javascript作为当今编程世界里面的编程语言的主角地位了，最多只是碎碎念说几句javascript这个语言的一些问题。

## 注释

多行注释推荐如下写法：

```javascript
/**
 * make() returns a new element
 * based on the passed-in tag name
 */
```

单行注释用 `//` ，然后注释都新起一行写，如果是代码块内的注释，则前面空一行：

```js
// This is a comment that the computer will ignore. 

function getType() {
  console.log('fetching type...');

  // set the default type to 'no type'
  const type = this.type || 'no type';

  return type;
}
```

然后就是注释文字具体内容要和注释符号空一空格。



## javascript代码放在那里

javascript的代码一般推荐是放在HTML文档最后面， `</body>` 标签之前，这样能够让浏览器更快地加载页面。至于其他倒没有特别的要求，刚开始简单的javascript代码就直接写上去也是可以的:
```html
<script>
your awesome javascript code
</script>
```
如果javascript代码量有一点了那么当然还是推荐另外单独放在一个js文件上，然后如下引入进来:
```html
<script src="where"></script>
```

## javascript代码REPL环境

你可以在浏览器的debug控制台上运行javascript代码，或者安装node环境之后进入node命令下的REPL环境。

## 程序中的操作对象

### 简介

javascirpt的数据类型分为两类，一类是原始类型：数值、字符串和布尔值；另一类是对象类型。此外javascript还有两个特殊的值：`null` 和 `undefined` 。javascript除了数值、字符串、布尔值、null、undefined之外就都是对象了。比如后面提到的数组，函数也都是对象，只不过其是javascipt内部定义的对象。

### 声明常量和变量

javascript的变量是区分大小写的。

javascript可以利用关键词 `var` ， `const` 和 `let` 来声明变量或常量，其中const是声明常量的，var和let是声明变量的。var声明变量是大家在javascript中常用的声明变量关键词，其声明的变量的作用域很不同于其他编程语言，叫做 **函数作用域** 。即你在函数区块内声明的变量整个函数体都是可以使用的，包括哪些花括号结构或任意的嵌套函数。因为程序员对于变量的作用域习惯了块作用域，所以airbnb规范提出不推荐使用 `var` ，而是推荐使用 `let`，因为 `const` 和 `let` 都是块作用域（block-scoped）。

参考mozilla上的相关讨论，变量作用域显得另类是一方面，更糟糕的是因为这个作用域会让变量声明语句可以随意放置，这会造成代码变得混乱和难以理解。**现代javascript编码推荐使用let，最好不用var**。

我们可能会看到某些javascript代码直接写上 `x=1` ，前面没有写上关键词，严格意义上来说这不叫声明变量，而是在全局对象上挂载了x这个属性，从编码规范来说是应该抵制这种写法的。

### 全局变量

在网页中有个全局对象 `window` ，所以我们可以把一些全局变量挂在 `window` 对象里面。

### 数值(number)

**javascript不区分整数值和浮点数值**，javascript中所有数字都用浮点数值表示，这是javascript和其他编程语言的很大不同。然后数值型那些运算，比如加减乘除之类的就不用多说了。其中 `%` 和python一样也是求余操作。在python3中有 `5//2` 是求商的概念，javascript没有这个概念，我们需要如下来获得类似的效果。

```
parseInt(5/2)
```

#### parseInt()

将字符串转成整数型。

```js
> parseInt('2.5')
2
```

### NaN

如果我们执行 `parseInt('abc')` ，那么将返回 `NaN` ，判断是否是NaN如下所示：

```js
> Number.isNaN('a')
false
> Number.isNaN(1)
false
> Number.isNaN(NaN)
true
```

**注意：** javascript还有一个全局函数`isNaN` ，其和Number.isNaN行为不太一样，一般推荐使用 `Number.isNaN` 。Number.isNaN意思很明显就是判断是否是NaN这个值，而全局的isNaN更像是在说输入的这个东西是不是一个数值或者能不能转成一个数值，true则不能，false则能。

### 字符串(string)

javascript同python一样单引号和双引号都是可以的。

```javascript
const name = 'Capt. Janeway';
```

你可以通过 `+` 来实现一些简单的字符串拼接工作，也可以如下进行字符串模板操作。

```javascript
`How are you, ${name}?`
```

javascript的字符串类型和python非常类似，比如 `string[0]` 是支持的。然后不可以这样用string[0:2]，幸运的是javascript提供了类似python中的那种切片概念，就是使用 `slice` 方法

```
> "hello".slice(0,2)
'he'
> [1,3,4,5].slice(0,2)
[ 1, 3 ]
```

不过javascript的slice方法和python的切片操作还是有点区别的，其只有 `(start,end)` 两个参数，然后其也有负数从末尾算起的概念，具体请参看 [这里](http://www.w3school.com.cn/jsref/jsref_slice_string.asp) 。



#### 字符串的一些方法

-   **length:** 字符串长度
-   **toUpperCase:** 变成大写
-   **toLowerCase:** 变成小写
-   **indexOf:** 返回子字符串出现的索引位置，index索引编号规则和python相同。
-   **substring:** 返回子字符串，如果熟悉python的那种切片规则的话，那么推荐就直接使用 `slice` 方法。
-   **replace:** 替换操作 
-   **split:**  分割操作

#### toString方法

javascript的数值、布尔值、对象和字符串都有一个 `toString` 方法，大体类似于python的 `str` 函数。自己定义的对象也可以加上 `toString` 方法：

```js
class Jedi {
  constructor(options = {}) {
    this.name = options.name || 'no name';
  }

  getName() {
    return this.name;
  }

  toString() {
    return `Jedi - ${this.getName()}`;
  }
}
```

### 布尔值(boolean)

javascript的布尔值是 `true` 和 `false` 。在进行比较判断操作时，如果你是希望比较值的话，类似python的比较判断 `==` 符号，在javascript中对应的是 `===` 。三个等号，这不是什么别出心裁，也没有任何实际的好处，就是javascript的历史遗留问题罢了。
```
=== Equal to
!== Not equal to
```
boolean值的判断遵循以下规则：

1.  `false` `0`  空字符串 `""`  `NaN`  `null`  `undefined` 都被视作false
2.  其他都被视作true

```js
> Boolean({})
true
```

### null

javascript的 `null` 。其是一个特殊值。类似于python的 `None` ，然后还有一个什么 `undefined` 。比如函数没有明确return值就会默认返回 `undefined` ，感兴趣的可能查一下这两个的区别，我看了一下，觉得挺无聊的。上面谈到 `==` 和 `===` 的区别，如果用 `===` ，则 `undefined` 是不等于 `null` 的，如果用 `==` ，则javascript会额外做一些类型转换工作，这两个又会看作相等的。

ECMA-262 规定：

```
null == undefined; -> return true
```

比较操作的时候一律推荐使用 `===`  和 `!==`  ，而不要使用 `==` 和 `!=` 。



### typeof操作符

查看某个对象的对象类型，typeof操作符只可能返回以下六种结果：

-   number
-   string
-   object
    -   function
    -   array
    -   date
    -   regexp
-   boolean
-   null
-   undefined
-   symbol (new in es6)

```javascript
typeof x
"undefined"
typeof 1
"number"
```



### 数组

javascript的数组（array）在数据结构概念上大体类似于python的列表。

#### 构建一个数组

```js
var array1 = [];
var array2 = new Array();
const items = [1, 2, 3.14, 'Hello', null, true];
```

其索引index编号法则也和python一致。

#### 数组的一些方法

- **length:** 数组长度
- **indexOf:** 返回数组某个子元素的索引位置
- **slice:** 切片操作，类似于python的 `lst[0:2]` 那种表达方法。slice方法不接受参数就默认返回该列表所有引用，也就是通常所说的 *浅拷贝* 。浅拷贝简单来说就是复制一个字典或者数组（或者其他复杂对象），根据第一层key赋值第一层value，如果第一层key是另外一个对象的引用，那么拷贝前对象和拷贝后对象都会指向统一对象，深拷贝就是进一步深入递归拷贝。
- **push:** 末尾添加一个元素
- **pop:** 最后一个元素删除
- **unshift:** 数组头部添加一个或多个元素，返回新数组的长度
- **shift:** 数组头部删除一个元素
- **sort:** 排序，破坏型。值得一提的是对于数字排序并不是按照从大到小的顺序来的，不太清楚为何:

```
> var lst = [1,5,2,3,51,4,45,545,541,48,77]
> undefined
> lst.sort()
> [ 1,
> 2,
> 3,
> 4,
> 45,
> 48,
> 5,
> 51,
> 541,
> 545,
> 77 ]
```

在python中最多说字符串就这样，但这里是number类型啊。然后要正常排序，我们需要如下操作（参看 [这个网页](http://www.w3school.com.cn/jsref/jsref_sort.asp) ）:

```js
var lst = [1,5,2,3,51,4,45,545,541,48,77]
function sortNumber(a,b){
return a - b
}
lst.sort(sortNumber)
alert(lst)
```

这里sort方法接受一个函数参数，这个函数接受两个参量，用来判断a和b的值大小，如果返回值小于0，则a放在前面。如果返回值大于0，则a放在后面。这种排序方法也支持数字字符串的情况。javascript在处理这种 `字符串 - 字符串` 的情况是会尝试做转换成number类型的才做。

- **reverse:** 反转，破坏型。
- **splice:** 从指定的索引删除某些元素，然后在此处添加某些元素，相当于update更新了。

```js
> var arr = ['Microsoft', 'Apple', 'Yahoo', 'AOL', 'Excite', 'Oracle'];
> undefined
> arr.splice(2, 3, 'Google', 'Facebook');
> ["Yahoo", "AOL", "Excite"]
> arr
> ["Microsoft", "Apple", "Google", "Facebook", "Oracle"]
```

参数意思是从索引2开始删除3个元素，然后添加后面的元素。从上面的例子可以看出splice方法是破坏型的方法，然后其返回的是删除了的那是那个元素。

splice方法也可以用于只删除不添加也就是纯删除操作，或只添加不删除的纯添加操作。

```
// 只删除,不添加:
arr.splice(2, 2);
// 只添加,不删除:
arr.splice(2, 0, 'Google', 'Facebook');
```

- **concat:** 连接两个数组，非破坏型。

```
> var lst1 = [1,2,3]
> undefined
> var lst2 = ['a','b','c']
> undefined
> lst1.concat(lst2)
> [1, 2, 3, "a", "b", "c"]
```

- **join:** 类似于python字符串的join方法，如下所示:

```
var arr = ['A', 'B', 'C', 1, 2, 3];
arr.join('-'); // 'A-B-C-1-2-3'
```

-   **fill:** 数组用某个值来填充

#### for遍历数组

```js
for (let value of array) {
  // do something with value
}
```

遍历数组还可以这样：

```js
> a = ['a', 'b', 'c']
< a.forEach(function(value, index){
    console.log(value, index);
});
> a 0
> b 1
> c 2
```

这大体实现了类似于python的 `enumerate` 写法。上面的forEach方法后面跟着的函数也可以只接受一个value参数。

#### 判断某个元素是否在数组中

```
['a','b'].indexOf('a')
```

如果返回 `-1` 则该元素不在数组中，否则在数组中。

```js
function is_in_array(array, element){
    if (array.indexOf(element) === -1){
        return false
    }else{
        return true
    }
}
```

#### map和filter和reduce

这三个函数是函数编程很重要的几个函数，在数组对象里面可以直接调用这些方法：

```
a.map(function)
```





### 对象

对象是一个整合了数据和函数的集合。

```javascript
> let x = {}
undefined
> x = {'a':1}
{ a: 1 }
```

下面演示了对象如何整合函数（或者叫做方法）的例子：

```javascript
let x= {
  'data': [1,2,3,4],
  'length': function(){return this.data.length}
}

console.log(x.length())
```

我们大概能够猜测出一些javascript底层如何实现的细节，但这对于目前阶段学习和使用这个编程语言来说是没有裨益的。前面在介绍typeof的时候提到数组，函数都是对象。

新建一个数组的完整写法是： `new Array()` ；新建一个对象的完整写法是：`new Object()` 。新建一个类的写法如下所示：

```javascript
class Rectangle {
  constructor(height, width) {
    this.height = height;
    this.width = width;
  }
}

let p = new Rectangle();
```

因为后面有class这样的概念，我是推荐将这些出现的对象看作类似python中字典的概念，一个键值对映射集合。从编程概念上讲也是需要这样一个数据类型的。然后数组，这里的对象，函数，用户自定义的类等用typeof去查看都是object，他们都属于object。这个object是否就是这里的Object，从实现层面上我还不大确切，但这不是重点，就算是，从编程概念上来说也是应该有所区分的。一个是实用的数据类型，一个是很抽象的面向对象编程概念上的底层表述。

#### 对象的原型

JavaScript的对象大多有一个原型对象，其从原型继承属性。可以通过 `Object.prototype` 来引用该对象的原型对象。

要检测一个对象是否是另外一个对象的原型可以使用 `isPrototypeOf` 方法：

```
p.isPrototypeOf(o) // if true then the p is the o's prototype.
```



#### in语句

判断某个对象时候有某个键。

```js
'name' in xiaoming;

> var d = {}
undefined
> d['a'] = 1
1
> d
Object {a: 1}
> 'a' in d
true
> 1 in [1,2,3]
true
```

#### delete语句

其对应的就是python的del语句。然后我们看到javascript的 `delete` 语句删除不存在键也不会报错。

```js
> d
Object {a: 1}
> delete(d.b)
true
> d
Object {a: 1}
> delete(d.a)
true
> d
Object {}
```

#### hasOwnProperty方法

对应于python2的has\_key方法，不过python2已经移除了，推荐用in语句。

```javascript
d = {'a':1}
d.hasOwnProperty('a')
true
```

#### shallow copy

```js
const original = { a: 1, b: 2 };
const copy = { ...original, c: 3 }; // copy => { a: 1, b: 2, c: 3 }
```

#### 遍历对象属性

`Object.keys(obj)` 将返回该对象的keys组成的数组，然后后续可以利用数组的遍历动作来实现对对象keys的遍历。

```
Object.keys(obj)
```





### 集合

javascript中的集合Set大体也和python中的集合概念相近。

var s1 = new Set(); // 空Set
var s2 = new Set([1, 2, 3]); // 含1, 2, 3

然后其也有 `add` 方法用于添加一个元素。用 `delete` 方法来删除某个元素。



## 函数

函数正如前面所说也是一个对象，一个简单的函数对象定义如下所示：

```javascript
let greeting = function(name){
	console.log(name);
}
greeting('hello')
```
上面的写法主要介绍了匿名函数的写法，某些情况下会用到，一般定义函数最好采用如下写法：

```js
function abs(x){
	if (x >= 0) {
      return x;
    } else {
      return -x;
    }
}
```

这两种定义风格是完全等价的。这里值得一提的是如果函数没有确定return值，则返回的是 `undefined` 。

### arguments用法

javascript的函数内部可以直接使用 `arguments` 这个变量，其不是一个Array，但可以如下使用:

```
arguments[0]
arguments.length
```

其会接受传入函数的所有参量。

### rest用法

这个有点类似于lisp语言的rest参量控制概念，也就是如下

```js
function func(a,b,...rest){
	console.log(rest);
}
```

rest是表示除了a和b之外的所有其余参量。注意前面三个点号: `...rest` 。

### 箭头函数

简单来说箭头函数就是 lambda 表达式的更简洁写法，只是说在javascript语境下其和一般function的区别是：<u>其没有this绑定</u>。

```js
(param1, param2, …, paramN) => { statements }
```



## 程序中的逻辑

这一块如果读者熟悉一门编程语言的话，粗略地了解下扫一遍基本上就掌握了javascript相关语句知识。下面本小节也不会过多地讨论，只是就某些应用上常见的知识点做出一些说明。

### 条件判断结构

条件判断结构，和python大同小异，除了那些圆括号（记住这个圆括号必须加上）和花括号。

```js
var feedback = 10
if (feedback > 8) {
	console.log("Thank you! We should race at the next concert!")
} else {
	console.log("I'll keep practicing coding and racing.")
}
```

虽然javascript不像python那样强制缩进风格，但还是推荐用缩进来增强你的代码可读性和逻辑清晰性，如:

```js
age = 20
if (age < 6) {
	console.log('kid')
} else if (age >= 18) {
	console.log('adult')
} else {
console.log('teenager')
}
```

javascript有switch语句，作为我们pythoner你懂的，用多个else if语句也是可以的。

### switch语句

```javascript
function set_choice() {
  choice = 'second'
  switch (choice) {
    case 'first':
      console.log('first');
      break;
    case 'second':
      console.log('second');
      break;
    default:
      console.log('default');
  }
}
```



###  三元运算符

```
> let b = null
undefined
> b = b ? b : 2
2
```

### for循环

javascript和python都有while语句，但while语句用的较少，更多的是使用for语句。

```js
var count = 10;
for (var i=0; i < count; i++){
   console.log(i);
}
```

### for遍历数组

```js
for (let value of array) {
  // do something with value
}
```

遍历数组还可以这样：

```js
> a = ['a', 'b', 'c']
< a.forEach(function(value, index){
    console.log(value, index);
});
> a 0
> b 1
> c 2
```

这大体实现了类似于python的 `enumerate` 写法。

### for遍历对象

然后递归遍历对象的key也是可以的:

```js
for (var i in {'a':1,'b':2}) {
	console.log(i)
}
```

### for实现while循环

下面是用for语句来实现while循环：

```js
var count = 10;
var i = 0;
for (; i < count; ){
  console.log(i);
  i++;
}
```

### for实现无限循环

下面是用for语句实现无限循环：

```
for (;;){
  dosomething;
}
```

### while语句

while语句简单了解下吧。

```js
var x = 0;
var n = 99;
while (n > 0) {
	x = x + n;
	n = n - 2;
}
```

还有do while 语句

```js
var n = 0;
do {
	n = n + 1;
}while (n < 100);
```


### 异常处理

类似于python的 `try...except...` ，javascript有：

```
try {
    throw （new Error("Invalid Parameters"));
}catch (e) {
    console.log(e);
}finally {
    //always do something.
}
```



## 面向对象编程

现代javascript推荐使用class来定义类：

```javascript
//定义类
class Point {
  constructor(x, y) {
    this.x = x;
    this.y = y;
  }

  toString() {
    return '(' + this.x + ', ' + this.y + ')';
  }
}
```

以前老式的写法如下所示，可以了解下：

```javascript
function Point(x, y) {
  this.x = x;
  this.y = y;
}

Point.prototype.toString = function () {
  return '(' + this.x + ', ' + this.y + ')';
};

var p = new Point(1, 2);
```



### this

在javascript里面，object里面定义的方法， `this` 指向的就是本对象的实例。

如果 this 在函数里面，如：

```
function (){
    this.x = 1;
}
```

那么指定的是当这个函数要运行的时候，具体调用这个函数的对象。

比如说某个函数将这样被调用： `jquery对象.what` 那么这个函数里面的this就是指定的那个jquery实例，通常也就是网页里面的某个标签元素。

### constructor方法

面向对象编程里面常见的概念，即该对象的构造方法，在新建实例化该对象时被调用。

### 属性的get和set

面向对象编程里面这个是自定义对象重要的一个设计点，javascript采用如下`get name()` 这样的写法： 

```javascript
class User {
  constructor(name) {
    this._name = name;
  }

  get name() {
    return this._name;
  }

  set name(value) {
    if (value.length < 4) {
      console.log("Name is too short.");
      return;
    }
    this._name = value;
  }
}

let user = new User("John");
console.log(user.name);

```

### 类的继承

关于面向对象的继承概念这里就不赘述了。

```javascript
class Dog extends Animal{
   //
}
```

### super

类似python语言里面的super概念，引用父类。

### instanceof

类似于python语言中的isinstance函数。

```
obj instanceof Class
```



## no-jquery

更多相关知识请参阅参考资料四，即 [这个Github项目](https://github.com/nefe/You-Dont-Need-jQuery/blob/master/README.zh-CN.md) 。下面就一些重点知识做出一些整理。

### 选择

jquery的选择是该库很核心的一个功能，现代JavaScript提供了 `document.querySelector()` 和 `document.querySelectorAll()` 来作为替代。然后原来的 `document.getElementById()`  ， `document.getElementByClassName()` 或 `document.getElementByTagName()` 性能更好。

```
// jQuery
$('selector');

// Native
document.querySelectorAll('selector');
```

#### 选择class

```
// jQuery
$('.class');

// Native
document.querySelectorAll('.class');

// or
document.getElementsByClassName('class');
```

#### 选择id

```
// jQuery
$('#id');

// Native
document.querySelector('#id');

// or
document.getElementById('id');
```





### ajax

更多信息请查看mozilla关于 [fetch函数的介绍](https://developer.mozilla.org/zh-CN/docs/Web/API/Fetch_API) 。

```javascript
fetch("http://localhost:8080").then(
  function(response) {
    console.log("请求状态: " + response.status);
    return response.text();
  }
).then(function(text){
  console.log("返回文本：" + text);
})

```

fetch将请求一个URL，然后调用后面的函数。其中`response.text()` 返回的是一个Promise对象，什么是Promise对象，可以类比作python异步编程里面的协程，继续调用then才能获得内容。

如果你请求的是JSON api接口，那么可以直接调用 response.json来处理返回结果：

```javascript
fetch("http://localhost:8080").then(
  function(response) {
    return response.json();
  }
).then(function(result){
  console.log(result);
})
```



## 参考资料

1. Javascript权威指南 David Flanagan著.
2. [mozilla docs](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript)
3. [现代javascript教程](https://zh.javascript.info/)
4. [you donot need jquery](https://github.com/nefe/You-Dont-Need-jQuery/blob/master/README.zh-CN.md)



<link href="https://cdn.bootcss.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet">

<script src="https://cdn.bootcss.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>