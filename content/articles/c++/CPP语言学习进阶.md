Category: c_and_cpp
Slug: cpp-language-learning-advanced
Date: 2021

[TOC]

### 类在namespace里面更简明的声明

如下，只是简单告诉编译器该类在某个namespace里面，后面再详细写上声明。

```c++
namespace ns {
    class A; // just tell the compiler to expect a class def
}

class ns::A {
    // define here
};
```

在Qt样例项目中有这样的代码：

```c++
#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private:
    Ui::MainWindow *ui;
};
#endif // MAINWINDOW_H
```

初看上去两个MainWindow很让人迷惑，其实这两个说的是两个东西。在Ui命名空间里面的MainWindow类的具体声明是在mainwindow.ui自动生成的ui_mainwindow.h文件那里：

```
namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui
```

如果将样例项目改成这样会更清晰一点：

```c++
#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MyMainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MyMainWindow(QWidget *parent = nullptr);
    ~MyMainWindow();

private:
    Ui::MainWindow *ui;
};
#endif // MAINWINDOW_H
```



### lambda函数写法

```c++
[](float a, float b) {
            return (std::abs(a) < std::abs(b));
} 
```

- 方括号里叫做capture clause
- 圆括号里面是lambda函数的参数
- 花括号里面是lambda函数的主体部分







### 参考资料

1. C++ Primer Plus 第六版中文版