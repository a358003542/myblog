Slug: pipenv-module
Status: draft
[TOC]

pipenv模块刚开始听说觉得virtualenv够用了，就没太在意。后来一试发现真的可以，很方便的，在设计理念上和nodejs那边的包管理有点接近了，很不错。

刚进入一个文件夹，然后运行：

```bash
pipenv install
```

当然运行前你需要：

```
pip install pipenv
```

其会创建 `Pipfile` 和 `Pipfile.lock` 这两个文件。如果读者有点熟悉nodejs那边的包管理机制，就对这两个文件的作用不需要做过多的说明了。

那么怎么激活进入虚拟环境呢：

```
pipenv shell
```

 或者你直接调用虚拟环境下运行某个命令：

```
pipenv run you_awesom_command
```

读者打开 `Pipfile` 文件会发现这一行

```
url = "https://pypi.douban.com/simple"
```

以前还要在系统的另外的地方去配置，现在直接在这里修改就可以了。

然后安装模块就是：

```
pipenv install requests
```

或者remove模块：

```
pipenv uninstall requests
```

值得注意的pipenv模块很好地解析的各个包包的依赖关系，这就是他比原 `requirements.txt` 要好一点的地方。

还有忘了什么 pip freeze 命令吧。

读者在使用pycharm的时候需要设置下pipenv管理的虚拟环境路径：在当前用户家目录下的 `.virtualenvs` 哪里。



## 文件夹格式引入

文件夹格式引入，就是一个简单的pypi包格式，主要是写好setup.py的那种，然后如下：

```
pipenv install -e "../what_your_pypi_package"
```

这种格式懂得人都会明白，这个功能简直是让人拍案叫绝。某个python模块，你直接修改源码就可以了，pycharm那边对接好，不管是python shell还是自动进入虚拟环境的shell都直接直接使用哪个文件夹格式的pypi包，**关键是重点** ：你不需要像以前那样运行 `python setup.py build` 或者install之类的等等，就已经正常工作了，有的你拍案叫绝有没有，有没有。