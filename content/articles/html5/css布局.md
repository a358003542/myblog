Title: css布局
Date: 2018-05-27
Modified: 2018-08-16

[TOC]

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