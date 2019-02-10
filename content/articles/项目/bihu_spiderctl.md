Title: bihu_spiderctl项目
Slug: bihu-spiderctl
Date: 2018-07-27
Modified: 2018-08-08
Tags: python,

[TOC]

## 简介

本项目源于 https://github.com/DormyMo/SpiderKeeper 项目[MIT LICENSE]，进行了django化，这样方便数据库和以后的其他django项目数据库合并在一起，然后对界面进行了部分调整和简化。



项目地址在 [https://github.com/a358003542/bihu_spiderctl](https://github.com/a358003542/bihu_spiderctl) 。




## 使用帮助

运行命令，进行project初始化：

```
python manage.py init_data
```
用于初始化项目默认项目 default ，本项目简化去除了deploy和project等等概念，实际上一般使用并不需要考虑这些概念，分布式爬虫也不一定要用deploy那个命令行工具，实际上完全可以和运维工具git仓库控制结合起来，实现多台机器自动化代码更新。分布式也不是那么神秘，各个机器scrapyd服务开起来就可以了，具体命令让那里分发完全可以更高层的调度系统来控制。

这种处理和目前流行的 应用 单进程 ，然后 多进程由专门的工具如nginx 来实现有异曲同工的意图，那就是具体某个小的功能应用，不用太考虑系统架构上的事情，越小巧，越专注于本职工作就好。这样将大大降低单应用开发人员的思维复杂度，Again，让我们再重温一下Unix编程艺术里面的金句：

> KEEP IT STUPID AND SIMPLE.

## 周期性爬虫参数说明

* 所有
*/n  每n

星期几  0-6 0表示周日

几号 1-31
几月 1-12

每周一 0 0 * * 1



## 版权声明

本项目同样遵循 MIT 协议。





