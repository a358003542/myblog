Title: clisp语言学习和AI模式研究
Slug: clisp-learning-AI-study
Date: 2019-12-29
Modified: 2019-12-29
Tags: clisp,

[TOC]

## 前言

这里先说个题外话，目前的所谓深度学习神经网络，其实只是原AI学派研究的一个小分支，只是目前取得了一点小成就，人们就将其等同于AI了，这是很门外汉的偏见；同样类似的因为统计自然语言分析学派目前取得了一点成就，但将自然语言处理等同于统计自然语言处理，那就大错特错了。现在在我看来离AI学研究大成胜利阶段还是很是遥远的，谈任何一种方法任何一个学派的彻底失败还为时过早。

lisp语言以前属于人工智能研究领域的热门语言，这不是偶然，最关键的一点是lisp能够基于符号进行运算。也正是lisp能够基于符号进行运算的独特特性，让lisp非常适合早期AI学派研究中的逻辑分析学派和自然语言处理研究中的规则学派，而这正是目前深度玄学学习需要加强补充的部分。

后面COMMON-LISP没有特殊情况都简称为clisp了。

## CLISP开发环境搭建

推荐使用 **protacle** ，其他emacs的操作和进一步配置请参看 [emacs学习笔记]({filename}./emacs学习笔记.md) 一文。

### 利用quicklisp安装cl-project

在slime-repl里面输入：

```lisp
(ql:quickload :quickproject)
(quickproject:make-project "wanze_clisp_project")
```

这就是一个快速创建lisp项目的模板项目，参考一下即可。

quicklisp 大概有这些操作：

```lisp
(ql:quickload "vecto") 
(ql:uninstall system-name)
```

### 加载自己编写的项目

新建的项目移动到 protacle 安装目录的 projects那个文件夹下，然后就可以调用：

```lisp
(ql:quickload "wanze_clisp_project") 
```

但是这样加载之后还什么东西都没有，package.lisp 下如要加上如下内容：

```lisp
;;;; package.lisp

(defpackage #:wanze_clisp_project
  (:use #:cl)
  (:export #:hello
  ))
  
(in-package wanze_clisp_project)
```

然后把那个hello函数加到 `wanze_clisp_project.lisp` 文件里面去。

```lisp
(defun hello () (print "hello"))
```

现在在slime repr 哪里你可以这样做了：

```text
CL-USER> (ql:quickload :wanze_clisp_project)
To load "wanze_clisp_project":
  Load 1 ASDF system:
    wanze_clisp_project
; Loading "wanze_clisp_project"

(:WANZE_CLISP_PROJECT)
CL-USER> (wanze_clisp_project:hello)

"hello" 
"hello"
CL-USER> 
```

这是一种做法，此外你还可以在emacs打开文件，一边编写函数一边在slime repr哪里测试。

具体就是首先在slime repr哪里加载目标项目，然后运行：

```
(in-package wanze_clisp_project)
```

现在你可以在slime repr哪里直接运行：

```
(hello)
```

然后你打开主lisp文件编写函数，然后光标放在那个函数哪里，然后执行 `Ctrl+c Ctrl+c` ，重新编译该函数。

然后再到slime repr 哪里运行 

```
(hello)
```

你会发现函数新的修改立马生效了。



## WHY LISP

下面通过一个例子来说明为什么是lisp。第二章有这样一个简单的例子，是一个简单的根据指定规则生成对话的例子：

```lisp
(defun sentence ()    (append (noun-phrase) (verb-phrase)))
(defun noun-phrase () (append (Article) (Noun)))
(defun verb-phrase () (append (Verb) (noun-phrase)))
(defun Article ()     (one-of '(the a)))
(defun Noun ()        (one-of '(man ball woman table)))
(defun Verb ()        (one-of '(hit took saw liked)))

;;; ==============================

(defun one-of (set)
  "Pick one element of set, and make a list of it."
  (list (random-elt set)))

(defun random-elt (choices)
  "Choose an element from a list at random."
  (elt choices (random (length choices))))
```

如果用python来实现的话是没有问题的：

```python
import random


def article():
    return random.choice(['the', 'a'])


def noun():
    return random.choice(['man', 'ball', 'woman', 'table'])


def verb():
    return random.choice(['hit', 'took', 'saw', 'liked'])


def noun_phrase():
    return [article(), noun()]


def verb_phrase():
    return [verb(), noun_phrase()]


def sentence():
    return [noun_phrase(), verb_phrase()]


def flatten(inlst):
    """
    将 **多层** 列表或元组变成一维 **列表**

    >>> flatten((1,2,(3,4),((5,6))))
    [1, 2, 3, 4, 5, 6]
    >>> flatten([[1,2,3],[[4,5],[6]]])
    [1, 2, 3, 4, 5, 6]
    """
    lst = []
    for x in inlst:
        if not isinstance(x, (list, tuple)):
            lst.append(x)
        else:
            lst += flatten(x)
    return lst


if __name__ == '__main__':
    print(flatten(sentence()))

```

这种直接实现对于任何一门语言去实现实际上区别都不大，但是lisp提供了第二种解决方法，是直接根据规则编写程序，而且那些语言规则到程序那边基本上没做很大的修改，把lisp作为符号运算的优点展露无疑了。

```lisp

(defparameter *simple-grammar*
  '((sentence -> (noun-phrase verb-phrase))
    (noun-phrase -> (Article Noun))
    (verb-phrase -> (Verb noun-phrase))
    (Article -> the a)
    (Noun -> man ball woman table)
    (Verb -> hit took saw liked))
  "A grammar for a trivial subset of English.")

(defvar *grammar* *simple-grammar*
  "The grammar used by generate.  Initially, this is
  *simple-grammar*, but we can switch to other grammars.")

;;; ==============================
(defun mappend (fn list)
  "Append the results of calling fn on each element of list.
  Like mapcon, but uses append instead of nconc."
  (apply #'append (mapcar fn list)))

(defun rule-lhs (rule)
  "The left hand side of a rule."
  (first rule))

(defun rule-rhs (rule)
  "The right hand side of a rule."
  (rest (rest rule)))

(defun rewrites (category)
  "Return a list of the possible rewrites for this category."
  (rule-rhs (assoc category *grammar*)))

;;; ==============================

(defun generate (phrase)
  "Generate a random sentence or phrase"
  (cond ((listp phrase)
         (mappend #'generate phrase))
        ((rewrites phrase)
         (generate (random-elt (rewrites phrase))))
        (t (list phrase))))
```

老实说看到 `*simple-grammar*`  给我的感觉还是很震撼的，这基本上就是语法规则的直白描述。后面文章进一步将语法规则复杂化之后，我觉得用python语言实现可能要花很大一番心思了，但是lisp却是应付自如的。

### 上面例子LISP知识补充

