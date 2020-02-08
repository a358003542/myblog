Title: C语言学习笔记
Date: 2019-08-28
Modified: 2019-08-28

[TOC]

## C语言开发环境

windows下推荐使用visual studio，虽说是C++开发环境，不过因为C++是C语言的超集，所以同样也是支持的。具体就是选择新建空的C++项目，然后添加项的时候记得把默认的后缀 `.cpp` 改为 `.c` 。



## helloworld

最简单最简单的版本：

```c
#include <stdio.h>
int main(void){
  printf("hello world.\n");
}
```

就是定义了一个函数，这个函数名比较特殊，叫做 `main` ，是默认程序的入口函数名。然后利用printf函数打印了一个字符串，而这个printf函数需要你引入stdio这个包。

下面这个版本稍微做了一些修改：相比较一般的helloworld程序多了个system函数，主要是让屏幕暂停一下，否则屏幕会一闪而过，我们会看不清具体打印了什么字。

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
	printf("hello world!\n");
	system("pause");
	return 0;
}
```

按照C11的标准推荐main函数采用这样的写法：

```c
int main(void){

}
```

## 头文件

C语言从源码到可执行程序 在各个操作系统平台上具体细节各有不同，但总会分为编译阶段【将C语言代码转成汇编语言代码】和 链接阶段【将汇编语言代码汇总】，现在我们关注编译阶段即可。

编译阶段也就是C语言编译器处理你写的C语言源码的过程，在这个过程中，C语言编译器会进行很多工作，一般推荐将这些和C语言编译器相关的工作代码汇总写入头文件中。

我们看到的 `#` 开头的命令都是C语言编译器的预处理过程相关的命令，比如 `#include` 。

### 定义宏

`#define` 命令定义了一个宏，其实就是一个简单的C语言编译器预处理阶段的文本替换操作，比如：

```c
#define PI 3.14
```

这里需要提醒一点的是，这个PI并不是后面C语言中讨论的常量或者变量，它就是一个文本替换操作，比如：

```c
printf("The PI is %f \n", PI);
```

实际上源码经过预处理之后是：

```c
printf("The PI is %f \n", 3.14);
```

这点和python这类动态语言有很大不同。

### 编写自己的头文件

首先我们新建一个 `consts.h` 头文件，里面的内容就是： 

```c
#define PI 3.14
```

然后我们新建一个 `myhead.h` 头文件，内容如下：

```c
#include <stdio.h>
#include <stdlib.h>
#include "consts.h"
```

上面两个包反正后面应该经常遇到，这里先一并包含进来了。

然后我们的主程序 `main.c` 就是：

```c
#include "myhead.h"

int main(void) {
	printf("The PI is %f \n", PI);
	system("pause");
	return 0;
}
```

读者一定注意到 `#include` 后面写法上有点差异，简单来说尖括号包围的主要是标准库或者系统标准目录里面能够找到的；而双引号包围的先从当前目录寻找，找不到再在标准系统目录下找，具体各个操作系统标准目录定义这里略过讨论了。

## 自己定义函数

helloworld程序里面包含了很多信息，至少对于刚接触C语言的读者来说是的。看完helloworld程序，读者就应该知道C语言函数的写法了：

```c
return_type function_name(function_parameters){
    // this is a comment.
    /* this is also a comment.*/
    return 0;
}
```

具体更多的细节后面再慢慢讨论，其实C语言是一个很简单的语言。

C90新增了函数原型的概念，比如：

```c
int add(int a, int b) {
	return a + b;
}
```

的函数原型是：

```c
int add(int a, int b);
```

函数原型也叫做函数声明，告诉编译器正在使用某个函数，所以函数声明语句一般放在头文件中。

## 基本数据类型

| name   | 说明     | printf输出            |
| ------ | -------- | --------------------- |
| int    | 整型     | %d                    |
| float  | 浮点型   | %f 【%e对应指数表示】 |
| char   | 单字符型 | %c                    |
| long   | 长整型   | %ld                   |
| double | 双浮点型 | %f 【%e对应指数表示】 |
| _Bool  | 布尔型   | %d                    |

