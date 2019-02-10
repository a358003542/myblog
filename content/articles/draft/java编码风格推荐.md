Title: java语言之-编码风格推荐
Slug: java-style-guide
Date: 2018-07-30
Modified: 2018-08-03
Tags: java,
Status: draft
[TOC]

## maven项目管理

maven项目管理的知识就不在这里赘述了，具体请参看maven项目管理一文。



## 命名规范

编程第一件头等大事就取名字，命名规范，java这边的推荐风格如下：

- package 接口参考maven项目管理部分，命名规范是全是小写字母。
- class 类名 首先首字母要大写，其次是驼峰写法，只有某些极常见的缩写如URL等之类的可以直接写上。
- interface 接口 命名规范和class相同
- method 方法的名字首字母要小写，其后是驼峰写法
- variables 首字母要小写，后面驼峰写法，变量名不应以下划线或美元符号开头 临时变量 i j k m 一般是整型；c d e一般是字符型
- 实例变量 和上面的变量名命名规范一致，除了以下划线开头
- 常量 全部大写，单词间用下划线分开。









## 参考资料

1. [java-code-conventions项目](https://github.com/waylau/java-code-conventions)



