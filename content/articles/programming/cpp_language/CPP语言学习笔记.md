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

### 头文件的扩展名

cpp新的风格头文件是没有扩展名的，比如 `iostream` 就是 iostream ，并没有.h或者.hpp之类的，这样可以使用 `namespace std` 。旧的风格大体类似于C语言带上 `.h` 后缀。

### 命名空间

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

### cout对象

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



### 声明变量

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

### 定义函数

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

## 数据类型

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

**注解：** `%` 是取模运算，整数之间的除法是取商运算。

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

**注解：** 本例主要演示了const定义常数项的用法。

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

**注解：** 本例主要演示了如何进行强制类型转换。

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

**注解：** 一般字符可以直接cout，但如果类型已经是int型了，那么希望输出对应的字符则需要使用`cout.get`。

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

**注解：** 本例主要了解下C风格的字符数组用法。

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

**注解：** 本例主要演示了结构体的用法。

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

**注解：** 本例主要演示了如何new一个结构体。

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

**注解：** 本例主要演示了vector的用法。



## 程序逻辑

这块C++和C语言内容基本上没什么区别，所以大多略过了，然后主要做一些习题也算是对前面学到的东西的再应用。

C++的for语句多了一个新的下面这种形式，这个要了解下：

```cpp
for (int x: {1,2,3}){
    cout << x;
}
```

这个熟悉python语言等高级语言的知道这是迭代遍历循环操作，然后后面可以是数组或者vector或者array。

关于cin的用法请看下面的演示例子，主要是这个补充知识点：cin.get获取字符之后返回的仍是cin对象，其如果在bool取值环境，如果读取成功则返回true，如果读取失败则返回fasle。读取失败也包括常规的EOF结尾情况。

```cpp
#include <iostream>


int main() {
	using namespace std;

	char ch;
	int count = 0;

	cout << "Enter characters:\n";

	while (cin.get(ch)) { //Ctrl+Z 
		cout << ch;
		++count;
	}

	cout << endl << count << endl;

	return 0;
}
```



1．编写一个要求用户输入两个整数的程序。该程序将计算并输出这两个整数之间（包括这两个整数）所有整数的和。这里假设先输入较小的整数。例如，如果用户输入的是2和9，则程序将指出2～9之间所有整数的和为44。

xiti_c5_1.cpp

```cpp
#include <iostream>


int main() {
	using namespace std;

	int start_int;
	int end_int;
	int sum = 0;
	cout << "please input the start integer: ";

	cin >> start_int;

	cout << "please input the end integer: ";
	cin >> end_int;


	for (int n = start_int; n <= end_int; n++) {
		sum += n;
	}

	cout << "the integer in range " << start_int << " - " << end_int << " summation is " << sum << endl;


	return 0;
}
```

**注解：** 本例主要演示了如何写for语句。

3．编写一个要求用户输入数字的程序。每次输入后，程序都将报告到目前为止，所有输入的累计和。当用户输入0时，程序结束。

xiti_c5_3.cpp

```cpp
#include <iostream>


int main() {
	using namespace std;

	
	int temp;
	int sum = 0;

	do {	
		cout << "please input a number, input 0 quit : ";
		cin >> temp;
		sum += temp;
	} while (temp);

	cout << "your input number summation is " << sum << endl;


	return 0;
}
```

**注解：** 本例演示了do-while语句。

5．假设要销售《C++ For Fools》一书。请编写一个程序，输入全年中每个月的销售量（图书数量，而不是销售额）。程序通过循环，使用初始化为月份字符串的char *数组（或string对象数组）逐月进行提示，并将输入的数据储存在一个int数组中。然后，程序计算数组中各元素的总数，并报告这一年的销售情况。

xiti_c5_5.cpp

