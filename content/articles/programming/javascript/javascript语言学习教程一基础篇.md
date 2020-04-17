Category: javascript

[TOC]

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



## 程序中的操作对象

### 简介

javascirpt的数据类型分为两类，一类是原始类型：数值、字符串和布尔值；另一类是对象类型。此外javascript还有两个特殊的值：`null` 和 `undefined` 。javascript除了数值、字符串、布尔值、null、undefined之外就都是对象了。比如后面提到的数组，函数也都是对象，只不过其是javascipt内部定义的对象。

### 声明常量和变量

javascript可以利用关键词 `var` ， `const` 和 `let` 来声明变量，其中const是声明常量的，var和let是声明变量的，其中var声明变量是大家在javascript中常用的声明变量关键词。其声明的变量的作用域很不同于其他编程语言，叫做 **函数作用域** 。即你在函数区块内声明的变量整个函数体都是可以使用的，包括哪些花括号结构或任意的嵌套函数。因为程序员对于变量的作用域习惯了块作用域，所有airbnb提出不推荐使用 `var` ，而是推荐使用 `let`，因为 `const` 和 `let` 都是块作用域（block-scoped）。对于此我持保留意见，因为javascript本身就是一个很宽松的语言，是否一定要遵从程序员那些习以为常的惯例，然后当作教条我决定大可不必。

### 全局变量

在网页中有个全局对象 `window` ，所以我们可以把一些全局变量挂在 `window` 对象里面。

### 数值(number)

**javascript不区分整数值和浮点数值**，javascript中所有数字都用浮点数值表示，这是javascript和其他编程语言的很大不同。然后数值型那些运算，比如加减乘除之类的就不用多说了。其中 `%` 和python一样也是求余操作。在python3中有 `5//2` 是求商的概念，javascript没有这个概念，我们需要如下来获得类似的效果。

```
console.log(parseInt(5/2))
```

#### parseInt()

将字符串转成整数型，否则返回NaN。

```js
parseInt('123', 10); // 123
parseInt('11', 2); // 3
```

#### parseFloat()

将字符串转成浮点型，否则返回NaN。

```js
parseFloat('3.14') 
3.14
```

NaN也属于number型，判断是否是NaN，airbnb推荐的风格是：

```js
Number.isNaN('a')
false
Number.isNaN(1)
false
Number.isNaN(NaN)
true
```



### 字符串(string)

javascript同python一样单引号和双引号都是可以的，airbnb规范是推荐使用 **单引号** 。

```javascript
const name = 'Capt. Janeway';
```

你可以通过 `+` 来实现一些简单的字符串拼接工作，然后aribnb规范提出字符串的程序性拼接推荐使用模块语言，也就是 `${variable}` ，这是很好的（注意必须用**`**符号）。

```javascript
`How are you, ${name}?`
```

javascript的字符串类型和python非常类似，比如 `string[0]` 是支持的。然后不可以这样用string[0:2]，幸运的是javascript提供了类似python中的那种切片概念，就是使用 `slice` 方法

```
console.log("hello".slice(0,2))
console.log([1,3,4,5].slice(0,2))
```

不过javascript的slice方法和python的切片操作还是有点区别的，其只有 `(start,end)` 两个参数，然后其也有负数从末尾算起的概念，不过其不会倒着来，都是从左到右的那种顺序。具体请参看 [这里](http://www.w3school.com.cn/jsref/jsref_slice_string.asp) 。



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
Boolean({})
true
```

### null

javascript的 `null` 。其是一个特殊值。类似于python的 `None` ，然后还有一个什么 `undefined` 。比如函数没有明确return值就会默认返回 `undefined` ，感兴趣的可能查一下这两个的区别，我看了一下，觉得挺无聊的。上面谈到 `==` 和 `===` 的区别，如果用 `===` ，则 `undefined` 是不等于 `null` 的，如果用 `==` ，则javascript会额外做一些类型转换工作，这两个又会看作相等的。

ECMA-262 规定：

```
null == undefined; -> return true
```

