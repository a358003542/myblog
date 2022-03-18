Slug: odoo-learning-notes
Date: 2019

[TOC]


## 前言
本文主体是笔者好几年前写的，现在因为工作关系笔者决定再次研究odoo这个模块，这些年来odoo发生了很多变化，笔者这次的目的是为了更好地学习odoo的源码，从odoo的源码中学习到代码设计和开发的思路或者说idea。本文原来的内容部分会得到更新和审核，一些照顾不到的内容将会扔到附录里面。虽然有些内容可能放在正文的某个部分是合适的，而且从odoo11到odoo15这些内容也许就是正确的没有发生变化，但笔者本着宁缺毋滥的精神决定最新版本没有得到审核的都扔到附录里面了。



## 简介

Odoo的前身是 Tiny ERP，最初是由比利时的Fabien Pinckaers 创建的。

![Fabien-Pinckaers]({static}/images/odoo/Fabien-Pinckaers.png "Fabien Pinckaers")

到2009年的时候，发布第5版，公司获得风投，盈利增长迅速，软件更名为OpenERP。OpenERP这个名字最为人们熟知，当时软件已经包含几百个模块了，从财务管理、采购/销售管理、库存管理到人力资源管理、销售点管理、项目管理等等都有。

在2014年9月，软件发布第8版，在之前版本逐渐优化的web client这一块的基础上，进行了大范围的功能加强。比如有了Website builder模块，可以方便公司快速架构出自己的网站；e-commerce模块方便公司快速搭建销售平台；还有business intelligence这个模块，可以辅助生成高质量的说明演示用的图形等等等等。这使得OpenERP这个名字已经不能很好地说明这个软件的雄心壮志了，于是软件更名为 **Odoo** 这个名字了。

在2017年10月份odoo发布了最新的稳定版，odoo11版，本文是基于最近最新的odoo15版来进行讨论的。

该软件的基本架构就是基于web client/server模型，将公司内部所涉及到的所有的信息流都整合起来，其不仅包括具体实施层面，也包括分析决策层面。可以预见不久的将来Odoo开发将快速为公司构建出这样一个生态:

![Odoo-sheng-tai-quan]({static}/images/odoo/Odoo-sheng-tai-quan.png "Odoo生态")



### 商业智能化

随着信息时代的到来，商业也不可避免地走向信息化，智能化。最新的ERPⅡ的概念包含的内容如下所示:

![ERP_Modules]({static}/images/odoo/ERP_Modules.png "商业智能化")



- Business Intelligence 商业智能，其主要关注于分析数据，并将数据变成知识这一过程。
- e-Commerce 电子商务，关注于对外战略。
- Enterprise asset management 企业资产管理，有效可持续地管理公司的资产生命周期，用强有力的分析工具来提高资产使用率和削减成本。
- Procurement(SRM) 采购，最大化的节约成本和支持终端对终端的采购，还有物流过程。
- Production(PLM) 生产，帮助管理和优化生产能力和物料资源。是MRP的升级版。（MRP是ERP的前身，是美国生产企业为了解决物料需求问题而提出来的，主要是要解决这个问题: 如果要生成多少产品，那么相应的ABC等等物料各自需要多少？）这里谈论的PLM不仅要解决物料需求问题，而且要解决生产的时间问题，从而达到优化生产能力的目的。
- Distribution(SCM) 配送，控制仓库流程，使其能够对补给需求或更改做出快速的反应。
- Accounting 会计，自动化财务管理，同时要确保管理的便捷和对绩效做出实时反映。
- Human Resource 人资，维护一个完整的雇员数据库，更好地使用所有雇员。
- Corporate performance and governance 公司表现监管，对公司的各个部门更高的控制，目标让他们能够流水线作业。
- Customer services(CRM) 客服，获取和维护和客户的关系，充分利用客户的体验来进行知识管理评估。（其和BI模块结合很紧密）
- Sales 销售，具体的定单确认，下单，货运和开发票等。



