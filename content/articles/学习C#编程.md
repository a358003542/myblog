

[TOC]



## 简介

C# 程序运行在.net平台上的，在介绍C#语言之前需要介绍下.net平台。对于.net平台内部的细节和微软的设计雄心之类的我们没必要去深究，简单来说.net平台提供了一个运行时，在这个运行时之下你可以运行.net应用。.net应用五花八门并可以跨多个平台，然后开发.net应用的程序员还需要下载.net sdk。熟悉JAVA语言的对这个运行时和SDK的概念不会很陌生，所不同的是.net平台还封装了一个中间语言层，然后才是上面具体的语言的编译器，也就是.net平台是支持多个编程语言的，当然包括这里谈论的C#语言。

Unity游戏开发就是构建在.net平台之上的，这也是笔者学习C#语言的原因。

### 开发环境

笔者还是推荐安装visual studio，然后通过visual studio来安装.net开发环境。具体就是 `.NET桌面开发` 工作负载。



### 基本语言特性

C# 采用 **统一的类型系统**。 所有 C# 类型（包括 `int` 和 `double` 等基元类型）均直接或间接继承自一个根 `object` 类型。



## helloworld

1. 创建新项目
2. 选择控制台应用(.net core)【.net core就是上面谈及的.net平台的运行时，此外还有.net framwork等。.net framework只支持windows系统，.net core支持多个操作系统，微软对.net framework处于待遗弃状态，visual studio2019，C#8，.net core3.0 这几个关键词需要了解下，它们是同一时间发布的。以后微软计划将各个.net平台运行时合并为一个——.net5。】
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

- `using` 导入某个命名空间，这里暂时将其理解为C++的命令空间，后面再看看有何差异。
- `namespace` 本命名空间的名字
- `class` 声明一个类
- `static void Main...` 这是定义一个类的方法，Main方法比较特殊，为本程序的入口方法
- `Console.WriteLine` 调用打印方法 



### 常量和变量

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

### 除法和求余或取模

如果是浮点型除法【即除法中至少有一个是浮点型数】，那么和我们理解的除法是没有区别的。

如果是整型间的除法，则除法 `/` 可以看做求商动作；然后求余或者取模是 `%` 。

```
5 / 3 = 1
5 % 3 = 2
```

### 注释

C#的注释单行是 `//` ，多行是 `/*...*/` 。

### 练习题

1. 定义一个常数 double pi
2. 定义半径 double r
3. 计算该半径的面积并报告结果。



## 类型系统

正如前面演示的 `int x = 1;` ，这个int就是一个类型声明，C#在这个变量类型声明赋值上语法和很多语言是类似的，不过具体类型系统各个语言就不一样了，有时甚至差异很大的。

### value type

C#有两种变量类型，value type直接存储变量的值，reference type存储的是对目标数据的引用。

value type变量赋值给另外一个变量，其值是copy过去的。比如说

```
int a = 50;
int b = a;
a = 20; //这个时候a是20而b则是50
```



#### 简单类型

- sbyte short **int** **long**
- byte ushort unit ulong
- **char**
- **float** **double** 
- decimal
- **bool**

#### 枚举类型

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

#### 结构体类型

C#里面的结构体和C++里面的结构体差异巨大，C++里面的结构体概念和C语言的结构体区别不大，只是一种比数组略灵活点的变量类型，专门用来存储呈现一定结构特征的数据用的。而C#里面struct则更接近于class这个概念，有一些小的使用上的区别，其他都大同小异，其中最大的一个区别是struct是类型是value type，而class的类型是reference type。

比如下面这个例子，C#里面的struct一样也可以有自己的构造方法：

```c#
struct Coordinate
{
    public int x;
    public int y;

    public Coordinate(int x, int y)
    {
        this.x = x;
        this.y = y;
    }
}

Coordinate point = new Coordinate(10, 20);
```

但需要注意的是**C#的struct不能再定义无参构造方法**，因为它默认已经有了。当然struct没有继承关系。

完整的struct不能class能的清单如下：

- You can't declare a parameterless constructor. Every structure type already provides an implicit parameterless constructor that produces the [default value](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/default-values) of the type.
- You can't initialize an instance field or property at its declaration. However, you can initialize a [static](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/static) or [const](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/const) field or a static property at its declaration.
- A constructor of a structure type must initialize all instance fields of the type.
- A structure type can't inherit from other class or structure type and it can't be the base of a class. However, a structure type can implement [interfaces](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/interface).
- You can't declare a [finalizer](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/destructors) within a structure type.



#### null

reference type变量的默认值就是null。

#### Tuple



