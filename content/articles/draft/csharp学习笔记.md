Title: csharp学习笔记
Slug: csharp-learning-notes
Date: 2019-12-22
Tags: csharp
Status: draft

[TOC]



## 简介

C# 采用 **统一的类型系统**。 所有 C# 类型（包括 `int` 和 `double` 等基元类型）均继承自一个根 `object` 类型。

## 程序结构

C# 中的关键组织结构概念包括**程序**、**命名空间**、**类型**、**成员**和**程序集**。 C# 程序由一个或多个源文件组成。 程序声明类型，而类型则包含成员，并被整理到命名空间中。 类型示例包括类和接口。 成员示例包括字段、方法、属性和事件。 编译完的 C# 程序实际上会打包到程序集中。 程序集通常具有文件扩展名`.exe`或`.dll`，具体取决于它们是否实现**应用程序**或**库**。



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





## 字符串

### 字符串内插

```c#
$"hello {name}";
```

- Length 属性 返回字符串长度
- TrimStart 方法 去除字符串前面的空格
- TrimEnd 方法 去除字符串后面的空格
- Replace 方法 子字符串替换动作
- ToUpper 方法  英文字母都转成大写
- ToLower 方法 英文字母都转成小写
- Contains 方法 查看某个子字符串是否存在
- StartsWith 方法 字符串是否以某个子字符串开始
- EndsWith 方法 字符串是否以某个子字符串结束



## 数字

### 除法和求余或取模

如果是浮点型除法【即除法中至少有一个是浮点型数】，那么和我们理解的除法是没有区别的。

如果是整型间的除法，则除法 `/` 可以看做求商动作；然后求余或者取模是 `%` 。

```
5 / 3 = 1
5 % 3 = 2
```

### decimal类型

decimal可容许最大值是高于int的，然后低于double，但是比double更加的精确。确切来说和钱相关的数值，一分一厘都不容许出错的是一定要用decimal类型的。

```c#
double x = 10000000000000000000;
x++;
Console.WriteLine(x);
Console.WriteLine(double.MaxValue);

decimal y = 10000000000000000000;
y++;
Console.WriteLine(y);
Console.WriteLine(decimal.MaxValue);
Console.WriteLine(int.MaxValue);
```

下面按照微软官网的教程会介绍下基本程序结构和列表集合。





OK，speed up。好了，基本的入门和大致的了解就到这里了，开始阅读c#语言规范。按照c#语言规范对c#语言有了一个更加全面的了解之后，后面就是针对更多的细节在应用中慢慢的了解了。











