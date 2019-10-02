Title: 前端开发之-vue技术栈基础
Date: 2018-05-26
Status: draft
[TOC]

## vue技术栈

### vue-cli

强烈推荐读者先了解下webpack和相关的nodejs技术栈，然后再来学习 `vue-cli` 来快速搭建一个vue项目骨架，这一块入门上手有点困难，上手之后很多东西都很方便了。这块东西不管你是走react路线，比如用 create-react-app 或者走vue路线，最后都会用到的。 [这篇文章](https://scotch.io/tutorials/getting-started-with-vue-router) 说的很详细，推荐读者阅读一下。

首先是全局安装 vue-cli ：

```
npm install --global vue-cli
```

然后是安装webpack模板初始化一个项目：

```
vue init webpack you_project_name
```

后面有些问题，一般会把 `vue-router` 加上，然后后面eslint和test相关，如果你暂时还不太明白，先放一放没问题，就回答No。

创建的项目如上面文章介绍的，先随便看看，大体了解下即可，一开始肯定不求全部都弄懂。先记住 热启动（随时修改随时生效）：

```
npm run dev
```

或者:

```
yarn start
```

然后如果我们运行：

```
yarn build
```

或输出一个dist文件，里面有 `index.html` 等相关文件，在服务器上用nginx指向这里生产环境就挂着这个网页了。

### vue-router

vue-router 是用来进行路由分发的，详细讨论见 [vue-router](vue技术栈/vue-router.md) 。



### bootstrap-vue

bootstrap-vue 将vue和bootstrap结合起来了，详细讨论见 [bootstrap-vue](vue技术栈/bootstrap-vue.md) 。



### 学习vue

vue的核心知识学习，详细讨论见 [学习vue](vue技术栈/学习vue.md) 。



### 其他问题

遇到的相关的其他问题，详细讨论见 [其他问题](vue技术栈/其他问题.md) 。