```cpp
#include <iostream>


int main() {
	using namespace std;

	int sum = 0;

	string months[12] = { "jan","feb","march","april","may","june","july","august","september","october","november","december" };
	int sales[12] = {};

	int count = 0;
	for (string month : months) {
		cout << "please input the sale of amount in " << month << " : ";
		cin >> sales[count];

		count++;
	}

	for (int x : sales) {
		sum += x;
	}
	cout << "this year's sale amount is: " << sum << endl;

	return 0;
}
```

**注解：** 本例主要演示了如何使用新式的for语句。

6．完成编程练习5，但这一次使用一个二维数组来存储输入—3年中每个月的销售量。程序将报告每年销售量以及三年的总销售量。

xiti_c5_6.cpp

```cpp
#include <iostream>


int main19() {
	using namespace std;

	int sum_all = 0;

	string months[12] = { "jan","feb","march","april","may","june","july","august","september","october","november","december" };
	int sales[3][12] = {};

	for (int i = 0; i < 3; i++) {
		int count = 0;
		int sum_year = 0;

		for (string month : months) {
			cout << "please input year " << i << " the sale of amount in " << month << " : ";
			cin >> sales[i][count];

			sum_year += sales[i][count];

			count++;
		}

		cout << "this year "<< i << "all sale amount is: " << sum_year << endl;

		sum_all += sum_year;
	}

	cout << "the three year all sale amount is: "<< sum_all  << endl;

	return 0;
}
```

**注解：** 本例主要演示了二维数组的用法。

10．编写一个使用嵌套循环的程序，要求用户输入一个值，指出要显示多少行。然后，程序将显示相应行数的星号，其中第一行包括一个星号，第二行包括两个星号，依此类推。每一行包含的字符数等于用户指定的行数，在星号不够的情况下，在星号前面加上句点。该程序的运行情况如下：

![img]({static}/images/programming/xiti_c5_10.png)

xiti_c5_10.cpp



```cpp
#include <iostream>

int main20() {
	using namespace std;

	int rows;

	cout << "Enter number of rows: ";

	cin >> rows;

	for (int i = 0; i < rows; i++) {
		for (int j = i+1; j < rows; j++) { //here we can not use the if statement.
			cout << ".";
		}

		for (int j = 0; j < i+1; j++) {
			cout << "*";
		}

		cout << endl;
	}


	return 0;
}
```

**注解：** 需要注意本例不能使用if语句，所以才有上面的写法。

下面这个例子中 cin >> fish[i] 返回cin对象，其bool值含义是如果获取输入成功则返回true，如果获取输入失败则返回false。

cinfish.cpp

```cpp
#include <iostream>


const int Max = 5;

int main() {
	using namespace std;


	double fish[Max];

	cout << "fish #1: ";
	int i = 0;

	while (i < Max && cin >> fish[i]) {
		if (++i < Max) {
			cout << "fish #" << i + 1 << ": ";
		}
	}
	double total = 0;
	for (int j = 0; j < i; j++) {
		total += fish[j];
	}
	if (i == 0) {
		cout << "No fish\n";
	}
	else {
		cout << "average weight is " << total / i;
	}

	return 0;
}
```

cinfish2.cpp

下面例子类似上面也是一个和用户交互请求输入数字的例子，不同的是上一个如果用户输入有误则退出，而这一个如果用户输入有误程序会继续请求用户输入。所以上一个例子是演示的不定数目的输入情况，而这一个演示的是如何处理用户输入有误时候的情况。为了和上面的例子进行比较我尽可能让这两个例子基本结构变动不大。

```cpp
#include <iostream>


const int Max = 5;

int main() {
	using namespace std;

	double fish[Max];

	cout << "fish #1: ";
	int i = 0;

	while (i < Max) {
		while (!(cin >> fish[i])) { //failed for input
			cin.clear();
			while (cin.get() != '\n') { //clear the wrong input line
				continue;
			}
			if (i < Max) {
				cout << "fish #" << i + 1 << ": ";
			}
		}
		i++;
		if (i < Max) {
			cout << "fish #" << i + 1 << ": ";
		}
	}

	double total = 0;
	for (int j = 0; j < i; j++) {
		total += fish[j];
	}
	if (i == 0) {
		cout << "No fish\n";
	}
	else {
		cout << "average weight is " << total / i;
	}

	return 0;
}
```

