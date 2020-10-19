Category: python_language
Slug: python-pypi
Date: 20191018
Tags: python, pypi


[TOC]

## setup.py配置

本章知识是我们理解前人编写的各个有用的模块包的基础，也是编写自己的模块包的基础。

请结合Github上的 [pyskeleton项目](https://github.com/a358003542/pyskeleton) 来阅读本章。

虽然官方内置distutils模块也能实现类似的功能，不过现在人们更常用的是第三方模块setuptools，其相当于distutils模块的加强版，初学者推荐就使用setuptools模块。更多内容请参看setuptools模块的 [官方文档](https://setuptools.readthedocs.io/en/latest/) 。

安装就是先安装pip3：

```text
sudo apt-get install python3-pip
```

然后通过pip3来安装setuptools：

```text
sudo pip3 install setuptools
```

最简单的"setup.py"文件如下所示：

```python
from setuptools import setup, find_packages
setup(
    name = "HelloWorld",
    version = "0.1",
    packages = find_packages(),
)
```

第一行是从setuptools模块中引入setup函数和 `find_packages` 函数。

setup函数接受一系列的字典值，下面就setup函数的一些字典值的含义慢慢道来：

name

:   本软件的名字

version

:   本软件的版本号

author

: 本软件的作者

author_email

: 本软件作者的邮箱

maintainer

: 本软件的维护者

maintainer_email

: 本软件维护者的邮箱

contact

: 本软件的联系人。可以不写，则是维护者的名字，如果没有则是作者的名字。

contact_email

: 本软件的联系人的邮箱，可以不写，则是维护者的邮箱，如果没有则是作者的邮箱。

license

: 本软件的license

url

: 本软件项目主页地址

description

: 本软件的简要描述
long_description

: 本软件的完整描述

platforms

: 本软件经过测试可运行的平台

classifiers

: 本软件的分类，请参考 [这个网页](<https://pypi.org/classifiers/> ) 给出一些值。是字符串的列表。

keywords

: 本软件在pypi上搜索的关键词，字符串的列表。

packages

: 你的软件依赖的模块。一般如下使用： 
```text
packages = find_packages()
```
则文件夹下有 `__init__.py` 文件的，都将视作python模块包，其内的py文件都将加入进去。

除此之外你也可以直接手工输入你的模块名字，具体就是字符串的列表。

entry_point
: 
```text
entry_points = {
'console_scripts' :[ 'zwc=zwc.zwc:main',],
}
```

其中zwc是你的shell调用的名字，然后zwc是你的模块，另外一个zwc是你的主模块的子模块，然后main是其中的main函数。这就是你的shell调用程序的接口了。类似的还有gui_script可以控制你调用GUI图形的命令入口。

install_requires
: 接受字符串的列表值，将你依赖的可以通过pip安装的模块名放入进去，然后你的软件安装会自动检测并安装这些依赖模块。

package_data

: 你的软件的模块额外附加的（除了py文件的）其他文件，具体设置类似这样 `{"skeleton":['*.txt'],}` 其中skeleton这里就是具体的你的软件的模块（对应的文件夹名），然后后面跟着的就是一系列的文件名列表，可以接受glob语法。注意这里只能包含你的模块文件夹也就是前面通过packages控制的文件夹下面的内容。

include_package_data

: 这个一般设置为True



其他不常用的属性值列在下面：

- scripts 不推荐使用，推荐通过entry_point来生成脚本。
- setup_requires 不推荐使用，基于PEP-518 。
- py_modules 不推荐使用，推荐使用packages来管理模块。
- data_files 前面的package_data是只能在你的模块文件夹里面的其他数据文件等，然后可能还有一些数据文件你需要包含的，用data_files来控制，具体后面跟着的参数格式如下面例子所示：

```text
data_files = [('icos',['icos/wise.ico'])],
#这是添加的icos文件夹下面的wise.ico文件
data_files = [('',['skeleton.tar.gz'])],
#这是添加的主目录下的skeleton.tar.gz文件
```

值得一提的是data_files不能接受glob语法。

data_files已经不推荐使用了，推荐用package_data来管理，可以方便用pkg_resources里面的方法来引用其中的资源文件。具体说明请看后面。

## pip的develop模式

本小节参考了 [这个问题](https://stackoverflow.com/questions/19048732/python-setup-py-develop-vs-install) 。

对于其他第三方包你不需要修改的，就直接 python setup.py install 就是了，而对于你自己写的包，可能需要频繁变动，最好是加载引用于本地某个文件夹，那么推荐是采用 python setup.py develop 命令来安装。

其对应于 `pip install -e .` 这个命令，或者直接安装本地文件夹不是develop模式 `python install .` 。

pipenv的 `pipenv install -e .` 也是这个develop模式，你修改的代码会实时生效。

## pkg_resources模块来管理读取资源文件

如下所示：
```
    from pkg_resources import resource_filename
    resource_stream('wise','icos/Folder-Documents.ico')
```


第一个参数是模块名字，第二个参数是模块中的文件的相对路径表达。

上面的例子是resource_filename，返回的是引用的文件名。此外还有命令：resource_string，参数和resource_filename一样，除了它返回的是字节流。这个字节流可以赋值给某个变量从而直接使用，或者存储在某个文件里面。


## 在pypi上传你的软件

### 正确处理README文档

现在pypi已经支持markdow文档格式了。推荐按照官方文档 [这里](<https://packaging.python.org/guides/making-a-pypi-friendly-readme/> ) 来处理：

```python
from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='an_example_package',
    # other arguments omitted
    long_description=long_description,
    long_description_content_type='text/markdown'
)
```

有段时间我用 `codecs` 来读取README文件一直出现一切奇怪的问题，原因不明。就如同上面这样直接读取即可。

注意上面配置的 `long_description_content_type` ，如果你喜欢 `reStructuredText` 格式，那么设置为 `text/x-rst` 即可。

首先推荐升级最新的setuptools，wheel和twine模块。

然后直接用下面这句：

```text
python setup.py sdist bdist_wheel
```

这样将直接dist文件夹下面生成源码tar包和wheel包。

然后推荐运行下：

```text
twine check dist/*
```

来确保你的文档格式没问题。

### 推荐使用twine上传

使用twine上传到pypi很简单：

```text
twine upload dist/*
```

你每次都需要输入用户名和密码，你可以安装 `keyring` 模块，然后运行：

```text
keyring set https://upload.pypi.org/legacy/ your-username
```

来本地安全保存你的用户名和密码。

## pypi下载使用国内源

豆瓣的pypi源 `https://pypi.douban.com/simple`  或者 清华的pypi源 `https://pypi.tuna.tsinghua.edu.cn/simple` 都可以吧。

临时使用用 `-i` 或者 `--index` 选项： 

```text
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package
```

永久更改本地配置：

```text
pip install pip -U
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```



## pypi只下载软件源文件

下载pypi上的目标软件源文件而不是安装。参考了 [这个网页](http://stackoverflow.com/questions/7300321/how-to-use-pythons-pip-to-download-and-keep-the-zipped-files-for-a-package) 。

```text
pip install --download="/pth/to/downloaded/files" package_name
```





## python虚拟环境管理

Virtualenv模块的主要作用就是建立一个封闭独立的python开发环境，因为一个python项目的开发通常会涉及到多个模块，而你激活virtualenv环境之后，通过pip命令安装的模块是安装在本项目文件夹内的，这样就建立了单独的固定某个模块版本的开发环境。通过python虚拟环境，一方面控制了python的版本，另一方面控制了python模块的版本，同时使得整个项目类似于绿色安装版具有可移植性。


安装就是用pip来安装常规安装即可。

```text
sudo pip install virtualenv
```


### 新建一个项目
新建一个项目就是使用virutalenv命令，然后后面跟一个文件夹名字，等下要新建的文件夹名字。

```text
virutalenv [path]
```

这里的path就是你的项目的名字，等下会创建该名字的文件夹，你也可以设定为 "." ，这样就是在当前文件夹下创建。 然后常用的选项有：


- `--python=python2` 或者 `--python=python3` 如果不指定这个选项，虚拟环境会使用当前操作系统的默认python版本。

- `--system-site-packages` ，如果加上这个选项，那么你的虚拟环境是可以使用安装到系统里去的那些python模块的。参考了 [这个网页](http://stackoverflow.com/questions/3371136/revert-the-no-site-packages-option-with-virtualenv) ，这是个很值得一提的小技巧，那就是如果你之前设定是venv可以引用系统级的那些python模块，后面你又不想了，这个时候是不需要重新安装虚拟环境的，只需要在虚拟环境中创建一个这个空白文件即可：

```text
lib/python3.5/no-global-site-packages.txt
```

如果你又想引用系统级的那些python模块了，把这个文件删除即可。



### 激活本地虚拟环境

运行下面的命令即进入本地虚拟环境：

```text
cd venv
source bin/activate
```

激活虚拟环境之后，使用python是使用的虚拟环境设定的python解释器，然后使用pip安装模块也是安装在虚拟环境之下。


### 退出本地虚拟环境

运行deactivate命令即可

```text
deactivate
```

