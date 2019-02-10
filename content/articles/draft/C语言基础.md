Title: C语言编程之-C语言基础
Status: draft

[TOC]



## 定义符号常量

```
#define PI 3.14
```



## 自动类型转换

C语言遇到不同数据类型运算，会发生自动类型转换的情况有 char -> int  int -> double ，当然也包括 char -> double 。

## 强制类型转换

```
(int)(3.14)
```

强制类型转换不影响原变量，是运算时的截取操作，不是四舍五入。



## 如何打印百分号

```
printf("%%")
```



## 字符串变量

字符串确切来说是一个字符型数组，以 '\0' 结束，比如 "sam" 实际存储的值如下所示：

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

1. C Primer Plus C Primer Plus 第六版中文版
2. Practical C programming Steve Oualline