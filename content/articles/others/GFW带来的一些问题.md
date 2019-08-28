Title: GFW带来的一些问题
Date: 2016-08-14 22:48
Modified: 2016-09-24 20:45
Tags: GFW,

[TOC]


# pypi下载用国内源

    pip install --trusted-host pypi.douban.com -i http://pypi.douban.com/simple carbon

或者修改本机的pypi配置，在当前用户主文件夹下的 `.pip/pip.conf` 下加入内容:

    [global]
    index-url = http://pypi.douban.com/simple

windows下是 `%HOMEPATH%\pip\pip.ini` 。

如果你遇到提示说要加入参数 `--trusted-host pypi.douban.com` ，你可以加上这个选项，或者在pypi配置里面加上：

    [install]
    trusted-host = pypi.douban.com

# js 用国内cdn源

推荐 [这个网站](http://www.bootcdn.cn/) 。



## docker国内加速镜像

推荐用类似下面的命令：

```
docker pull daocloud.io/ubuntu:16.04
docker pull daocloud.io/centos:7
docker pull daocloud.io/python:3
```

把镜像文件下载下来。



# ubuntu的更新源
ubuntu的更新源换成国内的源。

# android studio sdk更新太慢
请参考 [https://github.com/inferjay/AndroidDevTools](https://github.com/inferjay/AndroidDevTools) 。这个网站还有很多和android开发相关的资料。

