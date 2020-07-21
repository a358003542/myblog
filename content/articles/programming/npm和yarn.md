[TOC]

## npm和yarn

nodejs是运行在服务端的javascript，其基于Chrome V8引擎，整体架构是事件驱动的非阻塞的。

npm是nodejs里面的一个包管理工具，大体可以理解为python里面的pip。

在centos7直接安装npm：

```
yum install npm
```

也会顺便把nodejs也安装了。

windows下有直接安装的exe程序。

### npm init

本小节参考了 [阮一峰的npm文章](http://javascript.ruanyifeng.com/nodejs/npm.html) 。

在你想要新建的模块的根目录下运行 `npm init` ，程序会交互问一些问题，然后创建 `package.json` 文件。这样你的用户就可以利用这个 `package.json` 文件然后运行 `npm install` 命令来安装目标模块了。

```
npm install -g module_name
```

加上全局选项 `-g` 会安装在系统的 `/usr/lib/node_modules` 里面（centos7）。

```
npm install module_name
```

没有加上选项 `-g` ,node模块就直接安装在当前工作目录的 `node_modules` 文件夹里面。

### npm list

列出本地已经安装npm模块。如果加上 `-g` 那么是列出安装在系统里面的npm模块，以后就不罗嗦这个了。

### npm update

升级某个npm模块，你可以加上 `--save` 来更新 `package.json` 里面的信息。

### package.json

符号 `^` 之后的版本都可以
符号 `~` 是允许小版本内的升级

### npm publish

注册模块包，需要在 `npmjs.com` 上申请个用户名：

```
npm adduser
```

或者以前adduser过了那么：

```
npm login
```

然后：

```
npm publish
```

默认发送公开的模块，npm付费用户可以发布私有模块： `"private": false,` ，然后在发布的时候加上 `--scope` 选项和你的scope。

## 什么是模块

本小节参考了 [理解exports这篇文章](https://www.sitepoint.com/understanding-module-exports-exports-node-js/) 。

前面谈了一些关于模块的东西，那么什么是模块，简单来说一个js文件就是一个模块，和随便写个js文件不同，上面谈论的npm模块都通过npm良好地管理起来了。

在定义一个模块的时候你可以如下写：

```
exports.fun1 = function(){
    return 'aaa';
};
```

也可以这样写：

```
modules.exports = {
    fun1 : function(){
        return 'aaa';
    }
};
```

这个exports和 `modules.exports` 实际是一个东西，其都是一个对象。

然后在其他文件中使用模块：

```
var test = require('./your.js')
```

这个test变量获得的值就是之前模块定义的那个exports对象。所以你可以如下使用了现在 `test.fun1` 。那个test名字是随便取的，不过最好取模块的名字。

## yarn

yarn简单来说就是更好的npm。具体命令对应如下：

```
npm install --save    ->   yarn add
npm install --save-dev   -> yarn add --dev
npm install -g   -> yarn global add 
npm uninstall   ->  yarn remove
```

首先用npm来全局安装一个yarn： 

```
npm install -g yarn
```

yarn一样利用 `package.json` 来管理你的前端包，之前说的自动创建的lock文件，yarn会另外创建一个 `yarn.lock` 。


### scripts

在 `package.json` 里面我们可以定义自己的脚本名字，比如下面的 `start` 命令，我们如果输入 `npm start` 那么实际运行的是 `node .` ，同样也可以运行 `yarn start` 。

```
"scripts": {
  "start": "node ."
}
```













