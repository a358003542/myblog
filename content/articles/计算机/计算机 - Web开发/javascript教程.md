
## 前言

本文在行文上是假设读者已经掌握了一门编程语言了的，所以一些基本的编程语言方面的概念不会做过多的讨论。

javascript就历史起源来说似乎并不是一个主角命，更像是编程语言世界里面一个注定跑跑龙套的。1995年某个公司开发了某个浏览器，然后该公司需要为这个浏览器开发一个脚本语言，就把这个任务丢给了 Brendan Eich ，Brendan Eich很不情愿地接受了这个不喜欢的任务，大概花了10天时间仓促完成了Javascript的设计，而且javascript最开始名字不叫javascript，叫livescript，就连javascript这个名字后面改也有点蹭Java语言的热度的嫌疑。

后面javascript的流行和大热可能是其创始人也料想不到的，实际上就是javascript后面刚发展起来的那几年，大家也只是觉得其主要作为一个前端脚本语言，对其仍然是一种轻视的态度，觉得这个语言也就写写浏览器界面的动态效果之类的。随着node.js的出现和相关生态圈的日益成熟壮大，人们才惊讶地发现javascript已经是编程世界里面最大热的几门语言之一了，继而近几年，随着javascript生态的不断成熟和壮大，再也没有人去质疑javascript作为当今编程世界里面的编程语言的主角地位了，最多只是碎碎念说几句javascript这个语言的一些问题。

## 注释

多行注释推荐如下写法：

```javascript
/**
 * make() returns a new element
 * based on the passed-in tag name
 */
```

单行注释用 `//` ，然后注释都新起一行写，如果是代码块内的注释，则前面空一行：

```js
// This is a comment that the computer will ignore. 

function getType() {
  console.log('fetching type...');

  // set the default type to 'no type'
  const type = this.type || 'no type';

  return type;
}
```

然后就是注释文字具体内容要和注释符号空一空格。



## javascript代码放在那里

javascript的代码一般推荐是放在HTML文档最后面， `</body>` 标签之前，这样能够让浏览器更快地加载页面。至于其他倒没有特别的要求，刚开始简单的javascript代码就直接写上去也是可以的:
```html
<script>
your awesome javascript code
</script>
```
如果javascript代码量有一点了那么当然还是推荐另外单独放在一个js文件上，然后如下引入进来:
```html
<script src="where"></script>
```

## javascript代码REPL环境

你可以在浏览器的debug控制台上运行javascript代码，或者安装node环境之后进入node命令下的REPL环境。

## 程序中的操作对象

### 简介

javascirpt的数据类型分为两类，一类是原始类型：数值、字符串和布尔值；另一类是对象类型。此外javascript还有两个特殊的值：`null` 和 `undefined` 。javascript除了数值、字符串、布尔值、null、undefined之外就都是对象了。比如后面提到的数组，函数也都是对象，只不过其是javascipt内部定义的对象。

### 声明常量和变量

javascript的变量是区分大小写的。

javascript可以利用关键词 `var` ， `const` 和 `let` 来声明变量或常量，其中const是声明常量的，var和let是声明变量的。var声明变量是大家在javascript中常用的声明变量关键词，其声明的变量的作用域很不同于其他编程语言，叫做 **函数作用域** 。即你在函数区块内声明的变量整个函数体都是可以使用的，包括哪些花括号结构或任意的嵌套函数。因为程序员对于变量的作用域习惯了块作用域，所以airbnb规范提出不推荐使用 `var` ，而是推荐使用 `let`，因为 `const` 和 `let` 都是块作用域（block-scoped）。

参考mozilla上的相关讨论，变量作用域显得另类是一方面，更糟糕的是因为这个作用域会让变量声明语句可以随意放置，这会造成代码变得混乱和难以理解。**现代javascript编码推荐使用let，最好不用var**。

我们可能会看到某些javascript代码直接写上 `x=1` ，前面没有写上关键词，严格意义上来说这不叫声明变量，而是在全局对象上挂载了x这个属性，从编码规范来说是应该抵制这种写法的。

### 全局变量

在网页中有个全局对象 `window` ，所以我们可以把一些全局变量挂在 `window` 对象里面。

### 数值(number)

**javascript不区分整数值和浮点数值**，javascript中所有数字都用浮点数值表示，这是javascript和其他编程语言的很大不同。然后数值型那些运算，比如加减乘除之类的就不用多说了。其中 `%` 和python一样也是求余操作。在python3中有 `5//2` 是求商的概念，javascript没有这个概念，我们需要如下来获得类似的效果。

