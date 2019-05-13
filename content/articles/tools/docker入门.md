Title: docker入门
Slug: docker
Date: 2018-06-14
Modified: 2019-05-13
Tags: docker,


[TOC]



## 前言

关于docker是什么请参看 [这个网页](https://docker_practice.gitee.io/introduction/what.html) ，说docker将改变软件生态确实是不为过的。老实说在接触docker之后感觉之前学到的很多东西，比如linux系统相关的一些，ansible等等部署工具相关的一些，virtualbox和 vagrant相关的一些，都在慢慢过时和淘汰了。当然那些工具还是很有用的，说他们被淘汰了是有点过了，更确切来说，对于一般玩家来说，可以节省更多的精力和时间，而不需要折腾那些工具那些配置学习折腾个老半天了。

> That‘s why we love docker.

但实际上docker带来的变化远远不止于只是一个可以节省开发者做某些事情的时间的一个不错的工具那么简单，其伴随着SPPS，软件即服务，更确切来说整个互联网的大背景下，应运而生的。与之相应的，开发者们顺应这个时代，在编码，软件应用的很多方面，都需要做出改变。请读者进一步阅读 https://12factor.net/zh_cn/ 里面的讨论。

实际上之前我折腾vagrant的时候，就很是认同这个理念： 那就是开发，测试，生产一致的环境，彻底解决，在这里可以运行，在这里就不行了的问题。而vagrant的控制virtualbox创建虚拟机的方式，在我看来显得略微笨拙了点，配置的繁琐，似乎并没有很好地解决这个问题；而docker除了很好地解决了上述问题之外，他的虚拟化方案更轻量级，更接近原生。

docker包括三个核心概念： 镜像image，容器container，仓库

- image 镜像 用来创建docker容器的模板
- container 容器，可以看做镜像生成的一个实例
- docker仓库用来保存镜像的，[docker hub](https://hub.docker.com/) 哪里提供了很多docker的仓库。



## 安装

windows下安装如果你的操作系统不是专业版或者企业版，那么只能用 [docker tool box](https://docs.docker.com/toolbox/toolbox_install_windows/) 来安装。然后记得把 window10 的开发者模式打开。

如果你的windows10是企业版或者专业版，我没试过，我想按照官网哪个，直接就能安装成功吧。

kitematic 是docker 镜像的管理工具，推荐使用，很方便的。

### centos安装

```
yum install -y yum-utils
yum install -y device-mapper-persistent-data
yum install -y lvm2
yum-config-manager  --add-repo  https://download.docker.com/linux/centos/docker-ce.repo
yum install docker-ce
```

## 第一个项目

下面的内容参考了这个视频：

<iframe width="560" height="315" src="https://www.youtube.com/embed/YFl2mCHdv24" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

这个项目我们将新建一个自己的docker 镜像或者说image。

1. 首先新建一个文件夹，开始编写Dockerfile

```dockerfile
FROM php:7.0-apache
COPY src/ /var/www/html
EXPOSE 80
```

FROM what 表示本镜像基于这个镜像，该镜像的名字叫php，一个官方镜像，然后分支名字是 `7.0-apache` 。

然后执行COPY动作，将本文件夹下面的src文件夹里面的内容，复制到容器【根据本镜像生成的容器，源镜像是基于linux系统的】的 `/var/www/html` 文件夹下。

然后暴露容易的80端口

2. src下就是一个简单的php文件，这里不是讨论的重点。
3. 生成镜像 

```
docker build -t image_name .<where_foler>
```

4. 列出本地的镜像

```
docker image ls
```

5. 从网下下载某个镜像

```
docker pull hello-world
```

6. 删除某个镜像

```
docker image rm <id>
```

这里我制作镜像运行的命令如下，因为 `a358003542` 是我在docker hub 哪里注册的用户名，所以要采用这种写法：

```
docker build -t a358003542/first .
```

7. 启动镜像

```
docker run -p 8080:80 a358003542/first
```

docker run 命令有自动试着从docker hub那边下载镜像的功能，这个命令的run单词的含义是在一个容器内执行某个命令的意思，所以其也会自动根据一个镜像创建一个容器。

这里的端口转发，docker容器内是80，容器对外发布的是8080端口。你可以通过下面命令来查看下已经创建的容器：

```
docker container ls
```

8. 将你的项目提交到docker hub那边

```
docker login 
docker push a358003542/first
```

注意这里docker push 后面名字的格式一定是 `你在docker hub上的用户名/你的仓库名字` 。



## 进入docker shell

```
docker exec -it "id of running container" bash
```







​	

## 参考资料

1. http://www.ruanyifeng.com/blog/2018/02/docker-tutorial.html
2. https://docker_practice.gitee.io
3. https://docs.docker.com/