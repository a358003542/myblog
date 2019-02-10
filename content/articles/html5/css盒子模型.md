Title: css盒子模型
Date: 2018-05-27
Modified: 2018-08-16

[TOC]

## css的盒子模型

html的显示布局和 \(TeX\) 的显示布局一样也是采用的浮动盒子模型，从上到下，从左到右，一个个盒子排下来，只是 \(TeX\) 更复杂，还有一个分页算法。简言之就是每一个标签元素都是一个盒子(我还不太确定一个个字是不是一个盒子，在 \(TeX\) 里面一个个字都是一个盒子。) 。

下面这个图片来自 [这个网页](http://www.hicksdesign.co.uk/boxmodel/) 。

![img]({filename}/images/前端开发/html_box_model.png "html_box_model")


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
border-style情况比较多，常见的有 **solid** 实线 **dashed** 虚线 **double** 双线 **dotted** 点线等，更多请参看 [这个网页](http://www.w3school.com.cn/cssref/pr_border-style.asp) 。v