```
parseInt(5/2)
```

#### parseInt()

将字符串转成整数型。

```js
> parseInt('2.5')
2
```

### NaN

如果我们执行 `parseInt('abc')` ，那么将返回 `NaN` ，判断是否是NaN如下所示：

```js
> Number.isNaN('a')
false
> Number.isNaN(1)
false
> Number.isNaN(NaN)
true
```

**注意：** javascript还有一个全局函数`isNaN` ，其和Number.isNaN行为不太一样，一般推荐使用 `Number.isNaN` 。Number.isNaN意思很明显就是判断是否是NaN这个值，而全局的isNaN更像是在说输入的这个东西是不是一个数值或者能不能转成一个数值，true则不能，false则能。

### 字符串(string)

javascript同python一样单引号和双引号都是可以的。

```javascript
const name = 'Capt. Janeway';
```

你可以通过 `+` 来实现一些简单的字符串拼接工作，也可以如下进行字符串模板操作。

```javascript
`How are you, ${name}?`
```

javascript的字符串类型和python非常类似，比如 `string[0]` 是支持的。然后不可以这样用string[0:2]，幸运的是javascript提供了类似python中的那种切片概念，就是使用 `slice` 方法

```
> "hello".slice(0,2)
'he'
> [1,3,4,5].slice(0,2)
[ 1, 3 ]
```

