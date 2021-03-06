Slug: python-tutorial
Tags: python,
Date: 20191018
Modified: 20210117

[TOC]

## 初识python

Python是个成功的脚本语言。它最初由Guido van Rossum开发，在1991年第一次发布。Python由ABC和Haskell语言所启发。Python是一个高级的、通用的、跨平台、解释型的语言。一些人更倾向于称之为动态语言。它很易学，Python是一种简约的语言。它的最明显的一个特征是，不使用分号或括号，Python使用缩进。现在，Python由来自世界各地的庞大的志愿者维护。

python现在主要有两个版本区别，python2和python3。作为新学者推荐完全使用python3编程，本文档完全基于python3。

### 安装和配置

python的安装和配置在linux没什么好说了，windows下的安装主要是编辑好系统环境变量 `PATH` 值，好让读者可以在cmd或者powershell下调用python命令。

![img]({static}/images/python/python-env-windows.png "python在windows下PATH环境变量的配置")

这个初次安装的时候程序有这个选项的。

### 进入python的REPL环境

在终端中输入python即进入python语言的REPL环境，很多linux系统目前默认的是python2。你可以运行：

    python  --version

来查看默认的python版本号。

要进入python3在终端中输入python3即可。

### python命令行用法

命令行的一般格式就是：

```text
python3  [可选项]  test.py  [可选参数1 可选参数2]
```

同样类似的运行 `python3  --help`
即可以查看python3命令的一些可选项。比如加入**-i**选项之后，python执行完脚本之后会进入REPL环境继续等待下一个命令，这个在最后结果一闪而过的时候有用。

#### python执行脚本参数的传递

上面的命令行接受多个参数都没有问题的，不会报错，哪怕你在py文件并没有用到他们。在py文件中要使用他们，首先导入sys模块，然后sys.argv\[0\]是现在这个py文件在系统中的文件名，接下来的sys.argv\[1\]就是之前命令行接受的第一个参数，后面的就依次类推了。

### 代码注释

python语言的注释符号和bash语言（linux终端的编程语言）一样用的是\#符号来注释代码。然后py文件开头一般如下面代码所示：

    #!/usr/bin/env python3
    #-*-coding:utf-8-*-

其中代码第一行表示等下如果py文件可执行模式执行那么将用python3来编译[^1]，第二行的意思是py文件编码是utf-8编码的，python3直接支持utf-8各个符号，这是很强大的一个更新。

多行注释可以利用编辑器快速每行前面加上\#符号。

#### Unicode码支持

python3是可以直接支持Unicode码的，读者请实验下面这个小例子，这将打印一个笑脸符号：

    #!/usr/bin/env python3
    #-*-coding:utf-8-*-
    print('\u263a')
    
    ☺
    >>> 

上面的数字就是笑脸符号具体的Unicode码（十六进制）。

### 代码多行表示一行

这个技巧防止代码越界所以经常会用到。用反斜线 `\` 即可。不过更常用的是将表达式用圆括号 `()` 括起来，这样内部可以直接换行并继续。在python中任何表达式都可以包围在圆括号中。

#### 一行表示多行

python中一般不用分号，但是分号的意义大致和bash或者c语言中的意义类似，表示一行结束的意思。其中c语言我们知道是必须使用分号的。

### 输入和输出

input函数请求用户输入，并将这个值赋值给某个变量。注意赋值之后类型是字符串，但后面你可以用强制类型转换——int函数（变成整数），float函数（变成实数）——将其转成你想要的数据类型。

print函数就是编程语言中常见的的屏幕显示输出函数。

读者请运行下面的例子：
```
x=input('请输入一个实数：')
string='你输入的这个实数乘以2等于：'+ str(float(x)*2)
print(string)
```
### \_\_main\_\_和\_\_name\_\_

按照[这个网站](http://stackoverflow.com/questions/419163/what-does-if-name-main-do)的讲解，如果当前这个py文件是被执行的，那么`__name__`在本py文件中的值是`__main__`，如果这个py文件是被作为模块引入的，那么`__name__`在那个py文件中的值是本py文件作为模块的模块名。

比如说现在你随便新建一个test.py文件，这个py文件里面就简单打印`__name__`的值，然后我们再打开终端，运行：
```
python test.py
```
这个时候打印的是： `__main__` 。而如果你进入python的REPL环境，再输入：
`import test`

这个时候你会发现`__name__`的值是字符 "test"。

如果是mymodule模块里的mymod.py文件（也就是新建一个mymodule文件夹，里面再新建一个mymod.py文件。），那么mymod.py文件里面其`__name__`的值是 "mymodule.mymod"。



### 从源码编译python

本部分算是偏高级点的知识，这里主要讨论如何在windows系统下从源码编译出python，linux系统下反而会略微直观简单点。

这里笔者并不是闲的没事，从源码编译出python这个过程有助于我们更深入地学习python，而这也是阅读和学习python源码的必由之路。

首先当然是下载CPython的源码，选择一个你喜欢的版本，这里以python3.7为例，那么应该进而下载visual studio 2017。

visual studio2017安装桌面端C++开发环境和python开发环境，然后把python本地开发组件勾选上。

用visual studio打开源码里面 `PCbuild` 里的 `pcbuild.sln` 。你可以使用 `.\build.bat  -p x64` 来编译出64位python，不带`-p` 参数默认编译出32位。一开始可以使用这个来测试下看看能不能编译成功，后面再使用visual studio编译，毕竟后面的重点还是利用visual studio来学习CPython的源码。

`build.bat` 会自动调用 `get_externals.bat` 这个脚本来下载一些第三方组件，建议下执行下这个脚本看看，如果下载实在有问题可以参考 [这个Github项目](https://github.com/python/cpython-source-deps) 。执行后下载内容在 `externals` 文件夹哪里，可以保存起来方便后续使用。

visual studio的`生成->配置管理器`那里可以选择Debug或者Release，win32或者x64等。

这些依赖在linux下编译一样是需要的，如果报错什么 `ssl.h` 找不到或者 `_sqlite3` 找不到就是这些依赖的缺失问题。

更多关于python源码的知识请参阅后面的python源码学习一章。



## 程序中的操作对象

python和c语言不同，c 是 `int x = 3` ，也就是这个变量是整数啊，字符啊什么的都要明确指定，python不需要这样做，只需要声明 `x ＝ 3` 即可。但是我们知道任何程序语言它到最后必然要明确某一个变量（这里也包括后面的更加复杂的各个结构对象）的内存分配，只是python语言帮我们将这些工作做了。

    ''' 这是一个多行注释
        你可以在这里写上很多废话
    '''
    x = 10
    print(x,type(x))

python程序由各个模块（modules）组成，模块就是各个文件。模块由声明（statements）组成，声明由表达式（expressions）组成，表达式负责创造和操作对象（objects）。在python中一切皆对象。python语言内置对象有：数值、字符串、列表、数组、字典、文件、集合等，这些后面会详细说明之。

### 赋值

python中的赋值语法非常的简单，`x=1` ，就是一个赋值语句了。和c语言不同，c是必须先声明`int x` 之类，开辟一个内存空间，然后才能给这个x赋值。而python的 `x=1` 语句实际上至少完成了三个工作：

1. 判断1的类型（动态类型语言必须要有这步）
2. 把这个类型的对象存储在内存里面
3. 创建x这个名字和将这个名字指向这个内存

#### 序列赋值

    x,y=1,'a'
    [z,w]=['b',10]
    print(x,y,z,w)
    
    1 a b 10
    >>> 

我们记得python中表达式可以加上圆括号，所以这里`x,y`产生的是一个数组`(x,y)`，然后是对应的数组平行赋值，第二行是列表的平行赋值。这是一个很有用的技巧。

在其他语言里面常常会介绍swap函数，就是接受两个参数然后将这两个参数的值交换一下，交换过程通常要用到临时变量。而在python中不需要再创建一个临时变量了，因为序列赋值会自动生成一个临时的右边的序列（其中的变量都对应原来的原始值），然后再赋值（这里强调一一对应是指两边的序列长度要一致。）

##### 交换两个元素

在python中交换两个元素用序列赋值形式是很便捷的：

    >>> x = 1
    >>> y = 2
    >>> x,y = y,x
    >>> print(x,y)
    2 1

这个过程显然不是先执行x=y然后执行y=x，如上所述的，程序首先右边创建一个临时的序列，其中的变量都对应原来的值，即`x,y=(2,1)`，然后再进行序列赋值。

#### 同时赋相同的值

    x=y='a'
    z=w=2
    print(x,y,z,w)
    
    a a 2 2
    >>> 

这种语句形式c语言里面也有，不过内部实现机制就非常的不一样了。python当声明x=y的时候，x和y只是不同的变量名，但都指向同一块内存值。也可以说x和y就是一个东西，只是取的名字不同罢了。

我们用is语句[^2]来测试，显示x和y就是一个东西。

    >>> x=y='a'
    >>> x is y
    True
    >>> x == y
    True

但如果写成这种形式：

    >>> x = 'a'
    >>> y = 'a'
    >>> x is y
    True

x和y还是指向的同一个对象，关于这点python内部是如何实现的我还不太清楚【一个一般的原则是如果右边的这个对象是不可变的，那么python会尽可能让x和y指向同一内存值。】。为了说明is语句功能正常这里再举个例子吧：

    >>> x = [1,2,3]
    >>> y = [1,2,3]
    >>> x == y
    True
    >>> x is y
    False

我们看到这里就有了两个列表对象。

#### 增强赋值语句

`x=x+y` 可以写作 `x += y` 。类似的还有：

```
   +=    &=    >>=
   
   -=    |=    <<=
   
   *=   ^=   **=
   
   /=    %=    //=
```


#### 可迭代对象的迭代赋值

在我们对python语言有了深入的了解之后，我们发现python中迭代思想是深入骨髓的。我们在前面接触了序列的赋值模式之后，发现似乎这种赋值除了临时创建右边的序列之外，还似乎与迭代操作有关，于是我们推测python的这种平行赋值模式可以扩展到可迭代对象，然后我们发现确实如此！

    >>> x,y,z= map(lambda x : x+2,[-1,0,1])
    >>> print(x,y,z)
    1 2 3

最后要强调一点的是确保左边的变量数目和后面的可迭代对象的输出元素数目是一致的，当然进一步扩展的序列解包赋值也是支持的：

    >>> x,y,*z= map(lambda x : x+2,[-1,0,1,2])
    >>> print(x,y,z)
    1 2 [3, 4]

通配赋值，我喜欢这样称呼，通配之后收集的元素在列表里面；而函数参数的通配传递，收集的元素是在元组里面。

最后我们总结到，可迭代对象的赋值就是迭代操作加上各个元素的一对一的赋值操作。

### 数值

python的数值的内置类型有：int，float，complex等[^3]。python的基本算术运算操作有加减乘除（+ - \* /）。然后 `=` 表示赋值，然后是中缀表达式和优先级和括号法则等，这些都是一般编程语言说到烂的东西了。

    print((1+2)*(10-5)/2)
    print(2**100)

#### 进位制

二进制的数字以 `0b`（零比）开头，八进制的数字以 `0o`（零哦）开头，十六进制的数字以 `0x`（零艾克斯）开头。

    0b101010, 0o177, 0x9ff

以二进制格式查看数字使用 `bin` 命令，以十六进制查看数字使用 `hex` 命令。

    >>> bin(42)
    '0b101010'
    >>> hex(42)
    '0x2a'

下面写上一个进制转换小程序：

```python
number=input("请输入一个数字：")
number= eval(number)
#
radix= input('''请输入你想转换的进制系统
2   表示  二进制
8   表示  八进制
16  表示  十六进制
''')
radix =eval(radix)

while True:
    if radix == 2:
        print(bin(number))
        break
    elif radix == 8:
        print(oct(number))
        break
    elif radix == 16:
        print(hex(number))
        break
    else:
        print("sorry you input the wrong radix")
```

程序运行的情况如下所示：

```text
请输入一个数字：20
请输入你想转换的进制系统
2   表示  二进制
8   表示  八进制
16  表示  十六进制
8
0o24
```

此外字符串的format方法也提供了类似的功能。

#### 不要用eval

上面的例子用了eval这个函数，这非常的不好，非常的不安全，总的来说不应该使用eval函数。如果在某些情况下，你确实想要使用eval，那么也应该使用ast模块的`literal_eval` 函数。如下所示，这个函数试着接受一个字符串，将其转成python里面的对象：

    import ast
    def str2pyobj(val):
        '''str to python obj or not changed'''
        try:
            val = ast.literal_eval(val)
        except Exception:###
            pass
        return val

支持的python object有: strings, bytes, numbers, tuples, lists, dicts, sets, booleans, and None.

比如 "1"， "3.14"， "[1,2,3]" 将分别转化成为integer，float，和list。

#### int函数比你想的更强大

int函数用于强制类型转换的时候，可以将一个类数值字符串变成integer，但这个函数还隐藏了一个强大的功能，那就是其还有第二个可选参数，进位制。

```python
>>> int('a', base=16)
10
>>> int('0xa', base=16)
10
```

上面的效果就是将一个十六进制的字符按照十六进制处理之后再输出一个十进制的数值。

#### 进制转换问题总结

当我们说一个数在计算机里面，它都是以二进制形式存储的，也正是这个根源就一般数值类型来说实际上是实现不了我们预想的那种四舍五入操作的函数的，最多只能实现一种近似的版本。而在python这边我们说 `number=10` 或者 `number=0xa` ，number最终是存储了一个数值，当我们要求输出显示number的时候其都是以十进制的形式显示，于是就有了 `bin` ，`oct` 和 `hex` 这三个函数来获得另外进制输出显示的效果。

因为这个过程是将一个数值类型转成字符串类型，或者format方法也提供了这样的功能支持，具体对应关系如下：

```
f'{number:b}'  bin(number)
f'{number:o}'  oct(number)
f'{number:d}'  number
f'{number:x}'  hex(number)
```

format方法的输出没有进制标识前缀。

前面的例子我们说输入10，input获得的值都会保存为字符串。然后我们说eval成python内部的对象，也就是整型。eval或者literal_eval函数的一个好处就是你写上 `"0xa"`，其转成python对象自动将其转成十进制数值了。这个操作过程更确切的定义是将一个字符串类型转换成integer整型，而这恰好就是int函数负责的部分，于是我们发现这个过程用int函数处理会更合适，并继而我们发现int函数原来也可以很好地处理不同进制的字符串的输入问题，不过需要你额外指明该字符串代表的数值的进制。

```
number = int(number, input_radix)
```

于是上面的进制转换小程序改写如下：

```python

user_input = input("请输入一个数字和该数字的进制，以空格分开。")
number, in_radix = user_input.split()

number = int(number, int(in_radix))

out_radix = input('''请输入你想转换的进制系统
2   表示  二进制
8   表示  八进制
16  表示  十六进制
''')
out_radix = int(out_radix)

while True:
    if out_radix == 2:
        print(bin(number))
        break
    elif out_radix == 8:
        print(oct(number))
        break
    elif out_radix == 16:
        print(hex(number))
        break
    else:
        print("sorry you input the wrong radix")
```



#### 数学幂方运算

$x^y$，x的y次方如上面第二行所述就是用`x**y`这样的形式即可。此外pow函数作用是一样的，`pow(x,y)`。

#### 数值比较

数值比较除了之前提及的 >，<，==之外，\>=，<=，!=也是有的（大于等于，小于等于，不等于）。此外python还支持连续比较，就是数学格式 $a<x<b$ ，x在区间 $(a,b)$ 的判断。在python中可以直接写成如下形式：`a<x<b`。这实际实现的过程就是两个比较操作的进一步与操作。虽然python支持这种写法，但个人建议写成 `x < b && x > a` 这样会更具有编程语言上的通用性。

#### 相除取商或余

就作为正整数相除使用 `x//y` 得到的值意义还是很明显的就是**商**。相关的还有**取余**数，就是`x%y`，【这个百分号在其他编程语言里面对应那个mod函数，也就是取模操作，在数学上就是取余数的含义。】这样就得到x除以y之后的余数了。

#### 复数

python直接支持复数，复数的写法是类似`1+2j`这样的形式，然后如果z被赋值了一个复数，这样它就是一个复数类型，那么这个类具有两个属性量，**real**和**imag**。也就是使用`z.real`就给出这个复数的实数部。imag是imaginary number的缩写，虚数，想像出来的数。

#### abs函数

大家都知道abs函数是绝对值函数，这个python自带的，不需要加载什么模块。作用于复数也是可以的：

    z=3+4j
    print(z.real,z.imag)
    print(abs(z))

这个和数学中复数绝对值的定义完全一致，也就是复数的模：
$\left| z \right| =\sqrt { a^{ 2 }+b^{ 2 } }$

#### round函数

    >>> round(3.1415926)
    3
    >>> round(3.1415926,0)
    3.0
    >>> round(3.1415926,1)
    3.1
    >>> round(3.1415926,2)
    3.14
    >>> round(3.1415926,4)
    3.1416

第二个参数接受0或者负数多少有点没意义了，一般使用还是取1或大于1的数吧，意思就是保留几位小数。

round函数初看起来似乎是实现了数学上的四舍五入取整，但实际上并不确切。比如：

```
>>> round(0.5)
0
>>> round(1.5)
2
>>> round(2.5)
2
>>> round(3.5)
4
>>> round(4.5)
4
>>> round(5.5)
6
>>> round(6.5)
6
```

round函数返回的是距离该浮点数最近的那个整数，但计算机里面并没有那种所谓的确切的小数，请看下面这个例子：

```
>>> 0.1+0.1+0.1 == 0.3
False
>>> round(0.1+0.1+0.1,20) == round(0.3,20)
False
>>> round(0.1+0.1+0.1,15) == round(0.3,15)
True
```

计算机表示浮点数比如0.3都是用二进制来表示的，所以只可能获得一个无限接近于0.3的数值而不是十进制里面的那个确切的0.3。这也就是上面round函数对于1.5或者2.5等中间值没有采用一致策略的原因，因为round函数如上所示设计的目的不是用来实现数学上的四舍五入的，而是用来判断计算机世界里面浮点数是否近似相等的。

