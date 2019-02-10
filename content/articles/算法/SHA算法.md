Title: SHA算法
Slug: SHA-algorithm
Date: 2018-08-22
Modified: 2018-08-22
Status: draft

[TOC]



SHA算法可用于比较文件是否相同

可用于检查密码是否相同（数据库中不会明文存放密码的）

SHA-0 SHA-1 算法已经暴露出一些缺陷，推荐使用SHA-2 SHA-3，目前最安全的密码散列函数是bcrypt。



Simhash算法是局部敏感的hash算法，可用于判断

- 网页是否已经采集
- 论文是不是网上抄的
- 版权检测，侵权判断

Simhash算法你对字符串的局部修改，生成的散列值也只是局部修改，这样可以产生一个相似度的概念。