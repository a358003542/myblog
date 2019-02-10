Title: css基础
Date: 2018-05-27
Modified: 2018-08-16

[TOC]

# css基础

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

