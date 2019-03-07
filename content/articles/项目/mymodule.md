Title: mymodule for python
Slug: mymodule
Date: 2019-02-27
Modified: 2019-02-27
Tags: python,



[TOC]



## 简介

一个通用目的的python模块

项目源码在 <https://github.com/a358003542/mymodule>



# mymodule
个人学习研究python的结晶, 一个大杂烩性质的通用模块【但也不是什么都往里面扔，而是作者确实感觉到有实用价值】



## LICENSE
MIT LICENSE


## 安装和使用
已经移除了pip安装过程，觉得对于本项目完全没有必要。把你想要的代码部分复制粘贴到你想要开发的python项目目录下即可，或者称之为绿色安装版吧。

推荐的使用方式如下：

1. git clone 本项目到你当前正在开发的python项目根目录下

2. 

```
from mymodule.utils.path_utils import get_project_path

get_project_path() # 将返回你当前正在开发项目的根目录
```

### 必要的依赖
依赖的话基本上调用谁，谁的功能需要什么就要安装某个python模块，比如database部分，是依赖sqlalchemy的等。下面列出的依赖是必要的依赖：

- loguru 便捷的日志输出 因为很方便，后面写的logger都是从loguru生成的。



## 模块无关部分
- tests部分里面放着个人开发编写的一些单元测试，仅此而已。
- examples 部分里面放着其他一些样例，仅此而已。
- notebooks 一些jupyter notebook


## API
下面API部分简要说明本模块所包含的内容和基本使用情况，更详细的接口请查阅源码。


### 顶层部分
- gfun 早期学习python的一些东西 后面会慢慢整理出去的 
- exceptions 一些异常
- consts 一些常数

### algorithms算法部分
个人学习算法的一些积累 没有太大实用价值 可做学习时的参考

### compat
python2和python3兼容性模块 历史原因保留在这里 并没怎么用了 





### database部分
 database 里面放着很多便捷的对接数据库的通用操作模式。

#### mongodb
- mongodb连接操作 get_mongodb_client

- mongodb插入操作 加入了去重逻辑 insert_item

- mongodb upsert 操作 upsert_item

#### sqldb
sqldb利用sqlalchemy完成连接操作

- create_sqlalchemy_url 创建sqlalchemy支持的url

- SQLDataBase类 输入sqlalchemy支持的url格式，连接数据库后的一些操作，本类主要用于sqlalchemy的非原生ORM操作。
```
        self._engine
        self._conn
        self._meta
        self._session
        self.execute  执行
        self.all_tables 所有table name
        self.get_table(table_name) 返回sqlalchemy的Table对象，内省，会更加健壮，也更加底层
```

- sqldb插入或者忽略操作 insert_or_ignore

- sqldb 插入或者更新操作 insert_or_update

- sqldb更新一个记录操作 update_one



### ml机器学习部分
个人学习机器学习部分的一些积累，


- preprocessing 数据预处理支持 新增 ZeroMinMaxScaler2  同原0-1缩放 不同的是不会取值1,取值范围为 [0,1)

- reader 对接pandas io的 读取数据操作

- knn 很粗糙地对接了下knn算法 TODO


### stream_processing
流处理操作模式

比如：
```
filter_all = build_stream_function(filter_zh_ratio, filter_zhtext_length, filter_text_length)

```
这样就将多个过滤函数连接成为一个流处理函数。


### utils部分
utils里面有很多便捷的函数支持。

#### admin_utils
提升管理员权限工具 admin_utils 用于在windows下提升脚本运行权限

- is_admin 判断是否是管理员权限
- run_as_admin 已管理员方式运行本脚本

```python
if __name__ == '__main__':
    if not is_admin():
        run_as_admin()
    else:
        main()
```


- airflow_utils 对最小时间片的单个任务提供额外的运行状态记录支持

#### date_utils
- is_same_year 输入两个datetime 对象，判断是否是同一年
- is_same_month  判断两个datetime对象是否是同一月
- is_same_day 判断两个datetime对象是否是同一天
- is_same_hour 判断两个datetime对象是否是同一时
- round_to_day     datetime对象round到天，其他归零
- round_to_hour datetime对象round到小时，更小的刻度归零
- round_to_minute  datetime对象round到分钟
- round_to_second datetime对象round到秒

- get_date_range 参数是往前数的月份，TODO 其他参数补上
```
from utils.date_utils import get_date_range
get_date_range(5)
Out[3]: 
[datetime.datetime(2018, 10, 7, 2, 7, 1),
 datetime.datetime(2018, 11, 7, 2, 7, 1),
 datetime.datetime(2018, 12, 7, 2, 7, 1),
 datetime.datetime(2019, 1, 7, 2, 7, 1),
 datetime.datetime(2019, 2, 7, 2, 7, 1),
 datetime.datetime(2019, 3, 7, 2, 7, 1)]
```

- normal_format_now     标准格式 now '2018-12-21 15:39:20'
- normal_format_utcnow
- get_timestamp 获得当前的timestamp
- get_dt_fromtimestamp 根据timestamp获得对应的datetime对象

#### df_utils
pandas的DataFrame对象的一些便捷操作函数

- change_df_type     
输入 df column_name type

将df的某个列的类型更改为某个type 比如float等

- rename_df_columns 重新设置列名    

- rename_df_column_by_index 将index column 名字修改为 to

- rename_df_column_by_name 将某个column 名字修改为 to

- get_all_column 获取一列所有的值 默认去重

#### dll_utils
介绍了如何利用python对接dll文件

#### encrypt_utils
加密解密

- pbkdf2_sha256 加密
- encrypt_message 加密某个信息
- decrypt_message 解密某个信息


#### file_utils
- bigfile_read 大文件读写模式


#### id_utils

- build_query_id
唯一id生成 
根据关键和某个字典参数 生成 唯一的文件名或者唯一的id等等


#### path_utils
路径处理工具

- get_project_path 返回mymodule存放的根目录
- normalized_path 输入路径规范化 支持 '.' '~' 表达

- etc... 




- 绘图支持工具 plot_utils 基于matplotlib的绘图便捷支持



#### winreg_utils
windows的注册表读写工具
1. 默认的Key
```
    >>> HKEY_CURRENT_USER
    <regobj Key 'HKEY_CURRENT_USER'>
    >>> HKLM
    <regobj Key 'HKEY_LOCAL_MACHINE'>
```
2. 自组建Key 可以写上一连串path名字
```
    Key(parent, *name)
```
3. .subkeys() 列出所有该Key的子Key TODO 数据结构字典化支持按名字索引

4. .name 本Key的名字

5. .names 本Key完整路径名字

6. .get_subkey(name) 根据名字来向下获取子Key

7. .del_subkey(name) 删除某个子Key

8. .values() 列出该Key所包含的子值

9. .items() 列出该Key所包含的子值，不过返回的是字典格式

10. Key['name'] 实际获取某个Key的子值 没找到抛异常

11. Key['name'] = value 修改某个Key的子值

12. get(name) 试着获取某个Key的子值，没找到返回None

13. .delete() 删除本Key

14. .get_data(name) 试着获取某个Key的子值，直接返回值而不是Value对象


### web部分
web部分是我研究爬虫的一些结晶，其中比较实用的有：

- 获得一个随机的User-Agent get_random_user_agent

- 将一个url，相对的或者绝对的，转成绝对url to_absolute_url

- 下载操作 download
