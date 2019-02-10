Title: pyqt5编程之-ui文件管理
Date: 2018-05-26
Slug: pyqt5-ui-file


[TOC]

# ui文件管理

利用 Qt designer 设计输出的 ui 界面文件，是可以直接用 `PyQt5.uic.loadUi` 来加载进来的，不过ui文件需要利用pypi的资源管理机制，这固然是一种解决方案，但不够pythonic。

推荐是用 `pyuic5` 处理来输出ui文件对应的py文件。大体是利用如下命令行： 

```python
pyuic5 {filename}.ui -o {filename}_ui.py --import-from={project}'.format(filename=filename,
																project=PROJECT)
```

这里的 `--import-from` 选项影响输出py文件的资源引入语句，默认是 `import main_rc` ，设置这个选项之后更改为：

`from project import main_rc`

然后就是利用输出py文件里面的ui类了。



```python
from .uis.main_ui import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None, *args):
        super().__init__(parent, *args)

		### setup ui
        self.mainUi = Ui_MainWindow()
        self.mainUi.setupUi(self)
```

具体引入按照官方教程有几种写法，上面这种写法中 `setupUi` 函数跟着本窗体的parent，如果是self则是挂在本窗体上，然后如果本窗体挂在其他母窗体即可。

