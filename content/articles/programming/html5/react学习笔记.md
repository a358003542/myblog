Slug: react-learning-notes
Date: 2020
Category: html5
Tags: react



[TOC]

## 前言

react初学者实在不建议过早地涉及`create-react-app` 引入的那些工具链，而是推荐先在html上用起来，对react用的有点感觉了后面有时间再慢慢优化这些工具链。

而react只是在html作为一个简单的javascript库来使用的话，方便我们创建一些html组件，从而更方便地进行DOM操作，实际上react还是很好学的。

## 入门例子

react在html上的利用的一个简单的入门例子如下所示，其中babel库很有用，推荐入手就加上，其除了让我们即使在老旧的浏览器上也可以编写最新的es6代码，也提供了对jsx的支持。jsx是一种javascript和html的混合模板语言，这个后面再讨论。

```html
<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8" />

  <title>Hello React!</title>

  <script src="https://unpkg.com/react@16/umd/react.production.min.js"></script>
  <script src="https://unpkg.com/react-dom@16/umd/react-dom.production.min.js"></script>
  <script src="https://unpkg.com/babel-standalone@6/babel.js"></script>
</head>

<body>
  <div id="root"></div>

  <script type="text/babel">
    class App extends React.Component {
      render() {
        return <h1>Hello world!</h1>
      }
    }
    ReactDOM.render(<App />, document.getElementById('root'))
    </script>
</body>

</html>
```

```javascript
    class App extends React.Component {
      render() {
        return <h1>Hello world!</h1>
      }
    }
```

这是采用es6的类的写法，其继承自React.Component，简单来说这是你定义了一个自己的dom操作组件，其叫做 `App` 。该类必须实现一个 `render` 方法，上面`render` 方法返回的html标签这种写法其就是前面提到的jsx写法，这里render方法返回的是React元素。

```javascript
ReactDOM.render(<App />, document.getElementById('root'))
```

这一句的意思是在html的某个container里面渲染某个React元素。

### JSX简介

JSX初看起来是一种html，但其内在更接近javascript。其类似于jinja2模板引擎，可以如下调用javascript代码。

```jsx
const name = 'react';
const element = <h1>hello, {name}</h1>;
```

javascript的函数和属性点引用等都是可以正常在里面执行的。

JSX还支持React元素标签写入进来，比如：

```jsx
const element = <Welcome name="Sara" />;
```

上面的Welcome是一个react组件，其也可以直接写入到JSX里面。





## 参考资料

1. react官方教程和资料
2. [electron-react-boilerplate项目](https://github.com/electron-react-boilerplate/electron-react-boilerplate)
3. [getting-started-with-react](https://www.taniarascia.com/getting-started-with-react/)



