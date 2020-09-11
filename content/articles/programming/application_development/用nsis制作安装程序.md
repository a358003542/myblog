Slug: nsis
Date: 20200830
Category: application_development

[TOC]

## 简介

nsis安装程序是free的，通常制作一个简单的安装程序稍微熟悉学习一下够用了。

首先你需要下载 nsis基本程序，推荐到 [这里](https://nsis.sourceforge.io/Main_Page) 下载 。

然后推荐下载 [HM NIS Edit](http://hmne.sourceforge.net/) 这个简单的程序，这个程序可以向导式生成一个nsi脚本文件。具体nsi文件的编写倒不一定要在哪里编写。

**NOTICE** HM NIS Edit 这个软件界面不推荐选择中文，输出的文件编码会是GBK的，这和现在通用的UTF8编码很不兼容了。

利用HM NIS Edit填写一些信息，这个具体倒是很直观，没什么好说的。生成的脚本到另外的编辑器上一般还要做一些进一步的修改。这个脚本刷文件夹所有的文件变动还是很方便的。

## 一些基本信息

下面是定义软件名，软件版本号和软件出版人这些基本信息。

```
!define PRODUCT_NAME "yaogua"
!define PRODUCT_VERSION "0.1.1"
!define PRODUCT_PUBLISHER "wanze"
```



## 界面语言选择

之前如下这样设置是可行的：

```text
!insertmacro MUI_LANGUAGE "SimpChinese"
```
繁体中文是 `TradChinese` 。

但是最近我将我的win10系统全局设置为UTF8编码之后，其安装界面成乱码了。可能nsis的中文编码默认不是utf8的。稳妥起见还是选择英语吧，这肯定不会出现恼人的乱码问题：

```
; Language files
!insertmacro MUI_LANGUAGE "English"
```



## 快捷方式加图标
用上面提到的工具自动生成的nsi脚本，默认的快捷方式向导是没有加上图标的，你可以如下加上图标：
```text
  CreateShortCut "$SMPROGRAMS\timer\timer.lnk" "$INSTDIR\timer.exe" "" "$INSTDIR\myapp.ico"
```

第三个参数是可选的，命令行参数，没啥好填的。最后一个参数就是设置图标的，具体图标注意要填在文件复制到目的地操作之后，填写的值也是复制的目的地那边的哪里。

## `PRODUCT_DIR_REGKEY`

这个应该是向windows系统注册本软件的安装目录：

```
!define PRODUCT_DIR_REGKEY "Software\Microsoft\Windows\CurrentVersion\App Paths\yaogua"
```

默认的输出似乎有时exe会指错。

## OutFile

OutFile会控制你的输出exe的名字。

```
Name "${PRODUCT_NAME} ${PRODUCT_VERSION}"
OutFile "yaogua_Setup.exe"
InstallDir "$PROGRAMFILES\yaogua"
InstallDirRegKey HKLM "${PRODUCT_DIR_REGKEY}" ""
```

## 设置安装图标和删除图标

```
!define MUI_ICON "app.ico"
!define MUI_UNICON "app.ico"
```

这个应该是那个安装程序和那个删除程序 `uninst.exe` 的图标，前面提到的 `CreateShortCut` 是一些快捷方式的图标，比如桌面快捷方式。