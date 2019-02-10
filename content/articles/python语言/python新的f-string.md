Title: python新的f-string
Date: 2018-08-31
Modified: 2018-08-31
Slug: python-the-new-f-string
Tags: python,



现在python3版本迭代很快的，除了python3.4新加入的asyncio让我很是关心，最近还是接触一个新的f-string，是python3.6加入进来了。一开始对字符串前面加个f很是困惑，python2的时候字符串前面有u什么的，python3之后基本上字符串前面没什么东西了。但这次新加入的f-string，在初步使用之后就停不下来了，真的太好用了。

基本情况如下：

python新的format字符串

```
f"hello. {name}"
```
等价于

```
"hello. {name}".format(name=name)
```

一个变量还好，多个变量的时候这种f-string的写法的好处就很明显了，当时环境下你前面已经定义好的变量名是可以直接使用的，我只能用一句话来形容，太好用了，用上了你就会停不下来。