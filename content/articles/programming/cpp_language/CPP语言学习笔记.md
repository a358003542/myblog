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



---



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

请求行输入因为历史原因 cin.getline(charstr, max_size) 更接近于我们在C语言中熟知的那种概念，而友元函数 getline(cin, string) 反而更接近C++风格，因为cin是C++里面的概念，所以人们会预期cin的类方法会对接string接口，但这只是历史要兼容的原因罢了，并没什么特别的理由要弄得这样反常规。

C++里面的结构就基本的东西来说和C语言里面的讨论是没有太大区别的，C++里面的结构体当然也可以将string类作为成员对象。特别要强调的是C语言里面字符串数组实际上并没有所谓的字符串这个基本内存存储单元，因为字符串不定长，所以字符串数组实际下面存放的是指针，但是结构数组不同，C语言的结构体是如此基本，它就可以看做一个基本的内存存储单元，所以结构数组下面就是一个一个结构体而不是指向结构体的指针。因此结构体数组的引用语句是 `struct_array[0].name` 。

C++里面的Union和enum枚举和C语言里面的讨论也没有太大区别。

C++里面的指针还有相关内存管理malloc之类的等等和C语言里面的讨论也没有太大区别，不过需要注意的是C++编程一定程度上弱化了指针的概念，很多地方C++编程不一定要使用指针的，然后内存管理也不推荐使用malloc函数而是推荐使用new和delete运算符。

对于C++的基本类型和结构可以如下使用new来声明一个内存块，然后用给定的指针名来指向它，引用它和使用它。

```
typeName * pointer_name = new typeName;

int * pn = new int;
*pn = 1;
cout << *pn;
```

这个东西只能通过该指针来使用，参考资料1说这个东西更确切来说应该叫做数据对象，变量也是数据对象。不管怎么说，就是指内存里的那个东西。

delete运算符只能用于那些也就是上面讨论的new出来的指针。具体如下所示：

```
int * pn = new int;
delete pn;
```

使用new来创建数组和结构和其他又有所不同，以数组为例，常规声明数组叫做静态联编（static binding），即在编译阶段已经为该数组申请分配好内存了；而通过new来创建的数组只在后面运行阶段才可能创建，也就是运行阶段如果没使用这个数组也不会创建，这称为动态联编（dynamic binding）。这种数组叫做动态数组。

下面例子演示了其为何叫做动态数组，我们可以运行时用户指定该数组大小，然后运行时给定值：

```cpp
#include <iostream>
#include <string>

int main(void) {
	using namespace std;

	int x;

	cout << "please input the array length: ";
	cin >> x;

	int* parray = new int[x];

	for (int i = 0; i < x; i++) {
		cin >> parray[i];
	}

	for (int i = 0; i < x; i++) {
		cout << parray[i] << endl;
	}

	delete[] parray;

	return 0;
}
```

**注意new出来的动态数组 delete 运算符语句加上了 [] 。**

具体指针的使用C语言里面的东西了，这里可以回顾提醒一下， `arr[1]` 和 `*(arr+1)` 是一个意思， `arr[0]` 和 `*arr` 是一个意思。

关于指针和数组这块东西很多的，但因为都是C语言里面的知识点，我这里就略过讨论了，如果读者自觉在这块还有所欠缺，请在C语言教材对应的部分补习之。

也可以使用new一个动态的字符串，或者说动态字符数组，但这完全没有必要。因为string类内部也就是这样做的，你没必要去重复造轮子了，直接使用string类就是了。

使用new出来的结构参照前面的讨论，类似的叫做动态结构。这里的动态结构倒不是说结构的定义动态，结构体的定义还是要做的。

C语言里面就存储类型有自动存储和静态存储，简单来说自动存储变量的存活是程序自动管理的，而静态存储变量在整个程序运行期都是存活的。这一块C++和C语言是一致的，不同的是C++因为上面讨论的new运算符而提出了一个新的存储类型，叫做动态存储。具体new和delete运算符管理的内存池和静态变量和自动变量的内存池是分开的，其叫做自由存储空间或堆。如果new出来的动态存储变量没有delete，这叫做内存泄漏，内存泄露一般只是本程序那些内存没法用了，然后严重点本程序运行的内存被耗尽了，因为没有内存程序崩溃了。参考资料说这种严重的泄漏甚至导致操作系统或其他应用程序崩溃。

