Slug: react-learning-notes
Date: 20201120
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

在JSX中原html属性名字class需要写为 `className` 。



## 一个实时更新时钟的例子

这个例子介绍了react很多核心概念，同时又不是特别复杂，作为继入门例子之后的第二个教学例子是很合适的。

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
      constructor(props){
        super(props);
        this.state = {date:new Date()};
      }

      componentDidMount(){
        this.timerId = setInterval(()=>this.tick(), 1000);
      }

      componentWillUnmount(){
        clearInterval(this.timerId);
      }

      tick(){
        this.setState({
          date: new Date()
        });
      }

      render() {
        const element = (
          <div>
          <h1>Hello world!</h1>
          <h2>It is {this.state.date.toLocaleTimeString()}.</h2>
          </div>
        )
        return element
      }
    }

    ReactDOM.render(<App />, document.getElementById('root'));

    </script>
</body>

</html>
```

### class组件

如下使用ES6的class来定义了一个react里的组件。

```
    class App extends React.Component {
      constructor(props){
        super(props);
        this.state = {date:new Date()};
      }
```

其constructor构造函数必接受一个props参数，也就是该组件使用是后面跟着的一些属性值将传递进来。某些简单的情况你也可以利用javascript的函数来创建一个函数组件。

上面的例子就是创建了这样一个class组件。

### 函数组件

```javascript
function Welcome(props) {
  return <h1>Hello, {props.name}</h1>;
}
```

和一般函数的区别是其接受的第一个参数必是props参数。

在JAX中react会把小写字母开头的标签视作html原生标签，而将大写字母开头的视作react组件。

### 组件里面的state

组件里面的state似乎只是一个javascript对象，存储着一些值，这些值表示本组件的当前一些状态量。不过这个state值在react中会有一些特殊的用途。比如调用组件的 `setState` 方法来修改【注意只能通过setState方法才会有效】state的值，那么该组件是会重新渲染的。

### componentDidMount

这个方法里面的动作将会在组件已经渲染到DOM之后再执行。

上面例子中做的是开启一个计时器动作。

### componentWillUnmount

这个方法里面的动作将会在组件即将卸载之前执行。

上面例子中做的是将目标计时器移除。

## AJAX请求

使用fetch方法请求即可，需要注意的是请求动作应该挂在 `componentDidMount`  方法里面。获取数据之后要通过 `setState` 方法将数据更新到本组件的状态信息中去。

## 参考资料

1. react官方教程和资料
2. [electron-react-boilerplate项目](https://github.com/electron-react-boilerplate/electron-react-boilerplate)
3. [getting-started-with-react](https://www.taniarascia.com/getting-started-with-react/)



