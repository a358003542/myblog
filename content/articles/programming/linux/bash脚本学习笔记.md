Category: linux
Slug: bash-learning-notes
Tags: bash,
Date: 2019

[TOC]

##  前言

下面简单讲一下 bash shell 脚本知识，点到为止。就基本的了解在日常linux作业中还是很有用的。但作为一个蹩脚的编程语言【抱歉这么说】并不推荐大量编写bash脚本代码，如果有这块大量的需求，应该使用其他工具。


## 变量

```
i=2

echo $i
```

一般赋值就如上所示，和其他编程语言变量赋值大体类似吧，<u>但是要特别注意变量和值之间的等号是相连的，不能用空格隔开</u> 。变量的符号一般就是字母数字，可以加下划线。这样声明的变量为局部变量，也就是本shell中适用。如果要创建全局变量需要使用export命令。

一般使用这个变量就是在前面加上 `$` 符号，如果你需要用变量的字符和其他字符组合成一个新的字符，那么需要用花括号将变量名包围起来。即这样的形式 `${i}what` 。一般来说使用变量都推荐使用 `${}` 这样的形式。



### 应用：修改终端前缀

```
export PS1="=>"
```

利用export命令就可以将这个变量变为全局变量（这里所谓的全局变量主要指子shell继承了父shell的变量。），这样所有的shell脚本都可以通用。

如果你将以上代码放入你家目录的 `.bashrc` 文件里面，每次终端启动都会自动加载这个文件的。这样你后面开启的那些终端前缀都会变成`=>` 这样的形式。

这样可以节省点屏幕空间。你可以用pwd命令查看一下，其他一切都没有影响的。

这个PS1就对应的终端的一级前缀符号，PS2对应的是进一步输入时候的提示符号。你可以换成这样的形式：

```
export PS2=">"
```



## echo命令

echo命令前面接触很多了，这里不赘述了。echo命令就是用于查看某个变量的值或者直接输出一行字符串。

## unset命令

取消bash某个变量的赋值。

## read命令

请求用户输入某个变量的值

```
read name ; echo '你输入的是：'${name}
```




## bash里面的特殊符号

