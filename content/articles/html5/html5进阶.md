Title: html5进阶
Date: 2018-05-26
Modified: 2018-08-16

[TOC]
# html5进阶


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
<p>:before</p>

<textarea rows="5">
the textarea you say something
</textarea>

<p>:after</p>
```

<p>:before</p>

<textarea rows="5">
the textarea you say something
</textarea>

<p>:after</p>

### 加上action

也就是表单form标签上加上action属性，然后表单内定义submit的按钮或者input元素，点击之后将会将数据发送给action那边去，具体方法由method属性定义，默认是GET。

```
<form action="/where" method="POST">
  <input type="text">
  <button type="submit">submit</button>
</form>
```

### required

加上requird属性，该字段必须填上值。

```
<input type="text" required>
```

### placeholder

预显示的文字

```
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