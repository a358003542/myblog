Title: docker
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

下面的内容可能 **过时** 了，请参考官方文档来进行安装之。

### windows下的安装

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

### linux系统下安装之后

linux系统下安装docker之后如果出现运行：

```
sudo docker run hello-world
```

可以，但是运行：

```
docker run hello-world
```

不可以，那么应该把你的当前登录用户加入到docker群组中去：

```
sudo usermod -aG docker $USER
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

## 删除虚悬镜像

docker build 或者docker pull 同名镜像，旧镜像的仓库名和tag会变成none，这类镜像叫做虚悬镜像。可用以下命令删除组合这些虚悬镜像：

```
docker image prune
```

## `.dockerignore`

`.dockerignore` 类似于 `.gitignore` 文件，用于我们在docker build镜像的时候忽略掉那些不需要的文件或文件夹，因为docker在build镜像过程时，会自动将指定的上下文目录打包传递给docker引擎。

## Dockerfile

### FROM

指定基础镜像

### COPY

将某个文件或文件夹复制到容器的某个位置，COPY的本地内容路径应该是相对路径。

### ADD

ADD和COPY功能基本一致，除了ADD还增加了额外的功能，比如面向网络的下载等。



### RUN

相当于在容器内执行了某个shell命令，首先各个RUN之间环境是不共用的，其次一个RUN命令就对应容器的一层，所以推荐是RUN命令都合并在一起。

### CMD

CMD提供了运行容器的默认行为，比如 ubuntu 的镜像 CMD 是 `/bin/bash` ，那么输入：

```
docker run -it ubuntu
```

就会直接进入bash。

你在Dockerfile里面定义的ENV环境变量会先进入CMD的shell层的。

### ENV

设置环境变量

在Dockerfile后面， 你可以如下引用之前设置的环境变量： `$APP_PATH`

### VOLUME

定义匿名卷

比如：

```
VOLUME /home/data
```

就定义了容器的数据存储匿名卷，一般Dockerfile的最后会申明匿名卷，就算后面容器运行时用户忘记指定存储卷了，容器运行时也不会像容器的存储卷写入大量数据。而后面我们通过 `-v mydata:/home/data` 来制定存储卷，会覆盖之前Dockerfile声明的默认配置。



### EXPOSE

声明容器提供服务的端口，你还是需要使用 `-p 9001:9001` 来映射端口。



### WORKDIR

指定docker环境下的当前工作目录（当你运行docker run的时候也是在docker环境下）



## 保存某个镜像到文件

```
docker save <image>
```





## 启动某个容器

下面是启动某个容器并进入bash与之交互

```
docker run -it "id of running container" bash
```

如果某个容器已经在后台运行了，你希望登入该容器，则推荐使用 exec ：

```
docker exec -it <container> bash
```

因为使用exec登入容器，输入 exit 也不会导致容器停止。



### 容器运行时设定重启策略

- `--restart=no` 默认 容器退出不做什么

- `--restart=on-failure` 容器非0状态退出 docker会尝试启动该容器

- `--restart=always` 这个主要用于docker服务重启然后自动启动该容器

  



## 查看某个容器的输出日志

如果以后台的形式启动某个容器，那么可以如下查看该容器的日志：

```
docker logs <container>
```



## docker compose

虽然docker-compose说是对docker多容器的编排工具，但实际上就是对单个容器的一些启动配置定制也是很方便的。

一个简单的例子如下所示：

```yml
version: "3"

services:
  web:
    build: .
    env_file:
      - ./pycode/python.env
    volumes:
      - ./data:/home/data
      - ./pycode:/home/pycode
    ports:
      - 9001:9001
```

这些选项很多在 `docker run` 命令时的可选参数，具体功能大体也都是类似的。

运行docker-compose up即启动容器组，或者重启或者查看日志等等。

```
docker-compose up
```



## 多阶段构建

多阶段构建最常用的模式是将你的容器的dev环境和runtime环境分开，具体要有效的实施多阶段构建，你需要深刻理解你当前的项目那些包是运行时环境需要的，那些包是编译环境需要的。

1. 首先你新开一个编译环境的容器，里面装好编译你的项目代码需要的依赖等，然后将你的项目代码编译好。
2. 其次你新建一个运行时环境容器，其中最核心的代码是：

```
COPY --from=builder $ROOT/build $ROOT/build
```

也就是将builder容器的里面编译好的build内容复制到运行时容器里面

这样做有两个好处：

1. 编译依赖可能很多，但你实际的运行时容器镜像可以做到很小巧
2. 编译容器没有发生变动的情况下，重新build整个镜像，编译时容器会全部利用cache，不会再进行费时的编译工作





## Dokcerfile最佳实践

1. 使用 `.dockerignore`
2. 相同的命令尽量合并，因为dockerfile每一个命令就新建了一个docker层。docker早期这点很关键，现在docker重点要关注这三个命令，尽量合并起来： `RUN`  `COPY` `ADD` 

3. 使用多阶段构建，能够大大降低你的镜像的大小，从而不用再苦苦挣扎着去想如何减少中间层和文件。
4. 别安装不需要的软件
5. apt安装软件先update并尽量如下合并为一句话，如下是一个最佳实践，最后还将apt安装过程的缓存删掉了。

```dockerfile
RUN apt-get update && apt-get install -y \
    aufs-tools \
    automake \
    build-essential \
    curl \
 && rm -rf /var/lib/apt/lists/*
```





​	

## 参考资料

1. http://www.ruanyifeng.com/blog/2018/02/docker-tutorial.html
2. https://docker_practice.gitee.io
3. https://docs.docker.com/