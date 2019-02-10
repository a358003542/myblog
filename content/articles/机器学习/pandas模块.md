Title: pandas模块
Date: 2018-07-01
Modified: 2018-09-16
Tags: 科学计算

[TOC]

本文对pandas模块的一些核心概念进行说明。

## 基本入门

pandas最核心的两个数据结构就是 Series 类和 DataFrame 类。其中DataFrame可能会用的偏多一点，Series相当于一维情况下较简单的DataFrame，有的时候会用到。本文重点讨论DataFrame类。

DataFrame之所以很常用是因为这种数据结构太常见了，在excel中，在csv中，在sql中，等等来源的数据都可以汇总成为DataFrame数据结构，然后进行一些后面必要的数据处理，包括送入机器学习或者深度学习的模型中去。

pandas的io子模块写得很便捷，实际上我经常看到有些python程序员并不是在做数据处理，有时都会调用下pandas的io来做一些读写操作。

其大体有这些函数：

- read_csv    to_csv
- read_json   to_json
- read_html to_html
- read_excel to_excel
- read_sql to_sql

这其中，html的读写在网络抓取上有时可能有用，但不是很强大，还是推荐用专门的工具来做，sql的操作简单点可以用pandas那边的接口，但如果稍微复杂点还是推荐用sqlalchemy来做，这样写出来的代码可读性更好一些，orm层接口也更便捷写，代码里面全是一大堆sql语句，总不是太好的。



### 读txt文件