具体取整上的round策略有很多种，请参见 [这篇文章](https://realpython.com/python-rounding/)。 比如一种近似的四舍五入函数：

```
def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier
```

但正如前面谈论了，如果你想要实现的那个精确的四舍五入，那么上面这个函数也是有错误的。最好还是采用python的decimal来表达精确的小数。

```
>>> round_half_up(2.5)
3.0
>>> round(2.5)
2
```

round_half_up这个函数之所以能够部分有效，是因为2.5精度以下的偏差通过0.5的残余精度下的数值得到了修补。但如果：

```
>>> round_half_up(2.4999999999999999)
3.0
>>> round_half_up(2.499999999999999)
2.0
```

所以round_half_up只是说在浮点数精度下能够实现大致的四舍五入效果了。



#### min，max和sum函数

min，max函数的用法和sum的用法稍微有点差异，简单起见可以认为min，max，sum都接受一个元组或者列表，然后返回这个元组或者列表其中的最小值，最大值或者相加总和。此外min和max还支持 `min(1,2,3)` 这样的形式，而sum不支持。

    >>> min((1,6,8,3,4))
    1
    >>> max([1,6,8,3,4])
    8
    >>> sum([1,6,8,3,4])
    22
    >>> min(1,6,8,3,4)
    1

#### 位操作

python支持位操作的，这里简单说一下：位左移操作 `<<` ，位与操作 `&` ，位或操作 `|` ，位异或操作` ^` 。

    >>> x=0b0001
    >>> bin(x << 2)
    '0b100'
    >>> bin(x | 0b010)
    '0b11'
    >>> bin(x & 0b1)
    '0b1'
    >>> bin(x ^ 0b101)
    '0b100'

#### math模块

在`from math import *`之后，可以直接用符号 `pi` 和 `e` 来引用圆周率和自然常数。此外math模块还提供了很多数学函数，比如：

sqrt

:   开平方根函数，sqrt(x)。

sin

:   正弦函数，类似的还有cos，tan等，sin(x)。

degrees

:   将弧度转化为角度，三角函数默认输入的是弧度值。

radians

:   将角度转化位弧度，radians(30)。

log

:   开对数，log(x,y)，即$\log_y x$，y默认是e。

exp

:   指数函数，exp(x)。

pow

:   扩展了内置方法，现在支持float了。pow(x,y)

这里简单写个例子：

    >>> from math import *
    >>> print(pi)
    3.141592653589793
    >>> print(sqrt(85))
    9.219544457292887
    >>> print(round(sin(radians(30)),1))#sin(30°)
    0.5

更多内容请参见[官方文档](http://docs.python.org/3/library/math.html)。

#### random模块

random模块提供了一些函数来解决随机数问题。

random

:   random函数产生0到1之间的随机实数（包括0）。
​    random()-\>\[0.0, 1.0)。

uniform

:   uniform函数产生从a到b之间的随机实数（a，b的值指定，包括a。）。
​    uniform(a,b)-\>\[a.0, b.0)。

randint

:   randint函数产生从a到b之间的随机整数，包含a和b。
​    randint(a,b)-\>\[a,b\]

choice

:   choice随机从一个列表或者字符串中取出一个元素。

randrange

:   randrange函数产生从a到b之间的随机整数，步长为c（a，b，c的值指定，相当于choice(range(a,b,c))。整数之间就用randint函数吧，这里函数主要是针对range函数按照步长从而生成一些整数序列的情况。

sample(p,k)

:   sample函数从p中随机选取唯一的元素（p一般是range(n)或集合之类的，这里所谓的唯一的意思就是不放回抽样的意思，但如果p样品里面有重复的元素，最后生成的列表还是会有重复的元素的。）然后组成k长度的列表返回。

下面是一个简单的例子：

    >>> from random import *
    >>> print(random())
    0.36882919781549717
    >>> print(uniform(1,10))
    2.771065174892699
    >>> print(randrange(1,6))
    1
    >>> print(randint(1,10))
    3
    >>> print(choice('abcdefghij'))
    j
    >>> print(choice(['1','2','3']))
    2

作为随机实数，所谓开始包含的那个临界值可能数学意义大于实际价值，你可以写一个类似下面的小脚本看一下，随机实数是很难随机到某个具体的数的。

    from random import *
    i = 0
    while True:
        x = uniform(0,2)
        if x == 0:
            print(i)
            break
        else:
            print(x)
            i += 1

从上一个例子我们看到，虽然我不确定具体随机到某个实数的概率是不是永远也没有可能，但肯定很小很小。所以如果我们要解决某个问题，需要某个确定的概率的话还是用随机整数好一些。

更多内容请参见[官方文档](http://docs.python.org/3/library/random.html)。

### 序列

字符串，列表，元组（tuple，这里最好翻译成元组，因为里面的内容不一定是数值。）都是序列（sequence）的子类，所以序列的一些性质他们都具有，最好在这里一起讲方便理解记忆。

#### len函数

len函数返回序列所含元素的个数：

    string001='string'
    list001=['a','b','c']
    tuple001=(1,2,3,4)
    
    for x in [string001,list001,tuple001]:
        print(len(x))
    
    6
    3
    4
    >>> 

#### 调出某个值

对于序列来说后面跟个方括号，然后加上序号（程序界的老规矩，从0开始计数。），那么调出对应位置的那个值。还以上面那个例子来说明。

    string001='string'
    list001=['a','b','c']
    tuple001=(1,2,3,4)
    
    for x in [string001,list001,tuple001]:
        print(x[2])
    
    r
    c
    3
    >>> 

#### 倒着来

倒着来计数-1表示倒数第一个，-2表示倒数第二个。依次类推。

    string001='string'
    list001=['a','b','c']
    tuple001=(1,2,3,4)
    
    for x in [string001,list001,tuple001]:
        print(x[-1],x[-2])
    
    g n
    c b
    4 3

#### 调出多个值

前面不写表示从头开始，后面不写表示到达尾部。中间加个冒号的形式表示从那里到那里。看来python区间的默认含义都是包头不包尾。这样如果你想要最后一个元素也进去，只有使用默认的不写形式了。

    string001='string'
    list001=['a','b','c']
    tuple001=(1,2,3,4)
    
    for x in [string001,list001,tuple001]:
        print(x[1:3],x[-2:-1],x[:-1],x[1:],x[1:-1])
    
    tr n strin tring trin
    ['b', 'c'] ['b'] ['a', 'b'] ['b', 'c'] ['b']
    (2, 3) (3,) (1, 2, 3) (2, 3, 4) (2, 3)

用数学半开半闭区间的定义来理解这里的包含关系还是很便捷的。

1.  首先是数学半开半闭区间，左元素和右元素都是之前叙述的对应的定位点。左元素包含右元素不包含。

2.  其次方向应该是从左到右，如果定义的区间是从右到左，那么将产生空值。

3.  如果区间超过，那么从左到右包含的所有元素就是结果，。

4.  最后如果左右元素定位点相同，那么将产生空值，比如：`string001[2:-4]`，其中2和-4实际上是定位在同一个元素之上的。额外值得一提的列表插入操作可以通过`list001[a:b]= [1]` 这种形式来实现，如果a,b是某一个定位点的话，结果相当于在a定位点之前插入目标列表 ，请参看列表的插入操作这一小节。

#### 序列反转

这是python最令人叹为观止的地方了，其他的语言可能对列表反转要编写一个复杂的函数，我们python有一种令人感动的方法。

    string001='string'
    list001=['a','b','c']
    tuple001=(1,2,3,4)
    
    for x in [string001,list001,tuple001]:
        print(x[::-1])
    
    gnirts
    ['c', 'b', 'a']
    (4, 3, 2, 1)

之前在range函数的介绍时提及序列的索引和range函数的参数设置很是类似，这是我们可以参考理解之，序列（列表，字符串等）的索引参数 `[start:end:step]` 和range函数的参数设置一样，第一个参数是起步值，第二个参数是结束值，第三个参数是步长。这里end不填都好理解，就是迭代完即可，不过如果step是负数，似乎起点不填默认的是-1。

然后range函数生成的迭代器对象同样接受这种索引参数语法，看上去更加的怪异了：

    >>> range(1,10,2)
    range(1, 10, 2)
    >>> range(1,10,2)[::-2]
    range(9, -1, -4)
    
    >>> list(range(1,10,2))
    [1, 3, 5, 7, 9]
    >>> list(range(1,10,2)[::-2])
    [9, 5, 1]

我们可以看到对range函数进行切片操作之后返回的仍然是一个range对象，经过了一些修正。似乎这种切片操作和类的某个特殊方法有关，和python的slice对象有关。

#### 序列的可更改性

字符串不可以直接更改，但可以组合成为新的字符串；列表可以直接更改；元组不可以直接更改。

#### 序列的加法和减法

两个字符串相加就是字符串拼接了。乘法就是加法的重复，所以一个字符串乘以一个数字就是自己和自己拼接了几次。列表还有元组和字符串一样大致情况类似。

    print('abc'+'def')
    print('abc'*3)
    print([1,2,3]+[4,5,6])
    print((0,'a')*2)
    
    abcdef
    abcabcabc
    [1, 2, 3, 4, 5, 6]
    (0, 'a', 0, 'a')

### 字符串

python语言不像c语言，字符和字符串是不分的，用单引号或者双引号包起来就表示一个字符串了。单引号和双引号并没有什么特别的区别，只是如果字符串里面有单引号，那么就使用双引号，这样单引号直接作为字符处理而不需要而外的转义处理------所谓转义处理和其他很多编程语言一样用\\符号。比如要显示`'`就输入`\'`。

#### 三单引号和三双引号

在单引号或者双引号的情况下，你可以使用`\n`来换行。此外还可以使用三单引号 `"'` 或者三双引号 `"""` 来包围横跨多行的字符串，其中换行的意义就是换行。

    print('''\
    这是一段测试文字
      this is a test line
          其中空白和    换行都所见所得式的保留。''')

#### startswith方法

    >>> x = 'helloABC'
    >>> x
    'helloABC'
    >>> x.startswith('hello')
    True
    >>> x.endswith('ABC')
    True

startswith

:   测试字符串是否以某个子字符串开始

endswith

:   测试某个字符串是否以某个子字符串结束

#### find方法

字符串的find方法可用来查找某个子字符串，没有找到返回-1，找到了返回字符串的偏移量。用法就是：`s.find('d')`。

#### replace方法

字符串的replace方法进行替换操作，接受两个参数：第一个参数是待匹配的子字符串，第二个参数是要替换成为的样子。

    >>> print('a b 11 de'.replace('de','ding'))
    a b 11 ding
    >>> print('1,1,5,4,1,6'.replace('1','replaced'))
    replaced,replaced,5,4,replaced,6

#### upper方法

将字符串转换成大写形式。

    >>> str='str'
    >>> str.upper()
    'STR'

类似的还有：

lower

:   都变成小写

capitalize

:   首字母大写，其它都小写。

#### isdigit方法

isdigit

:   测试是不是数字

isalpha

:   测试是不是字母

isalnum

:   测试是不是数字或字母



#### split方法

字符串的split方法可以将字符串比如有空格或者逗号等分隔符分割而成，可以将其分割成子字符串列表。默认是空格是分隔符。

    >>> string='a=1,b=2,c=3'
    >>> string.split(',')
    ['a=1', 'b=2', 'c=3']

##### splitline方法

把一个字符串按照行分开。这个可以用上面的split方法然后接受`\n`参数来实现，所不同的是splitline方法不需要接受参数：

    >>> string
    'this is line one\nthis is line two\nthis is line three'
    >>> string.splitlines()
    ['this is line one', 'this is line two', 'this is line three']
    >>> string.split('\n')
    ['this is line one', 'this is line two', 'this is line three']

#### join方法

字符串的join方法非常有用，严格来说它接受一个迭代器参数，不过最常见的是列表。将列表中的多个字符串连接起来，我们看到他采用了一种非常优雅的方式，就是只有两个字符串之间才插入某个字符，这正是我们所需要的。具体例子如下所示：

    >>> list001=['a','b','c']
    >>> "".join(list001)
    'abc'
    >>> ','.join(list001)
    'a,b,c'

#### strip方法

##### rstrip方法

字符串右边的空格都删除。换行符也会被删除掉。

##### lstrip方法

类似rstrip方法，字符串左边的空格都删除。换行符也会被删除掉。

#### format方法

字符串的format方法方便对字符串内的一些变量进行替换操作，其中花括号不带数字跟format方法里面所有的替换量，带数字0表示第一个替换量，后面类推。此外还可以直接用确定的名字引用。

    >>> print('1+1={0}，2+2={1}'.format(1+1,2+2))
    1+1=2，2+2=4
    >>> print('my name is {name}'.format(name='Jim T Kirk'))
    my name is Jim T Kirk

#### 转义和不转义

`\n    \t  `这是一般常用的转义字符，换行和制表。此外还有`\\`输出\\符号。

如果输出字符串不想转义那么使用如下格式：

    >>> print(r'\t \n \test')
    \t \n \test

#### count方法

统计字符串中某个字符或某一连续的子字符串出现的次数。

    >>> string = 'this is a test line.'
    >>> string.count('this')
    1
    >>> string.count('t')
    3

#### r什么的方法

rfind rindex rjust rsplit
，这些方法有时会很有用，而具体其含义的理解就对应于： find index ljust
split。

我想大家应该看一下就知道了，区别就是从右往左了。

### 列表

方括号包含几个元素就是列表。

#### 列表的插入操作 

字符串和数组都不可以直接更改所以不存在这个问题，列表可以。其中列表还可以以一种定位在相同元素的区间的方法来实现插入操作，这个和之前理解的区间多少有点违和，不过考虑到定位在相同元素的区间本来就概念模糊，所以在这里就看作特例，视作在这个插入吧。

    list001=['one','two','three']
    list001[1:-2]=['four','five']
    print(list001)
    
    ['one', 'four', 'five', 'two', 'three']

extend方法似乎和列表之间的加法重合了，比如 `list.extend([4,5,6])`就和 `list=list+[4,5,6]`是一致的，而且用加法表示还可以自由选择是不是覆盖原定义，这实际上更加自由。

insert方法也就是列表的插入操作：

    >>> list = [1,2,3,4]
    >>> list.insert(0,5)
    >>> list
    [5, 1, 2, 3, 4]
    >>> list.insert(2,'a')
    >>> list
    [5, 1, 'a', 2, 3, 4]

#### append方法

python的append方法就是在最后面加**一个元素**，如果你append一个列表那么这一个列表整体作为一个元素。然后append方法会永久的改变了该列表对象的值。

<u>记住，append等等原处修改列表的方法都是没有返回值的。</u>

```text
>>> list = [1,2,3,4]
>>> list.append(5)
>>> list
[1, 2, 3, 4, 5]
```

如果你希望不改动原列表的附加，请使用加法来操作列表。

#### reverse方法

reverse方法不接受任何参数，直接将一个列表翻转过来。如果你希望不改变原列表的翻转，有返回值，请如下使用或者使用 `reversed`函数：

    >>> list
    [1, 2, 3, 4, 5]
    >>> listNew = list[::-1]
    >>> list
    [1, 2, 3, 4, 5]
    >>> listNew
    [5, 4, 3, 2, 1]

#### copy方法

copy方法复制返回本列表。其是浅复制，也就是里面如果有引入别处的变量的话，那么新复制出来的列表里面的该元素变量仍然指向原来的内存值。

##### sort方法

也就是排序，改变列表。默认是递增排序，可以用**reverse=True**来调成递减排序。

默认的递增排序顺序如果是数字那么意思是数字越来越大，如果是字符那么（似乎）是按照ACSII码编号递增来排序的。如果列表一些是数字一些是字符会报错。

    >>> list = ['a','ab','A','123','124','5']
    >>> list.sort()
    >>> list
    ['123', '124', '5', 'A', 'a', 'ab']

sort方法很重要的一个可选参数**key=function**，这个function函数就是你定义的函数（或者在这里直接使用lambda语句。），这个函数只接受一个参数，就是排序方法（在迭代列表时）接受的当前的那个元素。下面给出一段代码，其中tostr函数将接受的对象返回为字符，这样就不会出错了。

    def tostr(item):
        return str(item)
    
    list001 = ['a','ab','A',123,124,5]
    
    list001.sort(key=tostr)
    
    print(list001)
    
    [123, 124, 5, 'A', 'a', 'ab']

#### sorted函数

sorted函数在这里和列表的sort方法最大的区别是它返回的是而不是原处修改。其次sorted函数的第一个参数严格来说是所谓的可迭代对象，也就是说它还可以接受除了列表之外的比如等可迭代对象。至于用法他们两个差别不大。

    >>> sorted((1,156,7,5))
    [1, 5, 7, 156]
    >>> sorted({'andy':5,'Andy':1,'black':9,'Black':55},key=str.lower)
    ['Andy', 'andy', 'black', 'Black']

上面第二个例子调用了**str.lower**函数，从而将接受的item，这里比如说'Andy'，转化为andy，然后参与排序。也就成了对英文字母大小写不敏感的排序方式了。

##### 字典按值排序

同样类似的有字典按值排序的方法[^4]：

    >>> sorted({'andy':5,'Andy':1,'black':9,'Black':55}.items(),key=lambda i: i[1])
    [('Andy', 1), ('andy', 5), ('black', 9), ('Black', 55)]

这个例子先用字典的items方法处理返回(key,value)对的可迭代对象，然后用后面的lambda方法返回具体接受item的值，从而根据值来排序。

##### 中文排序

下面这个例子演示了如何对中文名字排序。整个函数的思路就是用[pypinyin](https://github.com/mozillazg/python-pinyin)（一个第三方模块），将中文姓名的拼音对应出来，然后组成一个列表，然后根据拼音对这个组合列表排序，然后生成目标列表。

    list001=['张三','李四','王二','麻子','李二','李一']
    def zhsort(lst):
        from pypinyin import  lazy_pinyin
        pinyin=[lazy_pinyin(lst[i]) for i in range(len(lst))]
        lst0=[(a,b) for (a,b) in zip(lst,pinyin)]
        lst1= sorted(lst0, key=lambda d:d[1])
        return [x[0] for x in lst1]
    print(zhsort(list001))
    
    ['李二', '李四', '李一', '麻子', '王二', '张三']

#### reversed函数

前面提到过序列反转可以这样做:

    lst[::-1]

不过更加推荐的做法是直接用reversed函数来做，reversed函数返回的是个可迭代对象。

    string001='string'
    list001=['a','b','c']
    tuple001=(1,2,3,4)
    
    for x in [string001,list001,tuple001]:
        print(list(reversed(x)))
    
    ['g', 'n', 'i', 'r', 't', 's']
    ['c', 'b', 'a']
    [4, 3, 2, 1]

然后我们马上就想到，列表有 `reverse`
方法，其是破坏型的方法，然后类似的还有 `sort`
方法，破坏型的，其对应非破坏型方法有 `sorted`
。一般使用没有特别需求时都应该使用非破坏型方法，reversed，sorted等等。

#### 删除某个元素

-   赋空列表值，相当于所有元素都删除了。

-   pop方法：接受一个参数，就是列表元素的定位值，然后那个元素就删除了，方法并返回那个元素的值。如果不接受参数默认是删除最后一个元素。

-   remove方法：移除第一个相同的元素，如果没有返回相同的元素，返回错误。

-   del函数：删除列表中的某个元素。
```
    >>> list001=['a','b','c','d','e']
    >>> list001.pop(2)
    'c'
    >>> list001
    ['a', 'b', 'd', 'e']
    >>> list001.pop()
    'e'
    >>> list001
    ['a', 'b', 'd']
    >>> list001.remove('a')
    >>> list001
    ['b', 'd']
    >>> del list001[1]
    >>> list001
    ['b']
```
#### count方法

统计某个元素出现的次数。

    >>> list001=[1,'a',100,1,1,1]
    >>> list001.count(1)
    4

#### index方法

index方法返回某个相同元素的偏移值。

    >>> list001=[1,'a',100]
    >>> list001.index('a')
    1

#### 列表解析

我们来看下面这个例子：

    def square(n):
        return n*n
        
    print(list(map(square,[1,2,3,4,5])))
    print([square(x) for x in [1,2,3,4,5]])
    
    [1, 4, 9, 16, 25]
    [1, 4, 9, 16, 25]

map函数将某个函数应用于某个列表的元素中并生成一个map对象（可迭代对象），需要外面加上list函数才能生成列表形式。第二种方式更有python风格，是推荐使用的列表解析方法。

在python中推荐多使用迭代操作和如上的列表解析风格，因为python中的迭代操作是直接用c语言实现的。

##### 列表解析加上过滤条件

for语句后面可以跟一个if子句表示过滤条件，看下面的例子来理解吧：

    >>> [s*2 for s in ['hello','abc','final','help'] if s[0] == 'h']
    ['hellohello', 'helphelp']

这个例子的意思是列表解析，找到的元素进行乘以2的操作，其中过滤条件为字符是h字母开头的，也就是后面if表达式不为真的元素都被过滤掉了。

##### 完整的列表解析结构

下面给出一个完整的列表解析结构，最常见的情况一般就一两个for语句吧，这里if外加个括号是可选项的意思。

    [ expression for var1 in iterable1 [if condition1 ]
                        for var2 in iterable2 [if condition2 ]
                        ........
                                ]

这里的逻辑是从左到右第一个for语句就是最先执行的for语句，然后是第二个for语句跟着执行。

这里的iterable1是指某个可迭代对象，也就是说那些能够返回可迭代对象的函数比如map，filter，zip，range等函数都可以放进去。不过我们要克制自己在这里别写出太过于晦涩的程序了。还有for循环语句也别嵌套太多了，这样极容易出错的。

下面这个程序大家看看：

    >>> [x+str(y) for x in ['a','b','c'] for y in [1,2,3,4,5,6] if y & 1]
    ['a1', 'a3', 'a5', 'b1', 'b3', 'b5', 'c1', 'c3', 'c5']
    >>> [x+str(y) for x in ['a','b','c'] for y in [1,2,3,4,5,6] if not  y & 1]
    ['a2', 'a4', 'a6', 'b2', 'b4', 'b6', 'c2', 'c4', 'c6']



##### 列表解析的好处

在熟悉列表解析的语句结构之后，一两个for语句不太复杂的情况下，还是很简单明了的。同时语法也更加精炼，同时运行速度较for循环要至少快上一倍。最后python的迭代思想深入骨髓，以后python的优化工作很多都围绕迭代展开，也就是多用列表解析会让你的代码以后可能运行的更快。

有这么多的好处，加上这么cool的pythonic风格，推荐大家多用列表解析风格解决问题。

##### 元组的生成

这个时候需要明确加个括号表示这是一个元组对象。

    >>> [(x,x**2) for x in range(5)]
    [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16)]

#### for语句中列表可变的影响

一般情况for迭代某个可迭代对象就是可迭代对象返回一个值然后利用这个值赋值并进行下面的操作，但是列表却是一个可变的东西，如果列表在操作中被修改了，情况会怎样呢？

    lst = [1,2,3,4,5]
    index = 0
    for x in lst:
        lst.pop(index)
        print(x)
    
    1
    3
    5

具体这个过程的细节我不清楚，但确定的是在这里for语句并没有记忆原列表，而只是记忆了返回次数或者偏移值。在实践中不要写出类似上面的变动的迭代循环风格，这样很容易出bug。

#### 列表元素替换

推荐用列表解析方法来实现列表元素的替换功能。

    def replace(x,a,b):
        if x == a:
            return b
        else:
            return x
    
    lst=[1,5,4,1,6]
    
    >>> [replace(i,1,'replaced') for i in lst]
    ['replaced', 5, 4, 'replaced', 6]

#### 列表元素去重

列表元素去重推荐用后来的set集合对象来处理之，其会自动去除重复的元素。

    >>> lst = [1,2,3,4,5,1,2,3,4,5]
    >>> [i for i in set(lst)]
    [1, 2, 3, 4, 5]

### 元组

圆括号包含几个元素就是元组(tuple)。元组和列表的不同在于元组是不可改变。元组也是从属于序列对象的，元组的很多方法之前都讲了。而且元组在使用上和列表极其接近，有很多内容这里也略过了。

值得一提的是如果输入的时候写的是*x,y*这样的形式，实际上表达式就加上括号了，也就是一个元组了*(x,y)*。

#### 生成器表达式

类似列表解析，如果元组在这里解析也是返回的元组吗？这里并不是如此，前面谈到python中一般表达式的圆括号是忽略了的，所以这里的元组解析表示式有个更专门的名字叫做生成器表达式，它返回的是生成器对象，和生成器函数具体调用之后返回的对象是一样的。生成器对象具有`__next__`方法，可以调用next函数。

    >>> x = [i for i in [1,2,3]]
    >>> x
    [1, 2, 3]
    >>> y = (i for i in [1,2,3])
    >>> y
    <generator object <genexpr> at 0xb70dbe8c>

### 字典

与列表一样字典是可变的，可以像列表一样引用然后原处修改，del语句也适用。

并非所有对象都可以做字典key，在python中所有的内置不可变对象都是可散列的，所有的可变对象都是不可散列的。而只有可散列的才可以做字典的key。可散列的对象具有：

- 具有 `__hash__` 方法，这样可以比较大小
- 具有 `__eq__` 方法，这样可以判断相等。

这里值得一提的就是元组是可以做字典的key的。首先说一下元组是如何比较大小的：

#### 元组和列表的比较大小

元组和列表的相等判断还是很好理解的，而对于这样的东西:

    >>> (1,-1) < (2,-2)

确实就有点古怪了。请读者参考[这个网页](http://stackoverflow.com/questions/5292303/python-tuple-comparison))，按照官方文档的说明：

> Tuples and lists are compared lexicographically using comparison of
> corresponding elements. This means that to compare equal, each element
> must compare equal and the two sequences must be of the same type and
> have the same length.

官方文档对于大于小于的情况并没有说得很清楚，然后我们从字里行间大体领会的精神是:

1.  可迭代对象比较大小，是逐个比较的。

2.  可迭代对象比较和相等测试最后一定返回True或False。

3.  逐个比较首先比较是不是相等，如果相等则跳过这个元素的比较，直到遇到某两个不相等的元素，然后返回的就是这两个元素的比较结果。

4.  最后快比较完了（以最小的可迭代对象长度为准），然后如果是相等判断操作，则长度相等就认为两者相等了；而如果是大小判断操作，则认为长度更长的那个对象更大。

下面是一些例子:

    >>> (1,-1) < (2,-2)
    True
    >>> (1,-1) < (-1,-2)
    False
    >>> (1,-1,-3) < (1,-1)
    False
    >>> (1,-1,) < (1,-1,0)
    True
#### 创建字典

字典是一种映射，并没有从左到右的顺序，只是简单地将键映射到值。字典的声明格式如下：

    dict001={'name':'tom','height':'180','color':'red'}
    dict001['name']

或者创建一个空字典，然后一边赋值一边创建对应的键：

    dict002={}
    dict002['name']='bob'
    dict002['height']=195

##### 根据列表创建字典

如果是\[\['a',1\],\['b',2\],\['c',3\]\]这样的形式，那么直接用dict函数处理就变成字典了，如果是\['a','b','c'\]和\[1,2,3\]这样的形式那么需要用zip函数处理一下，然后用dict函数处理一次就变成字典了：

    >>> lst
    [['a', 1], ['b', 2], ['c', 3]]
    >>> dict001=dict(lst)
    >>> dict001
    {'a': 1, 'b': 2, 'c': 3}



#### 字典里面有字典

和列表的不同就在于字典的索引方式是根据"键"来的。

    dict003={'name':{'first':'bob','second':'smith'}}
    dict003['name']['first']

#### 字典遍历操作

字典特定顺序的遍历操作的通用做法就是通过字典的keys方法收集键的列表，然后用列表的sort方法处理之后用for语句遍历，如下所示：

    dict={'a':1,'c':2,'b':3}
    dictkeys=list(dict.keys())
    dictkeys.sort()
    for key in dictkeys:
        print(key,'->',dict[key])

**警告**：上面的例子可能对python早期版本并不使用，保险起见，推荐使用sorted函数，sorted函数是默认对字典的键进行排序并返回键的值组成的列表。

    dict={'a':1,'c':3,'b':2}
    >>> for key in sorted(dict):
    ...   print(key,'->',dict[key])
    ... 
    a -> 1
    b -> 2
    c -> 3

如果你对字典遍历的顺序没有要求，那么就可以简单的这样处理：

    >>> for key in dict:
    ...     print(key,'->',dict[key])
    ... 
    c -> 2
    a -> 1
    b -> 3

##### keys方法

收集键值，返回。

##### values方法

和keys方法类似，收集的值，返回。

    >>> dict001.values()
    dict_values([3, 1, 2])
    >>> list(dict001.values())
    [3, 1, 2]

##### items方法

和keys和values方法类似，不同的是返回的是(key,value)对的。

    >>> dict001.items()
    dict_items([('c', 3), ('a', 1), ('b', 2)])
    >>> list(dict001.items())
    [('c', 3), ('a', 1), ('b', 2)]

嗯，python2上面的三个方法是直接返回的列表，python3返回可迭代对象更节省计算资源些。

#### 字典的in语句

可以看到in语句只针对字典的键，不针对字典的值。

    >>> dict001={'a':1,'b':2,'c':3}
    >>> 2 in dict001
    False
    >>> 'b' in dict001
    True

#### 字典对象的get方法

get方法是去找某个键的值，为什么不直接引用呢，get方法的好处就是某个键不存在也不会出错。

    >>> dict001={'a':1,'b':2,'c':3}
    >>> dict001.get('b')
    2
    >>> dict001.get('e')

#### update方法

感觉字典就是一个小型数据库，update方法将另外一个字典里面的键和值覆盖进之前的字典中去，称之为更新，没有的加上，有的覆盖。

    >>> dict001={'a':1,'b':2,'c':3}
    >>> dict002={'e':4,'a':5}
    >>> dict001.update(dict002)
    >>> dict001
    {'c': 3, 'a': 5, 'e': 4, 'b': 2}

#### pop方法

pop方法类似列表的pop方法，不同引用的是键，而不是偏移地址，这个就不多说了。

#### 字典解析 

这种字典解析方式还是很好理解的。

    >>> dict001={x:x**2 for x in [1,2,3,4]}
    >>> dict001
    {1: 1, 2: 4, 3: 9, 4: 16}

##### zip函数创建字典

可以利用zip函数来通过两个可迭代对象平行合成一个配对元素的可迭代对象，然后用dict函数将其变成字典对象。

    >>> dict001=zip(['a','b','c'],[1,2,3])
    >>> dict001
    <zip object at 0xb7055eac>
    >>> dict001=dict(dict001)
    >>> dict001
    {'c': 3, 'b': 2, 'a': 1}

#### 深入理解字典的寻址

```python
t = {True: 'yes', 1: 'no', 1.0: 'maybe'}
t
Out[3]: {True: 'maybe'}
```

造成这样的结果首先是python的字典的key相同的判断机制，比如是 值相同 而且是 hash 值相同 才认为是 key相同。

其次是认为key相同key就不做改变了，而值是取最新的。也正是因为这样，下面的字典更新语句写法是可行的：

```
x = {'a':1, 'b':2}
y = {'b':3}
z = {**x, **y}
```

```
z
Out[8]: {'a': 1, 'b': 3}
```

而且这也是最快的字典更新方式。



### 集合

python实现了数学上的无序不重复元素的集合概念，在前面讨论列表去重元素的时候我们提到过正好可以利用集合的这一特性。

    >>> list001=[1,2,3,1,2,4,4,5,5,5,7]
    >>> {x for x in list001}
    {1, 2, 3, 4, 5, 7}
    >>> set(list001)
    {1, 2, 3, 4, 5, 7}

用集合解析的形式表示出来就是强调set命令可以将任何可迭代对象都变成集合类型。当然如果我们希望继续使用列表的话使用list命令强制类型转换为列表类型即可，不过如果我们在应用中确实一直需要元素不重复这一特性，就可以考虑直接使用集合作为主数据操作类型。

集合也是可迭代对象。关于可迭代对象可以进行的列表解析操作等等就不啰嗦了。下面介绍集合的一些操作。

#### 集合添加元素

**警告**：值得一提的是集合只能包括不可变类型，因此列表和字典不能作为集合内部的元素。元组不可变，所以可以加进去。

    >>> set001=set()
    >>> set001.add(1)
    >>> set001
    {1}
    >>> set001.add(2)
    >>> set001
    {1, 2}
    >>> set001.add(1)
    >>> set001
    {1, 2}

我们看到用集合的**add**方法添加，那些重复的元素是添加不进来的。

或者使用update方法一次更新多个元素：

    >>> set001=set('a')
    >>> set001.update('a','b','c')
    >>> set001
    {'b', 'a', 'c'}

#### 集合去掉某个元素

有两个集合对象的方法可以用于去掉集合中的某个元素，discard方法和remove方法，其中discard方法如果删除集合中没有的元素那么什么都不会发生，而remove方法如果删除某个不存在的元素那么会产生KeyError。

    >>> set001=set('hello')
    >>> set001.discard('h')
    >>> set001
    {'e', 'o', 'l'}
    >>> set001.discard('l')
    >>> set001
    {'e', 'o'}

remove方法与之类似就不做演示了。

#### 两个集合之间的关系

##### 子集判断

集合对象有一个issubset方法用于判断这个集合是不是那个集合的子集。

    >>> set001=set(['a','b'])
    >>> set002=set(['a','b','c'])
    >>> set001.issubset(set002)
    True

还有更加简便的方式比较两个集合之间的关系，那就是>，<，>=，<=，==这样的判断都是适用的。也就是set001是set002的子集，它的元素set002都包含，那么 `set001<=set002` ，然后真子集的概念就是 `set001<set002` 即不等于即可。

#### 两个集合之间的操作

下面的例子演示的是两个集合之间的交集：*&*，并集：*\|*，差集：*-*。

```text
>>> set001=set('hello')
>>> set002=set('hao')
>>> set001 & set002 #交集
{'o', 'h'}
>>> set001 | set002 #并集
{'h', 'l', 'a', 'e', 'o'}
>>> set001 - set002 #差集
{'e', 'l'}
```

类似的集合对象还有intersection方法，union方法，difference方法：

```text
>>> set001=set('hello')
>>> set002=set('hao')
>>> set001.intersection(set002) #交集
{'h', 'o'}
>>> set001.union(set002) #并集
{'e', 'a', 'h', 'o', 'l'}
>>> set001.difference(set002) #差集
{'e', 'l'}
```

#### clear方法

将一个集合清空。

#### copy方法

类似列表的copy方法，制作一个集合copy备份然后赋值给其他变量。

#### pop方法

无序弹出集合中的一个元素，直到没有然后返回KeyError错误。

### bytes类型

#### 基本编码知识

具体存储在计算机里面的都是二进制流，而如果要将其正确解析成为对应的字符，是需要建立一定的编码规则的。比如大家熟悉的ASCⅡ编码规则。ACSⅡ编码是Latin-1和utf-8等编码的子集，也就是一连串基于ACSⅡ编码的字符串用utf-8编码也能正确解析。

python2中目前也支持 **bytes** 类型了  。然后python2还有一个
**unicode** 类型。

bytes简单的理解就是没有任何字符含义的二进制字节流。然后如这样 `b'test'`
，在前面加个字符b或者B，其将解析为bytes类型。

```text
>>> x = b'test'
>>> x
b'test'
>>> type(x)
<class 'bytes'>
>>> x[0]
116
>>> x[1]
101
>>> list(x)
[116, 101, 115, 116]
>>> 
```

python在打印时会尽可能打印可见字符，尽管上面的x打印显示出了具体的test这个字符，但我们应该认为x是一连串的数字序列而不具有任何字符串含义，如果我们调用bytes类型的**decode**方法，那么bytes类型解码之后将变成str类型。

```text
>>> y = x.decode('utf-8')
>>> y
'test'
>>> type(y)
<class 'str'>
```

当然具体编码方式是否正确，是否正确解析了原bytes字节流那又是另外一回事了。比如还可能是big5或者GB什么的编码。

此外字符串str类型有个**encode**方法可以进行编码操作从而输出对应编码的bytes字节流。

#### 使用方法

我们可以如下看一下str类型和bytes类型具体有那些方法差异:

```text
>>> set(dir('abc')) - set(dir(b'abc'))
{'isdecimal', 'casefold', '__rmod__', 'format_map', 'format', 'encode', '__mod__', 'isnumeric', 'isprintable', 'isidentifier'}
>>> set(dir(b'abc')) - set(dir('abc'))
{'decode', 'fromhex'}
```

我们看到bytes和str几乎拥有相同的功能，所以大部分之前学到的用于str字符串类型的那些方法同样可以用于bytes类型中。这多少有点方法泛滥了，因为bytes是字节流类型，内在是没有字符含义的，可能某些方法并不推荐使用。

比如下面的upper方法和replace方法:

```text
>>> b't'.upper()
b'T'
>>> b'testst'.replace(b'st',b'oo')
b'teoooo'
```

然后字节流的连接可以很方便的用加法或join方法来进行，如下所示:

```text
>>> b't' + b'e'
b'te'
>>> b''.join([b'a',b'c'])
b'ac'
```

但是要*注意*，python2里面不管是加法还是join方法都将丢掉那个b修饰符:

```text
>>> b''.join([b'a',b'c'])
'ac'
>>> b'a' + b'b'
'ab'
```

不过这也无关紧要，因为python2里面我们可以理解str就对应的是python3的bytes类型，然后unicode对应的就是python3的str类型。

### bytearray类型

bytearray和bytes类型类似，而且其内部支持的方法和操作也和bytes类型类似，除了其更像是一个列表，可以原处修改而字符串和bytes是不可变的。python2现在也有bytearray类型了，只是内在的文本和二进制是不分的。

### 文件

文件对象是可迭代对象。

#### 写文件

对文件的操作首先需要用**open**函数创建一个文件对象，简单的理解就是把相应的接口搭接好。文件对象的**write**方法进行对某个文件的写操作，最后需要调用**close**方法写的内容才真的写进去了。

    file001 = open('test.txt','w')
    file001.write('hello world1\n')
    file001.write('hello world2\n')
    file001.close()

如果你们了解C语言的文件操作，在这里会为python语言的简单便捷赞叹不已。就是这样三句话：创建一个文件对象，然后调用这个文件对象的wirte方法写入一些内容，然后用close方法关闭这个文件即可。

#### 读文件

一般的用法就是用**open**函数创建一个文件对象，然后用**read**方法调用文件的内容。最后记得用**close**关闭文件。

    file001 = open('test.txt')
    filetext=file001.read()
    print(filetext)
    file001.close()

此外还有**readline**方法是一行一行的读取某文件的内容。

#### open函数的处理模式

open函数的处理模式如下：

'r'

:   默认值，read，读文件。

'w'

:   wirte，写文件，如果文件不存在会创建文件，如果文件已存在，文件原内容会清空。

'a'

:   append，附加内容，也就是后面用write方法内容会附加在原文件之后。

'b'

:   处理模式设置的选项，'b'不能单独存在，要和上面三个基本模式进行组合，比如'rb'等，意思是二进制数据格式读。

'+'

:   处理模式设置的选项，同样'+'不能单独存在，要和上面三个基本模式进行组合，比如'r+'等，+是updating更新的意思，也就是既可以读也可以写，那么'r+'，'w+'，'a+'还有什么区别呢？区别就是'r+'不具有文件创建功能，如果文件不存在会报错，然后'r+'不会清空文件，如果'r+'不清空文件用write方法情况会有点复杂；而'w+'具有文件创建功能，然后'w+'的write方法内容都是重新开始的；而'a+'的write方法内容是附加在原文件上的，然后'a+'也有文件创建功能。

#### 用with语句打开文件

类似之前的例子我们可以用with语句来打开文件，这样就不用close方法来关闭文件了。然后with语句来提供了类似try语句的功能可以自动应对打开文件时的一些异常情况。

    with open('test.txt','w') as file01:
        file01.write('hello world1\n')
        file01.write('hello world2\n')
    
    with open('test.txt','r') as file01:
        filetext=file01.read()
        print(filetext)



## 函数

函数也是一个对象，叫函数对象。函数名和变量名一样都是引用，函数名后面带个括号才真正实际执行。比如下面不带括号就只是返回了对这个函数对象的引用地址。

    >>> print
    <built-in function print>

要理解函数也是一个对象，比如在下面的例子中，fun刚开始是一个函数列表，然后在for的迭代语句里，意思具体就是multiply这个函数对象，然后接下来又是plus这个函数对象。整个过程是对x\*a然后再加上b。即$a*x +b$

    x = 3
    
    def multiply(x,a):
        return x*a
    
    def plus(x,b):
        return x+b
    
    fun = [multiply , plus]
    para = [3,2]
    for fun,para in zip(fun,para):
        x = fun(x,para)
    print(x)



### 自定义函数

定义函数用def命令，语句基本结构如下：

    def yourfunctionname(para001,para002...):
        do something001
        do something002

### 参数传递问题

函数具体参数的值是通过赋值形式来传递的，这有助于理解后面的不定变量函数。而函数的参数名是没有意义的，这个可以用lambda函式来理解之，def定义的为有名函数，有具体的引用地址，但内部作用原理还是跟lambda无名函式一样，形式参数名是x啊y啊都无所谓。为了说明这点，下面给出一个古怪的例子：

    y=1
    def test(x,y=y):
        return x+y
    print(test(4))

输出结果是5。我们看到似乎函数的形式参数y和外面的y不是一个东西，同时参数的传递是通过赋值形式进行的，那么具体是怎样的呢？具体的解释就是函数的形式参数y是这个函数自己内部的**本地变量**y，和外面的y不一样，更加深入的理解请看下一节（变量作用域问题）。

然后还有：

    >>> x=[1,2,3]
    >>> for x in x:
    ...  print(x)
    ... 
    1
    2
    3

我们知道for语句每进行一次迭代之前也进行了一次赋值操作，所以for语句里面刚开始定义的这个x和外面的x也不是一个东西，刚开始定义的x也是for语句内部的**本地变量**。

想到这里我又想起之前编写removeduplicate函数遇到的一个问题，那就是for语句针对列表这个可变的可迭代对象的工作原理是如何的？具体请看下面的例子：

    >>> lst=[1,2,3,4]
    >>> for x in lst:
    ...  print(x,lst)
    ...  del lst[-1]
    ... 
    1 [1, 2, 3, 4]
    2 [1, 2, 3]

可迭代对象的惰性求值内部机制在我看来很神奇，目前还不太清楚，但从这个例子看来列表的惰性求值并没有记忆内部的数值，只是记忆了（合情合理），然后如果迭代产生了StopIteration异常就终止。

### 变量作用域问题

python的变量作用域和大部分语言比如c语言或lisp语言的概念都类似，就是函数里面是局部变量，一层套一层，里面可以引用外面，外面不可以引用里面。

具体实现机制是每个函数都有自己的命名空间，（和模块类似）就好像一个盒子一样封装着内部的变量。所谓的本地变量和函数有关，或者其他类似的比如for语句；所谓的全局变量和模块有关，更确切的表述是和文件有关，比如说在现在这个文件里，你可以通过导入其他模块的变量名，但实际上模块导入之后那些变量名都引入到这个文件里面来了。

具体实现和类的继承类似也是一种搜索机制，先搜索本地作用域，然后是上一层(def，lambda，for)的本地作用域，然后是全局作用域，然后是内置作用域。更加的直观的说明如下图所示：

![img]({static}/images/python/python-bian-liang-zuo-yong-yu.png)

简单来说python的变量作用域问题就是：盒子套盒子，搜索是从盒子最里面然后往外面寻找，里面可以用外面的变量，外面的不可以用里面的。

#### 内置作用域

内置作用域就是由一个`__builtin__`模块来实现的，python的作用机制最后会自动搜索这个内置模块的变量。这个内置模块里面就是我们前面学习的那些可以直接使用的函数名，比如print，range等等之类的，然后还有一些内置的异常名。

所以我们想到即使对于这些python的内置函数我们也是可以覆盖定义的，事实确实如此：

    >>> abs(-3)
    3
    >>> def abs(x):
    ...  print(x)
    ... 
    >>> abs(3)
    3
    >>> abs(-3)
    -3

以后学习单元测试会接触到mock的概念，其作用机制大体也与之类似就是覆盖掉之前定义的某个对象。

#### global命令

如果希望函数里面定义的变量就是全局变量，在变量声明的时候前面加上**global**命令即可。

通常不建议这么做，除非你确定需要这么做，然后你需要写两行代码才能实现，意思也是不推荐你这么做。

    def test():
        global var
        var= 'hello'
    test()
    print(var)
    
    hello

而且就算你这样做了，这个变量也只能在本py文件中被引用，其他文件用不了。推荐的做法是另外写一个专门用于配置参数的config.py文件，然后那些全局变量都放在里面，如果某个文件要用，就import进来。而对与这个config.py文件的修改会影响所有的py文件配置，这样让全局变量可见可管可控更加通用，才是正确的编程方式。

#### nonlocal命令

nonlocal命令python3之后才出现，这里实现的概念有点类似于lisp语言的闭包(closure技术)，就是如果你有某个需要，需要函数记忆一点自己的状态，同时又不想这个状态信息是全局变量，也不希望用类的方式来实现，那么就可以用nonlocal命令来简单地完成这个任务。

global意味着命名只存在于一个嵌套的模块中，而nonlocal的查找只限于嵌套的def中。要理解nonlocal首先需要理解函数里面嵌套函数的情况------也就是所谓的工厂函数，一个函数返回一个函数对象。比如说

    def add(x):
        x=x
        def action(y):
            return x+y
        return action
    
    >>> add1=add(1)
    >>> add1(5)
    6
    >>> add2=add(2)
    >>> add2(5)
    7

这里的return action是返回一个函数对象，这样add1的实际接口是`def action`那里。熟悉lisp语言的明白，action外面的那个函数的变量叫做自由变量，不过嵌套函数在这里可以引用自由变量。如果我们声明`nonlocal x`，那么就可以修改嵌套函数外面声明的变量了。

    def add(x):
        x=x
        def action(y):
            nonlocal x
            x=x+1
            return x+y
        return action
    
    >>> add2=add(2)
    >>> add2(5)
    8
    >>> add2(5)
    9
    >>> add2(5)
    10

然后我们看到这个生产出来的函数具有了运行上的状态性，实际上通过类也能构建出类似的效果，不过对于某些问题可能闭包方式处理显得更适合一些。

下面给出一个稍微合理点的例子：

    def myrange(n):
        i=n
        def action():
            nonlocal i
            while i>0:
                i=i-1
                return i
        return action
    
    >>> myrange5=myrange(5)
    >>> myrange5()
    4
    >>> myrange5()
    3
    >>> myrange5()
    2
    >>> myrange5()
    1
    >>> myrange5()
    0
    >>> myrange5()
    >>> 

下面给出类似的类的实现方法：

    class myrange:
        def __init__(self,n):
            self.i=n
        def action(self):
            while self.i > 0:
                self.i -= 1
                return self.i
    
    >>> myrange5=myrange(5)
    >>> 
    >>> myrange5.action()
    4
    >>> myrange5.action()
    3
    >>> myrange5.action()
    2
    >>> myrange5.action()
    1
    >>> myrange5.action()
    0
    >>> myrange5.action()
    >>> 

我们看到从编码思路上基本上没什么差异，可以说稍作修改就可以换成类的实现版本。推荐一般使用类的实现方法。但有的时候可能用类来实现有点不伦不类和大材小用了。这里就不做进一步讨论了，闭包思想是函数编程中很重要的一个思想，学习了解一下也好。

### 参数和默认参数

定义的函数圆括号那里就是接受的参数，如果参数后面跟个等号，来个赋值语句，那个这个赋的值就是这个参数的默认值。比如下面随便写个演示程序：

    def test(x='hello'):
        print(x)
    test()
    test('world')
    
    hello
    world

### 不定参量函数

我们在前面谈到sum函数只接受一个列表，而不支持这样的形式：sum(1,2,3,4,5)。现在我们设计这样一个可以接受不定任意数目参量的函数。首先让我们看看一种奇怪的赋值方式。

#### 序列解包赋值

**NOTICE:**
python2不支持本小节讨论的序列解包赋值。不过python2的函数定义中是支持
`*args` 这种写法的。

    >>> a,b,*c=1,2,3,4,5,6,7,8,9
    >>> print(a,b,c,sep=' | ')
    1 | 2 | [3, 4, 5, 6, 7, 8, 9]
    >>> a,*b,c=1,2,3,4,5,6,7,8,9
    >>> print(a,b,c,sep=' | ')
    1 | [2, 3, 4, 5, 6, 7, 8] | 9
    >>> *a,b,c=1,2,3,4,5,6,7,8,9
    >>> print(a,b,c,sep=' | ')
    [1, 2, 3, 4, 5, 6, 7] | 8 | 9

带上一个星号\*的变量变得有点类似通配符的味道了，针对后面的序列（数组，列表，字符串），它都会将遇到的元素收集在一个列表里面，然后说是它的。

for语句也支持序列解包赋值，也是将通配到的的元素收集到了一个列表里面，如：

    for (a,*b,c) in [(1,2,3,4,5,6),(1,2,3,4,5),(1,2,3,4)]:
        print(b)
    
    [2, 3, 4, 5]
    [2, 3, 4]
    [2, 3]

#### 函数中的通配符

    >>> def test(*args):
    ...  print(args)
    ... 
    >>> test(1,2,3,'a')
    (1, 2, 3, 'a')

我们看到类似上面序列解包赋值中的带星号表通配的概念，在定义函数的时候写上一个带星号的参量（我们可以想象在函数传递参数的时候有一个类似的序列解包赋值过程），在函数定义里面，这个args就是接受到的参量组成的*元组*。

#### mysum函数

    def mysum(*args):
        return sum(args[:])
    
    print(mysum(1,2,3,4,5,6))
    
    21

这样我们定义的可以接受任意参数的mysum函数，如上所示。具体过程就是将接受到的args（已成一个元组了），然后用sum函数处理了一下即可。

#### 任意数目的可选参数

在函数定义的写上带上两个星号的变量\*\*args，那么args在函数里面的意思就是接受到的可选参数组成的一个字典值。

    >>> def test(**args):
    ...  return args
    ... 
    >>> test(a=1,b=2)
    {'b': 2, 'a': 1}

我们看到利用这个可以构建出一个简单的词典对象生成器。

#### 解包可迭代对象传递参数

之前\*args是在函数定义中，然后通配一些参数放入元组中。这里是在函数调用中，针对可迭代对象，可以用一个\*星号将其所包含的元素迭代出来，然后和参数一一对应赋值。

    >>> map = map(lambda x:x+2,[1,2,3])
    >>> print(*map)
    3 4 5
    >>> print(*[1,2,3])
    1 2 3

##### 最简单的打印文件命令

前面说到文件也是一个可迭代对象，然后如果在这里解包文件对象将是一个最简单的打印文件命令，简单得惊天地泣鬼神了\...

    print(*open('test.py'))

#### 解包字典成为关键字参数

和上面的类似，通过\*\*args语法可以将某个字典对象解包成为某个函数的关键字参数。还是以上面那个函数f为例子：

    >>> def f(a,b,c=3):
    ...  print(a,b,c)
    >>> f(**{'c':6,'b':4,'a':2})
    2 4 6
    >>> f(1,2,5)
    1 2 5

这个例子也告诉我们不是可选参数的a和b同样也可以通过这种字典形式复制。

### 参数的顺序

老实说一般参数，可选参数（关键字参数），任意（通配）参数，任意（通配）关键字参数所有这些概念混在一起非常的让人困惑。就一般的顺序是：

1.  一般参数，这个如果有 ，然后通过位置一一对应分配参数。

2.  关键字参数，匹配一些关键字参数。

3.  通配一般参数，其他额外的非关键字的参数分配到\*args元组里面。

4.  通配关键字参数，其他额外的关键字参数分配到\*\*kwargs字典里面， 。

具体如下所示：

    def test(x, y, c=1, d=1, *args, **kwargs):
        print(x, y, c, d, args, kwargs)

这种写法也是python2和python3兼容的。然后python3又新加入了一个keyword-only参数（读者记住这不是关键字参数就行了），如下所示：

    def test(x, y, c=1, d=1, *args, z=None ,**kwargs):
        print(x, y, c, d,args, kwargs,z)

首先强调一点，python2里面没有这个东西，所以要考虑python2和python3兼容性的不用太关注这个东西了。看上面的例子，这个keyword-only参数是个极容易和keyword参数或者我们常说的关键字参数混淆的东西，这个keyword-only参数也确实是类似关键字参数，但它不能像常规的关键字参数那样按照位置赋值，而必须明确的指定名字赋值。

这个keyword-only参数的标志就是跟在那个星号后面。如下所示，你也别把那个z认为是个一般参数了，它只是一个还没有赋予默认值的keyword-only参数。

    def test(x, y, c=1, d=1, *args, z ,**kwargs):
        print(x, y, c, d,args, kwargs,z)

然后有的人就只想用keyword-only参数，对具体通配一般参数根本不感兴趣，会这样写：

    def test(x, y, c=1, d=1, *, z ,**kwargs):
        print(x, y, c, d,args, kwargs,z)

这样写的话就没有通配一般参数了，这样上面这个函数最多只能接受4个不指定名字的参数，x，y两个，c和d这两个关键字参数也可以匹配两个。

#### keyword-only参数的用处

keyword-only的参数的用处就是其是一个不能通过不指定名字而赋值的关键字参数，或者说如果你需要某个关键字参数在后面的使用中必须明确给出名字来使用，那么就可以使用keyword-only参数。

只是有一点，python2不支持这个东西，python2要实现类似的效果要通过
`**kwargs` 还有后面写上一些甚至很多行代码才行，如下所示：

    def test(x, y, **kwargs):
        a = kwargs.pop('a')
        b = kwargs.pop('b', False) # 第二个参数得到默认参数的效果
        
        if kwargs:
            raise TypeError(Unexpected kwargs: {0}'.format(kwargs))

异常信息随便写的，在这里不是重点。

### 生成器函数

一般函数的定义使用return语句，如果使用yield语句，我们可以构建出一个生成器函数，

```text
>>> def test(x):
...    for i in range(x):
...        yield 2*i+ 1
... 
>>> test(3)
<generator object test at 0xb704348c>
>>> [x for x in test(3)]
[1, 3, 5]
>>> [x for x in test(5)]
[1, 3, 5, 7, 9]
```

生成器函数返回的是生成器对象（generator object），通过yield这样的形式定义出来的生成器函数返回了一个生成器对象和range对象类似，都是描述性可迭代对象，里面的元素并不立即展开，而是请求一次运算一次，所以这种编程风格对内存压力很小，主要适合那些迭代元素特别多的时候的情况吧。

上面的test函数我们就可以简单理解为 `2x+1` ，其中` 0<=x<n`（赋的值）。

下面给出一个问题作为练习：描述素数的生成器函数。
这是网上流行的素数检验函数，效率还是比较高的了。

    def isprime(n):
        if n ==2:
            return True
        #按位与1，前面一定都是0个位数如果是1则
        #是奇数则返回1则真则假，如果是偶数则返回
        #0则假则真
        elif n<2 or not n & 1:
            return False
        #埃拉托斯特尼筛法...
    #查一个正整数N是否为素数，最简单的方法就是试除法，
    #将该数N用小于等于N**0.5的所有素数去试除，
    #若均无法整除，则N为素数
        for x in range(3,int(n**0.5)+1,2):
            if n % x == 0:
                return False
        return True

然后我们给出两种形式的素数生成器函数，其中prime2的意思是范围到（to）那里。而prime(n)的意思是到第几个素数。我们知道生成器函数是一种惰性求值运算，然后yield每迭代一次函数运算一次（即产生一次yield），但这种机制还是让我觉得好神奇。

    def prime2(n):
        for x in range(n):
            if isprime(x):
                yield x
    
    def prime(n):
        i=0
        x=1
        while i<n:
            if isprime(x):
                i +=1
                yield x
            x +=1

在加载这些函数之后我们可以做一些检验：

    >>> isprime(479)
    True
    >>> [x for x in prime2(100)]
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, ........]
    >>> [x for x in prime2(1000) if 100< x < 200]
    [101, 103, 107, 109, 113, 127, 131, 137, 139, 149, .......]
    >>> len([x for x in prime2(10000) if -1 < x < 3572])
    500
    >>> [x for x in prime(1)]
    [2]
    >>> [x for x in prime(2)]
    [2, 3]

### 递归函式 

虽然递归函式能够在某种程度上取代前面的一些循环或者迭代程序结构，不过不推荐这么做。这里谈及递归函式是把某些问题归结为数学函数问题，而这些问题常常用递归算法更加直观（不一定高效）。比如下面的菲波那奇函数：

    def fib(n):
        if n==0:
            return 1
        if n==1:
            return 1
        else:
            return fib(n-1)+fib(n-2)
            
    for x in range(5):
        print(fib(x))
    
    1
    1
    2
    3
    5

我们可以看到，对于这样专门的数学问题来说，用这样的递归算法来表述是非常简洁易懂的。至于其内部细节，我们可以将上面定义的fib称之为函式，函式是一种操作的模式，然后具体操作就是复制出这个函式（函数或者操作都是数据），然后按照这个函式来扩展生成具体的函数或者操作。

下面看通过递归函式来写阶乘函数，非常的简洁，我以为这就是最好最美的方法了。

    def fact(n):
        if n == 0:
            return 1
        else:
            return n*fact(n-1)
            
    print(fact(0),fact(10))
    
    1 3628800

#### 什么时候用递归？

最推荐使用递归的情况是这样的情况，那就是一份工作（或函数）执行一遍之后你能够感觉到虽然所有的工作没有做完，但是已经做了一小部分了，有了一定的进展了，就好比是蚂蚁吞大象一样，那么这个时候你就可以使用递归思想了。其次有的时候有那么一种情况虽然表面上看似乎并没有什么进展，但事情在发展，你能感受到有一个条件最终将会终止程序从而得到一个输出，那么这个时候就可以用递归。

递归思想最核心的两个概念就是一做了一小部分工作，你能感觉到做着做着事情就会做完了；二有一个终止判断最终将会起作用。

其实通过递归函式也可以实现类似for的迭代结构，不过我觉得递归函式还是不应该滥用。比如下面通过递归函式生成一种执行某个操作n次的结构：

    def dosomething(n):
        if n==0:
            pass
        elif n==1:
            print('do!')
        else:
            print('do!')
            return dosomething(n-1)
    
    print(dosomething(5))
    
    do!
    do!
    do!
    do!
    do!
    None

可以看到，如果把上面的print语句换成其他的某个操作，比如机器人向前走一步，那么这里dosomething换个名字向前走(5)就成了向前走5步了。

#### lisp的car-cdr递归技术

在lisp语言中，
car-cdr递归技术是很重要的一门技术，它的特长就是遍历随意嵌套的列表结构可以同一对列表中的每一个元素执行某种操作。

首先我们来看下面的例子，一个把任意嵌套列表所有元素放入一个列表中的函数：

    lst = [[1,2,[3]],[4,[5,[[[[10],11]]]],(1,2,3)],[{'a','b','c'},8,9]]
    
    def is_list(thing):
        return isinstance(thing, list)
    
    def flatten(iter):
        templst = []
        for x in iter:
            if not is_list(x):
                templst.append(x)
            else:
                templst += flatten(x)
        return templst
    
    print(flatten(lst))
    
    [1, 2, 3, 4, 5, 10, 11, (1, 2, 3), {'c', 'b', 'a'}, 8, 9]

这个函数的逻辑是如果是最小元素对象不是列表，那么收集进列表；如果不是，那么把它展开，这里就是调用的原函数继续展开函式。

上面的例子严格意义上来讲还不算lisp的经典car-cdr递归技术，下面给出一个典型的例子，就是复制任意嵌套结构的列表。当然列表的copy方法就可以做这个工作，这里主要通过这个例子来进一步深入car-cdr技术。

    def is_list(thing):
        return isinstance(thing, list)
    
    def copy_list(lst):
        if  not  is_list(lst):
            return lst
        elif lst == []:
            return []
        else:
            return [copy_list(lst[0])] + copy_list(lst[1:])
    
    print(copy_list([1,[2,6],3]))

这种嵌套列表的复制以及后面的修改等等操作，最合适的就是lisp的car-cdr技术了，但我不得不承认，这种递归写法是递归函式里面最难懂的了。

不管怎么严格，在这个基础之上，因为第一个if
not的语句中传递下来的lst实际上已经是非列表的其他元素了，然后我们可以进行一些其他修改操作，这样在保持原列表的复杂嵌套的基础上，等于遍历的对列表中的所有元素进行了某种操作。

比如所有元素都平方：

    def square(x):
        return x**2
    
    def square_list(lst):
        if  not  is_list(lst):
            return square(lst)
        elif lst == []:
            return []
        else:
            return [square_list(lst[0])] + square_list(lst[1:])
    
    print(square_list([1,[2,6],3]))

我们可以想像更加复杂功能的函数作用于列表中所有的元素同时又不失去原列表复杂的嵌套结构，lisp的car-cdr这种技术了解一下吧，但是不是一定要使用复杂的嵌套结构呢？也许没有必要吧。。

### lambda函式

python中的函数作为一个对象一般是通过 `def` 语句来定义的，定义之后该函数对象和函数名变量已经绑定在一起了。但实际上python中的函数作为一个对象名字不是那么重要的：

```
def add(x,y):
...     return x+y
... 
add
<function add at 0x000001B952B770D0>

add2 = add
del add
add2(1,2)
3
add
Traceback (most recent call last):
  File "<input>", line 1, in <module>
NameError: name 'add' is not defined
add2.__name__
'add'
```

而lambda λ表达式可以简单理解为没有名字的函数对象：

```
add = lambda x,y: x+y
add
<function <lambda> at 0x000001B952B77378>
add.__name__
'<lambda>'
add(1,2)
3
type(add)
<class 'function'>
type(add2)
<class 'function'>
```

如上所示我们看到，不管是通过def定义的函数还是lambda函式在python里面都是函数对象，或者说都属于function class。具体调用和使用也很类似，除了lambda函数定义的函数对象那个 `__name__` 只是默认的 `<lambda>` 。

lambda函数在某些地方会用到，一般是在将函数作为参数传递的情况下，某些简短的函数动作没必要另外再想个函数名字的应用场景。

### print函数

print函数接受任意的参量，逐个打印出来。然后它还有一些关键字参数：

- **sep**：默认值是 `' '` ，也就是一个空格，如果修改为空字符串，那么逐个打印出来的字符之间就没有间隔了。
- **end**：默认值是 `'\n'` ，为print函数执行完打印的字符，默认是打印一个换行符。
- **file**默认值是 `sys.stdout` ，也就是在终端显示，你可以修改为某个文件变量，这样直接往某个文件里面输出内容。

## 逻辑

### 布尔值

boolean类型，和大多数语言一样，就两个值：**True**，**False**。然后强制类型转换使用函数**bool**。

#### 其他逻辑小知识

在python中，有些关于逻辑真假上的小知识，需要简单了解下。

-   数0、空对象或者其他特殊对象None值都认为是假

-   其他非零的数字或非空的对象都认为是真

-   前面两条用bool函数可以进行强制类型转换

-   比较和相等测试会递归作用在数据结构中

-   比较和相等测试会返回True或False

上面最后两条在说个什么东西，读者请参看之前的元组和列表比较大小一小节。

#### None

有些函数没有return的值就会返回None值，None值是NoneType对象中的一个值，和列表的空值等是不同的，它和其他任何值都不一样的。比如re.search如果没有找到匹配就会返回None值。这个时候需要知道的是None值在逻辑上是逻辑假，not
None是逻辑真。

    >>> def f():
    ...  pass
    ... 
    >>> y = f()
    >>> y
    >>> type(y)
    <class 'NoneType'>

### if条件判断

python中的条件语句基本格式如下：

    if  test:
        条件判断执行区块

也就是if命令后面跟个条件判断语句，然后记住加个冒号，然后后面缩进的区块都是条件判断为真的时候要执行的语句。

    if  test:
        do something001
    else :
        do something002

这里的逻辑是条件判断，如果真，do something001；如果假，do something002。

    if  test001:
        do something001
    elif test002:
        do something002

显然你一看就明白了，elif是else和if的结合。

#### 逻辑与或否

and表示逻辑与，or表示逻辑或，not表示逻辑否。

下面编写一个逻辑，判断一个字符串，这个字符串开头必须是a或者b，结尾必须是s，倒数第二个字符不能是单引号'。在这里就演示一下逻辑。。

    x='agais'
    if ((x[0] == 'a' or x[0] == 'b')
        and x[-1] =='s'
        and (not x[-2] =="'")):
        print('yes it is..')
    
    yes it is..

#### 稍复杂的条件判断

现在我们了解了if，elif和else语句，然后还了解了逻辑与或非的组合判断。那么在实际编程中如何处理复杂的条件逻辑呢？

首先能够用逻辑语句"与或非"组合起来的就将其组合起来，而不要过分使用嵌套。如下面代码所示，如果一个情况分成两部分，那么就用if\...else\...语句，

    x=-2
    if x>0:
        print('x大于0')
    else:
        print('x小于0')

而如果一个情况分成三部分，那么就用if\...elif\...else语句。同一深度的这些平行语句对应的是"或"逻辑，或者说类似其他编程语言的switch语句。

    x=2
    if x>0:
        print('x大于0')
    elif x<0:
        print('x小于0')
    else:
        print('x等于0')

我们再看一看下面的代码，这个代码是*错误的*，两个if语句彼此并不构成逻辑分析关系。

    x=2
    if x>0:
        print('x大于0')
    if x<0:
        print('x小于0')
    else:
        print('x等于0')

然后我们看到下面的代码，这个例子演示的是在加深一个深度的条件判断语句它当时处于的逻辑判断情况，这个语句的条件判断逻辑是本语句的判断逻辑再和左边（也就是前面）的判断逻辑的"与"逻辑，或者说成是"交集"。比如说 `print('0<x<2')` 这个语句就是本语句的判断逻辑 `x<2`和上一层判断逻辑 `x>0` 的"交集"，也就是 `0<x<2`。

    x=-2
    if x>0:
        print('x大于0')
        if x>2:
            print('x>2')
        elif x<2:
            print('0<x<2')
        else:
            print('x=2')
    elif x<0:
        print('x小于0')
    else:
        print('x等于0')

整个过程的情况如下图所示：

![img]({static}/images/python/fu-za-tiao-jian-pan-duan.png "复杂条件判断")

为了在编程的时候对处于何种判断逻辑之下有一个清晰的认识，强烈建议读者好好思考一下。毕竟磨刀不误砍柴功。

#### try语句捕捉错误

try语句是编程中用来处理可能出现的错误或者已经出现但并不打算应付的错误最通用的方式。比如一个变量你预先想的是接受一个数值，但是用户却输入了一个字符，这个时候你就可以将这段语句包围在try里面；或者有时你在编程的时候就发现了这种情况，只是懒得理会他们，那么简单的把这块出错的语句包围在try里面，然后后面跟个except语句，打印出一个信息"出错了"，即可。用法如下所示：

    while True:
        x=input('请输入一个数，将返回它除以2之后的数值\n输入"quit"退出\n')
        if x=='quit':
            break
        try :
            num=float(x)
            print(num/2)
        except:
            print('出错了')

##### 异常处理完整语句

    try:
        yourCode
    except yourError:
        do something
    except yourError2:
        do something2
    ......
    else:
        do somethingN
    finally:
        do the funallystuff

这个语句的逻辑是试着执行try区块下的语句，如果出现异常，那么看是不是异常yourError，如果是则执行do
something，如果是yourError2，则执行do something2
\...\...等等，如果没有异常，则执行else字句: do
somethingN，如果还有异常，则这个异常将会返回（更上面的控制程序）。

那么finally语句的作用是什么呢，finally语句实际上和整个语句中异常判断情况没有关系，不管有没有异常发生，最后它都将被执行。和简单地不缩进直接写在下面的语句比起来，finally语句的特点就是就算程序发生异常了，它也会先被执行，然后将异常上传给上面的控制程序。

else语句和finally语句是可选的，根据具体情况来看。

##### for里面放try语句的情况

for语句里面放上try语句还需要细讲一下。

具体try语句相关逻辑前面说过了，这里的问题是for语句的继续执行问题。首先是第一个情况，try字句里面使用return，这在函数里面是会跳出for语句的，也就是执行多次只要成功一次就会被跳出。然后错误捕捉，如果错误捕捉里面再放入一个raise语句，再抛出一个错误，这个时候for语句是会被中止的。然后抛出这个异常。然后是else字句，其逻辑是try多次没有错误，那么将会执行else字句，但是如果你try一次，然后else语句里面加入break命令，则会跳出for语句的。

这里面情况稍微有点复杂，目前我接触到的有如下两种应用:

这是一个mongodb的安全调用的函数装饰器。其在试图调用mongodb的时候，如果发生AutoReconnect异常，那么将会sleep一秒然后再去try
之前的那个调用函数。如果成功了，那么进入return，然后自然就跳出for语句了。

    def safe_mongocall(call):
        '''mongodb replica set assistant'''
        def _safe_mongocall(*args, **kwargs):
            for i in xrange(100):#
                try:
                    return call(*args, **kwargs)
                except pymongo.AutoReconnect:
                    import time
                    time.sleep(1)
                    print("try to connect mongodb again...")
        return _safe_mongocall

第二个例子较为常用，就是在重复做某件事的时候可能会发生错误，然后捕捉这个错误，然后继续执行。然后捕捉的时候计了一下数。

    def test():
        failcount = 0
    
        for i in range(src_count):
            try:
                do something
            except Exception as ex:
                failcount += 1
    
        sucess_count = src_count - failcount
        return sucess_count

其实我们还可以想到另外一种程序结构，那就是try和else在for语句里面构成逻辑分支。当你试着做某件事的时候，try，如果正常则执行else字句然后break，如果发生某个异常则执行异常中的字句，就是try里面的内容不被执行。这有点反常规，但联系实际生活，我们确实也存在这样的逻辑，那就是假想如何如何，发生错误不行则执行else字句，就是假想try里面的内容不实际执行。

#### in语句

in语句对于可迭代对象都可以做出是否某个元素包含在某个对象之中的判断。

```text
>>> 'a' in ['a',1,2]
True
>>> dict
{'a': 1, 'c': 2, 'b': 3, 'd': 4}
>>> 'e' in dict
False
>>> '2' in dict
False
```

从上面例子可以看到，一般的列表判断元素是否存在和我们之前预料的一致，关于字典需要说的就是in语句，不判断值。

### for迭代语句

一般有内部重复操作的程序可以先考虑for迭代结构实现，实在不行才考虑while循环结构，毕竟简单更美更安全。

python的for迭代语句有点类似lisp语言的dolist和dotimes函数，具体例子如下：

    for x in 'abc':
        print(x)
    
    a
    b
    c

in后面跟的是**序列**类型，也就是字符串，列表，数组都是可以的。这个语句可以看作先执行x='a'或者类似的匹配赋值操作，然后执行缩进的区块，后面依次类推。

#### else分句

    for x in 'abc':
        if x == 'b':
            print(x)
            break
    else:
        print('test')

for语句加上else分句这种形式，如果for迭代完了就会执行else分句。但如果for语句还在迭代过程中，break或者return出来了，那么else分句将不会被执行。

#### range函数

range函数常和for迭代语句一起使用，其返回一个可迭代对象。

    range(1,10,2)

range函数的用法如上，表示从1开始到10，步长为2，如果用list函数将其包裹，将会输出\[1,3,5,7,9\]。如果不考虑步长的话。所以range(10)就可以看作\[0,10)，range(1,10)就可以看作\[1,10)。但是在这里再加上步长的概念和区间的概念又有所不同了。

    for x in range(-10,-20,-3):
        print(x)
    
    -10
    -13
    -16
    -19

上面例子还演示了range的负数概念，这里如果用区间概念来考察的话，是不能理解的，之所以行得通，是因为它的步长是负数，如果不是负数，那么情况就会和之前讨论的结果类似，将是一个空值。

#### 迭代加上操作

迭代产生信息流并经过某些操作之后生成目标序列。

    >>> squares=[x**2 for x in [1,2,3,4,5]]
    >>> squares
    [1, 4, 9, 16, 25]

#### enumerate函数

enumerate函数返回一个enumerate对象，这个对象将偏移值和元素组合起来，成为一个可迭代对象了。

    >>> enu = enumerate('abcd')
    >>> [i for i in enu]
    [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]

### while循环

while语句用法和大多数编程语言类似，就是条件控制，循环结构。

    while test:
        do something
    else :
        do something

值得一提的是else语句和while语句属于一个整体，通常情况下while执行完了然后执行下面的语句似乎不需要加上else来控制。不过else语句的一个功用就是如果while循环的时候遇到break那么else语句也不会执行而是直接跳过去了，见下面。

#### break命令

break跳出最近的while或者for循环结构。前面谈到了else和while语句构成一个整体的时候，break可以跳过else语句。

#### continue命令

continue命令接下来的循环结构的执行区块将不执行了，跳到条件判断那里看看是不是继续循环。如果是，那么继续循环。同样在for语句中continue命令的意思也是一样的。

#### pass命令

pass命令就是什么都不做。pass命令即可用于循环语句也可用于条件语句。

pass命令什么都不做似乎没有什么意义，不过作为一个空占位符还是很有用的。比如你编写一个大型的GUI程序，信号－槽机制都构思好了，只是对应的函数暂时还没写好，这个时候你可以将对应的函数，只是空的函数名加上pass语句写上，这样整个程序就可以继续边编写边调试了。



Slug: python-advanced
Category: python_language
Tags: python,
Date: 20191018



[TOC]

## 类

在python中一切皆对象。前面学的那些操作对象都是python程序语言自己内部定义的对象（Object），而接下来介绍的类的语法除了更好的理解之前的那些对象之外，再就是可以创造自己的操作对象。一般面向对象(OOP)编程的基本概念这里不重复说明了，如有不明请读者自己随便搜索一篇网页阅读下即可。

### python中类的结构

python中的类就好像树叶，所有的类就构成了一棵树，而python中超类，子类，实例的重载或继承关系等就是由一种搜索机制实现的：

![img]({static}/images/python/lei-sou-suo-jie-gou.png)

python首先搜索self有没有这个属性或者方法，如果没有，就向上搜索。比如说实例l1没有，就向上搜索C1，C1没有就向上搜索C2或C3等。

实例继承了创造它的类的属性，创造它的类上面可能还有更上层的超类，类似的概念还有子类，表示这个类在树形层次中比较低。

well，简单来说类的结构和搜索机制就是这样的，很好地模拟了真实世界知识的树形层次结构。

上面那副图实际编写的代码如下：

    class C2: ...
    class C3: ...
    class C1(C2,C3): ...
    l1=C1()
    l2=C1()

其中class语句是创造类，而C1继承自C2和C3，这是多重继承，从左到右是内部的搜索顺序（会影响重载）。l1和l2是根据类C1创造的两个实例。

对于初次接触类这个概念的读者并不指望他们马上就弄懂类这个概念，这个概念倒并一定要涉及很多哲学的纯思考的东西，也可以看作一种编程经验或技术的总结。多接触对类的学习更重要，而不是纯哲学抽象概念的讨论，毕竟类这个东西创造出来就是为了更好地描述现实世界的。

最后别人编写的很多模块就是一堆类，你就是要根据这些类来根据自己的情况来编写自己的子类，从而实现对原有类对象的改造。为了更好地利用前人的成果，或者你的成果更好地让别人快速使用和上手，那么你需要好好掌握类这个工具。

### 类的最基础知识

### 类的创建

    class MyClass:
        something

类的创建语法如上所示，然后你需要想一个好一点的类名。类名规范的写法是首字母大写，这样好和其他变量有所区分。

### 根据类创建实例

按照如下语句格式就根据MyClass类创建了一个实例myclass001。

    myclass001=MyClass()

### 类的属性

    >>> class MyClass:
    ...  name='myclass'
    ... 
    >>> myclass001=MyClass()
    >>> myclass001.name
    'myclass'
    >>> MyClass.name
    'myclass'
    >>> myclass001.name='myclass001'
    >>> myclass001.name
    'myclass001'
    >>> MyClass.name
    'myclass'

如上代码所示，我们首先创建了一个类，这个类加上了一个name属性，然后创建了一个实例myclass001，然后这个实例和这个类都有了name属性。然后我们通过实例加上点加上name的这种格式引用了这个实例的name属性，并将其值做了修改。

这个例子简单演示了类的创建，属性添加，实例创建，多态等核心概念。后面类的继承等概念都和这些大同小异了。

### 类的方法

类的方法就是类似上面类的属性一样加上def语句来定义一个函数，只是函数在类里面我们一般称之为方法。这里演示一个例子，读者看一下就明白了。

    >>> class MyClass:
    ...  name='myclass'
    ...  def double(self):
    ...   self.name=self.name*2
    ...   print(self.name)
    ... 
    >>> myclass001=MyClass()
    >>> myclass001.name
    'myclass'
    >>> myclass001.double()
    myclassmyclass
    >>> myclass001.name
    'myclassmyclass'

这里需要说明的是在类的定义结构里面，self代表着类自身（更多self意义细节请参看下面的self意味着什么一小节），self.name代表着对自身name属性的引用。然后实例在调用自身的这个方法时用的是 `myclass001.double()` 这样的结构，这里double函数实际上接受的第一个参数就是自身，也就是myclass001，而不是无参数函数。所以类里面的方法有一个参数self。

### 类的继承

实例虽然说是根据类创建出来的，但实际上实例和类也是一种继承关系，实例继承自类，而类和类的继承关系也与之类似，只是语法稍有不同。下面我们来看这个例子：

    class Hero():
        def addlevel(self):
            self.level=self.level+1
            self.hp=self.hp+self.addhp
    
    class Garen(Hero):
        level=1
        hp=455
        addhp=96
    
    garen001=Garen()
    for i in range(6):
        print('级别:',garen001.level,'生命值：' ,garen001.hp)
        garen001.addlevel()
    
    级别: 1 生命值： 455
    级别: 2 生命值： 551
    级别: 3 生命值： 647
    级别: 4 生命值： 743
    级别: 5 生命值： 839
    级别: 6 生命值： 935

![img]({static}/images/python/lei-de-ji-cheng-shi-li.png)

这里就简单的两个类，盖伦Garen类是继承自Hero类的，实例garen001是继承自Garen类的，这样garen001也有了addlevel方法，就是将自己的level属性加一，同时hp生命值也加上一定的值，整个过程还是很直观的。

### 类的内置方法

如果构建一个类，就只是简单的加上pass语句，什么都不做，python还是会为这个类自动创建一些属性或者方法。

    >>> class TestClass:
    ...  pass
    ... 
    >>> dir(TestClass)
    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__',
     '__eq__', '__format__', '__ge__', '__getattribute__',
      '__gt__',  '__hash__', '__init__', '__le__', '__lt__',
       '__module__', '__ne__', '__new__', '__reduce__', 
       '__reduce_ex__', '__repr__', '__setattr__', 
       '__sizeof__', '__str__', '__subclasshook__',
        '__weakref__']

这些变量名字前后都加上双下划线是给python这个语言的设计者用的，一般开发者还是不要这样命名变量。

这些内置方法用户同样也是可以重定义他们从来覆盖掉原来的定义，其中特别值得一讲的就是`__init__`方法或者称之为构造函数。

### \_\_init\_\_方法

`__init__`方法对应的就是该类创建实例的时候的构造函数。比如：

    >>> class Point:
    ...  def __init__(self,x,y):
    ...   self.x=x
    ...   self.y=y
    ... 
    >>> point001=Point(5,4)
    >>> point001.x
    5
    >>> point001.y
    4

这个例子重载了`__init__`函数，然后让他接受三个参数，self是等下要创建的实例，x，还有y通过下面的语句给这个待创建的实例的属性x和y赋了值。

### self意味着什么 

self在类中是一个很重要的概念，当类的结构层次较简单时还容易看出来，当类的层次结构很复杂之后，你可能会弄糊涂。比如你现在通过调用某个实例的某个方法，这个方法可能是一个远在天边的某个类给出的定义，就算如此，那个定义里面的self还是指调用这个方法的那个实例，这一点要牢记于心。

比如下面这个例子：

    class Test():
        x = 5
        def __init__(self):
            self.x = 10
    
    test = Test()
    
    >>> test.x
    10
    >>> Test.x
    5

其中self.x就是对应的创建的实例的属性x，而前面定义的x则是类Test的属性x。

### 类的操作第二版

现在我们可以写出和之前那个版本相比更加专业的类的使用版本了。

    class Hero():
        def addlevel(self):
            self.level=self.level+1
            self.hp=self.hp+self.addhp
    
    class Garen(Hero):
        def __init__(self):
            self.level=1
            self.hp=455
            self.addhp=96
            self.skill=['不屈','致命打击','勇气','审判','德玛西亚正义']
    
    garen001=Garen()
    for i in range(6):
        print('级别:',garen001.level,'生命值：' ,garen001.hp)
        garen001.addlevel()
    print('盖伦的技能有：',"".join([x + '  ' for x in garen001.skill]))
    
    级别: 1 生命值： 455
    级别: 2 生命值： 551
    级别: 3 生命值： 647
    级别: 4 生命值： 743
    级别: 5 生命值： 839
    级别: 6 生命值： 935
    盖伦的技能有： 不屈  致命打击  勇气  审判  德玛西亚正义

似乎专业的做法类里面多放点方法，最好不要放属性，不太清楚是什么。但确实这样写给人感觉更干净点，方法是方法，如果没有调用代码就放在那里我们不用管它，后面用了构造函数我们就去查看相关类的构造方法，这样很省精力。

### 类的操作第三版 

    class Unit():
        def __init__(self,hp,atk,color):
            self.hp=hp
            self.atk=atk
            self.color=color
        def __str__(self):
            return '生命值：{0}，攻击力：{1}，颜色：\
            {2}'.format(self.hp,self.atk,self.color)
    
    class Hero(Unit):
        def __init__(self,level,hp,atk,color):
            Unit.__init__(self,hp,atk,color)
            self.level=level
        def __str__(self):
            return '级别：{0},生命值：{1}，攻击力：{2}，\
            颜色：{3}'.format(self.level,self.hp,self.atk,self.color)
    
        def addlevel(self):
            self.level=self.level+1
            self.hp=self.hp+self.addhp
            self.atk=self.atk+self.addatk
    
    class Garen(Hero):
        def __init__(self,color='blue'):
            Hero.__init__(self,1,455,56,color)
            self.name='盖伦'
            self.addhp=96
            self.addatk=3.5
            self.skill=['不屈','致命打击','勇气','审判','德玛西亚正义']
    
    if __name__ == '__main__':
        garen001=Garen('red')
        garen002=Garen()
        print(garen001)
        unit001=Unit(1000,1000,'gray')
        print(unit001)
        for i in range(6):
            print(garen001)
            garen001.addlevel()
        print('盖伦的技能有：',"".join([x + '  ' for x in garen001.skill]))
    
    级别：1,生命值：455，攻击力：56，        颜色：red
    生命值：1000，攻击力：1000，颜色：        gray
    级别：1,生命值：455，攻击力：56，        颜色：red
    级别：2,生命值：551，攻击力：59.5，        颜色：red
    级别：3,生命值：647，攻击力：63.0，        颜色：red
    级别：4,生命值：743，攻击力：66.5，        颜色：red
    级别：5,生命值：839，攻击力：70.0，        颜色：red
    级别：6,生命值：935，攻击力：73.5，        颜色：red
    盖伦的技能有： 不屈  致命打击  勇气  审判  德玛西亚正义

现在就这个例子相对于第二版所作的改动，也就是核心知识点说明之。其中函数参量列表中这样表述`color='blue'`表示blue是color变量的备选值，也就是color成了可选参量了。

#### 构造函数的继承和重载

上面例子很核心的一个概念就是`__init__`构造函数的继承和重载。比如我们看到garen001实例的创建，其中就引用了Hero的构造函数，特别强调的是，比如这里 `Hero.__init__(self,1,455,56,color)` 就是调用了Hero类的构造函数，这个时候需要把self写上，因为self就是最终创建的实例garen001，而不是Hero，而且调用Hero类的构造函数就必须按照它的参量列表形式来。这个概念需要弄清楚！

理解了这一点，在类的继承关系中的构造函数的继承和重载就好看了。比如这里Hero类的构造函数又是继承自Unit类的构造函数，Hero类额外有一个参量level接下来也要开辟存储空间配置好。

#### \_\_str\_\_函数的继承和重载

第二个修改是这里重定义了一些类的`__str__`函数，通过重新定义它可以改变默认print某个类对象是的输出。默认只是一段什么什么类并无具体内容信息。具体就是return一段你想要的字符串样式即可。



## 类的高级知识


首先说下python2和python3的兼容性，如果读者在python2.7环境下，那么推荐定义class的时候都如下跟上object：

    class Test(object):
        pass

本章节围绕着下面这些内容逐步展开，从而逐步实现对python类的各个行为的深度定制。

1.  内省属性： `__dict__` ， `__class__`

2.  进行某种运算符操作或调用某个常见的方法时的行为重载。

3.  函数装饰器： 函数调用行为的定制

4.  一般属性访问行为定制

5.  特定属性访问时行为定制

6.  类实例创建时行为定制——类装饰器

7.  类对象创建时行为定制——metaclass

### \_\_dict\_\_

参考了 [这个网页](http://www.cnblogs.com/vamei/archive/2012/12/11/2772448.html) 。

首先读者记住class是个类似于def一样的语句，其也管理一个名字空间，然后区块里面的语句逐步执行。然后我们看下面这个例子：

```python
class A():

    def __init__(self, a):
        self.a = a

    def fun2(self, what):
        print('fun', what)

    @property
    def x(self):
        return 1
```


```text
class B(A):

    def __init__(self):
        self.d = 5
    b = 2

    def fun3(self):
        print('fun3')

b = B()

   b.__class__
=> <class 'B'>
   B.__class__
=> <class 'type'>
   b.__dict__
=> {'d': 5}
   B.__dict__
=> mappingproxy({'__module__': 'builtins', '__init__': <function B.__init__ at 0x7f13586057b8>, 'b': 2, 'fun3': <function B.fun3 at 0x7f1358605840>, '__doc__': None})
   A.__dict__
=> mappingproxy({'__module__': 'builtins', '__init__': <function A.__init__ at 0x7f1358605620>, 'fun2': <function A.fun2 at 0x7f13586056a8>, 'x': <property object at 0x7f1358604188>, '__dict__': <attribute '__dict__' of 'A' objects>, '__weakref__': <attribute '__weakref__' of 'A' objects>, '__doc__': None})
```

这个例子很有些东西，首先 `b.__class__` 是查看实例b的类型，大体输出接近于 `type(b)` ，然后我们看到类B的类型是type。后面在将metaclass会讲到这个，目前记住实例是根据类创建的，而类是根据元类也就是这个type创建的。

然后我们看到不管是实例b还是类B或者类A都记忆了一些自己的属性，至于继承来的属性是不需要重复记忆了。

然后类的 `__dict__`是 mappingproxy对象，其是只读的，也就是只有实例b的 `__dict__` 是 dict类型，是可以读写的（参考了[这篇文章](http://pyzh.readthedocs.io/en/latest/python-questions-on-stackoverflow.html#dict)）。

最后通过 `@property` 装饰器修饰的函数，我们会得到一个 property object，这个后面会谈到，这个特定的属性访问行为是可定制的，通过描述符对象。

### \_\_getitem\_\_

`__getitem__(self, key)` 方法定义了实例的这种形式 `Class['key']`的行为。

```python
class Test():
    a = 1
    def __getitem__(self,key):
        print('i accpeted: {0}'.format(key))
        return self.a

t = Test()

>> t['a']
i accpeted: a
=> 1
```

**默认一般的类是不支持这种 Test['x'] 这种写法。**  然后 `__setitem__(self, key, value)` 方法 对应 `t['x']=3` 这样的赋值形式；还有 `__delitem(self, key)__` 方法对应这样的运算符号表示： `del t['x']`。

按照python官方文档的介绍：在实现这个方法的时候，有几个异常规范：

- TypeError 当key是不恰当类型抛出
- IndexError 如果给定的值超出了序列的索引范围则应该抛出这个异常
- KeyError 如果没有这个key则应该抛出这个异常。



### 数学运算符号重载

一般应用层面很少有需求去重载这些数学运算符号操作吧。这里稍微了解下即可。

一般加法

:   X + other , `__add__(self,other)`

右侧加法

:   所谓加法是X+other，如果是右侧加法，则为radd，然后公式是：other+X。一般不区分左右的就用上面的一般加法。other +
    X , `__radd__(self,other)`

增强加法

:   X +=other ，`__iadd__(self.other)`

一般减法

:   X - other , `__sub__(self,other)`。同上面情况一样类似的还有rsub和isub。

`*`

:   乘法，`__mul__(self,other)`，下面的类似的都有右侧运算和增强运算，不再赘述了。

`//`

:   整除，`__floordiv__`，下面类似的参数都是self和other，不再赘述了。

`/`

:   除法 ，`__div__`

`%`

:   取余，`__mod__`

`**`

:   开方，`__pow__`

`<<`

:   左移运算，`__lshift__`

`>>`

:   右移运算，`__rshift__`

`&`

:   位与，`__and__`

`|`

:   位或，`__or__`

`^`

:   位异或，`__xor__`

类似的右侧运算名字前面加上r，增强运算名字前面加上i，不赘述了。

### 逻辑运算

### bool函数

bool(X) `__bool__(self)`

### \_\_eq\_\_

`__eq__`方法定义了两个对象之间A == B的行为。 比如下面：

```python
def __eq__(self,other):
    if self.__dict__.keys() == other.__dict__.keys():
        for key in self.__dict__.keys():
            if  not self.__dict__.get(key)==other.__dict__.get(key):
                return False
        return True
    else:
        return False
```

定义了这样的`__eq__`方法之后，我们运行==语句，如果两个对象之间内置字典键和值都是一样的，那么就返回True。

    >>> test=GClass()
    >>> test.a=1
    >>> test2=GClass()
    >>> test2.a=1
    >>> test == test2
    True
    >>> test is test2
    False

如果我们不重定义`__eq__`方法，似乎test和test2会从原始的object类继承`__eq__`方法，然后它们比较返回的是False，我想可能是这两个实例内部某些值的差异吧，但应该不是基于id。

### 比较判断操作

类似上面的==比较操作，还有如下比较判断操作和对应的内置方法可以重定义。

-   X != Y ，行为由`__ne__(self,other)`定义。

-   X >= Y ，行为由`__ge__(self,other)`定义。

-   X <= Y ，行为由`__le__(self,other)`定义。

-   X > Y ，行为由`__gt__(self,other)`定义。

-   X < Y ，行为由`__lt__(self,other)`定义。

### in语句

**NOTICE**：不知道是以前记错了还是python3改动了，现在in语句应该用 `__contains__` 来重载。

提供了`what in X` 语句的支持，上面的例子是基于类其内字典的内容而做出的判断。

### 类之间的相等判断

[参考网站](http://www.informit.com/articles/article.aspx?p=453682)。

这里先总结下is语句和==判断和isinstance和id还有type函数，然后再提及python类的内置方法`__eq__`。

python是一个彻头彻尾的面向对象的语言，python内部一切数据都是对象，对象就有类型type的区别。比如内置的那样对象类型：

    >>> type('abc')
    <class 'str'>
    >>> type(123)
    <class 'int'>
    >>> type([1,2,3])
    <class 'list'>

对象除了有type类型之外，还有id属性，id就是这个对象具体在内存中的存储位置。

当我们说lst=\[1,2,3\]的时候，程序具体在内存中创建的对象是\[1,2,3\]，而lst这个变量名不过是一个引用。然后我们看下面的例子：

    >>> x=[1,2,3]
    >>> y=[1,2,3]
    >>> type(x)
    <class 'list'>
    >>> type(y)
    <class 'list'>
    >>> id(x)
    3069975884
    >>> id(y)
    3062209708
    >>> x==y
    True
    >>> x is y
    False

type函数返回对象的类型，id函数返回对象具体在内存中的存储位置，而==判断只是确保值相等，is语句返回True则更加严格，需要对象在内存上（即id相等）完全是同一个东西。

对象之间的类型比较可以用如下语句来进行比较：

    >>> x=10
    >>> type(x) == int
    True
    >>> type(x) == type(0)
    True

不过不是特别好用，比如假设fun是你自己定义的一个函数，用type(fun) ==
function就会出错，然后type比较还要小心NoneType和其他空列表类型不同，而且type比较并没有将类的继承考虑进去。

一般推荐isinstance函数来进行类型比较，请参考[这个网站](http://stackoverflow.com/questions/1549801/differences-between-isinstance-and-type-in-python)的说明。推荐使用types模块的特定名字来判断类型，具体如下：

types.NoneType

:   None这个值的类型

types.TypeType

:   type对象。

types.BooleanType

:   还可以使用**bool**。

types.IntType

:   还可以使用**int**，类似的有**long**，**float**。

types.ComplexType

:   复数类型

types.StringType

:   字符串类型，还可以使用**str**。

types.TupleType

:   元组，还可以使用**tuple**，类似的有**list**，**dict**。

types.FunctionType

:   定义的函数类型，此外还有**types.LambdaType**。

    值得一提的是print等内置函数不是FunctionType而是BuiltinFunctionType。
    
        >>> import types
        >>> isinstance(print,types.FunctionType)
        False
        >>> isinstance(print,types.BuiltinFunctionType)
        True

更多内容请参见[types模块的官方文档](https://docs.python.org/3.4/library/types.html)。

### 强制类型变换

所包含的内置方法有：

```text
__int__(self)   返回整型
__long__(self)  长整型
__float__(self)  浮点型
__complex__(self)  复数型
__str__(self)  字符型
__oct__(self)  八进制
__hex__(self) 十六进制
__index__(self) 切片操作
```

### `len(what)`

`len(what)` 由`__len__(self)`提供支持。

### copy方法和deepcopy方法

X.copy() 由`___copy__(self)`提供。

X.deepcopy() 由`__deepcopy__(self)`提供。

这里就要提一下python的copy模块了，一般很少有人去专门针对某个类单独编写 `__deepcopy__` 方法，可能会有某些特殊的情况吧，其他很多情况使用 `copy.deepcopy(what)` 是够用的。



### with语句支持

按照PEP343的说法：

```text
with VAR = EXPR: 
    BLOCK
    
with EXPR as VAR:
    BLOCK
```

实际上就是：

```text
VAR = EXPR
VAR.__enter__()
try:
    BLOCK
finally:
    VAR.__exit__()
```

比如我们执行 `with open(...) as f` 的这类语句，最终离开就应该调用了文件对象的 `__exit__` 方法：

```
with open(...) as f:
    BLOCK

f = open(...)
f.__enter__()
try: 
    BLOCK
finally:
    f.__exit__()
```

此外在`contextlib` 那里还提供了一个**contextmanager** 装饰器，写法有点差异，但要实现的效果大致是类似的。下面是一个演示例子：

```python
class Mylock():
    def __enter__(self):
    	self.lock = acquire_lock()
        return self.lock
    def __exit__(self):
        self.lock.release()
        
with Mylock() as lock:
    # do something
    

from contextlib import contextmanager
@contextmanager
def get_lock(...):
    lock = acquire_lock()
    try:
        yield lock
    finally:
        lock.release()
        
with get_lock(...) as lock:
    # do something

```



### \_\_call\_\_

请看下面的例子：

```python
class Position():
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def __call__(self,x,y):
        self.x = x
        self.y = y
    def __repr__(self):
        return '('+str(self.x)+ ',' + str(self.y)+')'

>>> p1=Position()
>>> print(p1)
(0,0)
>>> p1(4,5)
>>> print(p1)
(4,5)
>>> 
```

有了`__call__(self,args)`方法，你的实例就好像函数一样可以被调用了。

### `__repr__` 和 `__str__` 的区别

简单来说就是 repr(what) 调用的是 `__repr__` 方法，str(what) 调用的是 `__str__` 方法。然后再简单实验了一下，和print函数和字符串format相关的使用的是 `__str__` 方法，如果你在python的REPL环境下，简单的输入该变量回显使用的是 `__repr__` 方法。如果你不实现`__str__` 方法，print函数或者字符串format相关的使用会调用 `__repr__` 方法，至于 `__repr__` 方法就算你不实现所有python对象都有默认的 `__repr__` 方法的。

### \_\_new\_\_

一个类创造出一个实例出来首先是调用 `__new__` 方法，然后才是调用`__init__`方法。其一个应用就是所谓的单例模式，也就是一个类只能创造一个实例，请参看 [这篇文章](https://segmentfault.com/a/1190000008141049) 。【下面代码做了一些修改，python3之后除了`super()` 写法可以简化之外，object的`__new__` 方法是不带参数的。然后python的`__new__` 和 `__init__` 是协作关系，似乎要求参数存在某种一致性，暂时还不太清楚。TODO】

```python
class Singleton(object):
    _instance = None
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)  
        return cls._instance  

class MyClass(Singleton):  
    a = 1

>>> one = MyClass()
>>> two = MyClass()
>>> one == two
True
>>> one is two
True
>>> id(one), id(two)
(4303862608, 4303862608)
```

这里还有一个点，为什么 `_instance` 在两个类初始化过程中指向同一个对象。因为 `_instance` 是属于类的，而实例是基于类的 `__new__` 和 `__init__` 方法生成出来的，所以假设你是python程序，那个类（class其实和def一样的一种东西）为什么不在内存里编译好了就可以了，后面都引用这个类就行了。那么这个内存编译好了的类里面的 `_instance` 变量当然也封装好了。理解这个过程有助于我们进一步理解类变量的作用范围。

### \_\_del\_\_

当对象内存存储被回收时，python最后将执行一个内置方法`__del__`。有的时候你定义的需要管理一些额外的资源，定制这个函数可以确保python程序关闭时目标资源已经自动关闭回收。

### \_\_getattr\_\_

如果某个属性不在对象的 `__dict__` 里面，然后python会调用`__getattr__(self,name)` 方法（参考了[这篇文章](http://www.cnblogs.com/vamei/archive/2012/12/11/2772448.html) ）。如果没定义这个方法那么将抛出 AttributeError 。

因为python语言内部是行为是可能发生变化的，这里更确切的表述参考python官方文档是，如果python默认属性查找没有找到，那么将试着调用该对象的 `__getattr__` 方法来查找，还找不到则抛出 `AttributeError` 异常。官方文档还强调，如果按照python默认的属性查找动作，找到目标属性了，也就是之前我们讨论的那些和类继承相关的属性找到等等。那么 `__getattr__` 方法是不会被调用的。所以我们要实现 `__getattr__` 方法加上额外的查找动作代码如下：

```python
    def __getattr__(self, item):
        if self.ref_element:
            if hasattr(self.ref_element, item):
                return getattr(self.ref_element, item)

        raise AttributeError(f'no such attribute in this object')
```



然后还有 `__setattr__(self,name,value)` 和 `__delattr__(self,name)`，这两个方法不管原属性在不在都会对其进行操作，谨慎使用！相关的`__getattribute__` 方法一般不推荐使用，这会干扰python默认的属性查找行为，这是一种很不好的编程实践。

## 迭代器和生成器

首先推荐 [这篇文章](https://foofish.net/iterators-vs-generators.html)，对本小节概念的理清帮助很大。下面我们慢慢来说。

![迭代器和生成器的关系](http://img2.foofish.net/relationships.png)

首先Iterable叫做可迭代对象，Iterator叫做迭代器。在collections里面有这两个类，可以做出判断：

    from collections import Iterable,Iterator
    isinstance(obj, Iterable)
    isinstance(obj, Iterator)

然后我们再来看官方文档的词语解释：

> iterable -- 可迭代对象
>
> 能够逐一返回其成员项的对象。可迭代对象的例子包括所有序列类型（例如 [`list`](https://docs.python.org/zh-cn/3/library/stdtypes.html#list)、[`str`](https://docs.python.org/zh-cn/3/library/stdtypes.html#str) 和 [`tuple`](https://docs.python.org/zh-cn/3/library/stdtypes.html#tuple)）以及某些非序列类型例如 [`dict`](https://docs.python.org/zh-cn/3/library/stdtypes.html#dict)、[文件对象](https://docs.python.org/zh-cn/3/glossary.html#term-file-object) 以及定义了 [`__iter__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__iter__) 方法或是实现了 [Sequence](https://docs.python.org/zh-cn/3/glossary.html#term-sequence) 语义的 [`__getitem__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__getitem__) 方法的任意自定义类对象。
>
> 可迭代对象被可用于 [`for`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#for) 循环以及许多其他需要一个序列的地方（[`zip()`](https://docs.python.org/zh-cn/3/library/functions.html#zip)、[`map()`](https://docs.python.org/zh-cn/3/library/functions.html#map) ...）。当一个可迭代对象作为参数传给内置函数 [`iter()`](https://docs.python.org/zh-cn/3/library/functions.html#iter) 时，它会返回该对象的迭代器。这种迭代器适用于对值集合的一次性遍历。在使用可迭代对象时，你通常不需要调用 [`iter()`](https://docs.python.org/zh-cn/3/library/functions.html#iter) 或者自己处理迭代器对象。`for` 语句会为你自动处理那些操作，创建一个临时的未命名变量用来在循环期间保存迭代器。参见 [iterator](https://docs.python.org/zh-cn/3/glossary.html#term-iterator)、[sequence](https://docs.python.org/zh-cn/3/glossary.html#term-sequence) 以及 [generator](https://docs.python.org/zh-cn/3/glossary.html#term-generator)。
>
> iterator -- 迭代器
>
> 用来表示一连串数据流的对象。重复调用迭代器的 [`__next__()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#iterator.__next__) 方法（或将其传给内置函数 [`next()`](https://docs.python.org/zh-cn/3/library/functions.html#next)）将逐个返回流中的项。当没有数据可用时则将引发 [`StopIteration`](https://docs.python.org/zh-cn/3/library/exceptions.html#StopIteration) 异常。到这时迭代器对象中的数据项已耗尽，继续调用其 `__next__()` 方法只会再次引发 [`StopIteration`](https://docs.python.org/zh-cn/3/library/exceptions.html#StopIteration) 异常。迭代器必须具有 [`__iter__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__iter__) 方法用来返回该迭代器对象自身，因此迭代器必定也是可迭代对象，可被用于其他可迭代对象适用的大部分场合。一个显著的例外是那些会多次重复访问迭代项的代码。容器对象（例如 [`list`](https://docs.python.org/zh-cn/3/library/stdtypes.html#list)）在你每次向其传入 [`iter()`](https://docs.python.org/zh-cn/3/library/functions.html#iter) 函数或是在 [`for`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#for) 循环中使用它时都会产生一个新的迭代器。如果在此情况下你尝试用迭代器则会返回在之前迭代过程中被耗尽的同一迭代器对象，使其看起来就像是一个空容器。

生成器函数区别一般函数是使用了yield语句返回，具体这块和python的异步相关，后面再说。然后还有生成器表达式：

```
test1 = (i+1 for i in range(5))
isinstance(test1, Iterator)
>>> True
isinstance(test1, Iterable)
>>> True
```

其都是生成器，生成器是某种简化版的迭代器，迭代器一定是可迭代对象。而某个可迭代对象经过 iter 函数处理就成了 迭代器了。就一般而言简单理解，认为某个对象具有 `__iter__` 方法，那么它就是一个可迭代对象，如果某个对象具有 `__next__` 方法，那么它就是一个迭代器。

常见的for遍历的过程如下所示：

```python
>>> list=[1,2,3]
>>> iter=iter(list)
>>> while True:
...    try:
...        x=next(iter)
...    except StopIteration:
...        break
...    print(x)
... 
1
2
3
```

iter函数是调用目标对象的 `__iter__` 方法（决定了该对象是可迭代对象的方法），就一般而言的简单情况是，`__iter__` 方法返回的目标对象自身，因为目标对象自身已经定义了 `__next__` 方法。

而就迭代器来说，其迭代过程就是调用自身的 `__next__` 方法来获取下一个值，遇到 `StopIteration` 异常停止获取。

上面提到的for语句，还有map zip 之类的函数是将这个过程自动做了的。包括iter函数处理和捕获终止异常。

比如文件对象本身就是可迭代的，调用`__next__`方法就返回文件中下一行的内容，到达文件尾也就是迭代越界了返回：**StopIteration**异常。

next函数比如next(f)等价于`f.__next__()` 。

    >>> for line in open('removeduplicate.py'):
    ...  print(line,end='')
    ... 
    #!/usr/bin/env python3
    #-*-coding:utf-8-*-
    #此处一些内容省略。
        
    >>> f=open('removeduplicate.py')
    >>> next(f)
    '#!/usr/bin/env python3\n'

所以你可以通过定义类的 `__next__` 方法来获得这个类对于next函数时的反应。

序列（列表，元组，字典，ranges对象）等是可迭代对象，不是迭代器。其经过iter函数处理就成了迭代器了。

除了上面提及的常规操作，通过 `__iter__` 返回自身，然后通过构建 `__next__` 方法来定制迭代器行为外：

```python
class Test(object):
    def __init__(self):
        self.count = 0
    def __iter__(self):
        return self
    def __next__(self):
        self.count += 1
        if self.count >= 3:
            raise StopIteration
        return self.count
```

```
isinstance(t, Iterator)
>>> True
list(t)
>>> [1, 2]
```

你也可以直接通过定义 `__iter__`方法返回一个生成器对象（generator object），这因为生成器总是迭代器。

下面这个例子通过重新定义字典类的`__iter__`方法来获得一个新类，这个类用iter函数处理之后的迭代器返回的是经过排序的字典的键。

```python
class SortedDict(dict):
    def __init__(self,dict={}):
        super().__init__(dict)

    def __iter__(self):
        self._keys = sorted(self.keys())
        for i in self._keys:
            yield i

dict02 = SortedDict()
dict02['a'] = 1
dict02['b'] = 1
dict02['d'] = 1
dict02['c'] = 1
```

```
for i in dict02:
    print(i)
```

```
a
b
c
d
```

但是要注意上面的例子，只在for语句直接迭代目标对象时才会调用 `__iter__` 方法的。

### 深入理解python的迭代操作

在python中一般复杂的代码运算效率就会低一点，如果完成类似的工作但你可以用更简单的语句那么运算效率就会高一点。当然这只是python的一个设计理念，并不尽然，但确实很有意思。

程序结构中最有用的就是多个操作的重复，其中有迭代和递归还有一般的循环语句。递归函式感觉对于某些特殊的问题很有用，然后一般基于数据结构的不是特别复杂的操作重复用迭代语句即可，最后才考虑一般循环语句。

迭代语句中for语句运算效率最低，然后是map函数（不尽然），然后是列表解析。所以我们在处理问题的时候最pythonic的风格，运算效率最高的就是列表解析了，如果一个问题能够用列表解析解决那么就用列表解析解决，因为python的设计者的很多优化工作都是针对迭代操作进行的，然后python3进一步深化了迭代思想，最后python中的迭代是用c语言来实现的。

可是让我们反思一下为什么列表解析在问题处理的时候如此通用？比如说range函数或者文件对象或者列表字符串等等，他们都可以称之为可迭代对象。可迭代对象最大的特色就是有一系列的元素，然后这一系列的元素可以逐个调出来，而列表解析就是对这些调出来的元素进行了某个表达式操作，然后将其收集起来。这是什么？我们看下面这张图片：

![img]({static}/images/python/lie-biao-jie-xi.png)

这张图片告诉我们列表解析和数学上所谓的集合还有函数的定义非常的类似，可迭代对象就好像是一个集合（有顺序或者没顺序都行），然后这些集合中的所有元素经过了某个操作，这个操作似乎就是我们数学中定义的函数，然后加上过滤条件，某些元素不参加运算，这样就生成了第二个可迭代对象（一般是列表也可以是字典什么的。）

有一个哲学上的假定，那就是我们的世界一切问题都可以用数学来描述，而一些数学问题都可以用函数即如上的信息操作过滤流来描述之。当然这不尽然，但我们可以看到列表解析在一般问题处理上是很通用的思想。

不过我们看到有限的元素的集合问题适合用迭代，但无限元素的集合问题也许用递归或者循环更适合一些。然后我们又想到集合的描述分为列举描述（有限个元素的列举）和定义描述。比如说 `1<x<10` ，x属于整数，这就定义了一个集合。那么我们就想到python存在这样的通过描述而不是列举（如列表一样）的集合吗？range函数似乎就是为了这样的目的而生的，比如说 `range(10)` 就定义了 `[0,10)`这一系列的整数集合，range函数生成一个range对象，range对象是一个可迭代对象，我们可以把它看作可迭代对象中的描述集合类型吧。这时我们就问了，既然 `0<=x<10`这样的整数集合可以通过描述来实现，那么更加复杂的函数描述可不可以实现呢？我们可不可以建立更加复杂的类似range对象的描述性可迭代对象呢？

### map和filter函数

按照之前的迭代模式的描述，虽然使用常见的列表解析格式(for语句)就可以完成对某个集合中各个元素的操作或者过滤，不过python中还有另外两个函数来实现类似的功能，map对应对集合中各个元素进行某个函数操作（可以接受lambda函式），而filter则实现如上所述的过滤功能。然后值得一提的是python3之后map函数和filter函数返回都是一个可迭代对象而不是列表，和range函数等其他可迭代对象一样可用于列表解析结构。

### map函数

这里列出一些例子：

```
>>> map(abs, [-2,-1,0,1,2])
<map object at 0xb707dccc>
>>> [x for x in map(abs, [-2,-1,0,1,2])]
[2, 1, 0, 1, 2]
>>> [x for x in map(lambda x : x+2, [-2,-1,0,1,2])]
[0, 1, 2, 3, 4]
```

map函数还可以接受两个可迭代对象的协作参数模式，这个学过lisp语言的会觉得很眼熟，不过这里按照我们的理解也是很便捷的。具体就是第一个可迭代对象取出一个元素作为map的函数的第一个参数，然后第二个可迭代对象取出第二个参数，然后经过函数运算，得到一个结果，这个结果如果不列表解析的话就是一个map对象（可迭代对象），然后展开以此类推。值得一提的是两个可迭代对象的*深度由最短的那个决定*，请看下面的例子：

```
>>> [x for x in map(lambda x,y : x+y, [-2,-1,0,1,2],[-2,-1,0,1,2])]
[-4, -2, 0, 2, 4]
>>> [x for x in map(lambda x,y : x+y, [-2,-1,0,1,2],[-2,-1,0,1])]
[-4, -2, 0, 2]
```

### filter函数

同样和上面的谈及的类似，filter函数过滤一个可迭代对象然后产生一个可迭代对象。类似的功能可以用列表解析的后的if语句来实现。前面谈到map函数的时候提及一般还是优先使用列表解析模式，但filter函数这里有点不同，因为列表解析后面跟个if可能有时会让人困惑，这时推荐还是用filter函数来进行可迭代对象的过滤操作。

filter函数的基本逻辑是只有 `return True`（用lambda表达式就是这个表达式的值为真) 的时候元素才被收集起来，或者说是过滤出来。

请参看下面的例子来理解：

```
>>> [x for x in filter(lambda x:x&1,[1,2,3,5,9,10,155,-20,-25])]
[1, 3, 5, 9, 155, -25]
>>> [x for x in filter(lambda x:not x&1,[1,2,3,5,9,10,155,-20,-25])]
[2, 10, -20]
```

当然你也可以传统的编写函数：

```
>>> def even(n):
...    if n % 2 ==0:
...         return True

>>> [x for x in filter(even,[1,2,3,5,9,10,155,-25])]
[2, 10]
```

### zip函数

这里就顺便把zip函数也一起提了，zip函数同样返回一个可迭代对象，它接受任意数目的可迭代对象，然后逐个取出可迭代对象元素构成一个元组成为自己的一个元素。和map函数类似*迭代深度由最短的那个可迭代对象决定*。

```
>>> zip(['a','b','c'],[1,2,3,4])
<zip object at 0xb7055e6c>
>>> [x for x in zip(['a','b','c'],[1,2,3,4])]
[('a', 1), ('b', 2), ('c', 3)]
>>> list(zip(['a','b','c'],[1,2,3,4]))
[('a', 1), ('b', 2), ('c', 3)]
>>> dict(zip(['a','b','c'],[1,2,3,4]))
{'c': 3, 'b': 2, 'a': 1}
```

### 列表到字典

这个例子似乎使用价值不大，只是说明zip函数接受任意数目参数的情况。y.items()解包之后是4个参数传递给zip函数，而zip函数的封装逻辑就是如果有人问我，我就把你们这些迭代对象每个取出一个元素，然后用元组包装之后返回。

```
x1 = ['a','b','c','e']
x2 = [1,2,3,4]
y = dict(zip(x1,x2))
print('列表到字典：',y)
new_x1,new_x2 = zip(*y.items())
print(new_x1,new_x2)

列表到字典： {'b': 2, 'c': 3, 'a': 1, 'e': 4}
('b', 'c', 'a', 'e') (2, 3, 1, 4)
```

这个例子如果到更加复杂的情况，我们可以跳过字典形式，来个数据映射对：

```
>>> x1 = ['a','b','c','e']
>>> x2 = ['red','yellow','red','blue']
>>> x3 = [1,2,3,4]
>>> list(zip(x1,x2,x3))
[('a', 'red', 1), ('b', 'yellow', 2), ('c', 'red', 3), ('e', 'blue', 4)]
>>> new_x1,new_x2,new_x3 = zip(*list(zip(x1,x2,x3)))
>>> new_x1
('a', 'b', 'c', 'e')
>>> new_x2
('red', 'yellow', 'red', 'blue')
>>> new_x3
(1, 2, 3, 4)
```

当然对于多属性数据问题一般还是推荐使用类来处理，不过某些情况下可能不需要使用类，就这样简单处理之。

值得一提的是这种数据存储形式和sql存储是一致的，而且不知道你们注意到没有，这似乎实现了矩阵的转置功能。



## 装饰器

装饰器的作用机制就是对接下来的函数进行进一步的封装，比如：

        @staticmethod
        def what():
            pass
            
        # 其就等价于在类声明语句里写上了这样一句。   
        what = staticmethod(what)

可见装饰器并不是一个什么神秘的难懂的概念，同样你可以定义自己的函数，这个函数处理某个函数对象，并对其进行某种封装。

### 自定义装饰器

    def print1(f):
        print('1',f)
        return f
    
    @print1
    def print3(c):
        print(c)
    
    print3('c')  # print1(print3)('c')

比如上面的print1函数就做成了一个装饰器函数，后面的print3函数可以理解为 `print3=print1(print3)` 。——在这里理解的关键在于理解python中函数名字是无关紧要的，关键是函数对象。比如这里右边的print3是`def print3 ` 时生成的那个函数对象，然后这个函数对象送给print1进行了处理并封装为一个新的函数对象，再把这个函数对象赋值给了变量print3。

### 多个装饰器

    def print1(f):
        print('1',f)
        return f
    
    def print2(f):
        print('2',f)
        return f
    
    @print2
    @print1
    def print4(c):
        print(c)
    
    print4('c')  

多个装饰器的装饰顺序是从下往上的，上面的例子原print4函数对象先经过print1处理，然后再经过print2的处理，最后这个函数对象赋值给了变量print4。

### 装饰器带上参数

在前面的例子中，我们就可以简单将装饰器函数理解为一个接受函数对象返回返回函数对象的函数，这很直观和简单。实际上装饰器也是可以带上自己的参数的，这需要通过函数的闭包结构【也就是函数里面定义函数的结构，这样内部函数是可以使用外部函数的那些参数和变量的】才能完成，如下面的例子所示:

    def print1(f):
        print('1',f)
        return f
    
    def print2(b):
        def test(f):
            print('2',f,b)
            return f
        return test
    
    @print2('b')
    @print1
    def print4(c):
        print(c)
    
    print4('c') 



### 一般装饰器写法

本小节参考了 [这个网页](https://stackoverflow.com/questions/10294014/python-decorator-best-practice-using-a-class-vs-a-function) 。一般书写一个装饰器函数有如下通用写法：

#### 无参数装饰器版本

```python
from functools import wraps

def mydecorator(func):
    @wraps(func)
    def wraper_func(*args, **kwargs):
        # do something
        
        return func(*args, **kwargs)
    return wraper_func

@mydecorator
def test(*args, **kwargs):
    """
    this is test function
    """
    print(args, kwargs)

    
test('test', a=1)
print(test.__doc__)
```

这里使用了 functools 模块的 wraps装饰器，其接受你要装饰的函数作为参数。如果不这样的话，你在原test函数中定义的说明文字将丢失，按照 `test=mydecorator(test)` ，实际上test变量接受的函数对象是 `wraper_func` ，不信你可以查看 `test.__name__` 其是等于 `wraper_func` 的。而如上使用wraps装饰器，你在原test函数中定义的名字和文档都将得到保留。

#### 带参数装饰器版本

```python
from functools import wraps

def mydecorator(arg1, arg2):
    def _mydecorator(func):
        @wraps(func)
        def wraper_func(*args, **kwargs):
            print('i know you pass to decorator parameters:', arg1, arg2)
			# do something
            
            return func(*args, **kwargs)
        return wraper_func
    return _mydecorator

@mydecorator('a', 'b')
def test(*args, **kwargs):
    """
    this is test function
    """
    print(args, kwargs)

    
test('test', a=1)
print(test.__doc__)
```



### 静态方法装饰器

    class Test:
    #    @staticmethod
        def hello():
            print('aaa')
    
    test=Test()
    test.hello()

在上面的例子中，我们希望创造一个函数，这个函数和self实例没有关系（这里指这个函数将不接受self这个默认参数了）。如上所示，hello函数只是希望简单打印一小段字符，如*上面这样的代码是错误*的，如果我们在这个函数上面加上 `@staticmethod` ，那么上面这段代码就不会报错了，

    class Test:
        @staticmethod
        def hello():
            print('aaa')
    
    test=Test()
    test.hello()

这样在类里面定义出来的函数叫做这个类的静态方法，静态方法同样可以继承等等，而静态方法通常使用最大的特色就是不需要建立实例，即可以直接从类来调用，如下所示：

    class Test:
        @staticmethod
        def hello():
            print('aaa')
    
    Test.hello()

静态方法的使用比如pyqt中的

    QtGui.QFileDialog.getOpenFileName(......)

就是一个静态方法，可以通过直接调用这个方法来弹出询问打开文件的窗口，并不需要先实例化一个对象，然后通过self.what等类似的形式来调用。

### 类方法装饰器

还有一个装饰器有时也会用到， `@classmethod`，叫什么类方法装饰器。其和前面的静态方法一样也可以不新建实例，而直接通过类来调用。其和静态方法的区别就是静态方法在调用的时候没有任何默认的第一参数，而类方法在调用的时候默认第一参数就是调用的那个类。

    class Test:
        @classmethod
        def hello(cls):
            print('from class:', cls, 'saying hello')
    
    Test.hello()
    
    from class: <class '__main__.Test'> saying hello

关于classmethod装饰器实际上东西就这么多，然后就是传进去的第一个参数cls看你有什么使用需要了，比如
`cls(...)` 将根据这个类来生成一个实例。



### 属性装饰器

其他编程语言的开发者可能会在类里定义一些针对某些属性的get和set之类的方法，这并不是Pythonic的风格，对于某些特定名字的属性，一般利用属性装饰器来构建，如下所示：

    class Apple():
        def __init__(self):
            self._color = 'red'
    
        @property
        def color(self):
            return self._color
    
    apple = Apple()

这样将给这个类定义个属性，具体调用这个属性就用这样的点号引用即可，然后实际执行的就是
`@property` 装饰的那个函数。 现在这个color属性只可读，不可更改。

    >>> apple.color
    'red'
    >>> apple.color = 'yellow'
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: can't set attribute

请参看
[这个网页](http://stackoverflow.com/questions/17330160/how-does-the-property-decorator-work)
，这里讲到了 `@color.setter`
装饰器，来装饰某个函数之后，通过这个函数来修改color属性。然后还有
`@color.deleter`
装饰某个函数之后，来通过这个函数来删除某个属性。这里deleter的使用可能较少，一般
`@property` 就能满足大部分需求了，有的觉得需要修改某个属性则定义setter。

一个简单的setter例子如下所示：

    class Apple():
        def __init__(self):
            self._color = 'red'
    
        @property
        def color(self):
            return self._color
    
        @color.setter
        def color(self, color):
            self._color = color
    
    apple = Apple()
    
    print(apple.color)
    apple.color = 'yellow'
    print(apple.color)



### 类作为装饰器

类作为装饰器就是利用类的 `__call__`内置方法，我把这段代码粘贴在下面了，有时可能看别人的源码有用吧，但装饰器这部分就到此为止吧，没必要弄得这么复杂了。

```
class MyDecorator(object):
    """Decorator example mixing class and function definitions."""
    def __init__(self, func, param1, param2):
        self.func = func
        self.param1, self.param2 = param1, param2

    def __call__(self, *args, **kwargs):
        ...
        #use self.param1
        result = self.func(*args, **kwargs)
        #use self.param2
        return result

def my_dec_factory(param1, param2):
    def decorator(func):
         return MyDecorator(func, param1, param2)
    return decorator
```

前面讲到class声明语句和def语句很类似，def语句是利用缩进区块内的代码（简单理解就是执行编译了一遍，当然应该还有其他处理）构建出一个函数对象，然后将这个函数对象和某个名字绑定起来。class语句也是利用缩进区块内的代码构建出一个类对象，然后将这个类对象和某个名字绑定起来。

那么类装饰器，也就是类上面挂个装饰器，如下所示是什么意思呢：

```
def decorator(C):
    return ProcessedC

@decorator    
class C:
    ....
```

这样我们得到的C是：

```
C = decorator(C)
```

所以函数装饰器相当于函数对象创建过程的深度定制DIY，而类装饰器就相当于类对象创建过程的深度DIY。

## 多重继承的顺序问题

我们来看下面这个例子：

```
class B1():x='B1'
class B2():x='B2'
class B3():x='B3'
class B(B1,B2,B3):x='B'
class A1():x='A1'
class A2():x='A2'
class A(A1,A2):x='A'
class D(B,A):x='D'
test=D()
print(test.x)
```

![多重继承示意图]({static}/images/python/duo-chong-ji-cheng.png)

你可以测试一下上面这个例子，首先当然结果是D自己的x被先查找，然后返回D ，如果你把类D的x定义语句换成pass，结果就是B。这说明这里程序的逻辑是如果test实例找不到x，那么再找D，D找不到再接下来找D继承自的父类，首先是B，到目前为止，没什么新鲜事发生。

然后我们再把B的x赋值语句换成pass，这时的结果是B1，也没什么好惊讶的。然后类似的一致操作下去，我们会发现python的值的查找顺序在这里是：D，B，B1，B2，B3，A，A1，A2。

于是我们可以总结道：恩，类的多重继承就是 **深度优先法则** ，先把子类或者子类的子类都查找完，确认没有值之后再继续从左到右的查找。

一般情况来说这么理解是没有问题的，但是在编程界多重继承中有个有名的问题——菱形难题。

### 菱形难题

参考资料：[维基百科菱形难题](http://en.wikipedia.org/wiki/Multiple_inheritance#The_diamond_problem)

![菱形难题]({static}/images/python/ling-xing-nan-ti.png )

菱形难题即在如上的类的继承中，如果C和A都有同名属性x，那么D会调用谁的呢？读者测试下面的例子：

```
class A():
    x = 'A'

class B(A):
    x = 'B'

class C(A):
    x = 'C'

class D(B, C):
    x = 'D'


test = D()
print(test.x)
```

然后我们会发现python的查找顺序是D，B，C，A。

实际上这个查找顺序python2和python3都是存在差异的，请参考 Guido 写的 [这篇文章](http://python-history.blogspot.com/2010/06/method-resolution-order.html) 。结论就是现在python3的MRO算法过程如下：

1. 搜索树会被预计算
2. 之前我们观察的深度优先算法大体是正确的，不同的是重复出现的类的处理逻辑是 **只保留最后的那个**。【因此上面的例子首先是D，B，A，C，A然后规约为了D，B，C，A】



### super如何面对菱形难题

super是引用父类动作，简单的情况就不说了，接下来请看下面这个例子：

```python
class Base():
    def __init__(self):
        print('Base')


class A(Base):
    def __init__(self):
        super().__init__()
        print('A')


class B(Base):
    def __init__(self):
        super().__init__()
        print('B')


class C(B, A):
    def __init__(self):
        super().__init__()
        print('C')


t = C()

```

这里例子刁钻就刁钻在其还多次调用了super这个函数，我一开始也以为类B那里引用super会指向Base。首先说一下这个例子的输出把：

```
Base
A
B
C
```

C那里的super引用B这没问题，B那里的super引用的是A这是我没想到的。具体原因是这个super引用逻辑还是调用的前面提到的MRO算法的预处理树，其搜索树为：C，B，A，Base。第二次调用会引用A。然后A那里super再引用Base。

最后我们的初始化动作就上面的例子来说是各个类的`__init__` 都执行了一遍。

## 描述器

本小节参考了[这个网页](http://pyzh.readthedocs.io/en/latest/Descriptor-HOW-TO-Guide.html) 。

上面谈及的属性装饰器，其实际上是调用的property函数，

    property(fget, fset, fdel, descrition) 

而这个函数返回的是一个描述器对象（Desriptor）。那么什么是一个描述器对象呢，简单来说这个对象里面定义了三个方法（最基本的是必须把
`__get__`方法定义了）。

现在让我们把思路再理一下，首先是某个instance.a这个表达，python将视图从
`__dict__` 里面去找这个属性，找得到那么一般 instance\['a'\]
这个表达也是可以获得值的（类的属性继承这里先不涉及），如果 `__dict__`
里面没有这个属性，那么python会去找 `__getattr__(self,name)`
方法，如果找不到那么就会报错。

在上面找属性的过程中，查找描述器的行为是很靠前的。如果找到的属性是一个描述器，那么python会根据这个描述器对象来决定如何提取这个属性，如何修改这个属性等的行为。

然后理解property这个函数返回的是一个怎样的描述器，看下面的python代码等价实现是最直观的了：

    class Property(object):
        "Emulate PyProperty_Type() in Objects/descrobject.c"
    
        def __init__(self, fget=None, fset=None, fdel=None, doc=None):
            self.fget = fget
            self.fset = fset
            self.fdel = fdel
            self.__doc__ = doc
    
        def __get__(self, obj, objtype=None):
            if obj is None:
                return self
            if self.fget is None:
                raise AttributeError, "unreadable attribute"
            return self.fget(obj)
    
        def __set__(self, obj, value):
            if self.fset is None:
                raise AttributeError, "can't set attribute"
            self.fset(obj, value)
    
        def __delete__(self, obj):
            if self.fdel is None:
                raise AttributeError, "can't delete attribute"
            self.fdel(obj)
    
        def getter(self, fget):
            return type(self)(fget, self.fset, self.fdel, self.__doc__)
    
        def setter(self, fset):
            return type(self)(self.fget, fset, self.fdel, self.__doc__)
    
        def deleter(self, fdel):
            return type(self)(self.fget, self.fset, fdel, self.__doc__)

## 缓存属性

下面这个例子灵感来自python官方装饰器 `@property`
的源码，稍作修改使得某个对象的属性具有记忆特性。

    import time
    import logging


```python
class memorized_property(property):

    def __init__(self, *args, **kwargs):
        super(memorized_property, self).__init__(*args, **kwargs)
        self.name = '_{}'.format(self.fget.__name__)

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError("unreadable attribute")

        if self.name in obj.__dict__:
            logging.debug('from memory--------------------')
            return obj.__dict__[self.name]
        else:
            logging.debug('from computing##########')
            value = obj.__dict__[self.name] = self.fget(obj)
            return value

    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        obj.__dict__[self.name] = value

    def __delete__(self, obj):
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        del obj.__dict__[self.name]
```


```python
class Test(object):

    def __init__(self):
        pass

    @memorized_property
    def x(self):
        return time.time()

    @x.setter
    def x(self, value):
        pass

    @x.deleter
    def x(self):
        pass

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    t = Test()
    print(t.x)
    print(t.x)
```



## 什么是metaclass

所有类都是由元类（type类）创建的，其对应的语句如下：

    class = type(classname, superclasses, attributedict)

type实际调用的是自身的 `__call__` 方法，这个方法将运行type的两个方法：
`__new__` ， `__call__` 。

这样就创造了一个类了，然后之前我们提到： 类还要调用自身的 `__new__` ，
`__call__` ，这样就创造出一个实例来了。

之前提到type的type也是type，type大体可以看作python中类型的最底层的原子结构吧。元类创造类，然后是类创造实例。

### 定义一个元类

    class Meta(type):
        def __new__(meta, classname, supers, classdict):
            # do something
            return type.__new__(meta, classname, supers, classdict)

### 使用一个元类

    class Test(Super, metaclass=Meta):
        pass

元类这里暂时还不深究，就一般的python程序员来说理解元类即可，实在不需要使用元类的。

## 进程和线程

进程的定义是: 一个正在执行的程序实例。每个进程都有一个唯一的进程ID，也就是所谓的 **PID** 。使用`ps`
命令的第一个列就是每个进程的PID属性。在python中你可以使用`os.getpid()`来查看当前进程的PID。

以前只有一个CPU的机器上，多任务操作系统实际上一次也只能运行一个进程，操作系统是通过不断切换各个进程给你一种多任务似乎同时在运行多个程序的感觉的。多CPU机器上是真的可以同时运行多个进程。

### 进程fork

进程fork进行了一些基本代码信息和其他配置以及其他相关信息的复制或注册。这就相当于在当前代码环境下，你有两个分别单独运行的程序实例了。

下面是一个非常简单的小例子，你可以把 `os.fork()`语句移到 `print('before fork')`之前来看看变化。

```python
import os, time

print('before fork ')
os.fork()

print('say hello from', os.getpid())

time.sleep(1)

print('after fork')
```

对于这个程序简单的理解就是，本py文件编译成字节码进入内存经过某些成为一个程序实例了（其中还包含其他一些信息），然后程序具体运行的时候会通过os.fork来调用系统的fork函数，然后复制本程序实例（以本程序实例目前已经所处的状态），因为 `print('before
fork')`已经执行了，所以子进程就不会执行这一行代码了，而是继续os.fork()下面的代码继续执行。此时就相当于有两个程序在运行了，至于后面的打印顺序那是说不准的。

关于操作系统具体如何fork的我们可以暂时不考虑，这两个程序实例里面的变量和运行环境基本上是一模一样的，除了运行的状态有所不同之外。fork可以做出一种程序多任务处理方案吧，不过os模块的fork方法目前只支持unix环境。

### 子进程和父进程分开

请看下面的代码:

```python
import os, time

print('before fork ')
pid = os.fork()
if pid:
    print(pid)
    print('say hello from parent', os.getpid())
else:
    print(pid)
    print('say hello from child', os.getpid())

time.sleep(1)

print('after fork')
```

其运行结果大致如下:

    before fork 
    13762
    say hello from parent 13761
    0
    say hello from child 13762
    after fork
    after fork

我们看到在父进程那一边，pid是本父进程的子进程PID，而在子进程那一边，os.fork()返回的是0。可以利用这点将父进程的操作和子进程的操作分开。具体上面的代码if
pid 那一块是父进程的，else那一块是子进程的。

### 线程入门

线程的内部实施细节其实比进程要更加复杂，可以看做是对于进程fork动作的更加轻量化实现解决方案。对于操作系统来说那怕是同一程序而来的不同的进程从程序员的角度来说可以看做完全不同的两个程序都是没有问题的，但是同一进程下的不同线程则不能这么看，首先是操作系统层面各个线程是共享进程的大部分资源，也就是这些线程对于系统资源的使用是彼此竞争关系；其次从程序员的角度来看各个线程之间也可能存在某些公有变量是各个线程之间共享的。

python操作线程的主要模块是**threading**模块，简单的使用就是新建一个线程对象(Thread)，然后调用**start**方法来启动它，具体线程要做些什么由本线程对象的**run**确定，你可以重定义它，如果是默认的就是调用本线程Thread类新建是输入的**target**参数，这个target参数具体指向某个函数。下面是一个简单的例子:

    import random, threading
    
    result = []
    
    def randchar_number(i):
        number_list = list(range(48,58))
        coden = random.choice(number_list)
        result.append(chr(coden))
        print('thread:', i)
    
    for i in range(8):
        t = threading.Thread(target = randchar_number, args=(i,))
        t.start()
    
    print(''.join(result))
    
    thread: 0
    thread: 1
    thread: 2
    thread: 3
    thread: 4
    thread: 5
    thread: 6
    thread: 7
    22972371

**注意: 控制参数后面那个逗号必须加上。**

我不太喜欢这种风格，因为线程对接的那个函数实际上并不能return什么值，而且其保存的值也依赖于前面的定义，并不能称之为真正意义上的函数（一个定义很好的函数必须复用特性很强）。所以线程还是如下类的风格编写。下面代码参考了[这个网页](http://www.ibm.com/developerworks/aix/library/au-threadingpython/index.html)。

```python
import random, threading

threads = []

class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.result = ''
    def run(self):
        number_list = list(range(48,58))
        coden = random.choice(number_list)
        self.result = chr(coden)
    def getvalue(self):
        return self.result
```


    for i in range(8):
        t = MyThread()
        t.start()
        t.join()
        threads.append(t)
    
    result = ''
    for t in threads:
        result += t.getvalue()
    print(result)
    
    05649040
    >>> 

上面调用线程对象的 **join**方法是确保该线程执行完了，其也可能返回异常。上面的做法不太标准，更标准的做法是单独写一行 `t.join` 代码:

    for t in threads:
        t.join()

来确保各个线程都执行完了，如之前的形式并不能达到多任务并行处理的效果。

上面的例子对线程的执行顺序没有特殊要求，如果有的话推荐使用python的queue模块，这里就略过了。

### 后台线程

下面的函数实现了一个后台警报线程，不会阻塞主程序。

```python
def beep(a,b):
    '''make a sound , 
    ref: http://stackoverflow.com/questions/16573051/
        python-sound-alarm-when-code-finishes
    you need install  ``apt-get install sox``

    :param a: frenquency
    :param b: duration

    create a background thread,so this function does not block
    '''
    def _beep(a,b):
        import os
        os.system('play --no-show-progress --null --channels 1 \
            synth %s sine %f' % (b,a))
    from threading import Thread
    thread = Thread(target=_beep,args=(a,b))
    thread.daemon = True
    thread.start()
```

如上所示，原beep函数调用系统的play命令制造一个声音，其中b是声音持续的时间，所以其是阻塞的。我们将其作为一个线程调用之后，然后其就没有阻塞主程序了。这里的`daemon` 的意思是让这个线程成为一个后台线程，请参看 [这个网页](http://stackoverflow.com/questions/190010/daemon-threads-explanation) ，其说道后台线程可以不用管了，后面会随着主程序自动关闭。

### 多线程: 一个定时器

这个例子主要参考了[这个网页](https://mail.python.org/pipermail/tutor/2004-November/033333.html)。

```python
import time
import threading

class Timer(threading.Thread):
    def __init__(self,interval, action=lambda:print('\a')):
        threading.Thread.__init__(self)
        self.interval = interval
        self.action = action

    def run(self):
        time.sleep(self.interval)
        self.action()

    def set_interval(self,interval):
        self.interval = interval

#timer = Timer(5)
#timer.start()

class CountDownTimer(Timer):
    def run(self):
        counter = self.interval
        for sec in range(self.interval):
            print(counter)
            time.sleep(1.0)
            counter -= 1
        ##
        self.action()

#timer = CountDownTimer(5)
#timer.start()

def hello():
    print('hello\a')

timer = CountDownTimer(5, action = hello)
timer.start()
```

具体还是很简单的，这里之所以使用线程就是为了timer.sleep函数不冻结主程序。

### 多线程下载大文件

本小节参考了 [这个网页](http://stackoverflow.com/questions/13973188/requests-with-multiple-connections) 和 [这个网页](http://stackoverflow.com/questions/16694907/how-to-download-large-file-in-python-with-requests-py) 。

下面的 `get_content_tofile`函数在目标内容大小大于1M的时候将启动多线程下载方法。其中`guess_url_filename`
函数是根据url来猜测可能的目标下载文件名字，还只是一个尝试版本。

注意下面使用requests.get函数的时候加上了`stream=True`参数，这样连接目标url的时候只是获得头文件信息而不会进一步下载content内容。这方便我们早期根据headers里面的信息做出一些判断。

接下来根据HTTP头文件的 `content-length`来判断要下载内容的大小，如果没有这个属性，那么目标url是没有content内容的，本函数将不会对这一情况做出反应，这通常是单网页url，使用requests的get方法获取网页文本内容即可。

然后如果目标长度小于1M，那么就直接打开文件，使用requests模块里response对象的`iter_content`方法来不断迭代完content内容。

如果目标长度大于1M，则采用一种多线程下载方法。首先是`get_content_partly`这个函数，接受url和index，这个index是一个简单的索引，具体多少bytes后面还需要计算。关于多线程操作和具体多少bytes的计算细节这里略过讨论了。唯一值得一提的就是HTTP协议的Range属性，begin-end，对应具体的范围0-1024，还包括1024位，所以实际上有1025个bytes，为了获得和我们python中一致的体验，我们让其end为begin+1024-1。这样就有1024个bytes位，然后定位是(0,1024)，即和python中的一样，不包括1024位。

然后还有一个小信息是，HTTP协议返回的头文件中的**content-range**属性，如果你请求Range越界了，那么将不会有这个属性。那么begin没有越界，end越界的请求如何呢？HTTP协议处理得很好，这种跨界情况都只返回最后那点content内容。

最后写文件那里降低内存消耗，使用了下面的语句来强制文件流写入文件中，好释放内存，否则你的下载程序内存使用率是剧增的。

```python
f.flush()
os.fsync(f.fileno())

import re
def guess_url_filename(url):
    '''根据url来猜测可能的目标文件名，'''
    response = requests.get(url, stream=True)##还有一个content-type信息可以利用
    s = urlsplit(url)
    guess_element = s.path.split('/')[-1]
    guess_pattern = re.compile(r'''
    (.png|.flv)
    $           # end of string
    ''', re.VERBOSE | re.IGNORECASE)

    if re.search(guess_pattern,guess_element):
        filename = guess_element
    else:
        filename = guess_element + '.html'
    return filename

import threading
import os
class DownloadThread(threading.Thread):
    def __init__(self, url,begin,chunk_size = 1024*300):
        threading.Thread.__init__(self)
        self.url = url
        self.begin = begin
        self.chunk_size = chunk_size
        self.result = b''
    def run(self):
        headers = {'Range':'bytes={begin}-{end}'.format(begin = str(self.begin),
            end = str(self.begin + self.chunk_size-1))}

        response = requests.get(url, stream=True, headers = headers)

        if response.headers.get('content-range') is None:
            self.result = 0##表示已经越界了
        else:
            self.result = response.content
            print('start download...', self.begin/1024, 'KB')

    def getvalue(self):
        return self.result

def get_content_partly(url, index):
    threads = []
    content = b''
    chunk_size = 1024*300# 这个不能设置太大也不能设置太小
    block_size = 10*chunk_size# 具体线程数

    for i in range(10):
        t = DownloadThread(url, index * block_size + i*chunk_size )
        t.start()
        threads.append(t)

    for i,t in enumerate(threads):
        t.join()

    for t in threads:
        if  t.getvalue():
            content += t.getvalue()

    return content

import os
def get_content_tofile(url,filename = ''):
    '''简单的根据url获取content，并将其存入内容存入某个文件中。
    如果某个内容size 小于1M 1000000 byte ，则采用多线程下载法'''

    if not filename:
        filename = guess_url_filename(url)

    # NOTE the stream=True parameter
    response = requests.get(url, stream=True)
    if not response.headers.get('content-length'):
        print('this url does not have a content .')
        return 0
    elif response.headers.get('content-length') < '1000000':
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
                    f.flush()
                    os.fsync(f.fileno())
    else:
        with open(filename, 'wb') as f:
            for i in range(1000000):##very huge
                content = get_content_partly(url, i)
                if content:
                    f.write(content)
                    f.flush()
                    os.fsync(f.fileno())
                else:
                    print('end...')
                    break
```



### 线程锁

python有两种类型线程锁 `Lock` 和 `RLock` ，其都是通过 `acquire` 来获取锁和 `release` 来释放锁。当一个线程试着访问某个unlocked的锁，`acquire` 将立即返回；如果访问的是locked的锁，那么该线程将阻塞，直到一个 `release` 释放了该锁。

RLock和Lock的区别是RLock可以被相同的线程acquire多次，RLock人们也称之为递归锁，如果你的某个（递归）函数在某个线程中多次访问资源，而这时被允许的，那么你应该使用RLock。

RLock常和with语句一起使用：

```
lock = threading.RLock()
with lock:
    do something...
```



## 网络编程

下面只讨论TCP套接字编程，UDP协议暂不讨论。整个TCP套接字编程的过程如下所述:

### 套接字编程

1.  客户机负责发起连接，其将新建一个套接字对象（在python中是通过**socket**函数来创建的），就好比在一个封闭的黑箱子里开了一个门，在创建这个套接字对象的过程中，你需要指定具体要连接的那个服务器的IP地址和端口号（**connect**方法）。

2.  接下来是进行TCP的三路握手过程，具体在传输层最底层的东西，客户机应用程序还是服务器应用程序都不用操心，其应该是是操作系统程序负责的。服务器程序需要关心的是在这三路握手期间，其类似于听到了敲门声，其需要开出一个门出来。服务器程序要听到这个敲门声，其应该处于监听该端口的状态。首先服务器程序需要创建一个套接字对象，然后**bind**某个端口号，然后调用**listen**方法开始监听这个端口。

3.  然后服务器那边的监听套接字调用**accept**方法，并形成阻塞，接下来就是听到了敲门声，这个敲门声是TCP三路握手第一路信号发送过来了，这后面TCP三路握手还有两路，这我们暂时不需要太关心了。等到TCP三路握手完成了，服务器之前的那个accept方法将创建一个套接字对象。这个套接字对象称之为*连接套接字*。我们在这里把服务器那边的连接套接字调用accept方法可以理解为接受了客户机的敲门，如果一切顺利的话，其将为客户机新开一个套接字，也就是一个新门。

4.  对于客户机那边只有一个套接字，情况稍微简单点，其往套接字里面塞信息（**sendall**方法）就是发送信息过去了，然后从套接字那里读（**recv**方法），就是读信息了。而服务器那边，实际上和客户机对等的来看的话，第二个新建的连接套接字可以看作看作类似客户机那边的第一个套接字，往里面读就是读信息，往里面写就是发送信息。之所以服务器那边要新开一个套接字，我们可以猜到，是因为服务器要同时处理多个客户机请求，可以把第一个监听套接字理解为总大门，然后后面开启的连接套接字理解为小门，其才是真正和具体那个客户机的一对一管道连接。

上面的简要描述太过于抽象，我们再来看一个最简单的实际代码，其就是python官方文档socket模块的第一个例子，可能有些地方稍作改动。

下面是服务器端 `server.py` 的代码:

    import socket
    
    HOST = 'localhost'
    PORT = 50007
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    print('Connected by', addr)
    while True:
        data = conn.recv(1024)
        if not data:break
        conn.sendall(data)
    conn.close()

首先我们运行server.py，如前所述，其首先需要根据socket函数来创建一个监听套接字，这个套接字具体监听的端口由bind方法指定，然后这个监听套接字开始监听（调用listen方法）。然后调用这个监听套接字的accept方法，其如果收到TCP连接请求，其将返回一个连接套接字，这里是conn。然后程序进入主循环，在这里连接套接字用recv方法来读，然后用sendall方法来写。最后是通过close方法来关闭本连接套接字。

下面是客户机端 `client.py` 的代码:

    import socket
    
    HOST = 'localhost'
    PORT = 50007
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)
    s.close()
    print('Received', repr(data))

这里客户机那边首先新建一个套接字，这个套接字可以直接用connect方法来拨号某个服务器，然后用sendall方法来写，用recv方法来读。整个过程大抵如此。

最后以一副图画来加深对本小节的印象把。

![img]({static}/images/python/tao-jie-zi-bian-cheng.png)

下面我们将更深入讨论套接字编程，并用python的socket模块来介绍具体编码的细节问题。

### socket模块

### host主机名

host最简单就是人们熟知的IP地址，然后就是由本地hosts文件解析或者网络DNS系统解析的名字。比如
`localhost` 或者 `python.org` 等。socket模块里面有 `gethostbyname`
函数，可以获取该hostname具体对应的IP地址。

    >>> socket.gethostbyname('python.org')
    '104.130.43.121'

不过gethostbyname函数只支持IPv4地址，现在推荐使用 `getaddrinfo`
函数，其同时支持IPv4和IPv6地址。其参数设置如下:

    socket.getaddrinfo(host, port, family=0, type=0, proto=0, flags=0)

port可以填写80或者'http'这样的形式，或者设置为None。然后后面的family是地址族，type是套接字类型等，这些这里先暂时略过讨论。

这个函数的返回值是一个列表，其内元素有如下结构:

    (family, type, proto, canonname, sockaddr)

具体如下所示:

    >>> socket.getaddrinfo('www.github.com','https')
    [(<AddressFamily.AF_INET: 2>, <SocketType.SOCK_STREAM: 1>, 6, '', ('192.30.252.131', 443)),
    (<AddressFamily.AF_INET: 2>, <SocketType.SOCK_DGRAM: 2>, 17, '', ('192.30.252.131', 443)), 
    (<AddressFamily.AF_INET: 2>, <SocketType.SOCK_STREAM: 1>, 6, '', ('192.30.252.128', 443)), 
    (<AddressFamily.AF_INET: 2>, <SocketType.SOCK_DGRAM: 2>, 17, '', ('192.30.252.128', 443))]

这里的 `AF_INET`
地址族是创建socket套接字对象时的默认地址族，其就是对应的IPv4地址。然后套接字类型
`SOCK_STREAM` 也是创建套接字对象的默认值，其是字节流套接字。

getaddrinfo函数返回的 `family,type,proto`
这三个参数可以传递给socket函数用于具体创建一个套接字对象。canonname比较冷门，然后
`sockaddr` 可以传递给套接字对象的 `connect`
方法来具体进行套接字连接操作。

我们来用下面这个脚本试一下:


    import socket
    socket.setdefaulttimeout(10)


    addrinfos = socket.getaddrinfo('www.baidu.com', 'http')
    
    for addrinfo in addrinfos:
        socket_parameter = addrinfo[:3]
        print(socket_parameter)
        addr = addrinfo[-1]
        print(addr)
    
        s = socket.socket(*socket_parameter)
        try:
            s.connect(addr)
            print('connected')
            print('peername',s.getpeername())
            print('hostname',s.getsockname())
        #except socket.timeout:
            #print('socket timeout')
        except Exception as e:
            print(e)

读者还可以用其他域名来试一下。

### 地址族

AF\_INET

:   IPv4地址

AF\_INET6

:   IPv6地址

此外还有一些冷门的地址族: AF\_UNIX ， AF\_NETLINK ， AF\_TIPC

### 套接字类型

SOCK\_STREAM

:   字节流套接字

SOCK\_DGRAM

:   数据报套接字

上面这两个套接字类型是全平台适用的。此外还有一些冷门的套接字类型:
SOCK\_RAW ， SOCK\_RDM ， SOCK\_SEQPACKET

### 传输协议

传输协议 `proto` 一般设置为0。也可以明确指定某个传输协议:

IPPROTO\_CP

:   TCP传输协议

IPPROTO\_UDP

:   UDP传输协议

IPPROTO\_SCTP

:   SCTP传输协议

### timeout

    socket.settimeout(None)
    socket.settimeout(0)
    socket.settimeout(sec)

-   如果设置为None，则套接字为阻塞模式

-   如果设置为0，则套接字为非阻塞模式

-   如果设置具体某个sec秒，则套接字会等待多少sec秒，然后抛出
    `socket.timeout` 异常。

此外还有 `setdefaulttimeout`
函数可以全局设置后面所有创建的socket对象的timeout。

    socket.setdefaulttimeout(10)

阻塞模式还可以如下设置：

    socket.setblocking(True)
    socket.setblocking(False)

### listen方法

服务器端套接字具体开始监听。

    socket.listen([backlog])

从python3.5开始，backlog参数为可选参数了。这个backlog的意思是最大等待连接数（如果超过这个数，新的连接将被拒绝）。这个数以前一般设置为5，因为那个时候系统最大也才允许是5，但现在可能需要再提高一点了，现在python3.5起，这个数成为可选参数了，文档上说会自动设置一个合适的数，所以就不需要我们操心了。

更多细节请参看官方文档。

## 异步编程

常规的所谓同步(synchronous)编程就是大家平时编程一般使用的模型，顺序结构，阻塞式，多个函数逐个执行，一个执行完才能执行下一个，如下图所示:

![img]({static}/images/python/tong-bu-bian-cheng-mo-xing.png)


此外还有一种线程并发模型:

![img]({static}/images/python/xian-cheng-bing-fa-mo-xing.png)

python有所谓的GIL概念，很多人对其有指责，而实际上那些支持多线程并发的语言，怕因为这个便利而带来的是更多的困扰吧。想一想我们人脑思考问题同一时间也只能做一件事，也许python的GIL限制并不是一种限制。实际上如果要用多线程并发，人们需要建立好模型，比如最终多个分支线路互不干扰，然后结果平行放入一个列表中等等约束，然后才能放心的使用多线程并发。而在这个约束模型下，python的
**multiprocess** 模块似乎也能很好地胜任这种类型的工作。

继续讨论异步编程模型:
![img]({static}/images/python/yi-bu-bian-cheng-mo-xing.png)


*异步编程*还有一个名字叫做*非阻塞编程*，我们看到上面主程序建立事件循环之后，主事件循环过程并没有阻塞其他的程序过程，而是允许其插入其中来执行。实际上这有点类似于我们看到的GUI程序的主设计理念------事件驱动循环机制，所以异步编程还有一个名字叫做*事件驱动编程*。

下面开始通过一些例子来学习吧。

### 低效的诗歌服务器

本例子来自参考资料 [@twisted与异步编程入门] ，我将其改成了python3版本
`slowpoetry.py` 。

    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-
    
    import argparse, os, socket, time
    
    def parse_args():
        usage = """usage: %prog [options] poetry-file
    
    This is the Slow Poetry Server, blocking edition.
    Run it like this:
    
      python3 slowpoetry.py ecstasy.txt
    
    """
    
        parser = argparse.ArgumentParser(usage)
    
        help = "The port to listen on. Default to a random available port."
        parser.add_argument('-p','--port', type=int, help=help)
    
        help = "The interface to listen on. Default is localhost."
        parser.add_argument('--iface', help=help, default='localhost')
    
        help = "The number of seconds between sending bytes."
        parser.add_argument('--delay', type=float, help=help, default=.1)
    
        help = "The number of bytes to send at a time."
        parser.add_argument('--num-bytes', type=int, help=help, default=20)
    
        parser.add_argument('poetry_file')
    
        args = vars(parser.parse_args())
    
        poetry_file = args['poetry_file']
        if not poetry_file:
            parser.error('No such file: %s' % poetry_file)
    
        return args


    def send_poetry(sock, poetry_file, num_bytes, delay):
        """Send some poetry slowly down the socket."""
    
        inputf = open(poetry_file)
    
        while True:
            bytes = inputf.read(num_bytes).encode()
    
            if not bytes:
                sock.close()
                inputf.close()
                return 'end'
    
            print('Sending %d bytes' % len(bytes))
    
            try:
                sock.sendall(bytes)
            except socket.error:
                sock.close()
                inputf.close()
                return 'error'
    
            time.sleep(delay)



    def serve(listen_socket, poetry_file, num_bytes, delay):
        while True:
            sock, addr = listen_socket.accept()
    
            print('Somebody at %s wants poetry!' % (addr,))
    
            result = send_poetry(sock, poetry_file, num_bytes, delay)
    
            if result == 'end':
                print('sending complete')
            elif result == 'error':
                print('error, sending stopped')
    
    def main():
        args= parse_args()
        poetry_file = args['poetry_file']
        port = args['port']
        iface = args['iface']
        num_bytes = args['num_bytes']
        delay = args['delay']
    
        sock = socket.socket()
        sock.bind((iface, port or 0))
        sock.listen(5)
        print('Serving %s on port %s.' % (poetry_file, sock.getsockname()[1]))
    
        serve(sock, poetry_file, num_bytes, delay)
    
        sock.close()


    if __name__ == '__main__':
        main()

下面是对应的获取诗歌的client端程序 `get_poetry.py` 。

    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-
    
    import datetime, argparse, socket
    
    def parse_args():
        usage = """usage: %prog [options] [hostname]:port ...
    
    This is the Get Poetry Now! client, blocking edition.
    Run it like this:
    
      python3 get_poetry.py port1 port2 port3 ...
    
    """
    
        parser = argparse.ArgumentParser(usage)
        parser.add_argument('port',nargs='+')
    
        args = vars(parser.parse_args())
        addresses = args['port']
    
        if not addresses:
            print(parser.format_help())
            parser.exit()
    
        def parse_address(addr):
            if ':' not in addr:
                host = '127.0.0.1'
                port = addr
            else:
                host, port = addr.split(':', 1)
    
            if not port.isdigit():
                parser.error('Ports must be integers.')
    
            return host, int(port)
    
        return map(parse_address, addresses)


    def get_poetry(address):
        """Download a piece of poetry from the given address."""
    
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(address)
    
        poem = b''
    
        while True:
            data = sock.recv(1024)
    
            if not data:
                sock.close()
                break
            else:
                print(data.decode('utf-8'),end='')
    
            poem += data
    
        return poem


    def format_address(address):
        host, port = address
        return '%s:%s' % (host or '127.0.0.1', port)


    def main():
        addresses = parse_args()
        elapsed = datetime.timedelta()
    
        for i, address in enumerate(addresses):
            addr_fmt = format_address(address)
            print('Task %d: get poetry from: %s' % (i + 1, addr_fmt))
            start = datetime.datetime.now()
    
            poem = get_poetry(address)
    
            time = datetime.datetime.now() - start
            msg = 'Task %d: got %d bytes of poetry from %s in %s'
            print(msg % (i + 1, len(poem), addr_fmt, time))
    
            elapsed += time
    
        print('Got %d poems in %s' % (len(list(addresses)), elapsed))


    if __name__ == '__main__':
        main()

读者可以利用上面的两个脚本来具体测试一下效果。上面的两个脚本，客户端和服务器端都是阻塞式的。我们先开一个服务器端:

    python3 slowpoetry.py -p 10000 ecstasy.txt

然后开两个终端，同时刷如下命令，我们就能看到其中后执行的那个终端的获取文本是被阻塞了的------这是服务器阻塞了。

    python3 slowpoetry.py -p 10000 ecstasy.txt

然后我们在开一个服务器端:

    python3 slowpoetry.py -p 10001  fascination.txt

然后一个客户端运行如下:

    python3 get_poetry.py 10000 10001

然后我们看到这个客户端获取文本是一个个来的，这是客户端阻塞了。

这种一个个来，一个任务做完才能进行下一个的模式是很好理解的，但进程间的通信可以不是这样，请看下面的select风格I/O复用的讨论。

### Select风格的诗歌服务器

#### Unix五种I/O模型

首先讨论一下Unix的五种I/O模型：

1.  阻塞式I/O ，默认的就是阻塞式I/O。

2.  非阻塞式I/O，应用程序持续轮询内核看看某个操作是否准备就绪。

3.  I/O复用，通过select或poll这样的多文件描述符来管理I/O。

4.  信号驱动式I/O

5.  异步I/O

这五种I/O模型中，最直接的阻塞式I/O模型，而非阻塞I/O轮询机制太过于浪费资源，然后信号驱动I/O和异步I/O应用很少，真正用的最多就是这里的
**I/O复用模型**
。python中的twisted模块和python3.4之后新出来的**asyncio**
模块里面的事件循环都是基于 然后再建立起来的类异步I/O概念。

下面将重点结合python的selectors模块来分析这种I/O复用模型。selectors模块从python3.4开始才有，其建构在select模块之上。其有如下五种内置的Selector:

    -   SelectSelector
    -   PollSelector
    -   EpollSelector
    -   DevpollSelector
    -   KqueueSelector

不过我们实际使用就使用 `DefaultSelector`
即可，python会自动选择当前平台最好的Selector。

具体创建一个Selector对象如下所示:

    sel = selectors.DefaultSelector()

#### 监控文件读写事件

Selector对象有个register方法，如下所示：

    register(fileobj, events, data=None)

其中fileobj为某文件对象（在Linux中一切皆文件，所以套接字也可以视为一个文件。）。

这里可以监控的事件有:

-   **EVENT\_READ** 可读事件，具体可读的定义按照参考资料
    [@Unix网络编程卷1] 是这样描述的:

    1.  该套接字接受缓冲区中的数据字节数大于等于套接字接受缓冲区低水平标记的当前大小。对这样的套接字的读是不会阻塞的，其将返回一个大于0的值（也就是具体读入的字节数）。我们可以使用
        `SO_RCVLOWAT`
        套接字选项来设置该套接字低水平标记，TCP和UDP套接字的默认值是1。【这个很好理解，就是1个字节，如果接受了1个字节或者更多的字节那么就有了可读事件了。】

    2.  该连接的读半部关闭，这样的套接字的读操作将不阻塞并返回0（也就是返回EOF）。【这里就是套接字对面关闭了，那么也将是可读的，我们可以用
        'if read' 这样的判断来进行读结束的后续处理。】

    3.  该套接字是一个监听套接字且已完成连接数不为0。【这主要是指服务器端一开始创建的那个监听套接字，其一般accept不会阻塞的，
        `conn, addr = s.accept()`
        ，也就是客户端那边有敲门了，就会有一个可读事件，就会批准自动创建一个监听套接字，除非已完成连接数为0------这个已完成连接数具体含义我还不清楚。】

    4.  上面的情况中，有一个套接字错误待处理，对这样的套接字读操作将不阻塞并返回-1。【这里细节暂时还不清楚。】

-   **EVENT\_WRITE** 可写事件，具体可写的定义按照参考资料
    [@Unix网络编程卷1] 是这样描述的:

    1.  该套接字发送缓冲区中的可用空间字节数大于等于套接字发送缓冲区低水平标记的当前大小，并且该套接字已连接（或者该套接字不需要连接，比如UDP套接字）。如果我们把这样的套接字设置为非阻塞，那么写操作将返回一个正值（具体传输层接受到的字节数）。我们可以使用
        `SO_SNDLOWAT`
        套接字选项来设置该套接字的可写低水平标记，TCP和UDP套接字默认值是2048。【如果套接字是阻塞的，那么写操作应该会因为套接字另一端recv的阻塞而阻塞，这是我的一个猜测。然后这里和上面可读实际上是个反的，可读是相当于数据量超过某个标记，也就是往里面送一点点数据是不行的，还需要送到一定的量，才可读；而可写是送一点点数据都是可写的，只有送的数据量很大之后，
        *可用的* 缓冲区空间 *小于* 某个标记之后，就不可写了。】

    2.  该连接的写半部关闭。对这样的套接字进行写操作将产生SIGPIPE信息。【我试过，后续程序会出错。对于服务器主动发动数据的模式，都应该考虑这种情况和捕捉好这个可能的异常。】

    3.  非阻塞连接的套接字已连接或连接已失败。【非阻塞连接初次连接成功可写很好理解，但为什么连接失败也可写？可能这里非阻塞初次连接失败被处理为连接半部关闭的情况了，也就是上面的哪一条。】

    4.  上面的情况中，有一个套接字错误待处理，对这样的套接字写操作将不阻塞并返回-1。

更多的内容请参看 selectors 模块的官方文档。

下面的例子将之前那个诗歌服务器写成了Select风格的异步版本
`select_slowpoetry.py`:

    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-


    import argparse
    import os
    import socket
    import time
    import selectors
    
    sel = selectors.DefaultSelector()


    def parse_args():
        usage = """usage: %prog [options] poetry-file
    
      python3 select_slowpoetry.py ecstasy.txt
    
    """
    
        parser = argparse.ArgumentParser(usage)
    
        help = "The port to listen on. Default to a random available port."
        parser.add_argument('-p', '--port', type=int, help=help)
    
        help = "The interface to listen on. Default is localhost."
        parser.add_argument('--iface', help=help, default='localhost')
    
        help = "The number of seconds between sending bytes."
        parser.add_argument('--delay', type=float, help=help, default=.1)
    
        help = "The number of bytes to send at a time."
        parser.add_argument('--num-bytes', type=int, help=help, default=20)
    
        parser.add_argument('poetry_file')
    
        args = vars(parser.parse_args())
    
        poetry_file = args['poetry_file']
        if not poetry_file:
            parser.error('No such file: %s' % poetry_file)
    
        return args


    def send_poetry(sock, poetry_file, num_bytes, delay, inputf):
        """Send some poetry slowly down the socket."""
    
        bytes = inputf.read(num_bytes)
    
        if not bytes:
            sel.unregister(sock)
            sock.close()
            inputf.close()
            print('sending complete')
            return True
    
        try:
            sock.sendall(bytes)
        except socket.error:
            sel.unregister(sock)
            sock.close()
            inputf.close()
            print('some error, sending stoped')
            return False
    
        time.sleep(delay)


    def serve(listen_socket, poetry_file, num_bytes, delay):
        sock, addr = listen_socket.accept()
        print('Somebody at %s wants poetry!' % (addr,))
        sock.setblocking(False)
    
        inputf = open(poetry_file, 'rb')
        sel.register(sock, selectors.EVENT_WRITE,
                     data={'callback': send_poetry, 
                            'args': [poetry_file, num_bytes, delay, inputf]})


    def main():
        args = parse_args()
        poetry_file = args['poetry_file']
        port = args['port']
        iface = args['iface']
        num_bytes = args['num_bytes']
        delay = args['delay']
    
        sock = socket.socket()
        sock.bind((iface, port or 0))
        sock.listen(100)
        sock.setblocking(False)
        print('Serving %s on port %s.' % (poetry_file, sock.getsockname()[1]))
    
        sel.register(sock, selectors.EVENT_READ,
                     data={'callback': serve, 'args': [poetry_file, num_bytes, delay]})
    
        while True:
            events = sel.select()
            for key, mask in events:
                callback = key.data['callback']
                callback(key.fileobj, *key.data['args'])
    
        sock.close()


    if __name__ == '__main__':
        main()

客户端的编写要更加简单一点，具体代码如下所示 `select_get_poetry.py`:

    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-
    
    import datetime
    import argparse
    import socket
    
    import selectors
    sel = selectors.DefaultSelector()


    def parse_args():
        usage = """usage: %prog [options] [hostname]:port ...
    
      python3 select_get_poetry.py port1 port2 port3 ...
    
    通过select I/O复用来建立一个异步诗歌下载客户端，可以同时面向多个诗歌服务器来进行下载。
    """
    
        parser = argparse.ArgumentParser(usage)
        parser.add_argument('port', nargs='+')
    
        args = vars(parser.parse_args())
        addresses = args['port']
    
        if not addresses:
            print(parser.format_help())
            parser.exit()
    
        def parse_address(addr):
            if ':' not in addr:
                host = '127.0.0.1'
                port = addr
            else:
                host, port = addr.split(':', 1)
    
            if not port.isdigit():
                parser.error('Ports must be integers.')
    
            return host, int(port)
    
        return map(parse_address, addresses)


    def download_poetry(sock, infile):
        """Download a piece of poetry from the given address."""
    
        bstring = sock.recv(1024)
    
        if not bstring:  # end fo reading
            sel.unregister(sock)
            infile.close()
            print('end of reading')
            return True
        else:
            print('writing to {}'.format(infile.name))
            infile.write(bstring)


    def connect(address):
        """Connect to the given server and return a non-blocking socket."""
        sock = socket.socket()
        sock.connect(address)
        sock.setblocking(False)
        return sock


    def format_address(address):
        host, port = address
        return '%s:%s' % (host or '127.0.0.1', port)


    def main():
        addresses = parse_args()
        elapsed = datetime.timedelta()
        sockets = map(connect, addresses)
    
        for sock in sockets:
            filename = str(sock.getpeername()[1]) + '.txt'
            infile = open(filename, 'wb')
            sel.register(sock, selectors.EVENT_READ,
                         data={'callback': download_poetry,
                               'args': [infile]})
    
        while True:
            events = sel.select()
            for key, mask in events:
                callback = key.data['callback']
                callback(key.fileobj, *key.data['args'])


    if __name__ == '__main__':
        main()

这里主要的改动有两点:

1.
客户端同时开启几个sock，然后这些sock和可读时间绑定了download\_poetry方法，只要有数据可读了，那么就会执行该操作。
2.
具体下载行为就是对目标fileobj进行write，把接受到的字节流给写进去即可。

### Asyncio风格的诗歌服务器

通过Selectors模块，不仅现在我们的程序是高效的异步模式了，而且之前代码中那几个丑陋的
`while True`
给压缩到只有一个了，对于追求代码美观的程序员来说他们会对这一进步会感到很满意。而程序刚开始那个
`while True`
人们也有点看不习惯它了。人们慢慢的构建出\"**reactor**\"这个术语来取代这个主循环，如下图所示:

reactor

在twisted模块中实际上就有这么一个reactor变量，来对应这个主Selector事件驱动。而asyncio模块里面也有类似的eventloop概念:

    import asyncio
    eventloop = asyncio.get_event_loop()

在进行事件驱动编程之前还需要强调一点，上图这个 *事件循环*
的概念是事件驱动编程的核心概念，实际上在前面的select风格异步编程中，我们就已经看到这点影子了，那就是开启事件循环之后，剩下的工作就是挂载一些函数，这些函数里面会涉及到另外一些函数的挂载和取消挂载操作等，我们可以在脑海中想象中间一个事件循环大圈，然后四周八围挂载着各种函数各种操作，这就是事件驱动编程风格了。实际上事件驱动编程会让很多工作变得简单，其没有让事情变得复杂，关键是我们的头脑要习惯这种编程风格，脑海里还熟悉这种事件驱动模型。

#### 常规eventloop版

下面是Asyncio风格的诗歌服务器第一版，关于asyncio模块有不懂的读者请参看该模块的官方文档。

    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-
    
    import argparse
    import os
    import socket
    import time
    import asyncio


    def parse_args():
        usage = """usage: %prog [options] poetry-file
    
      python3 asyncio_slowpoetry.py ecstasy.txt
    
    """
    
        parser = argparse.ArgumentParser(usage)
    
        help = "The port to listen on. Default to a random available port."
        parser.add_argument('-p', '--port', type=int, help=help)
    
        help = "The interface to listen on. Default is localhost."
        parser.add_argument('--iface', help=help, default='localhost')
    
        help = "The number of seconds between sending bytes."
        parser.add_argument('--delay', type=float, help=help, default=.1)
    
        help = "The number of bytes to send at a time."
        parser.add_argument('--num-bytes', type=int, help=help, default=20)
    
        parser.add_argument('poetry_file')
    
        args = vars(parser.parse_args())
    
        poetry_file = args['poetry_file']
        if not poetry_file:
            parser.error('No such file: %s' % poetry_file)
    
        return args


    def send_poetry(eventloop, sock, poetry_file, num_bytes, delay, inputf):
        """Send some poetry slowly down the socket."""
    
        bytes = inputf.read(num_bytes)
    
        if not bytes:
            eventloop.remove_writer(sock)
            sock.close()
            inputf.close()
            print('sending complete')
            return True
    
        try:
            sock.sendall(bytes)
        except socket.error:
            eventloop.remove_writer(sock)
            sock.close()
            inputf.close()
            print('some error, sending stoped')
            return False
    
        time.sleep(delay)


    def serve(eventloop, listen_socket, poetry_file, num_bytes, delay):
        sock, addr = listen_socket.accept()
        print('Somebody at %s wants poetry!' % (addr,))
        sock.setblocking(False)
    
        inputf = open(poetry_file, 'rb')
        eventloop.add_writer(sock, send_poetry, eventloop, sock,
                             poetry_file, num_bytes, delay, inputf)


    def main():
        args = parse_args()
        poetry_file = args['poetry_file']
        port = args['port']
        iface = args['iface']
        num_bytes = args['num_bytes']
        delay = args['delay']
    
        sock = socket.socket()
        sock.bind((iface, port or 0))
        sock.listen(100)
        sock.setblocking(False)
        print('Serving %s on port %s.' % (poetry_file, sock.getsockname()[1]))
    
        eventloop = asyncio.get_event_loop()
        eventloop.add_reader(sock, serve, eventloop, sock,
                             poetry_file, num_bytes, delay)
    
        try:
            eventloop.run_forever()
        finally:
            eventloop.close()
    
        sock.close()


    if __name__ == '__main__':
        main()

这里也将之前的诗歌获取客户端写成asyncio版本。代码如下所示，改动不是很大。

    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-
    
    import datetime
    import argparse
    import socket
    import asyncio


    def parse_args():
        usage = """usage: %prog [options] [hostname]:port ...
    
      python3 select_get_poetry3.py port1 port2 port3 ...
    
    """
    
        parser = argparse.ArgumentParser(usage)
        parser.add_argument('port', nargs='+')
    
        args = vars(parser.parse_args())
        addresses = args['port']
    
        if not addresses:
            print(parser.format_help())
            parser.exit()
    
        def parse_address(addr):
            if ':' not in addr:
                host = '127.0.0.1'
                port = addr
            else:
                host, port = addr.split(':', 1)
    
            if not port.isdigit():
                parser.error('Ports must be integers.')
    
            return host, int(port)
    
        return map(parse_address, addresses)


    def download_poetry(eventloop, sock, infile):
        """Download a piece of poetry from the given address."""
    
        bstring = sock.recv(1024)
    
        if not bstring:  # end fo reading
            eventloop.remove_reader(sock)
            sock.close()
            infile.close()
            print('end of reading')
            return True
        else:
            print('writing to {}'.format(infile.name))
            infile.write(bstring)


    def connect(address):
        """Connect to the given server and return a non-blocking socket."""
        sock = socket.socket()
        sock.connect(address)
        sock.setblocking(False)
        return sock


    def format_address(address):
        host, port = address
        return '%s:%s' % (host or '127.0.0.1', port)


    def main():
        addresses = parse_args()
        sockets = map(connect, addresses)
        eventloop = asyncio.get_event_loop()
    
        for sock in sockets:
            filename = str(sock.getpeername()[1]) + '.txt'
            infile = open(filename, 'wb')
    
            eventloop.add_reader(sock, download_poetry, eventloop, sock, infile)
    
        try:
            eventloop.run_forever()
        finally:
            eventloop.close()


    if __name__ == '__main__':
        main()

值得一提的是这里的读完毕的判断逻辑:

        if not bstring:##end fo reading
            eventloop.remove_reader(sock)
            sock.close()
            infile.close()
            print('end of reading')
            return True

如果读半部关闭，则将返回0，所以可以如上来判断读操作是否完毕了。

#### 自定义协议版

asyncio模块还提供了很多功能可以让读者不用使用socket模块，而直接更高层的基于协议来编写网络程序。下面是
诗歌服务器第二版，本例子参考了
[这个网页](http://www.getoffmalawn.com/blog/playing-with-asyncio)
然后修改而成。

    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-
    
    import argparse
    import os
    import time
    import asyncio


    def parse_args():
        usage = """usage: %prog [options] poetry-file
    
      python3 asyncio_slowpoetry3.py ecstasy.txt
    
    """
    
        parser = argparse.ArgumentParser(usage)
    
        help = "The port to listen on. Default to a random available port."
        parser.add_argument('-p', '--port', type=int, help=help)
    
        help = "The interface to listen on. Default is localhost."
        parser.add_argument('--iface', help=help, default='127.0.0.1')
    
        help = "The number of bytes to send at a time."
        parser.add_argument('--num-bytes', type=int, help=help, default=20)
    
        parser.add_argument('poetry_file')
    
        args = vars(parser.parse_args())
    
        poetry_file = args['poetry_file']
        if not poetry_file:
            parser.error('No such file: %s' % poetry_file)
    
        return args


    class PoetryServeProtocol(asyncio.Protocol):
    
        def __init__(self, inputf, num_bytes):
            self.inputf = inputf
            self.num_bytes = num_bytes
    
        def connection_made(self, transport):
            self.transport = transport
            print(self.transport)
    
        def data_received(self, data):
            if data == b'poems':
                poem = self.inputf.read(self.num_bytes)
                if poem:
                    self.transport.write(poem)
                else:
                    self.transport.write_eof()


    def main():
        args = parse_args()
        poetry_file = args['poetry_file']
        num_bytes = args['num_bytes']
        port = args['port']
        iface = args['iface']
    
        inputf = open(poetry_file, 'rb')
    
        eventloop = asyncio.get_event_loop()
    
        print(iface, port)
        coro = eventloop.create_server(
            lambda: PoetryServeProtocol(inputf, num_bytes), iface, port)
    
        server = eventloop.run_until_complete(coro)
        print(server)
    
        try:
            eventloop.run_forever()
        finally:
            eventloop.close()


    if __name__ == '__main__':
        main()

代码变得简单得可怕了。首先我们看到这个 `create_server`
方法。通过这个方法，我们可以基于自己定义的某个协议来创建一个TCP
server（返回的是协程对象）。下面主要看到具体创建的那个协议对象。

自定义的协议继承自Protocol类，然后定义一些方法:

connection\_made

:   这个callback继承自Protocol类，逻辑是如果一个连接建好了，那么执行该函数。其接受一个参数transport。也就是具体协议的传输层。

data\_received

:   这个callback继承自Protocol类，如果某个数据传进来了，那么该函数将被执行。其接受一个参数就是传进来的data。

eof\_received

:   数据结束完毕是调用。你可以在另外一端用transport发送写入结束信号
    `write_eof()` 。

配套的获取诗歌客户端如下所示:

    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-
    
    import datetime
    import argparse
    import asyncio


    def parse_args():
        usage = """usage: %prog [options] [hostname]:port ...
    
      python3 select_get_poetry3.py port1 port2 port3 ...
    
    """
    
        parser = argparse.ArgumentParser(usage)
        parser.add_argument('port', nargs='+')
    
        args = vars(parser.parse_args())
        addresses = args['port']
    
        if not addresses:
            print(parser.format_help())
            parser.exit()
    
        def parse_address(addr):
            if ':' not in addr:
                host = '127.0.0.1'
                port = addr
            else:
                host, port = addr.split(':', 1)
    
            if not port.isdigit():
                parser.error('Ports must be integers.')
    
            return host, int(port)
    
        return map(parse_address, addresses)


    class PoetryClientProtocol(asyncio.Protocol):
    
        def __init__(self, infile):
            self.infile = infile
    
        def connection_made(self, transport):
            print(transport.get_extra_info('peername'))
            self.transport = transport
            self.transport.write(b'poems')
    
        def data_received(self, data):
            if data:
                print(data)
                print('writing to {}'.format(self.infile.name))
                self.infile.write(data)
                self.transport.write(b'poems')
    
        def eof_received(self):
            print('end of writing')
            self.infile.close()


    def main():
        addresses = parse_args()
        eventloop = asyncio.get_event_loop()
    
        for address in addresses:
            host, port = address
            filename = str(port) + '.txt'
            infile = open(filename, 'wb')
            coro = eventloop.create_connection(
                lambda: PoetryClientProtocol(infile), host, port)
            t, p = eventloop.run_until_complete(coro)
            print(t, p)
    
        try:
            eventloop.run_forever()
        finally:
            eventloop.close()


    if __name__ == '__main__':
        main()


## 核心内置

### assert语句

assert语句简单的理解就是 `assert True` ，正常刷过去，而 `assert False` 将抛出`AssertionError` 。

assert语句实际上是非常重要的一个语句，程序员在编码的时候需要形成一种防御型编码风格，注意这不是所谓的编码规范，而是重要性更高一等级的编码风格，是一种思维方式。

那么什么是防御型编码风格，简言之就是你在编码的时候，你对于你即将面对的各个数据类型的预期。比如说 `is_even` 函数是一个判断输入的整数是否是偶数的函数，那么你预期输入的数值就是一个整数，这个时候你就可以加上`assert  isinstance(x, int)` ，来防御输入的x参数类型。那么假如程序运行过程中抛出了这个地方的assert异常，这个函数实际上在说，不是我的问题，是你给我的参数出问题了，是调用我的那个方法出了问题。

防御型编码风格就是一种去耦合思维，它和你编写各个函数的去耦合思维是一致的，所以不要把防御型编码风格当成某种规范，当作某种额外的约束工作，它就是和你正在编写各种函数时候的思维方式是一致的。如果你去观察那些没有防御型编码风格的初学者，你会发现他们的函数分离工作做得很不好，经常看到大段的代码，各个参数全局变量局部变量都乱七八糟的，整个代码文件混乱不堪。而他们还会嬉笑道，不就是防御型编码吗，我知道，我学过。

assert语句和相关条件判断等抛异常语句片段都属于防御型编码风格，那么什么时候用assert语句，什么时候抛出异常呢。实际上assert语句也是在抛异常，但assert语句和抛异常语句有一个很大的不同：**那就是assert语句可以通过设置python编译器来全局跳过，这个需要注意下。所以对于那些必须要做的校验，是应该使用异常语句的。** 所以一般来说项目早期的话可以写上很多assert语句，但后面时间充裕了很多assert语句是要替换为抛异常语句的。





### locals和globals

python的 `locals()` 返回本函数内的局部变量字典值，而 `globals()` 则返回本模块文件的全局变量。 `locals` 是只读的，而 `globals()` 不是，我们可以利用`globals()` 对脚本文件玩出一些新花样。

### and or not的运算优先级

一般是推荐用括号清晰表达，然后not我们知道优先级是最高的。我们再看下面这个例子:

```
>>> True or True and False
True
```

这个例子很好地说明了and和or的优先级顺序，具体就是 and的优先级比or的要高 。

### all和any关键词

这是python语言里面的关键词函数，源码很简单，下面列出来，看一下就清楚了:

```
def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True

def any(iterable):
    for element in iterable:
        if element:
            return True
    return False
```


如果用语言表述的话是:

- all，都是True，则返回True，否则返回False
- any，只要有一个True则返回True，否则返回False。





### 三元运算符

也就是类似这样的结构:

```
loop = loop if loop is not None else get_event_loop()
```

通常我们在处理函数的入口参数实现默认值的情况的时候会用到，比如上面一般函数参数那里写着 `loop=None` ，用上面这种一行形式更简洁一些。而我们不直接在函数定义的那里采用默认值可能有两种情况，一是该默认值并不方便作为默认值，而最好默认为None；还有一种情况是默认值是需要通过某个函数等运算得到的。

### 属性管理的函数

hasattr，setattr，getattr，delattr，这些函数都属于关于python中各个对象的属性管理函数，其都是内置函数。

其中hasattr(object, name)检测某个对象有没有某个属性。其实际调用的还是getattr方法，然后稍作封装。

setattr(object, name, value)用于设置某个对象的某个属性为某个值，`setattr(x,a,3)` 对应 `x.a = 3` 这样的语法。

getattr(object, name[, default])用于取某个对象的某个属性的值，对应 `object.name` 这样的语法。

delattr(object,name)用于删除某个对象的某个属性，对应 `del object.name` 这样的语法。




### `__name__` 和 `__file__`

这里所谓脚本被引入是指用import或者from语句被另外一个脚本引入进去，而这里所谓的脚本被执行是指直接如 `python test.py` 这样的形式执行该py脚本。

这两种形式很有一些区别，下面慢慢谈论:


- `__name__` 的区别。这个大家应该很熟悉了。如果脚本是被引入的，`__name__` 的值是该引入的脚本文件名，比如引入的是 `test.py` ，那么该脚本被引入，对于这个test.py文件来说，其内的 `__name__` 的值就是 `test` ，也就是 **模块名**  ；而如果是作为脚本被执行，则该 `__name__` 是 `__main__` 。
- `__file__` 的区别。如果脚本是被执行的，假设该脚本文件是 `hello.py` ，那么在这个被执行脚本中， `__file__` 的值是 `hello.py` ，也就是 **文件名** 。如果是被引用的，那么对于那个被引入的脚本来说， `__file__` 的值是该被引入脚本相对系统来说的 **完整文件名** ，比如是 `/home/wanze/桌面/hello.py` 。



### `__missing__`方法

对于字典或者字典的子类，你可以通过定义 `__missing__` 方法来回避找不到键值而抛出的 `KeyError` ，参考了 [这个网页](http://stackoverflow.com/questions/635483/what-is-the-best-way-to-implement-nested-dictionaries-in-python) 。如下所示:

```python
class NestedDict(collections.UserDict):
    '''
Implement this data structure:
{"section":{},
}
'''
    def __init__(data=None):
        super().__init__(data)

    def __missing__(self, key):
        value = self[key] = dict()
        return value
    
    def update_in_section(self, section, d):
        self[section].update(d)
    
    def get_in_section(self, section,key):
        return self[section].get(key)
    
    def delete_in_section(self,section,key):
        del self[section][key]
    
    def set_in_section(self,section,key,value):
        self[section][key] = value
```



如果找不到该key，则该类会自动赋值一个新的 dict()并作为该key的值。你可能希望使用 `type(self)()` ，但这种风格对json的兼容性不太好，推荐还是都用dict类。



### python中类继承的顺序

我们知道python中类的搜索顺序是从左到右的，比如：

```
class D(A,B): pass
```

D的属性是先从A找，然后再从B找。但从类的继承概念上来说，如果A类和B类之间没有层次关系，那么他们顺序随便都没问题，但如果B类是更底层的Base类，那么其是应该放在最右边的。这在关于Mixin类中写法是要严格如下所示的：

```
class MyClass(Mixin2, Mixin1, BaseClass):
    pass
```

### 字符串比较大小

读者可以实验一下python中字符串之间是可以比较大小的：

```
>>> 'abc' > 'ab'
True
>>> 'fabc' > 'abc'
True
>>> '3.04' > '3'
True
```

这个特性有的时候很有用的，具体是如何比较大小的呢？按照python官方文档的描述，采用的是词典编纂顺序。具体描述信息如下：

> 序列之间比较大小是，首先两个序列各自的第一个元素开始比较，如果它们相同，则进行下一个比较，直到任何一个序列被穷尽。如果两个序列各自比较的类型都是相同的，那么整个过程将一直进行下去。如果两个序列是相等的则认为它们是相等的，如果某一个序列是另外一个序列的子序列，则那个短的序列认为比长的序列要小。具体到每一个元素的大小比较，是按照ASCII顺序对其进行比较的。


#### 中文比较大小？

读者这时会想到，既然python中字符串都默认是unicode编码（utf-8），那么中文应该也是能够比较大小的吧，事实确实如此：

```
>>> '章' > '张'
True
>>> '章' < '张'
False
>>> ord('章')
31456
>>> ord('张')
24352
```

感兴趣的读者可以打开字符映射表看一下，'张'对应的unicode编号是U+5F20，你输入0x5f20，返回的正是24352。如果你输入hex(24352)，返回的就是'0x5f20'。


#### ord和chr函数

ord函数接受 一个字符，然后返回其unicode编码，十进制的。chr函数是ord函数的反向，比如你输入24352这个十进制uniocde，就返回了对应的字符。

```
>>> chr(24352)
'张'
```

所以我们可以总结到，python3的字符串比较大小，是基于utf-8编码的。





## 字符串

### format函数

format函数或者说字符串的format方法，一般的使用还是很简单的，但是有的时候有些特殊的高级需求，下面渐渐收集之。

更多关于python中format函数使用的信息请参考 [pyformat.info](https://pyformat.info/) 。

#### 等宽数字

```
 {:0>2d} 
```

目标数字宽度为两位，左边填充0 ， `>` 表示左边填充， `0>` 表示左边填充0，此外还有 `>` 表示右边填充。

#### 花括号的问题

花括号因为是特殊字符，要显示花括号，需要如下输入两次：

```
>>> print(f'{{----}}')
{----}
```



### f-string

python3.6加入进来的特性。基本情况如下：

python新的format字符串

```
f"hello. {name}"
```

等价于

```
"hello. {name}".format(name=name)
```

一个变量还好，多个变量的时候这种f-string的写法的好处就很明显了，当时环境下你前面已经定义好的变量名是可以直接使用的，我只能用一句话来形容，太好用了，用上了你就会停不下来。




## 文件

### 读取文件推荐方式

因为文件对象本身是可迭代的，我们简单迭代文件对象就可以对文件的一行行内容进行一些操作。比如：

```
f = open('removeduplicate.py')

for line in f:
    print(line,end='')
```

这个代码就将打印这个文件，其中end="的意思是取消`\n`，因为原来的行里面已经有`\n`了。

然后代码稍作修改就可以在每一行之前加上`>>>`这个符号了。

```
f = open('removeduplicate.py')

for line in f:
    print('>>>',line,end='')
```

什么？这个输出只是在终端，没有到某个文件里面去，行，加上file参数。然后代码变成如下：

```
import sys

f = open('removeduplicate.py')
pyout=open(sys.argv[1] ,"w")

for line in f:
    print('>>>',line,end='',file=pyout)

pyout.close()
f.close()
```

python的列表解析（迭代）效率是很高的，我们应该多用列表解析模式。

文件对象有一个readlines方法，能够一次性把整个文件的所有行字符串装入到一个列表中。然后我们再对这个列表进行解析操作就可以直接对整个文件的内容做出一些修改了。不过不推荐使用readlines方法了，这样将整个文件装入内存的方法具有内存爆炸风险，而迭代版本更好一点。

## python源码学习

### 基本结构

- `Doc` 文档
- `Grammar` 计算机可理解的语言定义
- `Include` C的头文件
- `Lib` 用python写的python内置模块部分
- `Mac` macOs支持
- `Misc` 杂项
- `Modules` 用C写的python内置模块部分
- `Objects` 核心对象和类
- `Parser`  python解析器
- `PC` 对windows系统旧版本的编译支持
- `PCBuild` 对windows系统的编译支持
- `Programs` python命令行程序
- `Python` CPython解释器
- `Tools` 单独的一些有用的工具
- `m4` 定制脚本用于自动配置makefile

### 一个简单的C语言扩展

如上面所示，CPython首先是一个C语言实现的解释器，其次是由C语言写的核心对象和类，再就是用C写的内置模块，最后就是用python写的内置模块。python写的模块源码是直接可以拿来阅读的，而C语言写的内置模块这就是本小节要展示。下面将通过C语言来编写一个最简单的python模块。

`ctest.c` 文件内容如下：

```c
#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>

static PyObject *
ctest_hello(PyObject *self, PyObject *args) {
    char *str;

    /* Parse arguments */
    if(!PyArg_ParseTuple(args, "s", &str)) {
        return NULL;
    }

    printf("hello %s\n", str);

    return Py_None;
}

static PyMethodDef CtestMethods[] = {
    {"hello", ctest_hello, METH_VARARGS, "a simple say hello function."},
    {NULL, NULL, 0, NULL}
};


static struct PyModuleDef ctestmodule = {
    PyModuleDef_HEAD_INIT,
    "ctest",
    "a simple python module writing in c",
    -1,
    CtestMethods
};

PyMODINIT_FUNC PyInit_ctest(void) {
    return PyModule_Create(&ctestmodule);
}
```

setup.py 是用来编译该模块的：

```python
from distutils.core import setup, Extension


def main():
    setup(
        ext_modules=[
            Extension("my_python_module.ctest", ["src/ctest/ctest.c"])]
    )


if __name__ == "__main__":
    main()
```

读者可能注意到了，该模块是作为my_python_module的子模块引入进来的。然后正常打包安装：

```
python -m build
pip install dist\***.whl
```

```
>>> import my_python_module.ctest
>>> my_python_module.ctest.hello("world")
hello world
```

因为这里不是C语言教程，所以这里不会就C语言作过多讨论，而上面的ctest.c先请读者简单看一下，熟悉一下，后面我们再慢慢学习熟悉这其中的细节。



### 基础知识

python解释器的工作不是将你输入的python代码编译为机器码，而是一种中间语言：`bytecode` 。`.pyc`文件下存储的就是这样的字节码。

python语言规范使用的是EBNF（Extended-BNF）规范。

- `*` 重复
- `+` 至少重复一次
- `[]` 可选部分
- `|` 可供选择的部分
- `()` grouping



## pypi生态圈

似乎讨论pypi生态圈超出了python语言的讨论范畴，但不讨论pypi的python语言教程是不完整的，因为pypi生态圈的丰富和强大正是python语言的一个很大的优势。

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

没有`setup.py` 的项目安装 `build` 模块，然后运行 `python -m build` 。

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



## 附录

### python虚拟环境

Virtualenv模块的主要作用就是建立一个封闭独立的python开发环境，因为一个python项目的开发通常会涉及到多个模块，而你激活virtualenv环境之后，通过pip命令安装的模块是安装在本项目文件夹内的，这样就建立了单独的固定某个模块版本的开发环境。

一般来说绝大部分项目都推荐开始之前就建立专属于自己的虚拟环境，除非是那种临时的测试项目。而一个项目运行时间越长，维护时间越长，虚拟环境所带来的好处就越大。


安装虚拟环境：

```text
python -m venv venv_folder_name
```

#### 激活虚拟环境

一般简单使用直接调用 `Script` 文件夹下的python解释器即可，但如果有多行命令，或者你后面使用了本python模块的可执行程序等，那么推荐还是激活下虚拟环境再进行后面的动作。

linux下：

```text
source venv/bin/activate
```

windows下有 `activate.bat` ：

```
call .\venv\Scripts\activate.bat
```





### 其他小技巧

#### 获取本模块对象

如下所示，可以获取本模块内的变量。

```python
import sys
current_module = sys.modules[__name__]

old_module_dict = copy(current_module.__dict__)


# for k, v in old_module_dict.items():
#     if k == 'case_base':
#         pass
#     elif k.startswith('case_'):
#         if issubclass(v, case_base):
#             URL_CASES.append(v)
```

#### 根据字符串获取模块对象

```
import importlib
importlib.import_module('what.what')
```



#### 检查某个变量是不是模块对象

参考了 [这个网页](https://stackoverflow.com/questions/865503/how-to-isinstancex-module)

```python
>>> import os, types
>>> isinstance(os, types.ModuleType)
True
```




#### 获取一个月最后的一天

首先要说的是利用python的datetime和timedelta对于 `days` 的加减操作是能够很好地支持跨月问题的:

```
    >>> from datetime import datetime
    >>> d = datetime.now()
    >>> d
    datetime.datetime(2016, 5, 29, 8, 50, 20, 337204)
    >>> from datetime import timedelta
    >>> d - timedelta(days = 29)
    datetime.datetime(2016, 4, 30, 8, 50, 20, 337204)
    >>> d - timedelta(days = 28)
    datetime.datetime(2016, 5, 1, 8, 50, 20, 337204)
```


但是有的时候你就是需要直接获知某个月份的最后一天是30还是31等等，然后利用replace来获得一个月的最后一天。这个时候你需要利用 calendar 的 `monthrange` 函数。参考了 [这个网页](http://stackoverflow.com/questions/42950/get-last-day-of-the-month-in-python) 。

```
    >>> d.replace(year = 2016,month=4,day = monthrange(2016,4)[-1])
    datetime.datetime(2016, 4, 30, 8, 50, 20, 337204)
```





### python编码规范

PEP8代码风格规范是每个python程序员都应该了解的内容，其具体内容官方文档在 [这里](https://www.python.org/dev/peps/pep-0008/) 。

关于空白和其他一些格式现在的编辑器加上插件都可以做到自动pep8格式调整，比如 autopep8 模块等，这一块就不多说了。

这里主要简单地说一下变量名的命名规范 【高质量python代码】：


- 字母都大写的变量，我们一般认为它是模块文件级别的常量，各单词用下划线隔开。

- 首字母大写的我们一般认为它是类或者异常名字，多个单词的用驼峰写法表示。

- 其他一律是小写字母，用下划线隔开。
- 一般开发者不应该命名下划线开头的变量，你若这样写你必须知道自己在干什么。




#### 其他编码风格推荐

- 不要使用带两个以上for语句的列表解析。
- 用生成器表达式改写数据量较大的列表解析。
```
it = (len(x) for x in open('/tmp/myfile.txt'))
```


- 不要在for和while循环后面写上else语句。这个建议有利于程序的简洁直观，可以接受。

- 函数的返回值是你需要的返回值才有意义，如果不是，而只是某些特殊的情况，那么最好抛出异常。



#### python哲学

参考了 [这个网页的翻译](https://github.com/oldratlee/translations/tree/master/python-philosophy) 。

<ol>
<li>美优于丑。</li>
<li>直白优于隐晦。</li>
<li>简单优于复杂。 </li>
<li>复杂优于纠结。 </li>
<li>扁平优于嵌套。 </li>
<li>稀疏优于稠密。 </li>
<li>可读性是有重要价值的。</li>
<li>特例可以有，但不能特例到打破规则。
<ul>
<li>尽管在纯粹性和实用性之间倾向的是实用性。</li>
</ul>
</li>
<li>出错决不能无声无息地忽略。
<ul>
<li>除非明确地说明了是无声无息的。</li>
</ul>
</li>
<li>面对二义性情况时，要拒绝任何猜的诱惑。</li>
<li>一件事应该一种做法 —— 并且宁愿只有一种做法 —— 一种显而易见的做法。
<ul>
<li>尽管在刚开始的时候这个做法可能不是那么显而易见，毕竟你不是荷兰人。 </li>
</ul>
</li>
<li>『现在』优于『决不』。 
<ul>
<li>尽管『决不』常常优于『<strong><em>马上</em></strong>』。 </li>
</ul>
</li>
<li>如果一个实现难于解释清楚，那它是个差的想法。</li>
<li>如果一个实现很容易解释清楚，那它可能是个好的想法。</li>
<li>命名空间是个拍案叫绝的想法 — 放手多多用起来吧！</li>
</ol>



### 参考资料

- python入门教程，python官网上的tutorial。原作者：Guido van Rossum  Fred L. Drake ；中文翻译：刘鑫等；版本：2013-10-28；pdf下载链接：[python入门教程](https://drive.google.com/open?id=0ByWxOeitx54PSW40bU5zNVhuMlU&authuser=0)  。
- learning python，主要python语言参考，我主要参看了python学习手册（第四版）。原作者：Mark Lutz，中文翻译：李军，刘红伟等。
- programming python，作者Mark Lutz对python编程的进阶讨论；版本：第四版。
- python [官网上的资料](https://docs.python.org/3/) 。
- dive into python3 [english version](http://www.diveintopython3.net/index.html) , 这是[中文版](http://sebug.net/paper/books/dive-into-python3/index.html) 。
- A Guide to Python's Magic Methods，作者：Rafe Kettler ,版本：2014-01-04，[Github 地址](https://github.com/RafeKettler/magicmethods) .
- Foundations of Python Network Programming ，python网络编程基础，[美] John Goerzen 著，莫迟等译 。这是 [中文在线阅读网页](http://likebeta.gitbooks.io/twisted-intro-cn/content/zh/index.html) ，这是 [english version](http://krondo.com/?page_id=1327) 。
- Unix网络编程卷1: 套接字联网API , Author: W. R. Stevens , Bill Fenner 等著 , version: 第三版 
- 计算机网络自顶向下方法 , Author: James F. Kurose , Keith W. Ross ,陈鸣译 。这本书作为入门了解有关计算机网络相关知识还是很不错的。
- 流畅的python, Luciano Ramalho著, 安道 吴珂译
- 深入理解python特性, 达恩·巴德尔著
- CPython Internals, REALPYTHON.com




## 脚注


[^1]: 也就是用chmod加上可执行权限那么可以直接执行了。第一行完整的解释是什么通过*env*程序来搜索python的路径，这样代码更具可移植性。这个问题还可以多说一点，后面会谈到virtualenv这个模块，类似上面这种引用python的写法是可以确保调用的是python虚拟环境下的python解释器。
[^2]: is语句用来测试对象的同一性，就是真正是内存里的同一个东西，而不仅仅是值相同而已。==只是确保值相同。
[^3]: 这些int、float等命令都是强制类型转换命令
[^4]: [参考网站](http://www.cnpythoner.com/post/266.html)