**注解：** `cin.clear()` 是让cin在遇到错误输入之后可以继续开始接受输入。后面的while语句是清空缓存区那一行错误输入。

下面这个例子演示了如何写入文件：

outfile.cpp

```cpp
#include <iostream>
#include <fstream>

int main() {
	using namespace std;

	char automobile[50];

	int year;
	double a_price;
	double d_price;

	ofstream outFile;
	outFile.open("carinfo.txt");

	cout << "Enter the make and modle of automobile: ";
	cin.getline(automobile, 50);

	cout << "Enter the model year: ";

	cin >> year;

	cout << "Enter the original asking price: ";
	cin >> a_price;

	d_price = 0.913 * a_price;

	cout << fixed; // 
	cout.precision(2); //
	cout.setf(ios_base::showpoint);
	cout << "Make and modle: " << automobile << endl;
	cout << "Year: " << year << endl;
	cout << "Was asking $" << a_price << endl;
	cout << "Now asking $" << d_price << endl;


	outFile << fixed;
	outFile.precision(2);
	outFile.setf(ios_base::showpoint);
	outFile << "Make and modle: " << automobile << endl;
	outFile << "Year: " << year << endl;
	outFile << "Was asking $" << a_price << endl;
	outFile << "Now asking $" << d_price << endl;
	outFile.close();


	return 0;
}
```

具体在新建一个ofstream对象之后，通过open方法将输出流和目标文件联系起来，然后剩下来的动作和使用cout没有区别，最后记得把文件输出流调用close方法关闭。

```
ofstream outFile;
outFile.open("carinfo.txt");

....

outFile.close();
```

- precision方法  控制输出流浮点数的精度
- `setf(ios_base::showpoint)` 显示浮点数小数点后面的零



1．编写一个程序，读取键盘输入，直到遇到@符号为止，并回显输入（数字除外），同时将大写字符转换为小写，将小写字符转换为大写（别忘了cctype函数系列）。

xiti_c6_1.cpp

```cpp
#include <iostream>
#include <cctype>

int main26() {
	using namespace std;

	char ch;

	while (cin.get(ch)) {
		if (ch == '@') {
			break;
		}
		else if (isdigit(ch)) {
			continue;
		}
		else if (isupper(ch)) {
			cout.put(tolower(ch));
		}
		else if (islower(ch)) {
			cout.put(toupper(ch));
		}
		else {
			cout.put(ch);
		}
	}

	return 0;
}
```

3．编写一个菜单驱动程序的雏形。该程序显示一个提供4个选项的菜单——每个选项用一个字母标记。如果用户使用有效选项之外的字母进行响应，程序将提示用户输入一个有效的字母，直到用户这样做为止。然后，该程序使用一条switch语句，根据用户的选择执行一个简单操作。该程序的运行情况如下：

![img]({static}/images/2020/xiti_c6_3.png)

xiti_c6_3.cpp

```cpp
#include <iostream>

using namespace std;
void help();

void help() {
	cout << "c) carnivore              p) pianist\n" <<
		"t) tree                   g) game\n";
}



int main() {

	cout << "Please enter one of the following choices:\n";

	help();

	char ch;

	(cin >> ch).get();

	bool quit = false;

	while (!quit) {
		quit = true;
		switch (ch) {
		case 'c':
			cout << "A maple is a carnivore";
			break;
		case 'p':
			cout << "A maple is a pianist";
			break;
		case 't':
			cout << "A maple is a tree";
			break;
		case 'g':
			cout << "A maple is a game";
			break;
		default:
			cout << "Please enter a c, p, t, or g: ";
			(cin >> ch).get();
			quit = false;

		}
	}


	return 0;
}
```

5．在Neutronia王国，货币单位是tvarp，收入所得税的计算方式如下：

5000 tvarps：不收税

