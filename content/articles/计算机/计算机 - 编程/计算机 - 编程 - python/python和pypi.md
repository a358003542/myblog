[TOC]
### 前言

本文讨论的内容有如果要编写自己的python模块，并上传到pypi.org则需要了解的知识点。主要有setuptool模块的使用，pip命令行工具，如何在pypi上上传自己的模块和其他相关知识。

### setuptools

本章知识是我们理解前人编写的各个有用的模块包的基础，也是编写自己的模块包的基础。

请结合Github上的 [pyskeleton项目](https://github.com/a358003542/pyskeleton) 来阅读本章。

虽然官方内置distutils模块也能实现类似的功能，不过现在人们更常用的是第三方模块setuptools，其相当于distutils模块的加强版，初学者推荐就使用setuptools模块。更多内容请参看setuptools模块的 [官方文档](https://setuptools.readthedocs.io/en/latest/) 。

现在setuptools推荐使用`setup.cfg`来进行相关配置管理，而不是之前的 `setup.py` 里的 `setup` 函数。pypi生态圈和相关PEP规范在不断完善中，现在推荐使用 `build` 模块，运行 `python -m build` 来进行你项目的打包工作。

你首先需要新建一个 `pyproject.toml` 文件，指定本项目的安装环境，setuptools相关如下：

````
[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"
````

#### 单python模块结构

一般推荐的项目结构有如下两种，现在假定这里我们讨论的python模块名字是pyskeleton，如果你的项目只有这样一个python模块，则推荐采用如下结构：

```
----pyskeleton
  --__init__.py
  
setup.cfg
pyproject.toml
```

对应的setup.cfg文件内容大体如下：

```
[metadata]
name = pyskeleton
version = attr: pyskeleton.__version__
description = quickly create a python module, have some other good concern.
url=https://github.com/a358003542/pyskeleton
long_description = file: README.md
long_description_content_type=text/markdown

[options]
include_package_data = True
packages = pyskeleton
```

也就是直接将packages写上去即可。

#### 多python模块结构

还有一种结构如下所示：

```
----src
  ----pyskeleton
    --__init__.py
  ----other_module
    --__init__.py
    
setup.cfg
pyproject.toml
```

现在甚至只有一个模块的python项目也推荐采用这种结构，因为这种结构可扩展性更好一些。一些C语言写的python扩展模块放在src文件夹下也能得到很好地管理。

这种结构的 `setup.cfg` 大体内容如下所示：

```
[metadata]
name = pyskeleton
version = attr: pyskeleton.__version__
description = quickly create a python module, have some other good concern.
url=https://github.com/a358003542/pyskeleton
long_description = file: README.md
long_description_content_type=text/markdown

[options]
include_package_data = True
packages = find:
package_dir =
    = src

[options.packages.find]
where = src
include = pyskeleton

[options.entry_points]
console_scripts =
    pyskeleton = pyskeleton.__main__:main
```

这里使用了find来自动从src文件夹下面寻找python模块，你可以将你的python的tests文件夹放在src之外，这样就避免了tests也被find进来了。你可以进一步通过 `include` 和 `exclude` 来控制find函数的行为。

`package_dir` 这个参数正是支持上面结构的关键，其传统的写法是这样的：

```
package_dir = {'': 'src'}
```

意思是你的根包在src文件夹下。这个配置还可以进行其他调配，但这会弄得太复杂了，这里就把上面具体的行为说明清楚：

find是自动寻找python模块，where指定要在那个寻找，所以现在find就开始在src文件夹下面寻找了，你可以通过include和exclude参数来进一步规范find的查找行为，就上面的例子来说将只会找到pyskeleton这个模块。为了后面讨论的方便现在假定找到了 `pyskeleton` 和 `other_module` 这两个模块。package_dir 定义了模块名和具体该模块在文件系统中文件夹的映射关系。比如上面设置根包在src文件夹下，则说 `pyskeleton` 就是预期要有 `src/pyskeleton/__init__.py` 这个文件，说得再具体一点，该模块将会拷贝到 `site-packages` 那里的根目录下面去。

为了加深理解我们可以将上面的include参数改成 `pyskeleton*` ，然后再随便新建一个pyskeleton2模块，经过测试就会发现又会多了一个pyskeleton2的模块。

一般子模块会放在总模块的下面方便管理，但项目合作的时候可能各个子模块会分开开发，那么这个时候你可以使用`find_namespace` 来实现多个子模块在一个父模块名字之下，这块讨论这里就略过了。

#### metadata

 一些metadata的填写还是很简单的，不过需要注意上面的 `attr:` 和 `file:` 写法。attr可以提取本模块的某些属性信息，而可用于提取某文件的内容。

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



#### options

options这里除了上面已经提到的一些，其他的都略过讨论了，一般只在某些特殊情况下才会使用到。

entry_point
: 

```text
entry_points = {
'console_scripts' :[ 'zwc=zwc.zwc:main',],
}
```

其中zwc是你的shell调用的名字，然后zwc是你的模块，另外一个zwc是你的主模块的子模块，然后main是其中的main函数。这就是你的shell调用程序的接口了。类似的还有gui_script可以控制你调用GUI图形的命令入口。

include_package_data

: 一般推荐设置为 True，然后通过 `MANIFAST.in` 文件来管理各个数据文件。

install_requires
: 接受字符串的列表值，将你依赖的可以通过pip安装的模块名放入进去，然后你的软件安装会自动检测并安装这些依赖模块。

package_data

: 你的软件的模块额外附加的（除了py文件的）其他文件，具体设置类似这样 `{"skeleton":['*.txt'],}` 其中skeleton这里就是具体的你的软件的模块（对应的文件夹名），然后后面跟着的就是一系列的文件名列表，可以接受glob语法。注意这里只能包含你的模块文件夹也就是前面通过packages控制的文件夹下面的内容。



#### 不推荐使用的选项

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

data_files已经不推荐使用了，推荐用`MANIFAST.in`来管理，可以方便用pkg_resources里面的方法来引用其中的资源文件。

### 读取资源文件

如下所示：

```
from pkg_resources import resource_filename
resource_stream('wise','icos/Folder-Documents.ico')
```


第一个参数是模块名字，第二个参数是模块中的文件的相对路径表达。

上面的例子是resource_filename，返回的是引用的文件名。此外还有命令：resource_string，参数和resource_filename一样，除了它返回的是字节流。这个字节流可以赋值给某个变量从而直接使用，或者存储在某个文件里面。

### pip的develop模式

本小节参考了 [这个问题](https://stackoverflow.com/questions/19048732/python-setup-py-develop-vs-install) 。

对于其他第三方包你不需要修改的，就直接 python setup.py install 就是了，而对于你自己写的包，可能需要频繁变动，最好是加载引用于本地某个文件夹，那么推荐是采用 python setup.py develop 命令来安装。develop模式下你修改了你的模块源码是直接生效的，因为安装过程只是提供了一个引用链接，实际还是用的你的源码这边的代码。

`python setup.py install` 对应的是 `pip install .` 命令，如果你没有setup.py这个文件了那么可以使用这个命令来从本地源码安装。develop模式对应的命令是： `pip install -e .`  。


### 在pypi上传你的模块

#### 正确处理README文档

现在pypi已经支持markdow文档格式了。推荐按照官方文档 [这里](<https://packaging.python.org/guides/making-a-pypi-friendly-readme/> ) 来处理：

```python
long_description = file: README.md
long_description_content_type=text/markdown
```

注意上面配置的 `long_description_content_type` ，如果你喜欢 `reStructuredText` 格式，那么设置为 `text/x-rst` 即可。

#### 打包模块

首先推荐升级最新的setuptools，wheel和twine模块。

然后直接用下面这句：

```text
python setup.py sdist bdist_wheel
```

这样将直接dist文件夹下面生成源码tar包和wheel包。

没有`setup.py` 的项目【<u>也就是采用setup.cfg新式管理方式的项目</u>】**需要安装 `build` 模块**，然后运行 `python -m build` 。

然后推荐运行下：

```text
twine check dist/*
```

来确保你的文档格式没问题。

#### 使用twine上传

使用twine上传到pypi很简单：

```text
twine upload dist/*
```

你每次都需要输入用户名和密码，你可以安装 `keyring` 模块，然后运行：

```text
keyring set https://upload.pypi.org/legacy/ your-username
```

来本地安全保存你的用户名和密码。

### pypi下载使用国内源

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



### pypi只下载软件源文件

下载pypi上的目标软件源文件而不是安装。参考了 [这个网页](http://stackoverflow.com/questions/7300321/how-to-use-pythons-pip-to-download-and-keep-the-zipped-files-for-a-package) 。

```text
pip install --download="/pth/to/downloaded/files" package_name
```
