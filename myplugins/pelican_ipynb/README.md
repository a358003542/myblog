# Pelican plugin for Jupyter Notebook

## CHANGELOG
大幅精简所有代码，然后发现效果还很好。
1. summary不需要处理，利用pelican自带的summary生成机制够用了
2. metadata用nbformat读入，然后传回去即可，去除了ipynb文件的两个额外的metadata，其他metadata如果读者在ipynb文件中加入的都会传过去。
3. html输出代码不带css目前看来显示效果还可以，就这样了。

## 安装

和其他pelican plugin安装过程一样的，除了需要额外加上这个选项配置：

```
MARKUP = ('md', 'ipynb')
```



## metadata的输入

打开 `.ipynb` 文件修改 `metadata` 标签(注意是最顶层的metadata数据，似乎一般在最后面。)：

```
{
    "metadata": {
        "name": "My notebook"
        ... { A_LOT_OF_OTHER_STUFF } ...
    },
{ A_LOT_OF_OTHER_STUFF }
```

必填的就是title，其他请使用者根据自己的需求来填写。