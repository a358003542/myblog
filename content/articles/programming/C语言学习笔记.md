Title: C语言学习笔记
Date: 2020-02-10
Modified: 2020-02-10

[TOC]

## 前言

本教程参考 [这个github样例项目](https://github.com/a358003542/HelloWorldC) 阅读更方便。



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

首先我们新建一个 `myhead.h` 头文件，里面的内容就是： 

```c
#include <stdio.h>
#include <stdlib.h>

#define PI 3.14
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

### 头文件里面加入函数原型

继续之前的描述，我们在 `myhead.h` 文件里面加上：

```c
int add(int a, int b);
```

然后我们新建一个 `myhead.c` 文件，加入函数定义：

```c
int add(int a, int b) {
	return a + b;
}
```

`main.c` 里面直接使用你定义的add函数即可。

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

## 基础知识继续

加减乘除就不说了，虽然各个语言各有不同，简单了解下即可。

### sizeof函数

```
sizeof(int)
```

返回目标对象的bytes大小，具体返回的是 `size_t` 类型，实际上就是 `unsigned int` 类型：

```c
typedef unsigned int size_t;
```

### 使用布尔值

推荐使用stdbool包，其让bool称为_Bool的别名，此外你还可以使用true和false。不要再使用0和1来表示布尔值了。

```c
int is_input_integer(void) {
	int input_len;
	char input[100];
	bool input_is_good = true;

	printf("Please enter an integer: ");
	scanf("%s", input);

	input_len = strlen(input);

	for (int i = 0; i < input_len; i++) {
		char test_char;
		test_char = input[i];
		if (!isdigit(test_char)) {
			input_is_good = false;
		}
	}

	return input_is_good;
}

```

```c
int main(void) {
	bool res;
	res = is_input_integer();
	if (res) {
		printf("yes it is a integer");
	}
	else {
		printf("no it is not a integer");
	}
	return 0;
}
```

### fabs函数

fabs函数在 `math.h` 库里面，其接受一个浮点数，返回该浮点数的绝对值。

### 规范for循环语句

python语言因为引入可迭代对象的概念使得for循环语句非常的简单，其他常规语言的for语句一般都建议在写法上遵循如下规范：

```c
for (int i=0; i< obj_length; i++){

}
```

1. 对目标对象的索引计数按照规范都是从0开始
2. 终止判断是小于目标对象的索引长度

按照这种标准写法，将形成一个对目标对象从索引0到最后一位的循环。

### getchar函数和putchar函数

这两个函数来自 `stdio.h` 库，一个是接受一个字符；一个是打印一个字符，相当于scanf和printf针对字符的精简mini版本。

```c
ch = getchar();
putchar(ch);
```

### ctypes.h库

ctypes.h 库提供了一些关于单个字符测试的函数：

- isalnum 是否是字母或者数字
- isalpha 是否是字母
- isblank 是否是空白字符【空格 水平制表符 换行符或其他本地化的空白字符】
- isdigit 是否是数字
- islower 是否是小写
- isupper 是否是大写
- isspace 是否是空白字符【空格 换行符 换页符 回车符 垂直制表符 水平制表符或其他本地化的空白字符】
- isprint 是否是可打印字符
- ispunct 是否是标点符号

此外还有转换字符函数：

- tolower 转成小写字母
- toupper 转成大写字母





## 字符串数据类型

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

C语言数组初始化是支持这样的形式写法的：

```c
void print_name2(void) {
	char name[4] = {'s','a','m','\0'};
	printf("name is %s\n", name);
}
```

然后C语言的数组在初始化的时候是支持自动计算数组大小的，所以上面的代码还可以简化为：

```c
void print_name3(void) {
	char name[] = { 's','a','m','\0' };
	printf("name is %s\n", name);
}
```

然后我们之前看到的双引号括起来的内容叫做 *字符串常量* ，其进入编译器会自动加上 `\0` 字符。字符串常量用法如下：

```c
void print_name4(void) {
	char name[] = "sam";
	printf("name is %s\n", name);
}
```

编译器在遇到字符串常量之后会将其存入内存，只存一次，存储在静态存储区。程序在遇到上面代码，会新建一个name数组，然后才实际将静态存储区里面的字符串常量数据拷贝过来。然后C语言还有一种利用指针的表示方法：

```c
void print_name5(void) {
	char * name = "sam";
	printf("name is %s\n", name);
}
```

这个时候是将字符串常量的地址拷贝给指针，也就是内存里面并没有两个拷贝。

从上面的分析看的出来数组就是数组，指针就是指针，这并没有什么好纠结的，不过似乎大家总喜欢讨论数组名是不是指针，虽然在使用上似乎有一些相似，最简单的回答就是不是，数组名里面存放的地址是固定的，而指针里面存放的地址是可以随意变动的。没什么好纠结。

关于两种表达的选择，参考资料1给出的建议就是如果你的字符串需要修改操作，那么应该使用数组表达方式。

### strlen函数

strlen函数由 `<string.h>` 包提供，它会返回字符串的长度。

### printf函数

#### 转换说明

- %d 整型
- %ld long长整型
- %o 八进制整数
- %x 十六进制整数
- %f 浮点型 十进制
- %e 浮点型 e记数法
- %c 单字符
- %s 字符串
- %p 指针
- %% 打印一个百分号

printf函数具体格式字符串类似于python的format，里面内容挺丰富的，这个可以后面再慢慢了解。下面列出几个简单的实用例子：

- "%3.1f" 打印一个浮点数，字符串宽度3，小数点后有效位数1位。
- "%10d" 打印一个整数，字符串宽度10，不足的部分左侧为空白。
- "%010d" 打印一个整数，字符串宽度10，不足的部分左侧填充为0。 



### scanf函数

在visual studio里面使用scanf会抛出错误：

```c
C4996	'scanf': This function or variable may be unsafe. Consider using scanf_s instead. To disable deprecation, use _CRT_SECURE_NO_WARNINGS. See online help for details.	
```

需要在 `myhead.h` 里面加上一行 ：

```c
#define _CRT_SECURE_NO_WARNINGS
```

scanf函数的使用就两条：

1. 读取基本变量类型的值，变量名前面要加上 `&`
2. 读取字符串到字符数组，不要使用 `&` ，直接使用数组名即可。

```c
char name[40];
scanf("%s", name);
```

scanf函数可以接受多个输入，以空白为分隔，直到读取到指定的数目为止。不过 `%c` 会把空白也作为字符读取进来。

#### 转换说明

- %c 字符型
- %d 整型
- %e %f 都会转成浮点型
- %p 指针
- %s 字符串

scanf函数也类似printf支持格式修饰符，不过scanf函数用的并不是特别多，实践中推荐使用 `getchar` 和 `fgets` 这两个函数。

#### 返回值

scanf函数的返回值：

- 如果成功读取，则返回读取的项数【比如请求输入一个%d，则返回1】
- 如果没有读取到任何项或者用户输入不合乎规范则返回0,
- 如果scranf检测到EOF文件结尾，则返回EOF【-1】



## 指针

指针是一个存储内存地址的变量。int类型存储的是整数，pointer类型存储的内存地址。指针声明如下：

```
int * p;
```

*表示该变量是个指针，int表示该指针指向的地址上的值是一个int值。

### 相关运算符

`&` 运算符是用于获得某个变量的内存地址； `*` 运算符用于根据某个内存地址或者指针名来获得该指针指向地址上的值。

### swap函数

swap函数接受两个变量的值，然后交换这两个变量的值，这个函数在C语言里面的实现必须要用到指针。

```c
void swap(int * p1, int * p2) {
	int temp;
	temp = *p1;
	*p1= *p2;
	*p2 = temp;
}
```

```c
int main(void) {
	int x = 2;
	int y = 3;
	swap(&x, &y);
	printf("%d %d", x, y);
	return 0;
}
```

如果函数只是处理值那么是不应该使用指针参数的，只有在目标函数需要实际改变外围调用环境中的变量的值，则可以采用这种指针参数的形式。

C Primer Plus的这段说的非常的好：

>普通变量把值作为基本量，把地址作为通过 `&` 运算符获得的派生量；而指针把地址作为基本量，把值作为 `*` 运算符获得的派生量。

现在我们假设p1指针指向变量x，那么： 

```
x = 1;
```

和 

```
*p1 = 1;
```

可以看做等价的，所以当我们说某个指针指向某个变量，其暗含的意思即 `*p` 这个名字是 `x` 另外一个别名。

## 数组

### 多维数组

C语言是直接支持用这样的形式 `matrix[3][4]` 来表示多维数组的，这个值得说明一下。

 ```c
	int x[3][2] = {
		{1,2},
		{1,2},
		{1,2}
	};
 ```

本来打算编写一个简单的函数先打印二维数组，然后竟发现还不是很方便。首先一维数组的情况怎么的都行，数组名你就可以看做一个指针：

```c
int print_1d(int* arr, int length) {
	for (int i = 0; i < length; i++) {
		printf("%d ", arr[i]);
	}
}
```

二维数组就不存在这种数组名和指针的无缝转换了，你必须建立一种二维指针数组，这个过程引入了太多的复杂度，实在不是一个明智的选项；而且就算是这样你在建立函数的时候，二维数组的列数也必须写死。同时我又了解到 `变长数组` 的概念，但是这个 变长数组 visual studio 现在是不支持的，而且似乎也没有支持的计划，而且这个特性最新的C语言标准也是打算废弃的意思了。

此外我在 [这个网页](https://solarianprogrammer.com/2019/03/27/c-programming-passing-multi-dimensional-array-to-function/) 了解到一种通过 malloc 函数 自动分配二维指针数组内存的方法，当然其内在本质还是依靠二维指针数组这个过于复杂的东西，个人不喜欢，尤其这种玩法还引入了 `int ** p` 这种东西，C语言的指针已经让大家很厌倦了，你还弄两个指针，显然这种玩法过于复杂现在不应该推荐了。

但我还是发现了唯一的解决方案，而这个方案利用的C语言的struct结构，个人觉得是优美的解决方案【也许你觉得里面的一维表达很丑，但实际上计算机内存里面存储的就是这种一维表达结构】。如果采取这种方案那么就应该抛弃C语言里面 `x[3][2]` 这样的表达，而回归一维数组的本源，然后继而可以扩展一些支持方法来进一步表达分组分行等内部属性。

```c
typedef struct {
	int rows;
	int cols;
	int data[];
} Matrix2D;

void print_2d(Matrix2D* m) {
	printf("[\n");
	for (int i = 0; i < m->rows; ++i) {
		printf("  [");
		for (int j = 0; j < m->cols; ++j) {
			printf("%3d ", m->data[i * m->cols + j]);
			if (!(j == (m->cols-1))) {
				printf(",");
			}
			else {
				printf("]");
			}
		}
		printf("\n");
	}
	printf("]\n");
}

```

```c
int main(void) {
	Matrix2D x = {
		.rows = 3,
		.cols = 4,
		.data = { 1,2,3,4,5,6,7,8,9,10,11,12 }
	};

	print_2d(&x);

	return 0;
}
```





## 参考资料

1. C Primer Plus 第六版中文版
2. Practical C programming Steve Oualline
3. 菜鸟教程