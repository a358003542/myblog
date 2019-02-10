Title: gitbook工具
Slug: gitbook-tools
Date: 2017-11-10 13:35
Modified: 2017-11-20 19:50
Tags: 写作工具,
[TOC]

请读者主要阅读 [http://www.chengweiyang.cn/gitbook/index.html](http://www.chengweiyang.cn/gitbook/index.html) 这篇教程。

下面我主要就我遇到的一些问题做一些补充说明。



## 安装

推荐安装的是 **gitbook-cli** ，gitbook安装之后会提示你应该安装 `gitbook-cli` ，推荐是全局安装。

### 安装插件

运行 `gitbook serve` 其会使用本地的插件，所以比如说要安装插件 `simple-page-toc` ，应该将其装在本地。

```
 npm install gitbook-plugin-simple-page-toc
```



## gitbook build

虽然gitbook serve也会输出一些内容，但更正式的做法是 `gitbook build the_foler` 来编译出你的gitbook内容供你的 webserver来服务。输出还是在 `_book` 那里，挂上 `index.html` 文件即可。

比如apache的话推荐用 `Alias` 语句来加载。

## gitbook和github的同步

首先是gitbook那边的配置要配置好，github那边也要新建一个对应的仓库。github的 `settings` 那里有个 Application 设置，里面也要设置好gitbook那边具体那些仓库对gitbook开放，否则你在gitbook那边是找不到这个仓库的。

然后就是第一次gitbook sync github是需要force 的，点下面两个大图标的左边，我还没有遇到过不需要force的情况，包括github那边新建一个空白仓库也不行。



## 一些特殊的文件的含义

-   主目录下 `book.json` ，插件配置就是在这里写的。
-   `assets` 文件夹一般放着图片，当然这个随意的，是参考了前gitbook图形界面的输出。
-   `README.md` 书在gitbook上一开始就显示这个文件。
-   `SUMMARY.md` 重要，控制书的目录，基本上你都可以将其看作gitbook对书处理的主入口。



## 中文文件名到底可不可以

gitbook那边自动生成的文件夹和文件名都不带中文的，那么通过github这边同步的内容，中文文件名到底可不可以。

经过测试中文文件夹和中文文件名都是<u>可以的</u>，在 `SUMMARY.md` 那边写好对应的路径就是了。