按照airbnb的推荐风格，比较操作的时候一律推荐使用 `===`  和 `!==`  ，而不要使用 `==` 和 `!=` 。



### typeof操作符

查看某个对象的对象类型，typeof操作符只可能返回以下六种结果，比如说前面提到的数组是属于object的；null也是属于object的。

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

### 构建一个数组

```js
var array1 = [];
var array2 = new Array();
const items = [1, 2, 3.14, 'Hello', null, true];
```

其索引index编号法则也和python一致。

### 数组的一些方法

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

### 比较两个数组是否相同

参考了 [这个网页](http://stackoverflow.com/questions/3115982/how-to-check-if-two-arrays-are-equal-with-javascript) 。

```js
function arraysEqual(a, b) {
if (a === b) return true;
if (a == null || b == null) return false;
if (a.length != b.length) return false;

// If you don't care about the order of the elements inside
// the array, you should sort both arrays here.

for (var i = 0; i < a.length; ++i) {
if (a[i] !== b[i]) return false;
}
  return true;
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

### 判断某个元素是否在数组中

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





### object

javascript的object其大体可以看作python中的字典类型。

创建空的object推荐如下写法：

```javascript
const item = {};
```

或者：

```javascript
const person = {
  name: 'Bob',
  age: 20,
  tags: ['js', 'web', 'mobile'],
  city: 'Beijing',
  zipcode: null
};
```
aribnb提出属性名直接写上就是了，包括函数也是如此：

```javascript
const lukeSkywalker = 'Luke Skywalker';
const obj = {
  lukeSkywalker,
};
```

然后函数可以先通过function声明，或者直接写进去：

```javascript
const atom = {
  value: 1,

  addValue(value) {
    return atom.value + value;
  },
};
```

然后还有一些属性名在javascript里面是非法的，那么当然只好用单引号包围起来了。

#### 动态生成对象属性名

```js
const obj = {
  id: 5,
  name: 'San Francisco',
  [getKey('enabled')]: true,
};
```



#### in语句
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

aribnb提出相关的一些建议，我持保留意见，可能是python出身，个人更喜欢in语句。

```javascript
// good
console.log(Object.prototype.hasOwnProperty.call(object, key));
```



#### shallow copy

```js
const original = { a: 1, b: 2 };
const copy = { ...original, c: 3 }; // copy => { a: 1, b: 2, c: 3 }
```



## 函数

一个简单的函数定义和使用如下所示（下面这种写法是airbnb规范推荐的风格）:
```javascript
let greeting = function(name){
	console.log(name);
}
greeting('hello')
```
我们看到javascript明确将函数名作为一个变量，这是唯一要值得注意的，不过你也可以采用这种写法，这样更加为我们所熟悉了:

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

简单来说箭头函数就是 lambda 表达式的更简洁写法，只是说在javascript语境里面其区别一般function的特点有：<u>其没有this绑定</u>。

```js
(param1, param2, …, paramN) => { statements }
```



## 逻辑

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



## this关键词

这个有点类似于python中的self，在javascript里面，object里面定义的方法， `this` 指向的就是本对象的实例。



面向对象传统写法

```js
function Point(x, y) {
  this.x = x;
  this.y = y;
}

Point.prototype.toString = function () {
  return '(' + this.x + ', ' + this.y + ')';
};

var p = new Point(1, 2);
```

新式写法
```js
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



如果 this 在函数里面，如：

```
function (){
    this.x = 1;
}
```

那么指定的是当这个函数要运行的时候，具体调用这个函数的对象。

比如说某个函数将这样被调用： `jquery对象.what` 那么这个函数里面的this就是指定的那个jquery实例，通常也就是网页里面的某个标签元素。






## 集合

javascript中的集合Set大体也和python中的集合概念相近。

var s1 = new Set(); // 空Set
var s2 = new Set([1, 2, 3]); // 含1, 2, 3

然后其也有 `add` 方法用于添加一个元素。用 `delete` 方法来删除某个元素。



##  三元运算符

```
test ? expression1 : expression2
```

