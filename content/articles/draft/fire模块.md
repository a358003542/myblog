Title: fire模块
Slug: fire-module
Status: draft
[TOC]

## 前言

初次接触 [fire模块](https://github.com/google/python-fire) 就不自觉的和 [click模块](https://github.com/pallets/click) 进行对比，老实说我一开始还真不太相信这是google团队的作品，google团队的产品会这么简洁，不过毕竟后面写着 ： `This is not an official Google product.`

首先说下fire模块的优点，这个初步了解一下优点是很明显的： 可以让你少写点代码。作为一个程序员最大的愿望是什么： 少写点代码就能把事办成了。当然继续往下说，fire模块可以让你的代码更简洁，现在真的一个python脚本就是一个命令行工具了，一句废话都没有了，包括函数类里面的文档定义都是有用的。就作为一般最简单的命令行需求，我是推荐fire模块的。

但是fire模块目前github上 commit很少，版本号也才 0.1.2，可能模块还有很多不稳定或者bug都是可能的，如果读者在项目需求上只是一两个python脚本需要做成命令行工具，我还是推荐click模块。如果读者有大量的python脚本转成命令行工具的需求，这在目前数据处理工作越来越多的大环境（实际上我怀疑这也是他们开发fire模块的初衷），那么使用fire模块无疑是能省点力气的，毕竟当初人们觉得click模块方便那也是只是相对于写一个命令行工具而言，现在情况确实有所不同了。

```bash
pip install fire
```

官方文档已经说的很详细了，本身使用是很简单的，下面我随便说说吧。

## 第一个例子

```python

import fire

def hello(name):
    return 'hello {name}.'.format(name=name)

def main():
    fire.Fire()

if __name__ == '__main__':
    main()
```

### 查看帮助信息

你需要在前面加上一个分隔符 `--` 然后再跟上 `--help` 或者 `-h` 才会显示帮助信息。

```
Usage:       test.py
             test.py fire
             test.py hello
             test.py main
```

我们看到 main 函数 fire 模块 hello 都暴漏出来了，这不太好。可以稍微改造一下，把文件名改为 hello.py

```python
import fire

def hello(name):
    return 'hello {name}.'.format(name=name)

if __name__ == '__main__':
    fire.Fire(hello)
```

这样：

```
PS C:\Users\a3580\Desktop> python .\hello.py -- --help

Usage:       hello.py NAME
             hello.py --name NAME
```

这种写法的好处就是控制只显示你想要的几个函数，而且输出少了很多乱七八糟的东西。如果你想写多个命令，可以这样：

### 多个命令

```python
import fire

def hello(name):
    return 'hello {name}.'.format(name=name)

def bang():
    return 'bang'


if __name__ == '__main__':
    fire.Fire({
        'hello': hello, 
        'bang': bang
    })
```

```
PS C:\Users\a3580\Desktop> python .\hello.py -- --help
Type:        dict
String form: {'hello': <function hello at 0x000001ED71FB2E18>, 'bang': <function bang at 0x000001ED740A5620>}
Length:      2

Usage:       hello.py
             hello.py hello
             hello.py bang
```

也许这样会更好一点，免得烂七八杂的东西混进来了。

不过本着尽量少些代码的追求，多个命令这样写也不错啊：

```python
def hello(name):
    """
    打印hello
    """
    return 'hello {name}.'.format(name=name)

def bang():
    """
    打印bang
    """
    return 'bang'

if __name__ == '__main__':
    import fire
    fire.Fire()
```

总之fire模块会把你定义的函数或者类（包括类里面的属性或者函数或者类）都暴露出来。



## 挂载类

fire模块挂载类不需要实例化，似乎是fire自动实例化了，然后你还可以指定实例化的参数：

```python
class Hello():
    def __init__(self, punctuation):
        self.punctuation = punctuation
    def hello(self, name):
        """
        打印hello
        """
        return 'hello {name}{p}'.format(name=name,p=self.punctuation)

    @staticmethod
    def bang():
        """
        打印bang
        """
        return 'bang'


if __name__ == '__main__':
    import fire
    fire.Fire(Hello)
```



```
PS C:\Users\a3580\Desktop> python .\hello.py hello world --punctuation=!
hello world!
```

总的感觉fire模块在开发前期可以让程序员写命令行工具省点心，专心在代码的编写上，后期有时间和精力觉得还是用click代码来实现更友好的命令行界面等。

