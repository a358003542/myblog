[TOC]

## powershell中文显示问题

现在UTF-8越来越成为主流了，不过powershell默认的当前代码页默认的是936，如果要改为UTF-8格式输出，很多程序现在也都是默认这个文本编码输出。那么需要执行 `chcp 65001` 。

现在【2020-8-13】最新的win10已经支持一种实验特性，如下图所示：

![img]({static}/images/2020/powershell_utf8.png)

这样会让你的系统默认powershell采用utf8编码，不过这个改动似乎是系统全局性的，可能有一些副作用。

## 当前目录启动powershell

现在的win10 按下shift键，然后点下鼠标右键，出来的菜单里面有个打开powershell功能就是当前目录启动powershell。

## 设置powershell启动的默认大小

右键点击powershell最上面的一栏，会看到默认值那个选项，设置布局的窗口大小即可，我这边宽度高度是100-40，感觉还行。

## 编写powershell脚本

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