实际上我们可能更常遇到的是txt文件，还是用 read_csv 函数来读，只是需要做一些额外的配置，比如 [这个问题](https://stackoverflow.com/questions/21546739/load-data-from-txt-with-pandas) 里面的例子是这样的：

```
data = pd.read_csv('output_list.txt', sep=" ", header=None)
```

- sep 设置读取csv时每个字段的分隔，默认是逗号，我遇到过是 `\t` 作为分隔符的情况
- header 默认取csv的第一行作为df数据的作为各个列的列名，如果设置了 `names` ，也就是手动指定列名，那么header相当于设置了None，如果header设置了None，将不会读取第一行作为列名。

read_csv 有很多选项，应付初步加载csv数据进入df内是绝对没问题的了。

### 读excel文件

利用pd.read_excel来读excel文件里面的数据，这个功能需要按照xlrdpython第三方模块支持。



### 直接加载python对象

这里支持的python对象有字典，或者已经是DataFrame了。

```python
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'], 
        'year': [2000, 2001, 2002, 2001, 2002, 2003], 
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}

frame = pd.DataFrame(data)

frame
```



实际上有些情况，可能利用python的其他模块进行数据源加载，然后整合为python字典之类，再存入DataFrame中会更方便一些，这个要根据具体情况来了。



### 执行某个sql查询语句

使用pd.read_sql 来从某个sql查询语句中获取数据，其有第二个必填参数conn，可以利用sqlalchemy如下获得：

```
import sqlalchemy
data_source = sqlalchemy.create_engine('sqlite:///mydata.sqlite')
```

上面的讨论我们可以汇总成为一个DataHandler对象，某些算法可以直接继承自这个类，直接加载数据，算法内部自动进行一些输出预处理，分类，测试，打标签，相应的算法计算等等。

```python
import os

import pandas as pd

class MissingSQLStatementError(Exception):
    pass

class DataHandler(object):
    """
    read data source from
    - file
    - python  DataFrame dict ...
    - sql
    """
    def __init__(self, data_source=None, data_source_type='file', sql_query=None, read_data_kwargs=None):
        self.data_source = data_source
        self.read_data_kwargs = read_data_kwargs if read_data_kwargs is not None else {}

        self.df = None

        if data_source_type == 'file':
            _, ext = os.path.splitext(self.data_source)
            ext = ext.lower()[1:]

            if ext in ['csv', 'txt']:
                self.df = pd.read_csv(self.data_source, **self.read_data_kwargs)
            elif ext in ['xlsx']: # sheet_name
                self.df = pd.read_excel(self.data_source, **self.read_data_kwargs)
        elif data_source_type == 'python':
            self.df = pd.DataFrame(self.data_source)
        elif data_source_type == 'sql':
            if sql_query is None:
                raise MissingSQLStatementError
            else:
                self.df = pd.read_sql(sql_query, self.data_source, **self.read_data_kwargs)

```



### 新建一个随机数填充的DataFrame

新建一个DataFrame对象，随机数填充6行4列，列名分别为 `['a','b','c','d']` 。

```
df = pd.DataFrame(np.random.randn(6,4), columns=['a','b','c','d'])
```

在实践中行row的名字也是可以定制的，但我们先重点看一下列名这个概念。上面 `columns` 参数是设置列名的，而上面提到的通用数据源加载类中，并没有提到columns这个概念，是因为，你的DataFrame创建之后，列名是可以随时修改定制的：

```python

    def set_columns(self, columns):
        self.df.columns = columns

    def rename_column(self, origin_column_name, column_name):
        """
        默认的column 可用 0 1 2 来引用
        :param origin_column_name:
        :param column_name:
        :return:
        """
        d = {}
        d[origin_column_name] = column_name
        self.df.rename(columns=d, inplace=True)

    def rename_columns(self, columns):
        self.df.rename(columns = columns, inplace=True)


```

首先我们看到第一个方法 `set_columns` ，其直接设置列名。

然后我们看到 `rename_column` 方法，如果你一开始不管列名这个问题，那么你新建的df默认的column就是 0,1,2... （是数值型不是字符串型），然后如上你可以定制那个列名，然后重命名之。



## DataFrame转numpy数据类型

如上pandas有很好的io接口，获取数据之后，然后我们就有了相应的dataframe对象了，但有的时候我们进行计算是希望以ndarray（numpy）的形式来进行的（我们引入DataFrame是因为其有label等等让各个列数据有含义的功能，而到了实际底层算法，可能就是特征1234了，我们不再关心具体特征的名字，这个时候将某部分数据退化为numpy的ndarray数据类型就很必要了，一方面底层算法层不在意这些，第二就是numpy的ndarray对象可以和以前我们常见的那些算法包括新出来的tensorflow很容易对接起来。）

实际转变如下，非常简单：

```
nd = df.values
```

参考了 [这个网页](https://stackoverflow.com/questions/13187778/convert-pandas-dataframe-to-numpy-array-preserving-index) 。



## 索引

### 按照列名选择

如果你已经定义列名了，那么选择一列按照列名是最直观的了：

```
df[column_name]
```

返回的是Series对象，原DataFrame对象的index部分继续保留，也就是原来你的DataFrame的index是有名字的，那么可以继续使用这些索引名字。

这种引用也可以用于添加某一列或者删除某一列：

```
del df[column_name]
df[column_name] = series
```

### 按照列名选择多个列

```python
df[['a','b','c']]
```

这样得到的将是一个copy！

### iloc方法

因为我是比较喜欢矩阵那种几行几列对于某一具体单元格的描述的，所以我很喜欢用 `df.iloc[i][j]` 这种形式来索引具体某个单元格的数据，就是i行j列，然后注意如果你的column是指定的数字，不是从0开始的，那么引用0就会出现索引异常【如果你的列名不是数字类型那么没有这个问题】。

唯一要注意的是就是和线性代数里面行列式下标有所不同，这里的索引都是从0开始计数的。

### 按照索引选择多个列

选择多个列【切片式】

```
df.iloc[:,0:2]
```

此外还有种写法【列举式】：

```
df.iloc[:, [0,2]]
```





## DataFrame

### 对某一特征列进行某个运算

利用pandas的DataFrame的apply方法将某个函数应用到某个特征列，然后赋值给新的一列。

```python
df['commas'] = df['text'].apply(lambda x: x.count(','))
```

### 搜索语句

DataFrame可以通过如下的搜索语句来对针对某些特征列的值进行判断，从而过滤掉某些行。

```
df[df['col1']==1]
df[(df['col1']==1)|(df['col2']==1)]
df[(df['col1']==0) & (df['col2']==0)]
```



### 按照行排序

```
df.sort_index(axis=1, ascending=False
```

### 按照列排序

```
df.sort_values(by='B')
```





## 绘图相关

### 绘制散点图

```
DataFrame.plot.scatter(x, y, s=None, c=None, **kwds)
```

根据数据记录 x 列（由x参数指定）和 y 列（由y参数指定）的一一对应的数据，来绘制散点图。

