Title: bihu模块
Slug: bihu-module
Date: 2018-07-27
Modified: 2018-07-27
Tags: python,



[TOC]



## 简介

一个通用目的的python模块，安装如下：

```
pip install bihu
```

项目源码在 <https://github.com/a358003542/bihu>


## 功能简介

1. web 里面有获取随机user-agent函数等其他辅助函数。
2. workflow里面写了一个状态控制类，在airflow调度的时候，最小的任务执行仍然有状态记录。
3. database 里面放着很多便捷的对接数据库的通用操作模式。具体请读者用心体会。
4. utils里面有很多便捷的函数支持。





## 更新说明





## 项目配置管理

本项目开发遵循12因素应用配置管理原则：

1. .env 不进入版本库，控制整个项目的配置选择，目前选用了三个阶段： development testing production，分别对应于 本机早期开发， 实际上机测试  和 生产环境
2. .secrets.toml 里面放着一些私密的配置信息，不进入版本库
3. settings.toml 里面放着其他一些配置

使用请参看 dynaconf 模块。


## 版权申明
本模块版权归cdwanze所有，不可用于商业目的，若有需要请联系作者本人。



## API

下面介绍API只是简单介绍下，具体使用请参阅代码。

### web

- get_random_user_agent 获取随机的user_agent
- to_absolute_url 将一个url转变成为绝对url
- download 在common下，下载文件便捷函数
- etc...



### database

- mongodb 便捷连接操作和有去重逻辑的insert逻辑和upsert逻辑。
- sqldb 利用sqlalchemy便捷连接sql database，utils里面定义了一些常见的操作，如 `insert_or_ignore` `insert_or_update` ，函数里面有去重判断，返回值选择和具体什么情况下才进行更新操作的函数钩子。
- sqldb里面还有一个便捷的 `SQLDataBase` 类，其可以直接连接已经存在的数据库，从而获取到sqlalchemy 的 orm对象。
- redis 简单的连接redis操作
- 

### utils

- date_utils 一些便捷的日期时间操作函数
- path_utils 一些便捷的路径操作函数，如获取某个路径下所有的某个后缀的文件等。
- 



### workflow

- 提供了 `StatusRecordHandler` 类，可以很方便的对airflow操作流程具体某个时间片上的操作加上状态记录功能。