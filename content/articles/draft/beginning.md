Title: C语言编程之-beginning
Status: draft
[TOC]


## 开发环境搭建
windows下推荐使用Microsoft visal studio来开发编写c语言或者c++语言程序。本小节主要参考了 [这篇文章](http://c.biancheng.net/cpp/html/3433.html) ，这篇文章写得是极好的。

安装好vs之后，选择C++开发环境安装之。进入程序之后，选择：

```
文件 -> 新建 -> 项目... -> 空白项目
```

对于初学者可以取消勾选 *为解决方案创建目录* 。点击确定之后，我们可以在源文件哪里:

```
右键 -> 添加 -> 新建项... C++文件
```

目前主要学习C语言可以将后缀改为 `.c` ，不过不改的话一般问题不大。



## helloworld
第一个helloworld的例子实在是太经典了。
```
#include <stdio.h>
#include <stdlib.h>

int main(void) {
	printf("hello world!\n");
	system("pause");
	return 0;
}
```

这里 `#` 开头标识了C语言的预处理语句，然后 `#include` 是包含另外一个头文件。stdio.h 里面提供了一些标准输入输出支持，比如下面的 printf 函数就是这个包提供的。

然后相比较一般的helloworld程序多了下面两行，主要是让屏幕暂停一下，否则屏幕会一闪而过，我们会看不清具体打印了什么字。
```
#include <stdlib.h>

system("pause");
```

下面实际上是一种定义函数的写法，只是这个函数名字比较特殊，叫做main，C程序会将main函数视为程序的入口。

按照C11的标准推荐main函数采用这样的写法：
```
int main(void){

}
```



## 计算最大公约数

### 除法和求余数
下面主要演示下除法和求余数，其他加法减法乘法还是很直白的。
```
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

```
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

```
int gcd(int a, int b) {
	if (b == 0) {
		return a;
	}
	else {
		return gcd(b, a%b);
	}
}
```


其中`a % b` 取余保证了其实最小或者更小的那个数，这是没有问题的。

另外辗转相除法，网上实现也已经有了：

```
int gcd_two(int a, int b) {
	int t; // 只是一个临时变量,记录最小值
	while (b) { // b最小值成为零了返回a
		t = a % b; // t记录取余后的最小值
		a = b; // a记录最大值
		b= t; // b记录最小值
	};
	return a;
}
```





## 参考资料

1. C Primer Plus C Primer Plus 第六版中文版
2. Practical C programming Steve Oualline










