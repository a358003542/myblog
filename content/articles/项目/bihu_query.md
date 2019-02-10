Title: bihu_query项目
Slug: bihu-query
Date: 2018-08-08
Modified: 2018-08-08
Tags: python,



[TOC]



## 简介

实现了一个通用的根据输入的url，然后用户自己编写对应的url 正则匹配规则，然后编写相应的页面爬取规则，从而实现一个实时爬虫接口功能。

项目地址在 [https://github.com/a358003542/bihu_query](https://github.com/a358003542/bihu_query) 。




## 功能简介

### query 接口

```
/query/?url=
```

输入url参数，实时爬取目标页面，返回数据。



### 快速创建爬虫的图形操作界面

实现了一个快速创建爬虫的图形操作界面





## 更新说明





## 项目配置管理

本项目开发遵循12因素应用配置管理原则：

1. .env 不进入版本库，控制整个项目的配置选择，目前选用了三个阶段： development testing production，分别对应于 本机早期开发， 实际上机测试  和 生产环境
2. .secrets.toml 里面放着一些私密的配置信息，不进入版本库
3. settings.toml 里面放着其他一些配置

使用请参看 dynaconf 模块。


## 版权申明
本模块版权归cdwanze所有，不可用于商业目的，若有需要请联系作者本人。