5001～15000 tvarps：10%

15001～35000 tvarps：15%

35000 tvarps以上：20%

例如，收入为38000 tvarps时，所得税为5000 0.00 + 10000 0.10 + 20000 0.15 + 3000 0.20，即4600 tvarps。请编写一个程序，使用循环来要求用户输入收入，并报告所得税。当用户输入负数或非数字时，循环将结束。

xiti_c6_5.cpp



```cpp
#include <iostream>

int calc_tax(int);

int calc_tax(int x) {
	float tax = 0;
	int temp = 0;

	temp = x - 35000;
	if (temp > 0) {
		tax += (temp * 0.2);
		x -= temp;
	}

	temp = x - 15000;
	if (temp > 0) {
		tax += (temp * 0.15);
		x -= temp;
	}

	temp = x - 5000;
	if (temp > 0) {
		tax += (temp * 0.10);
		x -= temp;
	}

	return tax;
}

int main() {
	using namespace std;

	int tvarps = 0;
	int count = 0;

	do {
		if (tvarps < 0) {
			break;
		}

		if (count != 0) {
			cout << "your income tax is " << calc_tax(tvarps) << " tvarps.\n";
		}
		count += 1;

		cout << "please input how many tvarps of your income: ";
	} while (cin >> tvarps);


	return 0;
}
```

8．编写一个程序，它打开一个文件文件，逐个字符地读取该文件，直到到达文件末尾，然后指出该文件中包含多少个字符。

xiti_c6_8.cpp



````cpp
#include <iostream>
#include <fstream>

int main() {
	using namespace std;

	string filename;

	cout << "Please input the filename you want to open: ";

	cin >> filename;

	ifstream inFile;

	inFile.open(filename);
	// check the file is open
	if (!inFile.is_open()) {
		cout << "Could not open the file " << filename << endl;
		exit(EXIT_FAILURE);
	}

	char ch;
	int count = 0;
	while (inFile.get(ch)) {
		count++;
	}

	cout << "This file contains " << count << " characters.\n";

	inFile.close();

	return 0;
}
````



## 函数

我估计这块应该C++和C语言差异也不会太大，主要做一些习题练习下。

### 数组作为函数的参数

数组作为函数的参数实际传递的是该数组的首地址，但C++还需要知道这个数组内元素的类型，所以你在函数原型声明的时候应该类似这样进行声明： `int sum_arr(int * arr, int n)` ，或者 `int sum_arr(int arr[], int n)` ，这两种写法在函数原型声明上是没有区别的，告诉C++编译器该数组内的元素类型就完成任务了。如果函数不应该修改数组里面的内容，那么应该在声明前面加上 `const` 关键字。

可以通过下面这个例子来加深对数组作为函数的参数的理解：

arrfun.cpp

```cpp
#include <iostream>

const int Max = 5;

int fill_array(double ar[], int limit);
void show_array(const double ar[], int size);
void revalue(double r, double ar[], int n);
double sum_array(const double* ar_begin, const double* ar_end);

int main(){
	using namespace std;

	double properties[Max];

	int size = fill_array(properties, Max);

	show_array(properties, size);

	if (size > 0) {
		cout << "Enter revaluation factor: ";
		double factor;
		while (!(cin >> factor)) {
			cin.clear();
			while (cin.get() != '\n') continue;
			cout << "Bad input; Please enter a number: ";
		}

		revalue(factor, properties, size);
		show_array(properties, size);
		
		double total;
		total = sum_array(properties, properties + size);
		cout << "array total sum = " << total << " .\n";
	}

	return 0;
}


double sum_array(const double* ar_begin, const double* ar_end) {
	const double* pt;
	double total = 0;

	for (pt = ar_begin; pt != ar_end; pt++) {
		total += *pt;
	}
	return total;
}

int fill_array(double ar[], int limit) {
	using namespace std;

	double temp;

	int i;

	for (i = 0; i < limit; i++) {
		cout << "Enter value #" << (i + 1) << ": ";
		cin >> temp;

		if (!cin) {
			cin.clear();
			while (cin.get() != '\n') continue;
			cout << "Bad input; input process terminated.\n";
			break;
		}
		else if (temp < 0) break;
		ar[i] = temp;
	}
	return i;
}



void show_array(const double ar[], int size) {
	using namespace std;

	for (int i = 0; i < size; i++) {
		cout << "Property #" << (i + 1) << ": $";
		cout << ar[i] << endl;
	}
}

void revalue(double r, double ar[], int n) {
	for (int i = 0; i < n; i++) {
		ar[i] *= r;
	}
}
```