### Odoo框架简介

下面一副图很好地说明了Odoo技术框架:

![client_server]({static}/images/odoo/client_server.png "odoo技术框架")


- PostgreSQL数据库
- Object Relation Mapping 也就是大家熟知的SQL ORM包装层。Odoo除了使用的基本的 **psycopg2** 作为接口之外，ORM层是Odoo自己写的。
- Base Module Distribution 官方基本模块
- Report Engine 负责生成各种报表。目前支持的报表格式有 PDF,OpenOffice,HTML 三种。
- Workflow Engine 工作流引擎。支持任意复杂度的工作流。
- WebService 提供网络调用接口。目前支持 Net-RPC、XML-RPC 两种。Odoo和flask一样使用Werkzeug作为WSGI层的包装，jinja2作为模板工具。然后剩下的框架部分是Odoo自己写的。



## 安装
**我简单看了以下，现在odoo似乎都提供专门的安装包程序了，所以读者如果只是想简单尝试和使用odoo，那么推荐使用安装包程序，本文是本着学习研究odoo的目的所以决定采用从源码安装的方式。**

下面主要讨论了windows下的从源码的安装过程，附录部分有odoo11在linux下的安装讨论可作参考。

### 配置python环境
这是python基本功了，这里就不赘述了。这里还只是最基本的python基础虚拟环境，其他python模块依赖后面再讨论。

### 安装postgresql数据库
如果是从postgresql的官网下载安装包来安装postgresql，那么没什么好说的。不过考虑到后面我极有可能需要将postgresql集成到应用中，所以那个Binaries的下载选择引起了我的注意，我决定提高难度试试这个安装看看。

