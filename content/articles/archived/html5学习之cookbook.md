Slug: html5-cookbook
Category: html5_tutorial
Tags: html5
Date: 20201121

[TOC]





## 表单提交按钮防止多次点击多次提交

参考了 [这个网页的第一小节](https://www.the-art-of-web.com/javascript/doublesubmit/) ，觉得这个解决方案很是简单，而且有效。对于单页面表单，也就是提交成功了通常切换到另外的网页那边去了的，还是很好地适用的。可能在某些情况下，本解决方案会令人不太满意，因为这个提交按钮只要提交之后就显示按钮一直处于禁用状态。



```html
<form method="POST" action="..." onsubmit="myButton.disabled = true; return true;">
...
<input type="submit" name="myButton" value="Submit">
</form>
```

