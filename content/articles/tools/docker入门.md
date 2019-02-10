Title: docker入门
Slug: docker
Date: 2018-06-14
Tags: docker,


[TOC]



## 前言

关于docker是什么请参看 [这个网页](https://docker_practice.gitee.io/introduction/what.html) ，说docker将改变软件生态确实是不为过的。老实说在接触docker之后感觉之前学到的很多东西，比如linux系统相关的一些，ansible等等部署工具相关的一些，virtualbox和 vagrant相关的一些，都在慢慢过时和淘汰了。当然那些工具还是很有用的，说他们被淘汰了是有点过了，更确切来说，对于一般玩家来说，可以节省更多的精力和时间，而不需要折腾那些工具那些配置学习折腾个老半天了。

> That‘s why we love docker.

但实际上docker带来的变化远远不止于只是一个可以节省开发者做某些事情的时间的一个不错的工具那么简单，其伴随着SPPS，软件即服务，更确切来说整个互联网的大背景下，应运而生的。与之相应的，开发者们顺应这个时代，在编码，软件应用的很多方面，都需要做出改变。请读者进一步阅读 https://12factor.net/zh_cn/ 里面的讨论。



实际上之前我折腾vagrant的时候，就很是认同这个理念： 那就是开发，测试，生产一致的环境，彻底解决，在这里可以运行，在这里就不行了的问题。而vagrant的控制virtualbox创建虚拟机的方式，在我看来显得略微笨拙了点，配置的繁琐，似乎并没有很好地解决这个问题；而docker除了很好地解决了上述问题之外，他的虚拟化方案更轻量级，更接近原生。



docker包括三个核心概念： 镜像image，容器container，仓库

- image 镜像 一个特殊的文件系统，和一般操作系统相比做了很多精简。
- container 容器，可以看做镜像生成的一个实例



## 安装

windows下安装如果你的操作系统不是专业版或者企业版，那么只能用 [docker tool box](https://docs.docker.com/toolbox/toolbox_install_windows/) 来安装。然后记得把 window10 的开发者模式打开。

如果你的windows10事企业版或者专业版，我没试过，我想按照官网哪个，直接就能安装成功吧。

kitematic 是docker 镜像的管理工具，推荐使用，这个工具的介绍就不做过多说明了，下面主要也是就一些命令行用法做一些说明。



### centos安装

```
yum install -y yum-utils
yum install -y device-mapper-persistent-data
yum install -y lvm2
yum-config-manager  --add-repo  https://download.docker.com/linux/centos/docker-ce.repo
yum install docker-ce
```



## 镜像

### 从网上拉取镜像

```
docker pull 
```



### 罗列镜像

```
docker image ls
```

### 删除镜像

```
docker image rm <id>
```

### 自建镜像

```
docker build -t image_name where_foler
```



## 容器

### 罗列容器

```
docker container ls
```

### 删除容器

```
docker container rm <id>
```

### 启动容器

```
docker container start <id>
```



### 重启容器

```
docker container restart <id>
```





## 运行镜像

```
docker run -p 4000:80 helloworld
```

具体有很多参数：

- -p   如上面所示，前面的宿主机的端口号，后面是容器内app的端口号。



只要docker 服务还在，哪些docker运行的容器都会在后台运行的额，



## 进入docker shell

```
docker exec -it "id of running container" bash
```



## sqlite数据库丢失问题

docker容器删除了，再从镜像启动一个容器，里面的sqlite或者说其他文件存储的数据都将丢失，可以在镜像制作的时候设置valume，但我总感觉这种做法不太优雅。





## Dockerfile 的编写

Dockerfile 文件就是定义了具体你的镜像从继承何者镜像，到你做了哪些修改等等的相关配置文件。





​	

## 参考资料

1. http://www.ruanyifeng.com/blog/2018/02/docker-tutorial.html
2. https://docker_practice.gitee.io
3. https://docs.docker.com/