我一开始以为在官方文档的这里： [install-binaries](https://www.postgresql.org/docs/current/install-binaries.html) 可以找到相关讨论，结果什么都没有。参考 [这个网站](https://stackoverflow.com/questions/26441873/starting-postgresql-and-pgadmin-in-windows-without-installation) 我半信半疑地开始尝试，主要就是要运行两个命令，`initdb` 和 `pg_ctl` 。 initdb是创建postgresql数据库集群的，pg_ctl 是用来对postgresql server进行启动、停止等操作。我实在不明白这块官方文档为什么不说明清楚。

将解压出来的bin文件夹添加进入 `PATH` 变量就不赘述了。

```
initdb -D D:\SourceCode\odoo_test\pgdata -U postgres -W -E UTF8 -A scram-sha-256
```

- `-D` 设置本数据库集群文件夹所在
- `-U` 设置本数据库集群的超级用户用户名
- `-W` 等下弹出提示方便输入超级用户的密码
- `-E` 本数据库集群的编码，没有特别理由一般设置UTF8
- `-A` 本数据库集群的默认认证方式

```
pg_ctl -D D:\SourceCode\odoo_test\pgdata -l logfile start
```
上面的命令开启postgresql server，`-D` 指定数据库配置文件所在的文件夹，和上面 `-D` 指定的应该是一样的。 `-l` 指定日志文件。

双击pgadmin/bin的 `pgAdmin4.exe` 可以看能否连接成功。如果连接成功那么postgresql算是安装成功了。

至于windows每次启动自动启动postgresql server这个暂时还不想弄。不过似乎我关闭那个开启postgresql server的powershell会关闭postgresql server，不管怎么说，这些都是小细节，暂时写个小脚本，先这么挂着吧。

`start_postgresql_server.bat` :

```
pg_ctl -D D:\SourceCode\odoo_test\pgdata -l logfile start
```

新建一个postgresql数据库用户，odoo禁止使用postgres这个用户。

在pgAdmin哪里，点击Login/Group Roles，鼠标右键，`Create -> Login/Group Roles` 。填写用户名和密码，然后选上Can Login 权限和 Create database权限。



### 安装nodejs环境
这个是一个可选项，笔者这边之前已经装上了，官方文档里面提到一个语种方面的问题需要安装一个npm包，不过笔者暂时不打算安装这个。

### 安装c++编译环境
这边笔者之前已经装上了，某些python模块或者npm包编译安装的时候需要本机的c++编译环境。没有安装的读者推荐安装visual studio生成工具，然后点击使用C++的桌面开发的工作负荷即可。visual studio生成工具更轻量级一点，因为其没有强制安装visual studio编辑器，那编辑器不是说不好，但如果一定要推荐编辑器，当然是推荐微软的code编辑器啊。

### 安装python包依赖
我这里是odoo15，python是3.10，有几个模块不能正常安装上。pypiwin32这个模块现在odoo15的requirements.txt里面已经有了。

有几个不能安装的模块先试着在 [这里](https://www.lfd.uci.edu/~gohlke/pythonlibs/) 下载对应的安装包来安装。

我遇到的不能安装成功的有： `greenlet` ， `psutil` ， `pillow` 。其他python版本不同等情况可能会有所不同。然后目标模块版本号稍微大一点一般问题不大的。pillow推荐版本8.4.0，9点几的版本似乎有点问题。

psycopyg2因为有dll依赖最好从上面那个网站安装。

bable需要更新最新版本。

3.10collections移除了 Collections Abstract Base Classes ，有几个报错的代码，需要修改为：

```
collections.abc.What
```

因为odoo源码里面的插件很是庞大，不推荐通过 `python setup.py install` 来安装odoo，而是将odoo源码移动到项目根目录，然后将setup文件夹里面的 `odoo` 文件重命名为 `odoo-bin` 然后移动到项目根目录，然后运行 `python odoo-bin` 即可。

首先推荐运行 `python odoo-bin --save` 在当前目录输出一个 `odoo.conf` 文件，读者可以在里面进行一些参数的配置，一般刚开始odoo是不能正常运行的，需要你先配置好数据库的一些参数。比较重要的有下面几个 ：

```
pg_path = 你安装的postgresql的bin目录
db_host = localhost
db_name = False
db_password = odoo
db_port = 5432
db_sslmode = prefer
db_user = odoo
```

以后直接运行 `python odoo-bin` 即可。

然后到 `http://localhost:8069/` 进行一些网页操作创建数据库。

---------------

odoo不容置疑是一个很优秀的项目，其解决的业务，比如进销存和会计等等方面的问题也许并不那么切合读者的需求，但odoo这个项目里面从某个业务问题到如何建造数据模型到如何视图层表现交互这一系列的Web应用开发流程，这个流程和这个研究解决问题的思路无疑是很值得我们去学习的，这也是笔者关注的焦点。

接下来先研究点什么再写点东西吧。


## 模型层代码研究
当然是优先看模型层的代码，odoo是自己写的ORM层我是知道的，我现在对它自家的ORM怎么实现的没什么兴趣，但通过ORM层来看看里面的模型架构无疑还是很有价值的。因为

重要的模型或表格：

- res.users 定义了用户 重要的字段有 name login email phone password groups_id【many2many】
- res.groups 定义了用户的群组概念 这个群组概念主要是控制权限用的
- ir.modle 模型清单 name
- ir.rule name group_id modle_id perm_read perm_write perm_create perm_unlink 【定义一系列的安全规则，比如某个群组对某个模型具有什么权限。】
- purchase.order 采购订单 具体业务可能不是采购订单，我看到里面有state字段，用一些确定的字符串选项来表示该采购订单的状态。

在大概阅读研究上面的代码之后，在权限控制等方面完善一下预期的Web应用似乎会有一点样子了，但似乎还少点什么东西，对了，odoo的workflow引擎。odoo的workflow引擎代码在哪里我一时找不到，不过没有问题，用其他的python实现的workflow引擎代码即可。


## 启用开发者工具
虽然安装一个模块之后，在设置的最下面有几行字写着激活开放者工具，激活开发者工具with资产等。



## 附录


### linux安装odoo11参考
先执行下面命令准备一下。
```
yum update
yum install epel-release
yum groupinstall Development tools
```

#### PostgreSQL数据库

PostgreSQL是很有名的一个开源数据库，最初由加州大学伯克利分校的计算机系开发，其和sqlite3最大的区别就是其采用了client/server模型，Odoo搭建在PostgreSQL基础之上了，也继承了这种client/server模型。Odoo对PostgreSQL数据库的版本号要求不是很严格，用最新的也是可以的。

```
yum install postgresql-server
yum install postgresql-contrib
postgresql-setup initdb
```

最基本的安装现在先暂时这样，关于数据库的配置后面我们再进一步讨论之。然后关于 Postgresql数据库的学习，读者可以简单参考我写的 postgresql数据库 一文。


#### 安装odoo依赖

常规通过pip安装即可，这里主要是一些系统方面的依赖问题，首先请确保安装了大环境 `python3` 和 `python3-dev` ，然后看到下面的内容：

##### centos那边

centos那边统一描述如下，请确保了这些软件包都安装上了：

```yaml
- name: libxml2  
  yum:
    name: libxml2
    state: present

- name: libxml2-devel
  yum:
    name: libxml2-devel
    state: present

- name: libxslt 
  yum:
    name: libxslt
    state: present

- name: libxslt-devel
  yum:
    name: libxslt-devel
    state: present

- name: libevent 
  yum:
    name: libevent
    state: present

- name: libevent-devel
  yum:
    name: libevent-devel
    state: present


- name: libjpeg-devel
  yum:
    name: libjpeg-devel
    state: present


- name: openldap-devel
  yum:
    name: openldap-devel
    state: present

- name: cyrus-sasl-devel
  yum:
    name: cyrus-sasl-devel
    state: present
```



##### ubuntu那边

关于python-ldap 模块的安装参考了 [这个网页](http://stackoverflow.com/questions/4768446/python-cant-install-python-ldap) ，请确保下面两个软件包都安装了（否则会提示找不到lber.h错误）: 

```
sudo apt-get install libldap2-dev 
sudo apt-get install libsasl2-dev
```

关于psycopg2模块请确保下面软件包安装了: 

```
sudo apt-get install libpq-dev
```

还有这几个软件包确保安装了，其中libxml2和lxml模块有关。

```
sudo apt-get install libxml2-dev
sudo apt-get install libxslt1-dev
```



pillow模块需要安装下面这个软件包:

```
sudo apt-get install libjpeg-dev
```



#### nodejs方面

centos那边现在只需要简单的通过yum命令安装了，安装之后npm工具也自动装上了。

```
yum install nodejs
npm install -g less
```



#### 安装odoo

由于odoo源码和addon生态较大，推荐不通过 `python setup.py install` 的方式安装，而是直接在odoo源码里面运行脚本启动。推荐方式如下，将setup文件夹里面的odoo文件重命名为 `odoo-bin` 然后移到项目主目录上，然后运行：

```
python odoo-bin

```

这样后面调试修改都方便一些。



#### 数据库那边的配置

数据库那边需要创建一个和你当前系统登录用户同名的用户，然后其要有创建数据库的权限，或者对某个数据库有所有权限。odoo将默认通过这个用户来和postgresql数据库进行交互（参考了 [这个网页](https://doc.odoo.com/7.0/install/linux/postgres/) ）。postgres用户名，root用户名都是不允许的。

```
sudo -u postgres createuser $USER

```



如果某个用户不存在，那么PostgreSQL将会报错: 

```
createdb: could not connect to database template1: FATAL:  role "wanze" does not exist

```



Odoo框架要求你这个用户还具有可以创建数据库的权限。这需要你如下这样去做: 

```
sudo -u postgres psql postgres

ALTER USER wanze CREATEDB;

```



这样你的用户就有了创建数据库的权限了，这块内容参考了 [这个网页](http://dba.stackexchange.com/questions/33285/how-to-i-grant-a-user-account-permission-to-create-databases-in-postgresql) 。

如果系统提示你没有 `.psql_history` 这个文件，那么简单的touch一下即可。

#### pg_hba.conf 

postgresql很多连接配置出了问题都是 `pg_hba.conf` 这个文件没配置好，更多细节请参看我写的 postgresql数据库 一文。

原来默认的配置是：

```
local   all             all                                     peer
# IPv4 local connections:
host    all             all             127.0.0.1/32           ident
# IPv6 local connections:
host    all             all             ::1/128                ident

```

有[文章](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-centos-7) 说下面两项需要改成 `md5` ， 然后postgresql的 [docker版](https://github.com/abevoelker/docker-postgres/blob/master/pg_hba.conf.default) 的默认配置也是改成了md5，刚开始我似乎遇到问题后来改成md5就好了，但现在odoo能够正常运行后我改回ident之后发现也能行。

总之记住odoo是用你当前的系统用户名来登录postgresql的，然后如果和数据库在一个系统内，那么用的就是后面两行的连接配置，推荐改成 md5 吧。



然后重启PostgreSQL服务器:

```
sudo service postgresql restart

```



#### 初步启动

运行 `python odoo-bin --help` 我们会看到很多选项，简单熟悉一下吧。

- -c CONFIG, --config=CONFIG 读取配置文件，这个很常见

- -s 或者 --save ，保存目前你的运行命令行配置，下次就可以简单使用 `python odoo-bin` 来运行了。具体配置文件是用户家目录下的 `.odoorc` 或者 `.openerp_serverrc` 文件 。

- --pidfile=PIDFILE   指定进程的pid文件，这个很常见。

- --addons-path=ADDONS_PATH 这个在加入用户自定义的addons时有用

  设置插件addons的路径，默认会把源码addons文件夹加上去，但可能会出错。这里设置为源码的addons文件夹。设置多个addons路径语法如下: `--addons-path=addons, myaddons` ，这可以用于加载你自己定义的某些模块。

- --http-interface=HTTP_INTERFACE 指定http端口，默认0.0.0.0，可以设置为localhost

- -p PORT, --http-port=PORT http服务的默认端口号是 8069 。

- --logfile=LOGFILE   日志文件保存，日志打印还有很多选项，这些后面有时间再研究。

- -u UPDATE, --update=UPDATE 升级某个模块

- -D DATA_DIR, --data-dir=DATA_DIR 设置odoo的data存放地

- --db-filter=REGEXP 用正则表达式过滤web UI可用的数据库

- -d DB_NAME, --database=DB_NAME odoo使用的数据库

- -r DB_USER, --db_user=DB_USER odoo连接数据库使用的用户名

- -w DB_PASSWORD, --db_password=DB_PASSWORD odoo连接数据库使用的密码

  


#### odoo.conf 

##### 数据库相关

- db_user 数据库连接时的用户名，
- db_password 数据库连接时使用的密码
- db_host 数据库host
- db_port 数据库端口号 默认 5432
- db-filter 正则表达式过滤，不匹配的数据库将会被隐藏（其中 %h hostname %d domain name (?i)%d `(?i)` 是忽略大小写，然后 `%d` 匹配域名名，比如说 `odoo.com` 匹配数据库 `odoo` 或者 `Odoo` 等。）
- db_template 默认 template1



##### 邮箱相关

- email_from odoo发送邮件时的显示邮箱地址 默认是 False
- smtp_server  smtp服务地址
- smtp_port  smtp服务端口号
- smtp_ssl  smtp服务是否开启 ssl
- smtp_user  登录smtp服务所使用的用户名
- smtp_password 登录smtp服务所使用的密码



```
;用于导入导出的csv文件的默认分隔符
csv_internal_sep = ,
;data目录，用于存放session信息、附件
data_dir = C:\Users\shun\AppData\Local\OpenERP S.A.\Odoo
;哪些模块加载demo数据
demo = {}
;在导入大量数据时使用这个选项，如果在导入期间程序宕机，你可以在当前状态下继续。指定一个存储中间导入状态的文件名。
import_partial =
;一个处理器允许使用的最大物理内存
limit_memory_hard = None
;一个处理器允许使用的最大虚拟内存
limit_memory_soft = None
;一个处理器接受的最大请求数
limit_request = None
;一个请求最多占用多少处理器时间
limit_time_cpu = None
;一个请求允许的最长实时时间
limit_time_real = None
;是否允许显示数据库列表
list_db = True
;是否将log写入db的ir_logging表
log_db = False
;保存在数据库中的日志记录的级别
log_db_level = warning
;指定模块日志级别，可以是一组module:log_level对，默认值是:INFO（表示所有模块的默认日志级别为INFO级别）
log_handler = :INFO
;日志的级别,可选值包括debug_rpc_answer,debug_rpc,debug,debug_sql,info,warning,error,critical
log_level = info
;指定用来存储日志的文件
logfile = D:\Program Files (x86)\Odoo 10.0\server\odoo.log
;是否按天存放日志，保留最新的30天
logrotate = False
;长连接池使用的端口号
longpolling_port = 8072
;处理当前计划任务的最大线程数
max_cron_threads = 2
;强制保存在virtual osv_memory表中的记录的最长时间，以小时为单位
osv_memory_age_limit = 1.0
;强制一个virtual osv_memory表的最大记录数
osv_memory_count_limit = False
;数据库可执行文件的路径
pg_path = D:\Program Files (x86)\Odoo 10.0\PostgreSQL\bin
;存储服务器pid的文件名
pidfile = None
;是否使用反向代理模式
proxy_mode = False
;是否压缩报表
reportgz = False
;指定用于SSL连接的证书文件
secure_cert_file = server.cert
;指定用于SSL连接的主密钥文件
secure_pkey_file = server.pkey
;server范围的模块,以逗号分隔
server_wide_modules = None
;是否把日志发送给系统日志服务器
syslog = False
;是否提交YAML或XML测试造成的数据库更改
test_commit = False
;是否允许YAML和单元测试
test_enable = False
;YML测试文件
test_file = False
;报表的范例的存放位置
test_report_directory = False
;为系统提供一个参照的时区
timezone = False
;哪些模块可翻译,默认为all
translate_modules = ['all']
;是否使用数据库的unaccent功能
unaccent = False
;在安装时哪些模块不加载演示数据
without_demo = False
;要使用的处理器数量
workers = None
;是否禁止使用XML-RPC协议
xmlrpc = True
;指定使用XML-RPC协议的IP地址，为空时表示绑定到现有IP
xmlrpc_interface =
;XML-RPC协议使用的TCP端口
xmlrpc_port = 8069
;是否禁止使用XML-RPC安全协议
xmlrpcs = True
;指定使用XML-RPC安全协议的IP地址，为空时表示绑定到现有IP
xmlrpcs_interface =
;XML-RPC安全协议使用的TCP端口
xmlrpcs_port = 8071

作者：itrojan
链接：https://www.jianshu.com/p/8fa53743bac8
來源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

```




### 参考资料



1. [wiki商业智能](https://zh.wikipedia.org/wiki/\%E5\%95\%86\%E4\%B8\%9A\%E6\%99\%BA\%E8\%83\%BD) [wiki ERP](http://en.wikipedia.org/wiki/Enterprise_resource_planning)
2. ERP不花钱, 作者: 老肖（OSCG）, 版本:  1.0 
3. Odoo Development Essentials , author: Daniel Reis , date: April 2015
4. [OdooV10 官方文档](https://www.odoo.com/documentation/user/10.0/zh_CN)
5. Odoo new API guideline Documentation , author: Nicolas Bessi , date: April 13, 2015 .
6. 会计学原理 第19版 作者: John J.Wild , Ken W. Shaw 等. 崔学刚译, 中国人民大学出版社.













