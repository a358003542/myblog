[TOC]

## 简介

所谓的exe制作也就是把你写python程序freeze起来，这样目标机器上用户没有安装python或者等等其他依赖都能正常运行程序。

推荐使用pyinstaller。 pyinstaller的官网在 [这里](http://www.pyinstaller.org/) 。安装就是用pip 安装即可。

然后推荐在你的项目根目录下创建一个简单的启动脚本，一方面方便平时测试，一方面作为pyinstaller的程序入口。

**NOTICE:**  注意该脚本的名字不要和你的程序的模块名字相同，之前我安装后闪退就是因为这个脚本名字没取好。

具体使用很简单：

```text
pyinstaller you_entry_point.py
```

如果一切顺利，到 `dist` 文件夹下运行你的目标程序exe运行正常，一切都OK，那么恭喜你了。没必要继续往下看了。如果出问题了，那么请钻研官方文档吧，下面也会做出一些补充说明。

首先你不能依靠自动生成的 `.spec` 文件了，接下来讨论了很多定制都是基于对这个 `.spec` 文件的修改。修改好了之后要如下运行了：

```text
pyinstaller you_entry_point.spec
```

比如将exe下来的一个参数选项调为 `console=False`，这样生成的exe执行的时候就不会弹出另外那个cmd窗口了。



### 添加额外的文件

spec文件下配置 `datas` 这个列表值：

```text
datas=[ ('src/README.txt', '.') ],
```

大概意思是把那里的那个文件copy到目标dist文件夹的那里。

