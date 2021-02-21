

[TOC]



## 简介

C# 采用 **统一的类型系统**。 所有 C# 类型（包括 `int` 和 `double` 等基元类型）均继承自一个根 `object` 类型。

C# 程序运行在.net环境上。



## 开发环境

1. 安装visual studio
2. 选择安装 `.NET桌面开发`



## helloworld

1. 创建新项目
2. 选择控制台应用(.net core)
3. 生成->生成解决方案
4. 调试->开始调试

```c#
using System;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
        }
    }
}
```

- `using` 导入某个命名空间
- `namespace` 本命名空间的名字
- `class` 声明一个类
- `static void Main...` 这是定义一个类的方法，Main方法比较特殊，为本程序的入口方法
- `Console.WriteLine` 调用打印方法 



## 常量和变量

```c#
const double pi = 3.14;
```

这是声明了一个常量，常量之后不可修改。

```c#
double x = 5.0;

int y;
y = 5;
```

这是声明了一个变量。

常见的变量类型有：

- string 字符串 `string x = "abc";`
- char 单字符型 `char x = 'a';`
- int 整型 `int x = 1;`
- double 浮点型 `double x = 1.0;`

### 强制类型转换

低精度到高精度可以自动转没问题，高精度到低精度需要明确强制类型转换：

```c#
int x;
double y = 3.0;
x = (int)y;
```







## 数字

### 除法和求余或取模

如果是浮点型除法【即除法中至少有一个是浮点型数】，那么和我们理解的除法是没有区别的。

如果是整型间的除法，则除法 `/` 可以看做求商动作；然后求余或者取模是 `%` 。

```
5 / 3 = 1
5 % 3 = 2
```



## 注释

C#的注释单行是 `//` ，多行是 `/*...*/` 。



## 类型系统

正如前面演示的 `int x = 1;` ，这个int就是一个类型声明，C#在这个变量类型声明赋值上语法和很多语言是类似的，不过具体类型系统各个语言就不一样了，有时甚至差异很大的。

### value type

#### 简单类型

- sbyte short int long
- byte ushort unit ulong
- char
- float double 
- decimal
- bool

#### 枚举类型

#### 结构体类型

#### null

#### Tuple



### reference type

#### class

#### interface

#### array

#### delegate





## 访问权限控制

经常看到 `public int x = 1;` ，这个public就是访问修饰符，控制控制该变量的访问权限的：

- public 访问权限无限制，只有声明public的变量你才能在unity 编辑器上看到。
- private 访问权限限于本类，C#中没有访问权限修饰符的变量声明默认是private。
- protected 访问权限限于本类或本类的子类
- internal 访问权限限于本汇编（exe或dll）
- protected internal
- private internal



## 字符串内插和常用的字符串方法

```c#
$"hello {name}";
```

此外你还可以使用 `"abc" + "def"` 加法来组合字符串。

- Length 属性 返回字符串长度
- TrimStart 方法 去除字符串前面的空格
- TrimEnd 方法 去除字符串后面的空格
- Replace 方法 子字符串替换动作
- ToUpper 方法  英文字母都转成大写
- ToLower 方法 英文字母都转成小写
- Contains 方法 查看某个子字符串是否存在
- StartsWith 方法 字符串是否以某个子字符串开始
- EndsWith 方法 字符串是否以某个子字符串结束



## 隐式类型声明

```
var x = 1;
```

C#是强类型语言，上面的语句只是说让编译器来决定该变量的类型。



## 变量的作用域

类似于C++等语言，C#也有变量作用域这个概念，同样的简单表述就是块作用域，具体就是某个花括号块或者方法区块或者类区块，在这些区块类声明的变量，可在本区块内直接访问，区块外则不行。

## 编写方法

C#有点特殊，因为其一切皆对象的设定，按照程序界的标准术语，那么在C#就没有所谓的编写函数，而只有编写方法这个说法了。

```
accessModifier returnType methodName(parameterType parameterName){
    // do something
}
```

