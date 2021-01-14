Category: javascript
Slug: node-learning-notes
Date: 20201121
Tags: javascript, node, npm, yarn

[TOC]

## 何为node

我们知道javascript作为前端的脚本语言是浏览器负责翻译执行的，也就是说javascript的运行是依赖于浏览器的。而node是一个javascript运行时，意思是你的javascript脚本可以类似于在浏览器上在node上运行。事实上node就实现组件结构来说也类似于chrome浏览器，一样是基于chrome的V8 javascript引擎，只是移除了一些和网页显示相关的webkit引擎之类的。

官网为node的定义如下：

> 一个搭建在Chrome JavaScript运行时上的平台，用于构建高速、可伸缩的网络程序。Node.js采用的事件驱动、非阻塞I/O模型，使它既轻量又高效，并成为构建运行在分布式设备上的数据密集型实时程序的完美选择。

V8引擎性能很高，javascript会被直接编译成本地机器码。所以node使用javascript也很高效。因为V8引擎原来处理网页上的javascript脚本就实现上必须是事件驱动，非阻塞IO的，于是到了node服务器这边也是事件驱动的，非阻塞IO编程的。

## node和npm

正如前面所说，node是一个平台，然后node人们也常称作node.js，因为node在作这个平台的时候内置了很多官方的js模块。比如说我们随便从网上找了一个最简单的nodejs入门样例web server程序：

```js
var http = require('http');

http.createServer(function (request, response) {
	response.writeHead(200, {'Content-Type': 'text/plain'});
	response.end('Hello World\n');
    
}).listen(8888);

console.log('Server running at http://127.0.0.1:8888/');
```

其最开始的语句 `require('http')` 就是在引入node.js的官方内置js模块http。

既然有了官方模块那当然就有第三方模块和模块管理工具了。一般安装好node之后除了node命令之外还有npm命令，最新的node现在还提供npx命令。

首先说一下npx命令有什么用，在本地安装一个npm包之后，该包提供了一个命令，如果你希望调用这个命令，以前的做法则可能需要修改 `package.json` 的 scripts 字段：

```
  "scripts": {
    "start": "electron .",
   }
```

然后你通过 `npm start` 来达到效果。现在你可以如下直接调用 `electron` 命令了。

```
npx electron .
```

然后我们继续往下说，上面提到的 `package.json` 是npm用于包管理的很重要的一个配置信息文件。你可以手工创建一个，或者通过 `npm init` 命令来生成一个。

在你想要新建的模块的根目录下运行 `npm init` ，程序会交互问一些问题，然后创建 `package.json` 文件。

### 配置npm国内源

免得后面有些包下载动作太慢了，这里就先讲了。

```
npm config set registry https://registry.npm.taobao.org
```

这个配置对后面提到的yarn也是一样有效的。

### npm的基本使用

- npm install  module_name  安装某个模块
- npm uninstall module_name 移除某个模块
- npm list  列出已经安装的模块
- npm update module_name 更新某个模块

你可以通过 `-g` 选项来说本次操作是针对全局的npm库，但除非有必要，现在是不推荐这样做了。 

npm install 命令还可以使用 `i` 或者 `add` 这两个别名，此外install提供一些安装选项：

- 默认是 `--save-prod` 或者 `-P` ，常规依赖包信息会放在 `dependencies` 字段下。一般和项目直接相关的包放在这里。
- `--save-dev` 或者 `-D` ，开发包信息会放在 `devDependencies` 。和开发调试封装打包等相关的包信息推荐放在这里，比如electron官方会提示我应该放在 **devDependencies** 那里。
- `--save-optional` 或者 `-O` ，可选的包信息：`optionalDependencies` 。

包信息后面的版本有一些特殊符号，其含义是：

- 符号 `^` 表示之后的版本都可以
- 符号 `~` 表示是允许小版本内的升级





## yarn

很多人都推荐使用yarn而不是npm，yarn一方面是基于npm包的，然后和npm比较起来有很多优点，比如并发的网络请求，对依赖版本的处理优化等。

yarn在windows下也提供了安装包，去 [官网](https://classic.yarnpkg.com/zh-Hans/docs/install) 上下载即可。

### yarn的基本使用

- `yarn init` 对应于 `npm init` ，适用于初始化一个新项目的，如果你的项目已经有`package.json` 这个文件了，那么你应该使用 `yarn install` 。
- `yarn add` 对应于 `npm install` ，yarn add 不加上选项将安装到dependencies哪里， 然后 `--dev` 对应npm的 `--save-dev`  ，`--optional` 对应npm的 `--save-optional` 。此外yarn还多了一个 `--peer` 选项，其控制的字段是 `peerDependencies` ，这是一种特殊的依赖，叫做同伴依赖，在发布包的时候需要。
- `yarn upgrade` 升级包
- `yarn remove` 移除包
- `yarn install` 安装项目所有依赖

假设你自定义了npm start这个命令，那么通过 yarn start也是一样可以调用的。

## 模块简介

前面谈了一些关于模块的东西，本小节将进一步介绍node的模块。

首先我们新建一个文件夹mymodule，然后里面新建一个 `index.js` 文件。在`index.js` 文件里面定义一个简单的函数：

```
function add2(a,b){
  return a + b;
}
```

然后导出这个函数

```
exports.add2 = add2
```

然后我们在外面新建一个 `test_mymodule.js` 来实际使用mymoudle模块：

```
var mymodule = require('./mymodule')

console.log(mymodule.add2(1,2))
```

### 补充说明

前面简单的模块创建例子中默认的  `index.js` 入口你可以通过新建 `package.json` 文件然后通过设置 `main` 字段属性来指定其他入口js文件。

如果你的模块很大型了，那么可能 `exports.` 这种写法不太合适了，你可以通过设置 `module.exports` 为其他对象来改进之。


### 发行你自己的npm包

首先你需要在 `npmjs.com` 上申请个用户名：

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

默认发送公开的模块，npm付费用户可以发布私有模块： `"private": false`。




## 参考资料

其他官方文档就不赘述了。

1. node.js实战 图灵设计丛书 Node.js in action
2. [阮一峰的npm文章](http://javascript.ruanyifeng.com/nodejs/npm.html) 
3. [理解exports这篇文章](https://www.sitepoint.com/understanding-module-exports-exports-node-js/) 
4. [npx使用教程](https://www.ruanyifeng.com/blog/2019/02/npx.html)