这个例子演示了基本的数组作为函数参数的使用方法，演示了const的使用，还演示了第二种数组作为函数参数的写法，具体请看sum_array函数，其接受的是数组的首地址和末地址，你可以通过 `sum_array(properties, properties + size);` 这种写法来传入数组的长度，或者随意计算数组前面几个元素的和都是可以的。

### C风格字符串作为函数的参数

本质上C风格字符串属于字符数组，只是里面有个`\0`来标记字符串的结尾。具体使用参考上面的数组的讨论。

### 结构体作为函数的参数

结构体其实更加简单，其使用基本上可以看作某种额外的基本数据类型，你可以传值，也可以传指针，只是如果结构体比较大的话，还是推荐传指针。

关于C++新增的类的概念，比如string类，array类等，这些作为函数的参数大体可以参考结构体的使用，也就是可以看作某种额外的基本数据类型。关于类的使用后面会有更详细的讨论了。

### 函数作为函数的参数

函数名就是函数的地址，你可以直接将函数名作为参数传递进去，不过麻烦在这个函数指针的类型声明上：

```
void estimate(int repeat, double(*pf)(int));
```

声明的这个pf就是指针那个目标函数的指针，只是因为声明的时候要带上指向函数的类型声明，有的时候语句会很长。

可以利用typedef进行简化：

```
typedef double(*test_func_type)(int);
```
具体请看下面的样例来加深理解：

```cpp
#include <iostream>

using namespace std;

typedef double(*test_func_type)(int);
void estimate(int , test_func_type);
double test_func(int a);


double test_func(int a) {
	double b;
	b = a * 3.14;

	cout << a << " * 3.14 = " << b << endl;
	return b;
}

void estimate(int repeat, test_func_type pf) {
	for (int i=0; i < repeat; i++) {
		(*pf)(3);
	}
}

int main() {
	estimate(10, test_func);
	return 0;
}
```



1．编写一个程序，不断要求用户输入两个数，直到其中的一个为0。对于每两个数，程序将使用一个函数来计算它们的调和平均数，并将结果返回给main( )，而后者将报告结果。调和平均数指的是倒数平均值的倒数，计算公式如下：

调和平均数=2.0 * x * y / (x + y)

xiti_c7_1.cpp

```cpp
#include <iostream>
#include <cctype>

using namespace std;

double calc_harmonic_mean(double, double);

double calc_harmonic_mean(double x, double y) {
	double result;

	result = (2.0 * x * y) / (x + y);
	return result;
}


int main() {
	double f1;
	double f2;
	double result;
	
	while (true) {
		if ((cout << "please input two number:") && (cin >> f1 >> f2)) {
			bool input_line_right = true;
			char ch;

			while (cin.get(ch)) {
				if (ch == '\n') {
					break;
				}
				else if (isblank(ch)) {
					;
				}
				else {
					cin.clear();
					while (cin.get() != '\n') continue;
					cout << "Bad input!\n";
					input_line_right = false;
					break;
				}
			}

			if (input_line_right) {
				if (f1 == 0 || f2 == 0) break;

				result = calc_harmonic_mean(f1, f2);
				cout << f1 << " and " << f2 << " harmonic mean is: " << result << endl;
			}
		}
		else {
			cin.clear();
			while (cin.get() != '\n') continue;
			cout << "Bad input!";
		}
	}

	return 0;
}
```