类似string类，C++用vector类来实现动态数组，类似上面的string类的讨论，如果你要自己利用new和delete来实现某种动态数组的效果，那么不要重复造轮子了，请用vector类，vector类内部就是这样做的。下面将上面动态数组的例子写成vector版本：

```cpp
#include <iostream>
#include <string>
#include <vector>


int main(void) {
	using namespace std;

	int x;

	cout << "please input the array length: ";
	cin >> x;

	vector<int> vec;

	for (int i = 0; i < x; i++) {
		int tmp;
		cin >> tmp;
		vec.push_back(tmp);
	}

	for (int i = 0; i < x; i++) {
		cout << vec[i] << endl;
	}

	return 0;
}
```

vector类还有很多其他用法，但在这里不是重点。我们看到vector初始化不需要指定长度参数了，其通过push_back方法来新增元素。

vector类因为是动态数组，所以效率有点低，C++又实现了一个新的类array类，其内部存储和原来的数组存储风格一致，所以效率等价，然后因为是类，所有多了一些便捷的操作方法。这些方法后面有时间再慢慢了解。



---



编写一个C++程序，如下述输出示例所示的那样请求并显示信息：

![img]({static}/images/programming/cpp_xiti_c4_1.png)

注意，该程序应该接受的名字包含多个单词。另外，程序将向下调整成绩，即向下调一个字母。

xiti_c4_1.cpp

```cpp
#include <iostream>
#include <string>

int main(void) {
	using namespace std;

	string first_name;
	string last_name;
	char grade;
	int age;

	cout << "What is your first name? ";
	getline(cin, first_name);

	cout << "What is your last name? ";

	getline(cin, last_name);

	cout << "What letter grade do you deserve? ";
	cin.get(grade).get();

	cout << "What is your age? ";

	cin >> age;

	cout << "Name: " << last_name << ", " << first_name << endl;
	cout << "Grade: "; 
	cout.put(grade + 1);
    cout << endl;
	cout << "Age: " << age << endl;

	return 0;
}
```



编写一个程序，它要求用户首先输入其名，然后输入其姓；然后程序使用一个逗号和空格将姓和名组合起来，并存储和显示组合结果。请使用char数组和头文件cstring中的函数。下面是该程序运行时的情形：

![img]({static}/images/programming/cpp_xiti_c4_2.png)



xiti_c4_3.cpp

```cpp
#include <iostream>
#include <cstring>

int main(void) {
	using namespace std;

	char first_name[20];
	char last_name[20];
	char name[40];


	cout << "What is your first name? ";
	cin.getline(first_name, 20);

	cout << "What is your last name? ";

	cin.getline(last_name,20);

	strcpy_s(name, last_name);
	strcat_s(name, ", ");
	strcat_s(name, first_name);

	cout << "Here's the information in a single string: " << name << endl;

	return 0;
}
```



结构CandyBar包含3个成员。第一个成员存储了糖块的品牌；第二个成员存储糖块的重量（可以有小数）；第三个成员存储了糖块的卡路里含量（整数）。请编写一个程序，声明这个结构，创建一个名为snack的CandyBar变量，并将其成员分别初始化为“Mocha Munch”、2.3和350。初始化应在声明snack时进行。最后，程序显示snack变量的内容。

xiti_c4_5.cpp

```cpp
#include <iostream>
#include <string>

using namespace std;

struct CandyBar {
	string name;
	float weight;
	int calories;
};

int main(void) {
	CandyBar snack = {
		"Mocha Munch",
		2.3,
		350
	};

	cout << "CandyBar " << snack.name << " weight: " << snack.weight <<
		" and calories: " << snack.calories << endl;

	return 0;
}
```

