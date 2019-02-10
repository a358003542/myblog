Title: pyqt5编程之-exe制作和安装程序制作
Date: 2018-05-26
Slug: pyqt5-intall


[TOC]
## exe制作和安装程序制作

### exe制作

所谓的exe制作也就是把你写的pyqt程序或者说python程序freeze起来，这样目标机器上用户没有安装python或者等等其他依赖都能正常运行程序。

推荐使用pyinstaller。 pyinstaller的官网在 [这里](http://www.pyinstaller.org/) 。

首先是用pip 安装之，然后推荐在你的项目根目录下创建一个简单的启动脚本，一方面方便平时测试，一方面作为pyinstaller的程序入口。

```python
"""
for pyinstaller
注意本脚本名字不能设置为 quicktikz
"""
import quicktikz.main

if __name__ == '__main__':
    quicktikz.main.gui()
```



**NOTICE:**  注意该脚本的名字不要和你的pyqt程序的模块名字相同，之前我安装后闪退就是因为这个脚本名字没取好。

具体使用很简单：

```python
import subprocess

PROJECT = 'quicktikz'

cmd = 'pyinstaller.exe --noconsole -y QuickTikz.py'

subprocess.call(cmd, shell=True)
```

上面的 `-y` 选项是自动删除原输出文件， `--noconsole` 是隐藏你的pyqt程序的终端界面，否则后面程序会开两个窗口不太好看。

如果一切顺利，到 `dist` 文件夹下运行你的目标程序exe运行正常，那么一切都OK，如果出问题了，那么请钻研官方文档吧。。

### 安装程序的制作

推荐使用 advanceinstaller程序，这是该程序的 [官网地址](https://www.advancedinstaller.com/) 。推荐一开始安装官网的simple 过程来，请参看官网的这个基本 [入门tutorial](https://www.advancedinstaller.com/user-guide/tutorial-simple.html) 。

在设置文件和文件夹的时候把在 `dist` 里面的所有内容都加进去即可，注意这个软件操作说是添加文件那么只能添加文件的，所以dist里面的 PyQt5文件夹需要再操作添加文件夹之。

如果一切运行顺利，那么太好了，我们就有了我们程序的安装程序，赶快分享给小伙伴们吧。

![img](/assets/adinstaller.png "adinstaller")