C语言的char单字符型是用单引号表示的：

```c
char a = 'a';
```

C99新增了_Bool也就是布尔型，其实际上也是一种整数型，0表示false；1表示true。



### 自动类型转换

C语言遇到不同数据类型运算，会发生自动类型转换的情况有 char -> int  int -> double ，当然也包括 char -> double 。

### 强制类型转换

```
(int)(3.14)
```

强制类型转换不影响原变量，是运算时的截取操作，不是四舍五入。



## 计算最大公约数

### 除法和求余数

下面主要演示下除法和求余数，其他加法减法乘法还是很直白的。

```text
	float x = 12.2;
	float y = 2;
	
	float z = x / y;
	// 一般除法
	printf("z is: %f.\n", z);
	
	int w = 13 % 2;
	// 求余数
	printf("w is: %d.\n", w);
```

取余数： `a % b` 和  `b % a` 总是返回 a和b这两个数中的最小或者更小的数，其中假设a比b大，那么 `a % b` 相当于 a - b 多次得到一个正数， 而 `b % a` 则直接返回 最小的 b。

### 欧几里得算法

本小节主要参考了维基百科的 欧几里得算法，这里程序不是很复杂，关键是理解算法思想。欧几里得算法最核心的思想是：

> 两个数的最大公约数等于相对较小的那个数和两个数的差的最大公约数。



简要证明如下：

```text
a = mk
b = nk
a和b的最大公约数是k，所以m和n互质
于是有：
a-b = (m-n)k
b = nk 
现在的任务就是要证明m-n 和n是互质的，反证，假设 m-n 和 n 不是互质的，则有：
m-n = ix
n = iy
于是：
m = n+ ix = i(x + y)
我们得 m 与 n 是可以同时被i整除的，这和之前的m和n互质假设违背，
于是我们得到 m-n 和 n是互质的，于是进一步得到:
a-b 和 b的最大公约数也是 k。
```

以上过程可以记作：

```
gcd(a, b) = gcd(b, (a-b))
```

因为 b是小的， a-b 也是小的，整个过程会逐步让这两个数越来越小。

举例： 

```
36 ~ 9 =>  27 ~9 =>  18 ~ 9 =>  9~9 =>  0
```

下面用递归的写法可能是最直观的写法了，基本上就是上面定义的程序实现：

```c
int gcd(int a, int b) {
	if (b == 0) {
		return a;
	}
	else {
		return gcd(b, a % b);
	}
}
```

其中`a % b` 取余保证了其实最小或者更小的那个数，这是没有问题的。

另外辗转相除法，网上实现也已经有了：

```c
int gcd2(int a, int b) {
	int t; // 只是一个临时变量,记录最小值
	while (b) { // b最小值成为零了返回a
		t = a % b; // t记录取余后的最小值
		a = b; // a记录最大值
		b = t; // b记录最小值
	};
	return a;
}
```





## 如何打印百分号

```
printf("%%")
```

## 字符串数据类型



## 字符串操作

字符串确切来说是一个字符型数组，以 `'\0'` 结束，比如 "sam" 实际存储的值如下所示：

```c
void print_name(void) {
	char name[4];
	name[0] = 's';
	name[1] = 'a';
	name[2] = 'm';
	name[3] = '\0';

	printf("name is %s\n", name);
}
```

将字符串作为变量推荐采用如下指针的风格：

```c
void print_one(void) {
	char * first_name = "Gustav";
	char * second_name = "Mahler";
	printf("%s %s\n", first_name, second_name);
}

void print_two(char * name, char * address) {
	printf("your name is: %s\n", name);
	printf("your address is: %s\n", address);
}
```










## 参考资料

1. C Primer Plus 第六版中文版
2. Practical C programming Steve Oualline
3. 菜鸟教程