3．下面是一个结构声明：

```
struct box{
	char maker[40];
	float height;
	float width;
	float length;
	float volume;
};
```

a．编写一个函数，按值传递box结构，并显示每个成员的值。

b．编写一个函数，传递box结构的地址，并将volume成员设置为其他三维长度的乘积。

c．编写一个使用这两个函数的简单程序。

xiti_c7_3.cpp

```cpp
#include <iostream>


using namespace std;

typedef struct box {
	char maker[40];
	float height;
	float width;
	float length;
	float volume;
}Box;

void show_box(Box box1);
void calc_box_volume(Box* pbox);



void show_box(Box box1) {
	cout << 
		"box: " << box1.maker << endl <<
		"height: " << box1.height << endl <<
		"width: " << box1.width << endl <<
		"length: " << box1.length << endl <<
		"volume: " << box1.volume
		<< endl;
}

void calc_box_volume(Box* pbox) {
	pbox->volume = pbox->width * pbox->height * pbox->length;
}

int main() {
//int main33() {

	Box box1 = {
		"box1",
		2.5,
		3.6,
		7,
		0
	};

	show_box(box1);

	calc_box_volume(&box1);

	show_box(box1);

	return 0;
}
```

5．定义一个递归函数，接受一个整数参数，并返回该参数的阶乘。前面讲过，3的阶乘写作3!，等于`3*2!`，依此类推；而0!被定义为1。通用的计算公式是，如果n大于零，则`n!=n*（n−1）!`。在程序中对该函数进行测试，程序使用循环让用户输入不同的值，程序将报告这些值的阶乘。

xiti_c7_5.cpp

```cpp
#include <iostream>

using namespace std;

int factorial(int);


int factorial(int x) {
	if (x == 0) {
		return 1;
	}else {
		return factorial(x - 1) * x;
	}
}


int main() {
	//int main34() {
	int n;
	int result;

	while (true) {
		if ((cout << "please input one integer number:") && (cin >> n)) {
			bool input_line_right = true;
			char ch;

			while (cin.get(ch)) {
				if (ch == '\n') {
					break;
				}
				else if (isblank(ch)) {
					;
				}
				else {
					cin.clear();
					while (cin.get() != '\n') continue;
					cout << "Bad input!\n";
					input_line_right = false;
					break;
				}
			}

			if (input_line_right) {
				if (n < 0) break;

				result = factorial(n);
				cout << n << " factorial is: " << result << endl;
			}
		}
		else {
			cin.clear();
			while (cin.get() != '\n') continue;
			cout << "Bad input!\n";
		}
	}

	return 0;
}
```



9．这个练习让您编写处理数组和结构的函数。下面是程序的框架，请提供其中描述的函数，以完成该程序。

```cpp
#include <iostream>

using namespace std;

const int SLEN = 30;
struct student {
	char fullname[SLEN];
	char hobby[SLEN];
	int ooplevel;
};

// getinfo has two arguments: a pointer to the first argument of
// an array of student structures and an int representing the
// number of elements of the array. the function solicits and
// stores data about students. It terminates input upon filling 
// the array or upon encountering a blank line for the student 
// name. the function returns the actual number of array elements 
// filled.
int getinfo(student pa[], int n);

// display1 takes a student structure as an argument
// and display its contents.
void display1(student st);

// display2 takes the address of students structure as an 
// argument and display the structure's cntents.
void display2(const student* ps);

// display3 takes the address of the first element of an array
// of student structures and the number of array elements as 
// arguments and displays the contents of the structures
void display3(const student pa[], int n);

int main() {
//int main35() {
	cout << "Enter class size: ";

	int class_size;
	cin >> class_size;

	while (cin.get() != '\n') continue;

	student* ptr_stu = new student[class_size];
	int entered = getinfo(ptr_stu, class_size);
	for (int i = 0; i < entered; i++) {
		display1(ptr_stu[i]);
		display2(&ptr_stu[i]);
	}
	display3(ptr_stu, entered);
	delete[] ptr_stu;

	cout << "Done\n";

	return 0;
}
```