不过javascript的slice方法和python的切片操作还是有点区别的，其只有 `(start,end)` 两个参数，然后其也有负数从末尾算起的概念，具体请参看 [这里](http://www.w3school.com.cn/jsref/jsref_slice_string.asp) 。



#### 字符串的一些方法

-   **length:** 字符串长度
-   **toUpperCase:** 变成大写
-   **toLowerCase:** 变成小写
-   **indexOf:** 返回子字符串出现的索引位置，index索引编号规则和python相同。
-   **substring:** 返回子字符串，如果熟悉python的那种切片规则的话，那么推荐就直接使用 `slice` 方法。
-   **replace:** 替换操作 
-   **split:**  分割操作

#### toString方法

javascript的数值、布尔值、对象和字符串都有一个 `toString` 方法，大体类似于python的 `str` 函数。自己定义的对象也可以加上 `toString` 方法：

```js
class Jedi {
  constructor(options = {}) {
    this.name = options.name || 'no name';
  }

  getName() {
    return this.name;
  }

  toString() {
    return `Jedi - ${this.getName()}`;
  }
}
```

### 布尔值(boolean)

javascript的布尔值是 `true` 和 `false` 。在进行比较判断操作时，如果你是希望比较值的话，类似python的比较判断 `==` 符号，在javascript中对应的是 `===` 。三个等号，这不是什么别出心裁，也没有任何实际的好处，就是javascript的历史遗留问题罢了。
```
=== Equal to
!== Not equal to
```
boolean值的判断遵循以下规则：

1.  `false` `0`  空字符串 `""`  `NaN`  `null`  `undefined` 都被视作false
2.  其他都被视作true

```js
> Boolean({})
true
```

### null

javascript的 `null` 。其是一个特殊值。类似于python的 `None` ，然后还有一个什么 `undefined` 。比如函数没有明确return值就会默认返回 `undefined` ，感兴趣的可能查一下这两个的区别，我看了一下，觉得挺无聊的。上面谈到 `==` 和 `===` 的区别，如果用 `===` ，则 `undefined` 是不等于 `null` 的，如果用 `==` ，则javascript会额外做一些类型转换工作，这两个又会看作相等的。

ECMA-262 规定：

```
null == undefined; -> return true
```

比较操作的时候一律推荐使用 `===`  和 `!==`  ，而不要使用 `==` 和 `!=` 。



### typeof操作符

查看某个对象的对象类型，typeof操作符只可能返回以下六种结果：

-   number
-   string
-   object
    -   function
    -   array
    -   date
    -   regexp
-   boolean
-   null
-   undefined
-   symbol (new in es6)

```javascript
typeof x
"undefined"
typeof 1
"number"
```



### 数组

javascript的数组（array）在数据结构概念上大体类似于python的列表。

#### 构建一个数组

```js
var array1 = [];
var array2 = new Array();
const items = [1, 2, 3.14, 'Hello', null, true];
```

其索引index编号法则也和python一致。

#### 数组的一些方法

- **length:** 数组长度
- **indexOf:** 返回数组某个子元素的索引位置
- **slice:** 切片操作，类似于python的 `lst[0:2]` 那种表达方法。slice方法不接受参数就默认返回该列表所有引用，也就是通常所说的 *浅拷贝* 。浅拷贝简单来说就是复制一个字典或者数组（或者其他复杂对象），根据第一层key赋值第一层value，如果第一层key是另外一个对象的引用，那么拷贝前对象和拷贝后对象都会指向统一对象，深拷贝就是进一步深入递归拷贝。
- **push:** 末尾添加一个元素
- **pop:** 最后一个元素删除
- **unshift:** 数组头部添加一个或多个元素，返回新数组的长度
- **shift:** 数组头部删除一个元素
- **sort:** 排序，破坏型。值得一提的是对于数字排序并不是按照从大到小的顺序来的，不太清楚为何:

```
> var lst = [1,5,2,3,51,4,45,545,541,48,77]
> undefined
> lst.sort()
> [ 1,
> 2,
> 3,
> 4,
> 45,
> 48,
> 5,
> 51,
> 541,
> 545,
> 77 ]
```

在python中最多说字符串就这样，但这里是number类型啊。然后要正常排序，我们需要如下操作（参看 [这个网页](http://www.w3school.com.cn/jsref/jsref_sort.asp) ）:

```js
var lst = [1,5,2,3,51,4,45,545,541,48,77]
function sortNumber(a,b){
return a - b
}
lst.sort(sortNumber)
alert(lst)
```

这里sort方法接受一个函数参数，这个函数接受两个参量，用来判断a和b的值大小，如果返回值小于0，则a放在前面。如果返回值大于0，则a放在后面。这种排序方法也支持数字字符串的情况。javascript在处理这种 `字符串 - 字符串` 的情况是会尝试做转换成number类型的才做。

- **reverse:** 反转，破坏型。
- **splice:** 从指定的索引删除某些元素，然后在此处添加某些元素，相当于update更新了。

```js
> var arr = ['Microsoft', 'Apple', 'Yahoo', 'AOL', 'Excite', 'Oracle'];
> undefined
> arr.splice(2, 3, 'Google', 'Facebook');
> ["Yahoo", "AOL", "Excite"]
> arr
> ["Microsoft", "Apple", "Google", "Facebook", "Oracle"]
```

参数意思是从索引2开始删除3个元素，然后添加后面的元素。从上面的例子可以看出splice方法是破坏型的方法，然后其返回的是删除了的那是那个元素。

splice方法也可以用于只删除不添加也就是纯删除操作，或只添加不删除的纯添加操作。

```
// 只删除,不添加:
arr.splice(2, 2);
// 只添加,不删除:
arr.splice(2, 0, 'Google', 'Facebook');
```

- **concat:** 连接两个数组，非破坏型。

```
> var lst1 = [1,2,3]
> undefined
> var lst2 = ['a','b','c']
> undefined
> lst1.concat(lst2)
> [1, 2, 3, "a", "b", "c"]
```

- **join:** 类似于python字符串的join方法，如下所示:

```
var arr = ['A', 'B', 'C', 1, 2, 3];
arr.join('-'); // 'A-B-C-1-2-3'
```

-   **fill:** 数组用某个值来填充

#### for遍历数组

```js
for (let value of array) {
  // do something with value
}
```

遍历数组还可以这样：

```js
> a = ['a', 'b', 'c']
< a.forEach(function(value, index){
    console.log(value, index);
});
> a 0
> b 1
> c 2
```

这大体实现了类似于python的 `enumerate` 写法。上面的forEach方法后面跟着的函数也可以只接受一个value参数。

#### 判断某个元素是否在数组中

```
['a','b'].indexOf('a')
```

如果返回 `-1` 则该元素不在数组中，否则在数组中。

```js
function is_in_array(array, element){
    if (array.indexOf(element) === -1){
        return false
    }else{
        return true
    }
}
```

#### map和filter和reduce

这三个函数是函数编程很重要的几个函数，在数组对象里面可以直接调用这些方法：

```
a.map(function)
```





### 对象

对象是一个整合了数据和函数的集合。

```javascript
> let x = {}
undefined
> x = {'a':1}
{ a: 1 }
```

下面演示了对象如何整合函数（或者叫做方法）的例子：

```javascript
let x= {
  'data': [1,2,3,4],
  'length': function(){return this.data.length}
}

console.log(x.length())
```

我们大概能够猜测出一些javascript底层如何实现的细节，但这对于目前阶段学习和使用这个编程语言来说是没有裨益的。前面在介绍typeof的时候提到数组，函数都是对象。

新建一个数组的完整写法是： `new Array()` ；新建一个对象的完整写法是：`new Object()` 。新建一个类的写法如下所示：

```javascript
class Rectangle {
  constructor(height, width) {
    this.height = height;
    this.width = width;
  }
}

let p = new Rectangle();
```

因为后面有class这样的概念，我是推荐将这些出现的对象看作类似python中字典的概念，一个键值对映射集合。从编程概念上讲也是需要这样一个数据类型的。然后数组，这里的对象，函数，用户自定义的类等用typeof去查看都是object，他们都属于object。这个object是否就是这里的Object，从实现层面上我还不大确切，但这不是重点，就算是，从编程概念上来说也是应该有所区分的。一个是实用的数据类型，一个是很抽象的面向对象编程概念上的底层表述。

#### 对象的原型

JavaScript的对象大多有一个原型对象，其从原型继承属性。可以通过 `Object.prototype` 来引用该对象的原型对象。

要检测一个对象是否是另外一个对象的原型可以使用 `isPrototypeOf` 方法：

```
p.isPrototypeOf(o) // if true then the p is the o's prototype.
```



#### in语句

判断某个对象时候有某个键。

```js
'name' in xiaoming;

> var d = {}
undefined
> d['a'] = 1
1
> d
Object {a: 1}
> 'a' in d
true
> 1 in [1,2,3]
true
```

#### delete语句

其对应的就是python的del语句。然后我们看到javascript的 `delete` 语句删除不存在键也不会报错。

```js
> d
Object {a: 1}
> delete(d.b)
true
> d
Object {a: 1}
> delete(d.a)
true
> d
Object {}
```

#### hasOwnProperty方法

对应于python2的has\_key方法，不过python2已经移除了，推荐用in语句。

```javascript
d = {'a':1}
d.hasOwnProperty('a')
true
```

#### shallow copy

```js
const original = { a: 1, b: 2 };
const copy = { ...original, c: 3 }; // copy => { a: 1, b: 2, c: 3 }
```

#### 遍历对象属性

`Object.keys(obj)` 将返回该对象的keys组成的数组，然后后续可以利用数组的遍历动作来实现对对象keys的遍历。

```
Object.keys(obj)
```





### 集合

javascript中的集合Set大体也和python中的集合概念相近。

var s1 = new Set(); // 空Set
var s2 = new Set([1, 2, 3]); // 含1, 2, 3

然后其也有 `add` 方法用于添加一个元素。用 `delete` 方法来删除某个元素。



## 函数

函数正如前面所说也是一个对象，一个简单的函数对象定义如下所示：

```javascript
let greeting = function(name){
	console.log(name);
}
greeting('hello')
```
上面的写法主要介绍了匿名函数的写法，某些情况下会用到，一般定义函数最好采用如下写法：

```js
function abs(x){
	if (x >= 0) {
      return x;
    } else {
      return -x;
    }
}
```

这两种定义风格是完全等价的。这里值得一提的是如果函数没有确定return值，则返回的是 `undefined` 。

### arguments用法

javascript的函数内部可以直接使用 `arguments` 这个变量，其不是一个Array，但可以如下使用:

```
arguments[0]
arguments.length
```

其会接受传入函数的所有参量。

### rest用法

这个有点类似于lisp语言的rest参量控制概念，也就是如下

```js
function func(a,b,...rest){
	console.log(rest);
}
```

rest是表示除了a和b之外的所有其余参量。注意前面三个点号: `...rest` 。

### 箭头函数

简单来说箭头函数就是 lambda 表达式的更简洁写法，只是说在javascript语境下其和一般function的区别是：<u>其没有this绑定</u>。

```js
(param1, param2, …, paramN) => { statements }
```



## 程序中的逻辑

这一块如果读者熟悉一门编程语言的话，粗略地了解下扫一遍基本上就掌握了javascript相关语句知识。下面本小节也不会过多地讨论，只是就某些应用上常见的知识点做出一些说明。

### 条件判断结构

条件判断结构，和python大同小异，除了那些圆括号（记住这个圆括号必须加上）和花括号。

```js
var feedback = 10
if (feedback > 8) {
	console.log("Thank you! We should race at the next concert!")
} else {
	console.log("I'll keep practicing coding and racing.")
}
```

虽然javascript不像python那样强制缩进风格，但还是推荐用缩进来增强你的代码可读性和逻辑清晰性，如:

```js
age = 20
if (age < 6) {
	console.log('kid')
} else if (age >= 18) {
	console.log('adult')
} else {
console.log('teenager')
}
```

javascript有switch语句，作为我们pythoner你懂的，用多个else if语句也是可以的。

### switch语句

```javascript
function set_choice() {
  choice = 'second'
  switch (choice) {
    case 'first':
      console.log('first');
      break;
    case 'second':
      console.log('second');
      break;
    default:
      console.log('default');
  }
}
```



###  三元运算符

```
> let b = null
undefined
> b = b ? b : 2
2
```

### for循环

javascript和python都有while语句，但while语句用的较少，更多的是使用for语句。

```js
var count = 10;
for (var i=0; i < count; i++){
   console.log(i);
}
```

### for遍历数组

```js
for (let value of array) {
  // do something with value
}
```

遍历数组还可以这样：

```js
> a = ['a', 'b', 'c']
< a.forEach(function(value, index){
    console.log(value, index);
});
> a 0
> b 1
> c 2
```

这大体实现了类似于python的 `enumerate` 写法。

### for遍历对象

然后递归遍历对象的key也是可以的:

```js
for (var i in {'a':1,'b':2}) {
	console.log(i)
}
```

### for实现while循环

下面是用for语句来实现while循环：

```js
var count = 10;
var i = 0;
for (; i < count; ){
  console.log(i);
  i++;
}
```

### for实现无限循环

下面是用for语句实现无限循环：

```
for (;;){
  dosomething;
}
```

### while语句

while语句简单了解下吧。

```js
var x = 0;
var n = 99;
while (n > 0) {
	x = x + n;
	n = n - 2;
}
```

还有do while 语句

```js
var n = 0;
do {
	n = n + 1;
}while (n < 100);
```


### 异常处理

类似于python的 `try...except...` ，javascript有：

```
try {
    throw （new Error("Invalid Parameters"));
}catch (e) {
    console.log(e);
}finally {
    //always do something.
}
```



## 面向对象编程

现代javascript推荐使用class来定义类：

```javascript
//定义类
class Point {
  constructor(x, y) {
    this.x = x;
    this.y = y;
  }

  toString() {
    return '(' + this.x + ', ' + this.y + ')';
  }
}
```

以前老式的写法如下所示，可以了解下：

```javascript
function Point(x, y) {
  this.x = x;
  this.y = y;
}

Point.prototype.toString = function () {
  return '(' + this.x + ', ' + this.y + ')';
};

var p = new Point(1, 2);
```



### this

在javascript里面，object里面定义的方法， `this` 指向的就是本对象的实例。

如果 this 在函数里面，如：

```
function (){
    this.x = 1;
}
```

那么指定的是当这个函数要运行的时候，具体调用这个函数的对象。

比如说某个函数将这样被调用： `jquery对象.what` 那么这个函数里面的this就是指定的那个jquery实例，通常也就是网页里面的某个标签元素。

### constructor方法

面向对象编程里面常见的概念，即该对象的构造方法，在新建实例化该对象时被调用。

### 属性的get和set

面向对象编程里面这个是自定义对象重要的一个设计点，javascript采用如下`get name()` 这样的写法： 

```javascript
class User {
  constructor(name) {
    this._name = name;
  }

  get name() {
    return this._name;
  }

  set name(value) {
    if (value.length < 4) {
      console.log("Name is too short.");
      return;
    }
    this._name = value;
  }
}

let user = new User("John");
console.log(user.name);

```

### 类的继承

关于面向对象的继承概念这里就不赘述了。

```javascript
class Dog extends Animal{
   //
}
```

### super

类似python语言里面的super概念，引用父类。

### instanceof

类似于python语言中的isinstance函数。

```
obj instanceof Class
```



## no-jquery

更多相关知识请参阅参考资料四，即 [这个Github项目](https://github.com/nefe/You-Dont-Need-jQuery/blob/master/README.zh-CN.md) 。下面就一些重点知识做出一些整理。

### 选择

jquery的选择是该库很核心的一个功能，现代JavaScript提供了 `document.querySelector()` 和 `document.querySelectorAll()` 来作为替代。然后原来的 `document.getElementById()`  ， `document.getElementByClassName()` 或 `document.getElementByTagName()` 性能更好。

```
// jQuery
$('selector');

// Native
document.querySelectorAll('selector');
```

#### 选择class

```
// jQuery
$('.class');

// Native
document.querySelectorAll('.class');

// or
document.getElementsByClassName('class');
```

#### 选择id

```
// jQuery
$('#id');

// Native
document.querySelector('#id');

// or
document.getElementById('id');
```





### ajax

更多信息请查看mozilla关于 [fetch函数的介绍](https://developer.mozilla.org/zh-CN/docs/Web/API/Fetch_API) 。

```javascript
fetch("http://localhost:8080").then(
  function(response) {
    console.log("请求状态: " + response.status);
    return response.text();
  }
).then(function(text){
  console.log("返回文本：" + text);
})

```

fetch将请求一个URL，然后调用后面的函数。其中`response.text()` 返回的是一个Promise对象，什么是Promise对象，可以类比作python异步编程里面的协程，继续调用then才能获得内容。

如果你请求的是JSON api接口，那么可以直接调用 response.json来处理返回结果：

```javascript
fetch("http://localhost:8080").then(
  function(response) {
    return response.json();
  }
).then(function(result){
  console.log(result);
})
```

## 字符串

### 字符串的match方法

字符串的match方法可以跟上RegExp 对象来继续正则表达式匹配操作。

## 对象

### 获取对象的keys数组

```
attrs = attrs || {};
Object.keys(attrs);
```



## JSON

如下所示，下面也演示了利用 `JSON.parse` 来将相应的JSON字符串转成JavaScript对象。

```javascript
> let x = JSON.stringify({ x: 5, y: 6 });
undefined
> x
'{"x":5,"y":6}'
> typeof x
'string'
> let y = JSON.parse(x)
undefined
> y
{ x: 5, y: 6 }
> typeof y
'object'
```



## 函数

### 立即执行的匿名函数

我们常见到某个js脚本一整段都被这样一种写法包围着：

```
(function($){…})(jQuery)
```

这是定义了一个匿名函数，其将立即执行，接受了一个jQuery参数，并传递给了匿名函数。

之所以这种写法很常见是因为这样做可以将整个模块的代码都放在一个匿名函数里面，这样模块里面定义的全局变量就成了函数内的局部变量了，这样不会污染全局变量命名空间。

## window

window对象里面的属性都是全局变量，可以直接调用的。

### setInterval

```
setInterval(func, 1000)
```

启动一个计时器，第二个参数是时间间隔，每个那个时间间隔将会执行一次目标函数，默认单位是ms。

### setTimeout

类似setInterval，启动一次性任务。

### location

该窗口的Location对象

### history

该窗口的History对象

## document

### getElementById

### createElement

```
var e = document.createElement(name);
```

创建一个标签，返回的是一个 `Element` 对象。

### createTextNode

```
child = document.createTextNode(child);
```

创建一个文本节点。

```javascript
var e = document.createElement('li');
var t = document.createTextNode('this is text.')
e.appendChild(t);
```

上面的例子创建了一个li标签，然后创建了一个文本节点，然后将这个文本节点附加到该li标签上，最后该li标签内容如下：

```
<li>this is text.</li>
```

## Element对象

### querySelector

之前接触到的`document.querySelector` 是因为Document对象继承自Element对象，该方法实际来自Element对象。具体就是在本Element下继续进行搜索动作。

### setAttribute

`Element` 对象可以调用这个 `setAttribute` 方法来设置标签内的属性值。

```
element.setAttribute(name, value);
```

### dataset

查询到的元素如果div则是更具体的HTMLdivElement等等，其继承自HTMLElement，HTMLElement有一些专门的方法。比如这个dataset，其是可以只读属性，对应html中的`data-*` 这样的属性值，比如说 `data-name` 将变成dataset的`{'name': 'what'}` 。

### classList

类似上面的讨论也是HTMLElement的一个属性，表示class属性数组。



## Node对象

### textContent

之前提到querySelector查到某个Element之后想要取出其文本内容可以调用 `textContent` 属性，document和Element都能这样做只是因为它们继承自Node对象，具体textContent这个属性的定义是在Node对象这里。

### parentElement

返回本节点的父节点

```
parentElement = node.parentElement
```

### removeChild

移除本节点的某个子节点

```
node.removeChild(child);
```



## 事件

Element对象继承自EventTarget从而获得了这些方法： `addEventListener` ， `removeEventListener` 和 `dispatchEvent` ，这几个方法都是和事件处理相关的。

熟悉GUI桌面程序的话会对事件有个大致的理解，大体类似于QT里面的信号。



### CustomEvent

自定义一个事件，第二个参数可以是任意的信息。

```
  new CustomEvent(name, { bubbles: true, cancelable: false })
```

### dispatchEvent

程序触发某个Element元素上监听的事件

```javascript
target.dispatchEvent(
      new CustomEvent(name, { bubbles: true, cancelable: false })
);
```

### addEventListener

给某个元素增加一个事件监听

### removeEventListener

移除某个元素上的事件监听

### event.target和event.currentTarget的区别

事件响应到调用函数那边，通过event.target或者event.currentTarget可以引用触发事件的浏览器对象，不过它们是有一点区别的。

首先说一下事件的冒泡机制，当某个元素触发了某个事件，其会触发本元素上事件响应处理程序，然后该事件会继续冒泡到本元素的父元素之上，再触发父元素的事件响应处理程序。

event.target是引用那个最开始触发事件的那个目标元素，而event.currentTarget是引用那个实际处理事件的元素。比如说某个div里面有一个button，你给div绑定了事件监听处理函数，然后那个事件监听处理函数里面调用 `event.currentTarget` 则会指向那个div，而如果你调用 `event.target` 则会引用最开始触发click事件的那个元素，也就是button。

在一个目标button里面处理click事件使用event.target或者event.currentTarget是没有区别的。

## 其他

## 其他

### 表单提交按钮防止多次点击多次提交

参考了 [这个网页的第一小节](https://www.the-art-of-web.com/javascript/doublesubmit/) ，觉得这个解决方案很是简单，而且有效。对于单页面表单，也就是提交成功了通常切换到另外的网页那边去了的，还是很好地适用的。可能在某些情况下，本解决方案会令人不太满意，因为这个提交按钮只要提交之后就显示按钮一直处于禁用状态。



```html
<form method="POST" action="..." onsubmit="myButton.disabled = true; return true;">
...
<input type="submit" name="myButton" value="Submit">
</form>
```

## jquery基本操作

### 基本用法

jquery的基本用法就是:

```js
$(selector).action()
```

 `$(selector)` 返回的是找到的对象的数组，而进行某个action的时候是对所有找到的对象都进行如此动作。



### 文档初始化之后执行的动作

```js
$(document).ready(function(){
   // jQuery methods go here...
});
```

此外我们还常见到一种简化的写法：

```
$(function(){});
```



### 选择元素

一般按照css语法选择元素并没什么好讲的，很是直观，简单看下即可。

#### 特殊符号的元素选择

目前我遇到的情况是 `fn:1` 这个按照jquery是选择不了的，实际上这个用document.querySelect也选择不了，里面有个非法符号`:` ，不过 `document.getElementById` 可以正常选择。

一定要使用jquery的话需要如下加上两个转义符号。

```
$('#fn\\:1')
```

#### 选择多个元素之后迭代

```
$('.footnote-ref').each(function(){

    // $(this)
    
}
```

在迭代过程里面的那个匿名函数里面调用 `$(this)` 就是目标元素。

### 当前节点选择子元素

```
$('sup',this)
```

第二个参数写上 `this` 就是在当前节点下继续选择某个子元素。

#### 选中父元素

```
$('#target1').parent().css('background-color','red');
```

即调用parent方法。

#### 选中子元素

```
$('#right-well').children().css('color','orange');
```

即调用children方法。

#### 选中元素的第几个

```
$('.target:nth-child(2)').addClass('animated bounce');
```

```
$('.target:even').addClass('animated shake');  # 选中元素的偶数个，0 2 4...
```

这个语法实际上来自css的选择语法。

### 获取文本和修改文本

```
$('div').text()  # 获取文本
$('div').text('new text') # 修改文本
```

此外还有 `html()` 方法，其可以写上html标签。

如果使用JavaScript原生的document.querySelect之类的方法，获取到的元素想要看文本可以调用 `textContent` 属性。

### 删除某个元素

```
$('sup',this).remove();
```

即调用remove方法。

### 修改元素的某个属性

```
$(this).attr('data-toggle','popover');
```

### 移除元素的某个属性

```
$(this).removeAttr('href');
```

### class属性修改

#### 添加class

```
div.addClass('highlight'); // 添加highlight这个class
```

#### 删除class

```
div.removeClass('highlight'); // 删除highlight这个class
```

#### 修改css

    $('div').css('background-color', '#ffd351');



### 获取表单value值或修改

```
$('input').val()  # 获取值
$('input').val('new value') # 修改值
```



### 让按钮变为不可选

prop方法设置或返回被选元素的属性。

```
$("button").prop('disabled', true)
```



### 事件绑定动作

```
$(selector).click(function)
```



#### 鼠标事件

-   **click:** 鼠标单击时触发；
-   **dblclick:** 鼠标双击时触发；
-   **mouseenter:** 鼠标进入时触发；
-   **mouseleave:** 鼠标移出时触发；
-   **mousemove:** 鼠标在DOM内部移动时触发 （接受e ，e.pageX是鼠标x值，e.pageY是鼠标Y值）
-   **hover:** 鼠标进入和退出时触发两个函数，相当于mouseenter加上mouseleave。

#### 键盘事件

键盘事件仅作用在当前焦点的DOM上，通常是 `<input>` 和 `<textarea>` 。

-   **keydown:** 键盘按下时触发；
-   **keyup:** 键盘松开时触发；
-   **keypress:** 按一次键后触发。



#### 取消某个事件绑定

```
a.off('click', hello);
```

### 获取屏幕的宽度和高度

```js
var width = $(window).width()
var height = $(window).height()
```

这两个方法更确切的描述是返回所选元素的宽度或高度。此外还有 `innerWidth` 和 `innerHeight` 方法（包含内边距）， `outerWidth` 和 `outerHeight` 包含内边距和边框。

### hide方法

实际上就是css设置 `display:none` 。

```js
$('#test').hide()
```

这样将隐藏所有id为test的元素。

### jquery 动画效果

#### 面板展开和隐藏

```html
<script> 
$(document).ready(function(){
  $(".slidepanel").click(function(){
    $("#panel-one").slideToggle("slow");
  });
});
</script>

<div class="slidepanel" style="background-color:#efefef; padding:5px">滑动面板</div>
<div id="panel-one" style="border:solid 1px #efefef; padding:5px">just jquery it.</div>

```

<div class="slidepanel" style="background-color:#efefef; padding:5px">滑动面板</div>
<div id="panel-one" style="border:solid 1px #efefef; padding:5px">just jquery it.</div>
<script> 
$(document).ready(function(){
  $(".slidepanel").click(function(){
    $("#panel-one").slideToggle("slow");
  });
});
</script>




## ajax

jquery是基于 `XMLHttpRequest` 的，不得不承认jquery的ajax这块写得实在是太好了。

### get

```js
$("button").click(function(){
		$.get("/try/ajax/demo_test.php",function(data,status){
			alert("数据: " + data + "\n状态: " + status);
		});
```
回调函数接受两个参数，传回来的data和状态码。其等价于：

```js
$.ajax({
  url: url,
  data: data,
  success: callback,
  dataType: dataType
});
```

get请求上面的data将附加到url上。

### getJSON

等价于：

```
$.ajax({
  url: url,
  data: data,
  success: callback,
  dataType: json
});
```

注意dataType设置为json

### post

```js
jQuery.post(url,data,success(data, textStatus, jqXHR),dataType)
```
等价于：

```js
$.ajax({
  type: 'POST',
  url: url,
  data: data,
  success: callback,
  dataType: dataType
});
```

上面的data是发送请求发送给服务器的数据。dataType可选，会智能判断服务器响应的数据。

### 跨域问题

参看了 [js跨域](https://segmentfault.com/a/1190000006146207) 这篇文章， `XMLHttpRequest` 是不能跨域的。我们通常所说jsonp，就是一种实现跨域的解决方案，具体我不想太深究，因为一般restful api都是采用的json格式，而除了jsonp之外，服务端如下加上响应头也是可以的：

```
header('Access-Control-Allow-Origin:*');//允许跨域请求的域名，允许全部设为*
header('Access-Control-Allow-Methods:POST,GET');
```



## 其他

### 先网络加载jquery或者本地加载

这里代码的意思应该是先网络加载jquery，如果没有则本地找找看。

```
<script src="https://code.jquery.com/jquery-{{JQUERY_VERSION}}.min.js"></script>

<script>window.jQuery || document.write('<script src="js/vendor/jquery-{{JQUERY_VERSION}}.min.js"><\/script>')</script>

```
