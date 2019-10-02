Title: 前端开发之-nodejs技术栈
Date: 2018-05-26
Status: draft
[TOC]

## nodejs技术栈

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



## eslint-从入门到放弃

eslint大体类似于python里面的pylint或者pep8之类的，因为python本来对写法很是严格，所以那边问题不是太大，但javascript这边写法风格很多，很是让人纠结，而且更加让人纠结的是比如说react又引入了自己的jsx语法，说eslint从入门到放弃真不是开玩笑。。

而且这些功能有的和编辑器的有所重合，比如说create-react-app有自己的eslint配置等，

```js
{
  "extends": "react-app"
}
```

一般建议是完全从你喜爱的编辑器入手来做一些调配工作，包括eslint和对应的prettier功能。下面本文就webstorm的一些配置做出说明。

### webstorm设置javascript版本

```
Settings -> language & frameworks -> javascript
```

作者走的是react路线，所以选的是 react 的 jsx in es6。

### webstorm设置eslint环境

一般项目根目录下创建一个 `.eslintrc` 文件，然后编辑器应该会提醒你具体配置eslint环境的，如果没有你可以到： 

```
Settings -> language & frameworks -> javascript -> Code Quality Tool -> Eslint
```

那里看一下，然后要把 eslint对应的那个config包安装上，多少有点麻烦：



### webstrom设置自动格式调整

这大体类似于python里面的autopep功能，具体鼠标右键会看到： `fix eslint problem` 这个快捷键，其对应的命令是 `eslint --fix` 。

### 但是也许应该放弃。。

似乎webstrom会自动把这些环境配置好，似乎是用的webstorm自带的eslint和配置？不太清楚，总之把

```
Settings -> language & frameworks -> javascript
```

要选择好。

然后 `.eslintrc`  这个文件创建下总没有坏处，其他的如果有问题请读者参看  [webstorm的官方文档](https://blog.jetbrains.com/webstorm/2015/05/ecmascript-6-in-webstorm-transpiling/) 。







