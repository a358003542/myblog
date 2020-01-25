Title: 用nsis制作安装程序
Date: 2020-01-20
Modified: 2020-01-20
Tags: 安装程序

[TOC]

nsis安装程序是free的，通常制作一个简单的安装程序稍微熟悉学习一下够用了。

首先你需要下载 nsis基本程序，推荐到 [这里](https://nsis.sourceforge.io/Main_Page) 下载 。

然后推荐下载 [HM NIS Edit](http://hmne.sourceforge.net/) 这个简单的程序，这个程序可以向导式生成一个nsi脚本文件。具体nsi文件的编写倒不一定要在哪里编写。

**NOTICE** HM NIS Edit 这个软件界面不推荐选择中文，输出的文件编码会是GBK的，这和现在通用的UTF8编码很不兼容了。

利用HM NIS Edit填写一些信息，这个具体倒是很直观，没什么好说的。生成的脚本到另外的编辑器上一般还要做一些进一步的修改。这个脚本刷文件夹所有的文件变动还是很方便的。

### 界面语言选择
默认的界面语言选择没看到中文，我翻了一遍确实没有，难道是S开头的我当时没看到？无所谓了，NSIS的modren UI是支持简体中文的，如下修改：
```text
!insertmacro MUI_LANGUAGE "SimpChinese"
```
繁体中文是 TradChinese 。

### 快捷方式加图标
默认的快捷方式向导是没有加图标的操作的，你可以如下加上图标：
```text
  CreateShortCut "$SMPROGRAMS\timer\timer.lnk" "$INSTDIR\timer.exe" "" "$INSTDIR\myapp.ico"
```

第三个参数是可选的，命令行参数，没啥好填的。具体图标注意要填在文件复制到目的地操作之后，填写的值也是复制的目的地那边的哪里。