访问修饰符如果省略类似于变量声明那边，默认是private。



## switch语句

switch语句在C#这边和C++那边差异很大，C++的switch语句的目标测试变量必须是整型或者枚举类型或者能够转成整型或枚举类型的class。而C#那边之前支持的类型就很多，现在是任何非null表达式都行。比如下面就是直接对字符串是否相等然后进行switch，这在C++那边是不行的。

```c#
            string x = "xxxx";
            switch (x)
            {
                case "hello":
                    Console.WriteLine("HELLO");
                    break;
                default:
                    Console.WriteLine("default");
                    break;
            }
```

C#switch语句和C++还有一个不同，那就是它从语法层面是禁止这种写法的：

```
                case "hello":
                    Console.WriteLine("HELLO");

                case "world":
                    Console.WriteLine("world");
                    break;
```

C++那边也不推荐这种写法，但并没有禁止，如果这样写的话，C++那边hello的case激活之后没有break会继续下面的case语句执行，这确实很不好，即使是C++也应该避免这种写法。

## 枚举类型

C#的枚举类型和C++的enum class有点接近，但在使用上略有差异。

比如C++的下面语句：

```
enum class Color { red, green, blue };
Color color = Color::blue;
```

转成C#应该是：

```
enum Color { red, green, blue };
Color color = Color.blue;
```

具体到枚举类型的内部细节，和C语言的枚举类型是一脉相承。

## Array

C#的Array不能对比为C语言或C++的数组，和C++的array类有点类似：

```
std::array<int, 3> a2 = {1, 2, 3};
```

上面的写法转成C#是：

```
int[] a2 = {1,2,3};
```

但也只是类似，就底层实现细节可以按照传统概念上的数组来思考理解，而就具体程序上来说其是一个对象，还有很多一些额外的方法支持。

声明一个array如下所示：

```
elementType[] name = new elementType[numberOfElements];
```

## lambda表达式

```
(input-parameters) => expression
```



## List

C#的List类型与C++的vector类更接近，其仍然要求内部存储的元素为相同的类型，所以不能对标python的列表。因为和array相比list可以更加灵活地增删元素所以很多情况下会更好用，使用它需要加载 `System.Collection.Generic` 。

```c#
using System;
using System.Collections.Generic;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            List<int> nums = new List<int>();

            nums.Add(1);
            nums.Add(2);
            nums.Add(5);

            nums.ForEach((num) => Console.WriteLine(num));
        }
    }
}
```

此外还有Insert方法，RemoveAt和Remove方法等。

- `.Count` 返回List的元素数

## Dictionary

Dictionary类型声明语句如下所示，就是类似于python语言的dict类型。

```
Dictionary<keyType, valueType> name = new Dictionary<keyType, valueType>();
```

```c#
using System;
using System.Collections.Generic;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            Dictionary<string, int> dict = new Dictionary<string, int>();

            dict.Add("a", 1);
            dict.Add("b", 2);
            dict.Add("c", 3);

            foreach (KeyValuePair<string, int> item in dict)
            {
                Console.WriteLine($"{item.Key}: {item.Value}");
            }
        }
    }
}
```

Dictionary引用值和修改值语句：`dict["a"]` 或者 `dict["a"]=3` ，这种引用值写法如果分配一个key原字典没有则会新增。

此外还有 ContainsKey方法来确认某个key是否存在。

还有Remove方法用于删除某个key。



## foreach语句

C#的foreach语句在C++那边可以类比for range语句或者就是python的for语句：

```C++
for (int x: {1,2,3}){
    cout << x;
}
```

C#的foreach语句写法是：

```c#
foreach (var x in new int[] { 1, 2, 3 }){
    Console.WriteLine(x);
}
```

## class

C#的class类只允许单继承，也就是最多只能继承自一个父类。



## 参考资料

1. [microsoft docs: a tour of csharp](https://docs.microsoft.com/en-us/dotnet/csharp/tour-of-csharp/)







