Title: powershell入门
Slug: powershell-tutorial
Date: 2018-01-20 12:56
Modified: 2018-01-20 12:56
Tags: powershell,
Status: draft
[TOC]

## 简介

之前一直在linux系统做服务器的环境下玩一些东西，现在竟然要在windows服务器下做一些东西，其实python这一块都还好，很多python模块现在都支持windows系统，就是到了很多和linux系统相关的进程等等东西就出现差异了。

实际项目中确实有这样的需求，尤其到数据处理这一块，后台各个处理进程是多个杂的，luigi模块更多的关注工作流，有的时候有些处理进程各自是完全毫无关系的，这个时候就需要开两个进程等等。在linux系统下，进程的开启和后台管理还有bash脚本的编写都是基本功，在wondows下感觉这一块也是需要学习接触好的。

bat脚本是针对cmd的，现在powershell越来越成为主流了，而且powershell功能也是更加强大和完善的，只是powershell更加不为人们熟悉罢了。

本文作者也是一边用一边有问题，一边写吧，题目权记作 powershell 入门。

powershell脚本的后缀是 `ps1` ，人们开始编写powershell遇到的第一个挫折就是会提示没有权限执行脚本，这是windows的默认安全策略，你需要以管理员身份运行：

```powershell
set-executionpolicy remotesigned
```

## 启动一个进程

```powershell
Start-Process -FilePath "ping.exe" -Args "www.baidu.com"
```

然后进程的输出可以如下进行重定向：

```powershell
Start-Process -FilePath "ping.exe" -Args "www.baidu.com" -RedirectStandardOutput '.\console.out' -RedirectStandardError '.\console.err'
```

## 获取当前工作目录

下面的例子也同时讲解了基本的关于powershell里面如何定义变量和字符串中如何使用变量等知识。

```powershell
$curpath=$(Convert-Path .)
echo $curpath
cd "$curpath\logs"
echo $(Convert-Path .)
cd $curpath
```

熟悉脚本的看到这个例子，基本上所谓的子命令调用返回，或者字符串中变量的替换，或引用变量等都一看就清楚了。



