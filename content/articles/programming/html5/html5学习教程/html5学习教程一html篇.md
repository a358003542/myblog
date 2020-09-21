Slug: html5-tutorial-html
Category: html5_tutorial
Date: 2019


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