### reference type

reference type变量赋值给另外一个变量，它们两个都是指向的同一数据对象。但string情况略有不同，因为string是不可变的，所以string发生变化实际上是又新建了一个string。

#### class

#### string

字符串，不可变的reference type类型。值得一提的是C#的字符串不需要以`\0` 结尾。

字符串内插和常用的字符串方法有：

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

#### object

C#的所有类型都直接或间接继承自object。读者可能会问int不是value type吗，其继承自object，而object则是reference type，这怎么回事。这涉及到什么 Boxing and Unboxing 的概念。

将一个object转成value type称之为unboxing过程，反之是boxing过程。value type存储在堆栈stack里面的，reference type存储在堆heap里面的。boxing过程先需要将value type里的value取出存入heap，然后获得heap的reference指向。而unboxing过程是从heap里面将对应值取出来然后存放入stack。

下面是boxing过程：

```
int i = 123;
object o = i;
```
下面是unboxing过程：
```
o = 123;
i = (int)o;  
```



#### interface

#### array

C#的Array不能对比为C语言或C++的数组，和C++的array类有点类似：

```
std::array<int, 3> a2 = {1, 2, 3};
```

上面的写法转成C#是：

```
int[] a2 = {1,2,3};
```

但也只是类似，就底层实现细节可以按照传统概念上的数组来思考理解，而就具体程序上来说其是一个对象，还有很多额外的方法支持。

声明一个array如下所示：

```
elementType[] name = new elementType[numberOfElements];
```

#### delegate



## 访问权限控制

经常看到 `public int x = 1;` ，这个public就是访问修饰符，控制该变量的访问权限的：

- public 访问权限无限制，只有声明public的变量你才能在unity 编辑器上看到。
- private 访问权限限于本类，C#中没有访问权限修饰符的变量声明默认是private。
- protected 访问权限限于本类或本类的子类
- internal 访问权限限于本汇编（exe或dll）
- protected internal
- private internal



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





## class

C#的class类只允许单继承，也就是最多只能继承自一个父类。一般类的声明和使用和C++类似：

```
public class Character
{
    public string name;
    public int exp = 0;

    public Character(string name)
    {
        this.name = name;
    }
}

Character hero = new Character("lucy");
```

### this

this关键词类似于python里面的self，和C++上的this大体含义也是一样的，是一个指向本类实例的指针。同样在本类里面定义的方法下面都默认带入了this这个参数，也就是在各个方法里面直接使用即可。



### 继承

C#就继承上的概念和写法和C++相比很类似，不过就语法书写层面会更友好一点，比如提供了base关键词对父类的引用，还有概念上简化，只允许有一个父类，此外还有一些C#代码和C++代码上的通用差异。除开这些，我们仍然可以从C#的继承和构造方法编写中看到C++的影子。比如下面的 `: base(name)` 在C++那边具体叫做成员初始化列表写法，也就是 `base(name)` 里面的name这个参数是直接来自 `Paladin(string name)` 接受到的参数name的。

```c#
public class Paladin : Character
{
    public Paladin(string name): base(name)
    {
    
    }

}
```

### virtual和override

C++就多态这个议题从C++11开始也有virtual和override这两个关键词了，不过都不是强制性的，正因为不是强制性的，所以引出很多问题。比如不使用virtual，如果你的子类声明的时候采用的是子类引用变量或者子类指针，那么使用的方法都将是基类的。而引入virtual这个关键词会根据实例的类型来决定使用的方法。override在C++那边更多的是一个规避bug的写法，表明你的子类的这个方法是要重载基类的某个方法，因为有时一不注意，参数类型没对上，重载行为就会无意跳过去。

在C#这边virtual和override用来描述OOP面向对象编程的多态概念是推荐的标准写法了。

简单来说就是基类的方法要加上virtual，子类的方法要加上override表明这里有重载行为。

```c#
    // base class
    public virtual void printStatusInfo()
    {
        Debug.LogFormat("Hero: {0} - {1} EXP", this.name, this.exp);
    }
    
    // derived class
    public override void printStatusInfo()
    {
        Debug.LogFormat("Paladin: {0} - take up your weapon: {1}", this.name, this.weapon.name);
    }
```



## 属性值的get和set写法

```c#
    private string _name;
    public string Name{
    get {
        return _name;
    }
    set {
        _name = value;
    }
    
    }
```





## 参考资料

1. [microsoft docs: a tour of csharp](https://docs.microsoft.com/en-us/dotnet/csharp/tour-of-csharp/)
2. learning C# programming by Marius Bancila and Raffaele Rialdi and Ankit Sharma







