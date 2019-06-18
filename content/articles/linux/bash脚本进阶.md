Title: bash脚本进阶
Slug: bash-advanced
Date: 2019-06-17
Modified: 2019-06-17
Tags: bash, 

[TOC]

## xargs多行转一行

```
sudo rmdir --ignore-fail-on-non-empty  $(ls -U | head -n 10000 | xargs)
```

这是一个批量删除空文件夹的命令，假设现在空文件夹数目很多。首先 `ls -U` 单纯列出来，然后管道导向 `head` 只打印最开始的几行，然后管道导向 `xargs` 命令，这样多行转成一行，就可以作为 rmdir 的参数了。