xiti_c7_9.cpp

```cpp
#include <iostream>
#include <cstring>

using namespace std;

const int SLEN = 30;
struct student {
	char fullname[SLEN];
	char hobby[SLEN];
	int ooplevel;
};

int getinfo(student pa[], int n);
void display1(student st);
void display2(const student* ps);
void display3(const student pa[], int n);

int getinfo(student pa[], int n) {
	int entered = 0;

	for (int i = 0; i < n; i++) {
		cout << "please input student fullname: ";
		cin.getline(pa[i].fullname, SLEN);

		cout << "please input student hobby: ";
		cin.getline(pa[i].hobby, SLEN);

		cout << "please input student ooplevel: ";
		(cin >> pa[i].ooplevel).get();

		entered += 1;
	}
	return entered;
}


void display1(student st) {
	cout <<"student " << st.fullname <<
		" hobby: " << st.hobby <<
		" ooplevel: " << st.ooplevel << endl;
}

void display2(const student* ps) {
	cout <<"student " << ps->fullname <<
		" hobby: " << ps->hobby <<
		" ooplevel: " << ps->ooplevel << endl;
}

void display3(const student pa[], int n) {
	for (int i = 0; i < n; i++) {
		display1(pa[i]);
	}
}

int main() {
//int main35() {
	cout << "Enter class size: ";

	int class_size;
	cin >> class_size;

	while (cin.get() != '\n') continue;

	student* ptr_stu = new student[class_size];
	int entered = getinfo(ptr_stu, class_size);
	for (int i = 0; i < entered; i++) {
		display1(ptr_stu[i]);
		display2(&ptr_stu[i]);
	}
	display3(ptr_stu, entered);
	delete[] ptr_stu;

	cout << "Done\n";

	return 0;
}
```



10．设计一个名为calculate( )的函数，它接受两个double值和一个指向函数的指针，而被指向的函数接受两个double参数，并返回一个double值。calculate( )函数的类型也是double，并返回被指向的函数使用calculate( )的两个double参数计算得到的值。例如，假设add( )函数的定义如下：

```
double add(double x, double y){
	return x + y;
}
```

则下述代码中的函数调用将导致calculate( )把2.5和10.4传递给add( )函数，并返回add( )的返回值（12.9）：

```
double q = calculate(2.5, 10.4, add)
```

请编写一个程序，它调用上述两个函数和至少另一个与add( )类似的函数。该程序使用循环来让用户成对地输入数字。对于每对数字，程序都使用calculate( )来调用add( )和至少一个其他的函数。如果读者爱冒险，可以尝试创建一个指针数组，其中的指针指向add( )样式的函数，并编写一个循环，使用这些指针连续让calculate( )调用这些函数。提示：下面是声明这种指针数组的方式，其中包含三个指针：

```
double (*pf[3])(double, double);
```

可以采用数组初始化语法，并将函数名作为地址来初始化这样的数组。

xiti_c7_10.cpp

```cpp
#include <iostream>

using namespace std;

typedef double (*func_call)(double, double);

double addition(double , double );
double subtraction(double, double);
double multiplication(double, double);

double calculate(double x, double y, func_call func);

double calculate(double x, double y, func_call func) {
	return (*func)(x, y);
}
double addition(double x, double y) {
	cout << "running addition...\n";
	return x + y;
}
double subtraction(double x, double y) {
	cout << "running subtraction...\n";
	return x - y;
}
double multiplication(double x, double y) {
	cout << "running multiplication...\n";
	return x * y;
}


int main() {
	double (*pf[3])(double, double);

	pf[0] = addition;
	pf[1] = subtraction;
	pf[2] = multiplication;

	for (int i : {0, 1, 2}) {
		double q = calculate(2.5, 10.4, pf[i]);
		cout << "result: " << q << endl;
	}

	return 0;
}
```



## 内存模型和名称空间



## 类



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