上面的分号bash和其他编程语言都大体类似，就是表示一行的结束。但bash还有很多其他的特殊符号，下面讲一下，这些特殊符号有的时候看到了搜索都不太好搜索。 更多信息请参阅 [这个网页](http://stackoverflow.com/questions/5163144/what-are-the-special-dollar-sign-shell-variable) 。



-   `$0` 本命令名字，在shell脚本里面那么就成了本脚本的名字。

-   `$1 $2 ...` 命令接受的参数
-   `$@` 所有参数： `{$1, $2, $3 ...}` ，其是一个array。
-   `$?` 上一个命令返回的状态，一般0表示成功。
-   `$!` 上一个命令运行的进程号
-   `&&` 比如 `cmd1 && cmd2` 意思是前一个命令执行成功了再执行第二个命令
-   `&` 如果某个命令以 `&` 结尾，那么该命令将是异步的，进入后台执行。（PS：虽然这样，但如果你是通过远程连接服务器来创建的命令，远程关闭该后台进程也将自动关闭。这需要使用nohup或者screen。）



## if条件判断

if条件语句格式是：
```bash
if  [ test expression ]
then    do what
fi
```


对于短小的shell命令行，可以写成这样的一行格式，其中分号表示换行。

```bash
if [ test expression ]; then do what ; fi
```

还值得提醒一下的是：条件判断语句（就是上面的test expression）要和那个方括号[]有一个空格表示分开，（上古神器都有一些怪僻，淡定就好）。



### 应用：确认某个文件夹是不是存在

```bash
if [  !  -d  workspace  ];  then mkdir workspace   ; fi
```

`-d` 表示检测某个文件夹是不是存在，`!` 符号在这里进行逻辑否操作。也就是这里如果workspace不存在，那么新建workspace文件夹。

## for循环

本小节参考了 [bash for loop](http://www.cyberciti.biz/faq/bash-for-loop/) 这篇文章，其关于bash编程的循环部分讲的很详细。

for循环语句格式如下：

```bash
for  var in 1 2 3
    do cmd1
         cmd2
done
```

同样，你也可以将其写成一行的样子：
```bash
for var in 1 2 3 ; do cmd1 ; cmd2 ; done
```
​    

其中加分号的地方为多行格式下必须换行的地方。

### 应用：小数点递加输出流

```bash
for animate in $(seq 4.0 0.1 8.0); do  echo ${animate} ; done
```

关于seq命令我简单说下，请通过 `--help` 来查阅具体信息：
```
用法：seq [选项]... 尾数
    或：seq [选项]... 首数 尾数
    或：seq [选项]... 首数 增量 尾数
```



### 应用：批量创建文件

在文件夹里面输入如下命令：

```bash
for (( i=1; i<=10; i++ )); do  touch file$i.txt; done
```


### 应用：批量缩小图片大小

这是一个多行脚本，用于批量缩小图片的大小。

```bash
if [  !  -d  smallsize  ];  then mkdir smallsize   ; fi
    cd smallsize

    let i=1
        for it in $(ls *.png)
            do convert -resize 50%x50% $it  $i-$it
                let i=i+1
                echo $it is smallsized
            done
```

### 应用：批量重命名文件

```bash
let i=1 && for f in $(ls *.jpg); do  mv -vi ${f} 0000${i}.jpg && let i=i+1; done
```

## 调用子命令返回值

在前面几个例子中，已经出现多次这个形式了： `$(cmd)` ，其将执行子shell命令，并将返回结果作为字符串值。



## array

shell编程最好不要过多涉及复杂的编程的内容，那将是很痛苦的，但是在某些情况下你可能需要了解array这个概念。下面来演示这样一个例子，其需求就是在一个自动备份程序之上再加上自动删除逻辑。


```bash
DATE=$(date +%F)
DAYS=30

## here is the autodump code, and the output filename is whatdump_${DATE}
### the allowed list
ALLOWED[0]=whatdump_${DATE}

for (( i=1; i&lt;=${DAYS}; i++ ))
    do  ALLOWED[i]=whatdump_$(date -d "now -${i}days" +"%F")
    done

### use the python script , it is really hard to write it on bash
python ~/thepython/scripts/whatdump_autoremove.py ${ALLOWED[@]}
```


这个程序整个逻辑就是创建一个名字叫做 `whatdump_DATE` 的备份文件（你可以通过crontab来控制好每天运行一次），然后我们希望目标文件只保留最近三十天的文件。因为这个逻辑较为复杂，本来我是打算直接将 `DATE` 参数传递给python脚本来做接下来的工作的，但是在了解到date命令强大的人类友好的日期时间表达功能（请参考 [这个问题](http://unix.stackexchange.com/questions/24626/quickly-calculate-date-differences)），我决定将整个允许存在的文件名都传递进python脚本中去。

有兴趣的可以了解下date命令-d选项的灵活表达支持，比如 `date -d "now -3days"` 就是现在之前三天的日期时间，而 `date -d "+3weeks"` 就是现在三周之后的日期时间。用兴趣的可以继续了解下，这个date命令的-d选项真的好强大。


好了下面详细讲一下这里array涉及到的语法。

### 赋值和引用

```bash
=>array[0]="hello"
=>array[1]="world!"
=>echo ${array[0]} ${array[1]}
hello world!
```

这种表达和我们常见的那种数组概念相近，记得索引从0开始这个惯例即可。或者如下一起赋值:
```bash
=>array2=("hello" "python")
=>echo ${array2[@]}
hello python
```


上面的 `${arrayname[@]}` 这种表达方式就是引用所有的array，然后还有 `${#arrayname[@]}` 这种表达是返回这个array的长度。
```
=>echo ${#array2[@]}
2
```


然后最后这句:
```
python ~/thepython/scripts/whatdump_autoremove.py ${ALLOWED[@]}
```

就是将收集到的所有允许的文件名array传递进python脚本中去了。在python脚本中一个粗糙的做法就是如下这样引用
```
def main(args,path=""):
    print args

main(sys.argv[1:])
```

这样所有的这些array就传递进args里面去了，读者有兴趣可以试一下，这个args在python中就是一个列表对象了。到python里面了更复杂的逻辑我们都可以很快写出来了，我就不说了。

大概类似下面所示，注意这里的pathlib在python3.4之后才会有，之前需要用pip安装之。

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import sys
from datetime import datetime
import os
from pathlib import Path
import shutil


def main(args,path=""):
    allowed = args
    p = Path(path)
    pfolds = [p for p in p.iterdir() if p.is_dir()]
    print(pfolds)
    for p in pfolds:
        if p.name in allowed:
            print(p.name,"passed")
        else:
            print(p.name,"removed")
            ### really do the remove thing
            shutil.rmtree(p.name)

if __name__ == '__main__':
    ### 切换到autodump目录
    os.chdir(os.path.expanduser("~/autodump"))
    
    main(sys.argv[1:])
```



## date命令

之所以把date命令放在一章是因为date命令如果单独作为一个命令来使用，打印显示日期其实意义不是很大。但是在bash脚本中，在管道中，date命令却变得非常有用了。读者可以用 `--help` 查看一下帮助信息，这个命令比我们预想的还要复杂的多，而且这里的那些输出格式参数控制语法，就是到了其他编程语言中也是有用的（比如python的time模块中的strftime函数）。

### date返回日期字符

date命令返回某个特定格式的日期在某些shell脚本中很有用，如下所示就是一个简单的例子：

```
date=$(date +"%F_%R");echo $date
```


date命令前面已谈到一点，更多信息请参看 [这篇文章](http://www.cyberciti.biz/faq/linux-unix-formatting-dates-for-display/)  。这里就不赘述了。



## xargs多行转一行

```
sudo rmdir --ignore-fail-on-non-empty  $(ls -U | head -n 10000 | xargs)
```

这是一个批量删除空文件夹的命令，假设现在空文件夹数目很多。首先 `ls -U` 单纯列出来，然后管道导向 `head` 只打印最开始的几行，然后管道导向 `xargs` 命令，这样多行转成一行，就可以作为 rmdir 的参数了。