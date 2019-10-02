Title: 前端开发之-webpack
Date: 2018-05-26
Status: draft
[TOC]

# webpack打包工具

本文待完善，待我把 create-react-app 更深入的熟悉了之后，再考虑更深一层定义，目前就基本依赖于 create-react-app的自带的webpack机制。

##  entry

```js
module.exports = {
  entry: {
    app: path.resolve(__dirname, './src/main.js'),
  },
```

`entry.app` ：指定主程序的入口

## output

```js
  output: {
    path: path.resolve(__dirname, 'build'),
    publicPath: '',
    filename: 'chemorigin.js',
  },
```

`output.path` :  指定输出的路径

`output.filename` : 指定输出的文件名

## loaders

```js
  module: {
    loaders: [
      { test: /\.(png|jpg)$/, loader: 'url-loader?limit=8192' },
      { test: /\.(ttf|eot|svg|woff2|woff)(\?v=[0-9]\.[0-9]\.[0-9])?$/, loader: 'file-loader?outputPath=build' },
      {
        test: /\.css$/,
        use: ExtractTextPlugin.extract({
          fallback: 'style-loader',
          use: 'css-loader',
        }),
      },
    ],
```

webpack实际只能处理js文件，其他非js文件都是通过loader来处理的。

上面代码的意思是如果遇到 png jpg 这样的图片文件，那么用 url-loader处理一下；

如果遇到 ttf woff2之类的文件用file-loader处理以下。

如果遇到css文件那么用 css-loader处理一下，fallback是如果遇到问题的候选项，style-loader。然后这里使用了 `ExtractTextPlugin` 插件，为的是将css文件单独提出来。

## plugins

```js
  plugins: [
    new ExtractTextPlugin('styles.css'),
    new webpack.ProvidePlugin({
      $: 'jquery',
      jQuery: 'jquery',
      moment: 'moment',
    }),
  ],
```

插件提供了其他额外的功能。

## 使用

webpack具体使用就是就是在你的项目根目录下如上编写一个 `webpack.config.js` 文件，然后运行：

```
webpack
```

命令即可。

