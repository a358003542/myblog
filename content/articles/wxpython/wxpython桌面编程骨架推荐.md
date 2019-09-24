Title: wxpython桌面编程骨架推荐
Date: 2019-09-24
Modified: 2019-09-24
Slug: wxpython-bone
Tags: wxpython,


[TOC]

## 前言

笔者钻研wxpython桌面编程有一段时间了，一些样例请参见 [这个项目](https://github.com/a358003542/wxpython_examples) 。

然后多查看wxpython的demo程序还有API文档。

剩下来的就是具体编程需求，思考如何界面设计等等问题。

不过在开始编写项目之前，wxpython还是有一个通用的骨架可以参考的，这和后面的实际编程需求或者说业务并不是很相关。

具体读者可以参考 [这个项目](https://github.com/a358003542/image_process_tool) 的前面几个commit。下面简要说明下。

### 图片文件管理

 图片文件都应该放在一个文件夹里面，然后编写 [encode_bitmaps.py](https://github.com/a358003542/image_process_tool/blob/master/encode_bitmaps.py) 文件，然后你的项目里面通过

```python
import images
images.Favicon
```

来获取图片对象。

### 程序主入口

你应该编写一个程序主入口文件， [image_process_tool.py](https://github.com/a358003542/image_process_tool/blob/master/image_process_tool.py) ，这对于你平时测试运行是方便的，对于你后面利用 pyinstaller 来编译exe文件，也是需要这样一个脚本文件入口的。

### 编写pyinstaller的spec文件

从个人实践经验来看，推荐你还是手工编写pyinstaller的spec文件。

### 编写一个全局变量文件

某些参数和全局变量是推荐编写一个 [global_var.py](https://github.com/a358003542/image_process_tool/blob/master/global_var.py) 文件，同样后面在程序中可以直接

```
import global_var as g_var
```

来调用，很多情况下这是很方便的。

### MVC分离架构

实际源码中分为 `gui`表示视图层， `models` 表示模型层， `controllers` 表示控制层，在一些非常小的图形界面中，可能控制层和模型层并没有代码，但这种MVC分离架构还是推荐保留着。

### 常数配置统一管理

桌面GUI程序，哪怕是很小型的桌面GUI程序都可能遇到很多const常数，推荐统一管理。

### 自定义颜色

请参看 [app.py](https://github.com/a358003542/image_process_tool/blob/master/src/gui/app.py) 的 `update_self_defined_color` 操作，建立自己的颜色定义库来规范化你的程序代码。

### 应用程序启动唯一性

在某些个别的情况下可能会允许桌面程序多开，但绝大部分情况应该都是要求一个应用程序一个界面，而且需要应用程序有这样的反应，那就是点击应用程序图标，会自动弹出来之前你创建的那个应用程序实例。

请参看  [app.py](https://github.com/a358003542/image_process_tool/blob/master/src/gui/app.py)  的解决方案。

### 异常信息更好的处理

利用pubsub操作来更好的对异常信息进行捕捉，否则随着你的桌面程序代码变得庞大，如果你的异常无法定位了，将会让调试变得非常困难。具体请参看 [exception_utils.py](https://github.com/a358003542/image_process_tool/blob/master/src/exception_utils.py) 文件。

### 实际图形界面编码

到实际图形界面编码那就根据情况编写mainFrame到各个panel等等，更多的这方面编码细节和推荐规范，请参看 [wxpython编码规范]({filename}./wxpython编码风格推荐.md) 一文。