结构CandyBar包含3个成员，如上面讨论的。请编写一个程序，创建一个包含3个元素的CandyBar数组【使用new来动态分配数组，而不是声明一个包含3个元素的CandyBar数组】，并将它们初始化为所选择的值，然后显示每个结构的内容。

xiti_c4_6.cpp

```cpp
#include <iostream>
#include <string>

using namespace std;

struct CandyBar {
	string name;
	float weight;
	int calories;
};

int main(void) {

	CandyBar* psnack = new CandyBar[3];

	psnack[0].name = "aaa";
	psnack[0].weight = 2.3;
	psnack[0].calories = 5;

	psnack[1] = {
		"bbb",
		2.5,
		6
	};

	psnack[2] = {
		"ccc",
		2.6,
		7
	};

	for (int i = 0; i < 3; i++) {
		cout << "CandyBar " << psnack[i].name << " weight: " << psnack[i].weight <<
			" and calories: " << psnack[i].calories << endl;
	}


	delete[] psnack;

	return 0;
}
```

William Wingate从事比萨饼分析服务。对于每个披萨饼，他都需要记录下列信息：

披萨饼公司的名称，可以有多个单词组成。
披萨饼的直径。
披萨饼的重量。
请设计一个能够存储这些信息的结构【请使用new来为结构分配内存，请使用vector来实现动态数组】，并编写一个使用这种结构变量的程序。程序将请求用户输入上述信息，然后显示这些信息。请使用cin（或它的方法）和cout。

xiti_c4_7.cpp

```cpp
#include <iostream>
#include <string>
#include <vector>


using namespace std;

struct Pizza {
	string name;
	float diameter;
	float weight;
};

int main(void) {
	int x;

	cout << "please input the array length: ";
	(cin >> x).get();

	vector<Pizza *> vec;

	for (int i = 0; i < x; i++) {
		Pizza* ppizza = new Pizza;

		cout << "Please input your pizza name: ";
		
		getline(cin, ppizza->name);

		cout << "Please input your pizza diameter: ";
		(cin >> ppizza->diameter).get();

		cout << "Please input your pizza weight: ";
		(cin >> ppizza->weight).get();

		cout << "-----------------" << endl;

		vec.push_back(ppizza);
	}


	for (int i = 0; i < x; i++) {
		cout << "CandyBar " << vec[i]->name << " weight: " << vec[i]->diameter <<
			" and calories: " << vec[i]->weight << endl;
	}

	for (int i = 0; i < x; i++) {
		delete vec[i];
	}

	return 0;
}
```



## CPP程序逻辑

这块C++和C语言内容基本上没什么区别，所以大多略过了，然后主要做一些习题也算是对前面学到的东西的再应用。



## CPP函数

我估计这块应该C++和C语言差异也不会太大，主要做一些习题练习下。



## CPP类



## 附录

### cin详解

- `cin >>` 遇到Enter Space Tab 即结束，适合char，无空格的string和单个值的int float之类的输入。需要注意的是经过个人实践换行符还是在缓冲区的，为了把这个缓冲区消掉获得更好的输入体验，一般采用这种表达方式：`(cin >> what).get()` ，这是因为 `cin >> what` 会返回cin对象，然后继续调用下面的 get 方法来消掉最后的换行符。
-  `cin.get`  和 `cin.getline`  都可以用于字符数组的行输入，不同的是 get方法不会丢弃缓冲区的换行结束符，此外cin.get还有一个重载变体，`cin.get(char &ch)` ，用于读取第一个字符，假设缓冲区下一个字符是换行符，然后在遇到 `cin.get()`  则将把那个换行符读取下来。
- getline函数 ，和cin.getline的区别就是 `getline(cin, string)` getline会读入到C++的string类，而不是C风格的字符数组。

### cout详解

- `cout <<` 一般使用
- `cout.put(char &ch)`  输出一个字符，如果输入的整型也会正常显示该字符。

## 参考资料

1. C++ Primer Plus 第六版中文版