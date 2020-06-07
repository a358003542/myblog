Category: cpp_language
Slug: cpp-language-learning-notes

[TOC]

## 前言

本教程参考 [这个github样例项目](https://github.com/a358003542/cpp_practice) 阅读更方便。

本文假定读者已经学会C语言了，如果没有请先学习C语言，这不冲突的。读者可以参看笔者写的 [C语言学习笔记一文]({filename}../c_language/C语言学习笔记.md) 。



## CPP语言开发环境

CPP语言开发环境还是推荐使用visual studio。



## hello world

```cpp
#include <iostream>

int main(void) {
	using namespace std;
	cout << "hello world!";
	cout << endl;

	return 0;
}
```

## 头文件的扩展名

cpp新的风格头文件是没有扩展名的，比如 `iostream` 就是 iostream ，并没有.h或者.hpp之类的，这样可以使用 `namespace std` 。旧的风格大体类似于C语言带上 `.h` 后缀。

## 命名空间

这个算是和C语言很大的一个不同点了，命名空间这个概念对于熟悉编程的人来说并不是一个默认的概念了，大体类似于python的模块名，一些其他编程语言也有类似的概念。比如：

```cpp
Microflot::hello("hello");
GooGloo::hello("hello");
```

上面一个是调用的命名空间Microflot里面的hello函数，另一个是调用的GooGloo命令空间的hello函数。之前的hello world程序 `using namespace std;` 的话就是如下写的：

```
#include <iostream>

int main(void) {
	//using namespace std;
	std::cout << "hello world!";
	std::cout << std::endl;

	return 0;
}
```

这个有点类似于python里面的 `from what import *` 将里面的函数名等都给导进来了，所以就可以直接使用cin，cout了。此外还有一种推荐的做法是：

```cpp
using std::cout;
using std::endl;
```

这大体类似于python里面的 `from what import cout` ，只是具体导入了某个函数名之类的。

## cout对象

cout是一个对象，其内部有方法知道如何打印字符串。

```
cout << "string";
```

上面代码的过程就是cout对象调用插入运算符 `<<` ，从而执行某个操作将字符串插入到输出流中。

std::endl是一个特殊的C++符号 【换行符？】，将其插入输出流将导致屏幕光标换行。

```cpp
cout << 25;
```

是的， cout可以直接打印int数值。



## 声明变量

cpp这点和c语言最大的区别是cpp是推荐在首次使用变量之前声明它而不是集中在文件开头。

```cpp
#include <iostream>


int main(void) {
	using namespace std;

	int x;
	int y;

	cout << "please input the x value: ";

	cin >> x;
	
	cout << "please input the y value: ";
	cin >> y;

	cout << "x + y = " << x + y << endl;

	return 0;
}
```

cin 和cout相比较之前C语言哪一套实在方便多了，然后我们看到cout可以进行简单的字符串拼接操作。

## 定义函数

```cpp
#include <iostream>

int add(int a, int b) {
    return a + b;
}

int add(int, int);

int main(void) {
    using namespace std;

	int x;
	int y;

	cout << "please input the x value: ";

	cin >> x;

	cout << "please input the y value: ";
	cin >> y;

	cout << "x + y = " << add(x,y) << endl;

	return 0;

}
```

就cpp和c语言的函数定义和函数原型声明这块来说区别不是太大。熟悉C语言的这块简单温习下就好。

## CPP数据类型

整型有：short，int，long 和 long long 。一般没有有说服力的理由就应使用int。

char类型：char类型一般用于存储一个字节大小的字符，但也用于存储比short更小的整型。

bool类型：true or false

符号常量修饰符：const

浮点数类型：float、double、long double。



1．编写一个小程序，要求用户使用一个整数指出自己的身高（单位为英寸），然后将身高转换为英尺和英寸【这里的意思是取整部分为英尺余下部分继续为英寸】。该程序使用下划线字符来指示输入位置。另外，使用一个const符号常量来表示转换因子。

inch2foot.cpp

```cpp
#include <iostream>
#include <cmath>

const int CONVERSION = 12;


int main(void) {
	using namespace std;

	int height_inch;

	cout << "please input your height value in inch: ";

	cin >> height_inch;

	if (height_inch % CONVERSION == 0) {
		cout << "your height value is " << height_inch / CONVERSION
			<< " foots." << endl;
	}
	else {
		cout << "your height value is " << height_inch / CONVERSION
			<< " foots and " << height_inch % CONVERSION << "inchs." << endl;
	}

	return 0;

}
```



3．编写一个程序，要求用户以度、分、秒的方式输入一个纬度，然后以度为单位显示该纬度。1度为60分，1分等于60秒，请以符号常量的方式表示这些值。对于每个输入值，应使用一个独立的变量存储它。下面是该程序运行时的情况：

![img]({static}/images/programming/cpp_xiti_1.png)

to_degress.cpp

```cpp
#include <iostream>
#include <cmath>

const float CONVERSION = 60;


int main(void) {
	using namespace std;

	int degrees;
	int minutes;
	int seconds;
	float result;

	cout << "Enter a latitude in degrees, minutes, and seconds:" << endl ;

	cout << "First, enter the degrees: ";
	cin >> degrees;

	cout << "Next, enter the minutes of arc: ";
	cin >> minutes;

	cout << "Finally, enter the seconds of arc: ";
	cin >> seconds;

	result = degrees + minutes / CONVERSION + seconds / (CONVERSION * CONVERSION);

	cout << degrees << " degrees, "  << minutes << " minutes, " << seconds << " seconds = " <<
			result
			<< " degrees." << endl;
	

	return 0;

}
```



5．编写一个程序，要求用户输入全球当前的人口和美国当前的人口（或其他国家的人口）。将这些信息存储在long long变量中，并让程序显示美国（或其他国家）的人口占全球人口的百分比。该程序的输出应与下面类似：

![img]({static}/images/programming/cpp_xiti_2.png)

usa_population.cpp



```cpp
#include <iostream>
#include <cmath>


int main(void) {
	using namespace std;

	long long word_population;
	long long usa_population;
	float population_ratio;

	cout << "Enter the world's population: ";

	cin >> word_population;

	cout << "Enter the population of the US: ";
	cin >> usa_population;

	population_ratio = (float)usa_population / word_population * 100;

	cout << "The population of the US is " << population_ratio << "% of the world population." << endl;

	return 0;

}
```



7．编写一个程序，要求用户按欧洲风格输入汽车的耗油量（每100公里消耗的汽油量（升）），然后将其转换为美国风格的耗油量—每加仑多少英里。注意，除了使用不同的单位计量外，美国方法（距离/燃料）与欧洲方法（燃料/距离）相反。100公里等于62.14英里，1加仑等于3.875升。因此，19mpg大约合12.4l/100km，27mpg大约合8.71/100km。

to_usa_mpg.cpp

```cpp
#include <iostream>
#include <cmath>

int main(void) {
	using namespace std;

	float eu_fuel;
	int usa_mpg;

	const float KILOMETER_CONVERT_MILES = 0.6214;
	const float GALLON_CONVERT_LITERS = 3.875;

	cout << "Please input how many your car use fuel[unit liter] on running 100 kilometers: ";

	cin >> eu_fuel;

	usa_mpg = (int)(100 * KILOMETER_CONVERT_MILES) / (eu_fuel / GALLON_CONVERT_LITERS);

	cout << "The mpg your car in usa standard is : " << usa_mpg << endl;

	return 0;

}

```

 

long totals[500] = {0};  //初始化一个500个元素的数组，索引为0的元素设值为0，其他元素自动设值为0。

你也可以如下：

long totals[500] = {} ; // 这样所有元素都自动设值为0。

字符串类型，C严格意义上来说并没有所谓的字符串类型，C语言风格的字符串这里略过讨论了，C++添加了string类，你需要包含头文件string，然后就可以如下使用string类了。

```
string str1;
str1 = "abc";
```

熟悉C语言风格字符串使用的一下就看出一个巨大的区别了，那就是这里可以直接初始化字符串变量，不需要操作数组长度之类的东西了，非常好的改进！

然后C语言风格的字符串不可以将一个字符串的值赋值给另一个字符串，但是string类可以如下做：

```
string str1;
string str2 = "abc";
str1 = str2;
cout << str1 + str2;
```

你还可以用加法来进行字符串拼接，终于，类似python的那些基本字符串操作在C语言那边还要让人头疼好久这里终于顺畅一些了。

```
cout << str1.size(); // 返回3
```





## 参考资料

1. C++ Primer Plus 第六版中文版