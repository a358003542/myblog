Slug: odoo-learning-notes
Category: archived
Date: 2018

[TOC]

## WARNING

**警告，本文档已经归档，年久失修，可能内容已过于陈旧，放在这里权做读者参考。【2018】**



## 历史

Odoo的前身是 Tiny ERP，最初是由比利时的Fabien Pinckaers 创建的。

![Fabien-Pinckaers]({static}/images/odoo/Fabien-Pinckaers.png "Fabien Pinckaers")

到2009年的时候，发布第5版，公司获得风投，盈利增长迅速，软件更名为OpenERP。OpenERP这个名字最为人们熟知，当时软件已经包含几百个模块了，从财务管理、采购/销售管理、库存管理到人力资源管理、销售点管理、项目管理等等都有。

在2014年9月，软件发布第8版，在之前版本逐渐优化的web client这一块的基础上，进行了大范围的功能加强。比如有了Website builder模块，可以方便公司快速架构出自己的网站；e-commerce模块方便公司快速搭建销售平台；还有business intelligence这个模块，可以辅助生成高质量的说明演示用的图形等等等等。这使得OpenERP这个名字已经不能很好地说明这个软件的雄心壮志了，于是软件更名为 **Odoo** 这个名字了。

在2017年10月份odoo发布了最新的稳定版，odoo11版，本文是基于odoo11版来进行讨论的。

该软件的基本架构就是基于web client/server模型，将公司内部所涉及到的所有的信息流都整合起来，其不仅包括具体实施层面，也包括分析决策层面。可以预见不久的将来Odoo开发将快速为公司构建出这样一个生态:

![Odoo-sheng-tai-quan]({static}/images/odoo/Odoo-sheng-tai-quan.png "Odoo生态")



## 商业智能化

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



## Odoo框架简介

下面一副图很好地说明了Odoo技术框架:

![client_server]({static}/images/odoo/client_server.png "odoo技术框架")





- PostgreSQL数据库
- Object Relation Mapping 也就是大家熟知的SQL ORM包装层。Odoo除了使用的基本的 **psycopg2** 作为接口之外，ORM层是Odoo自己写的。
- Base Module Distribution 官方基本模块
- Report Engine 负责生成各种报表。目前支持的报表格式有 PDF,OpenOffice,HTML 三种。
- Workflow Engine 工作流引擎。支持任意复杂度的工作流。
- WebService 提供网络调用接口。目前支持 Net-RPC、XML-RPC 两种。Odoo和flask一样使用Werkzeug作为WSGI层的包装，jinja2作为模板工具。然后剩下的框架部分是Odoo自己写的。





## python版本

python3， please.

# 安装和配置

因为odoo的git仓库比较大了，推荐还是下载odoo发布的压缩包文件作为源码。下面主要讨论的是从源码安装的过程和一些问题。这其中数据库的相关配置是个难点，后面会再详细的讨论之。下面本文的叙述更多的偏向centos7，当然了从源码安装本身基于linux系统大环境，其他linux发行版除了个别安装包的支持差异外，差别不是太大了。

## 准备

```
yum update
yum install epel-release
yum groupinstall Development tools
```

## PostgreSQL数据库

PostgreSQL是很有名的一个开源数据库，最初由加州大学伯克利分校的计算机系开发，其和sqlite3最大的区别就是其采用了client/server模型，Odoo搭建在PostgreSQL基础之上了，也继承了这种client/server模型。Odoo对PostgreSQL数据库的版本号要求不是很严格，用最新的也是可以的。

```
yum install postgresql-server
yum install postgresql-contrib
postgresql-setup initdb
```

最基本的安装现在先暂时这样，关于数据库的配置后面我们再进一步讨论之。然后关于 Postgresql数据库的学习，读者可以简单参考我写的 postgresql数据库 一文。

## python虚拟环境等的配置

这一块和odoo关系不是太大，请读者自行调配之。

## 安装odoo依赖

常规通过pip安装即可，这里主要是一些系统方面的依赖问题，首先请确保安装了大环境 `python3` 和 `python3-dev` ，然后看到下面的内容：

### centos那边

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



### ubuntu那边

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



## nodejs方面

centos那边现在只需要简单的通过yum命令安装了，安装之后npm工具也自动装上了。

```
yum install nodejs
npm install -g less
```



## 安装odoo

由于odoo源码和addon生态较大，推荐不通过 `python setup.py install` 的方式安装，而是直接在odoo源码里面运行脚本启动。推荐方式如下，将setup文件夹里面的odoo文件重命名为 `odoo-bin` 然后移到项目主目录上，然后运行：

```
python odoo-bin

```

这样后面调试修改都方便一些。



## 数据库那边的配置

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

### pg_hba.conf 

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



## 初步启动

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

  

## windows下从源码安装

windows下有exe安装包，其会开启一个odoo的后台常驻服务，因为我需要在windows下进行一些早期开发工作，本地网络和调试等等都会便利一些。下面将我从源码启动odoo的一些经验说一下：

1. 原来通过exe安装postgresql数据库还在，原来的数据库和等等其他配置都在，所以这一块就忽略了。

2. nodejs的安装和通过npm安装less就不多说了。

3. 那么下面主要就是odoo的一些python包依赖的安装，安装官方文档的介绍，但不是完全按照官方文档来：

   1. 我加上了pypiwin32包

   2. 原requirements.txt 使用的一些包经过尝试，有几个包通过pip安装不会成功，推荐到 [这里](https://www.lfd.uci.edu/~gohlke/pythonlibs/) 下面对应的安装包，具体版本稍微高一点点没事的：

      ```
      greenlet
      lxml
      MarkupSafe
      Pillow
      pyldap
      reportlab
      
      ```

      官方文档说的 `psutils` 和 `psycopg2`  直接通过pip就安装成功了。到上面下载下来的whl包然后如下安装即可：

      ```
      pip install what.whl
      
      ```

4. 然后如之前所述，将setup文件夹里面的 `odoo` 文件重命名为 `odoo-bin` 然后运行 `python odoo-bin` 即可。

5. 之前说过的 `--save` 选项会在当前目录输出一个 `odoo.conf` 文件，读者可以在里面配置好一些数据库设置，比较重要的有下面几个 ：

   ```
   pg_path = 你安装的postgresql的bin目录
   db_host = localhost
   db_name = False
   db_password = openpgpwd
   db_port = 5432
   db_sslmode = prefer
   db_user = openpg
   
   ```

## odoo.conf 

### 数据库相关

- db_user 数据库连接时的用户名，
- db_password 数据库连接时使用的密码
- db_host 数据库host
- db_port 数据库端口号 默认 5432
- db-filter 正则表达式过滤，不匹配的数据库将会被隐藏（其中 %h hostname %d domain name (?i)%d `(?i)` 是忽略大小写，然后 `%d` 匹配域名名，比如说 `odoo.com` 匹配数据库 `odoo` 或者 `Odoo` 等。）
- db_template 默认 template1

### 网络相关



### 日志相关



### 翻译相关



### 邮箱相关

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



# 初入odoo

本章节主要浅显地讲一下刚进入odoo的界面熟悉，具体更多用户操作和开发者知识等都后面再慢慢讨论。

## 数据库管理界面

数据库管理界面在 `/web/database/manager` 那里，你可以新建数据库（create）；复制数据库（duplicate）；删除数据库（drop）；备份数据库（backup）；恢复数据库（restore）。

我们注销Administor账户，然后就会看到一个登录界面。

## 登录界面

登录界面在 `/web/login` 那里，然后我们也可以看到数据库管理的操作也可以从这里进入。



## Administrator首选项

在右上角Administrator→首选项那里可以设置网站的语言，时区，还有管理员的头像，管理员的邮箱和个性签名。



## 导入一个翻译

看到左侧翻译一栏，点击导入一个翻译即可加载一个翻译。



## 新的Demo用户

看到左侧用户一栏，点击创建一个新用户，即进入创建一个新用户的界面。新建的用户可以先手工设置密码，然后随着你模块的安装不同会给这个用户设置一些权限，从而决定网页导航条那些是可以被这个用户可见的。比如说这个新的Demo用户没有管理员权限，那么就不能看到设置这个选项。



## 模块管理

模块可以是可安装的模块或者叫做应用，比如你的模块的 `__manifest__.py` 那里设置 `'application': True` ，这样你的模块就成为一个应用了。

模块有 安装，更新，卸载操作。其中卸载模块的时候，会把相应的数据库里面关联的数据给清空掉，所以卸载模块前建议先备份一下数据库，这花不了多少时间。

## 修改公司信息

在最左上角那里，鼠标划过会看到编辑公司数据的信息，然后点击进入即可以看到如下的修改公司信息界面:

比如设置公司的Logo，名字，地址，网站等等。然后在设置选单那里还可以设置币种，这个币种设置会影响后面会计模块的默认币种行为。还有一些信息设置能够填上的最好都填上。



## 进销存和财务系统的抽象讨论

进销存和财务软件系统目前大多融为一体了。然后进销存那块以前最开始的软件是仓库管理软件，后面采购和销售是慢慢加上去的。理解这点很重要，我们可以把仓库管理看作最底层的模块，而采购和销售是于之上的模块，然后采购和销售又和财务存在着很多信息交流。具体如下图所示: 

![进销存和财务]({static}/images/odoo/jin-xiao-cun-cai-wu.png)

简单来说就是不管是采购还是销售其一笔成交的订单都必然产生两个信息流，一个是仓管那边；一个是财务那边。而这个信息流的过程最好是由系统自动化完成。下面以采购部门为例子来说明系统内部的这种信息流自动化过程。



### 以采购部门为例

采购部门一般职能是接受其他各部门的采购要求，定期汇总做成采购计划；然后根据采购计划会对相应的供应商询价、议价；然后下采购单；然后跟踪供货商及时发货；货到后验货、入库。如果有问题则要求供应商换货、退货。

首先看采购计划那边，本公司各个部门根据实际需要应该都可以向采购部门发送采购需求，然后某些部门的模块会根据自己的实际情况有自动发送采购需求的功能，比如仓管的最小库存原则，再比如销售部门的某些紧急需求等等（原则上其他部门不紧急的需求应该发送给仓管，然后由仓管根据最小库存原则来发送采购需求，但某些部门具有特别紧急的需求是可以直接给采购部门发送采购需求的。当然还可能某些公司的某些部门的情况是种类繁多库存较小的情况，那么也是可以直接向采购部门发送需求的）。这个信息采购需求的发送机制需要根据不同的公司实际情况进行优化。

对于采购需求，系统应该具备一定的自动整理功能，比如按照供应商分类，紧急程度插队机制等等。采购人员处理经过初步整理出来的采购需求，将这些信息自动生成 **询价单** ，此时系统可以提供电邮，打印询价单的功能，或者和供应商洽谈视频的功能等。询价结束之后对方同意之后采购员可以点击确定然后将这些信息发送给采购部门的经理，由经理确认之后， **采购单** 就自动生成了。

采购单确认之后，前面讲的信息流分成仓管和财务两边。首先我们看仓管那边，在货物还没送到之前，仓管那边就可以看到将要到的货物了，这样他们可以预先对仓库进行整理，方便后面的快速存放工作。货物送到之后首先是采购员验收，验收确认采购单上单击 **收货** ，然后是点击 **入库** 操作，就表示这个货物正式入库了，然后仓管那边对于是什么产品，单价多少，重量多少甚至体积多少都可能有所说明自动存放在软件系统仓管那一栏了。

然后是财务那边，在采购单确定之后，财务那边应该 **接受发票** ，然后点击 **确认生效** ，这是相应的信息应该送到财务那边去了。财务那边还有一些付款事宜。财务付款完了采购员就会看到这个采购单已经完成了。

这里谈论的以采购部门为例的一般流程，这个流程不是死的，也不一定是最优的。具体要根据公司的实际情况的不同和功能需求不同对这些底层的信息流程做出调整和优化。



# 创建自己的addon

## 开发前

Odoo开发的一条黄金准则就是我们最好不要修改现有的模块，特别是官方内置的那些模块。这样做会让原始模块代码和我们的修改混为一谈，使得很难对软件进行升级管理。我们应该创建新的模块（在原有的模块基础之上）来达到修改和扩展功能的目的。Odoo提供了一种继承机制，允许第三方模块扩展现有模块，或者官方的或者来自社区的，这种继承修改可从任意层次来开展，从数据模型到业务逻辑到用户界面。



### 快速生成模块骨架

可以如下快速生成一个模块骨架:

```
python odoo-bin scaffold  mymodule myaddons
```

这将在当前位置新建一个myaddons文件夹，然后在myaddons文件夹下创建一个名字叫mymodule的模块骨架。创建好了之后读者可以进入翻一下。官方推荐的模块结构如下所示：

```
addons/<my_module_name>/
|-- __init__.py
|-- __manifest__.py
|-- controllers/
|    |-- __init__.py
|    `-- controllers.py
|-- demo/
|    |-- <main_model>_data.xml
|    `-- <inherited_main_model>_demo.xml
|-- models/
|    |-- __init__.py
|    |-- modles.py
|-- security/
|    |-- ir.model.access.csv
|-- static/
|    |-- img/
|    |-- lib/
|    `-- src/
|        |-- js/
|        |-- css/
|        |-- less/
|        `-- xml/
`-- views/
    |-- templates.xml
    |-- views.xml
```

上面只是一个泛泛而论的情况，具体有些文件夹或文件可能是不需要的。下面对这些内容进一步说明之。

推荐将所有的模型定义python文件都放入models文件夹中，然后其他一些简要介绍如下：

- demo文件夹 ，放着demo.xml
- controllers文件夹，http路径控制
- views文件夹，网页视图和模板
- static文件夹，网页的一些资源，里面还有子文件夹:css，js，img，lib等等。



### 作为Odoo模块的说明文件

然后本模块作为Odoo框架的模块还必须新建一个 `__manifest__.py` 文件。

scaffold自动创建的 `__manifests__.py`  文件大致内容如下: 

- depends 本模块的依赖关系，这里主要是指本模块对于Odoo框架内其他的模块的依赖。如果本模块实在没什么依赖，就把 `base` 模块填上去。
- data 本模块要加载的数据文件，别看是数据文件，似乎不怎么重要，其实Odoo里面视图，动作，工作流，模型具体对象等等几乎大部分内容都是通过数据文件定义的。具体这些xml或csv文件如何放置后面再讲。
- demo 这里定义的数据文件正常情况下不会加载，只有在demonstration模式下才会加载，具体就是你新建某个数据库是勾选上了加载演示数据那个选项。

其他大体有点类似于pypi包常见的setup.py 文件里面的一些内容：

- name 模块名字
- summary 简短介绍
- description 详细介绍
- author 模块作者
- website 模块网站
- category 模块分类
- version 模块版本号
- license 模块版权信息，默认是AGPL-3
- installabel 默认True，可设为False禁用该模块
- auto\_install 默认False，如果设为True，则根据其依赖模块，如果依赖模块都安装了，那么这个模块将自动安装，这种模块通常作为胶合(glue)模块。
- application 默认False，如果设为True，则这个模块成为一个应用了。你的主要模块建议设置为True，这样进入Odoo后点击本地模块，然后默认的搜索过滤就是 `应用` ，这样你的主模块会显示出来。



### 安装自定义模块

前面说了设置  `--addons-path=addons, myaddons` ，就可以加载自定义的模块了。具体安装就和安装其他模块没有两样，除了你需要清除搜索栏然后输入搜索关键词，如果你的模块是应用的话那么就可以直接在应用面板看到了。然后注意如果模块是第一次安装，那么需要 <u>激活开发者模式</u> ，然后 <u>更新应用列表</u> ，然后找到你想要的模块。

自定义的模块如果只是简单内容修改，那么重启odoo即可当即生效，如果你的模块有数据库也就是模型定义的改动或者其他额外文件的添加等，那么还需要更新该模块。



## 我们的第一个模块

```
python odoo-bin scaffold  first myaddons
```



### controllers

首先修改controllers里面的 `controllers.py` 文件：

```python
from odoo import http

class First(http.Controller):
    @http.route('/first/first/', auth='public')
    def index(self, **kw):
        return "Hello, world"
```

现在请读者安装之前所说的安装和更新自定义模块（也就是激活开发者模式，然后更新模块列表，然后安装模块）。

现在先进入 `/first/first/` 来看一下效果。这里的controllers文件大体类似于的django的views.py文件，里面需要定义一些视图函数。

如果没有什么问题，你应该能看到一行hello world文字，祝你好运。

### views

views文件夹里面的内容更有点类似于django的模板文件，其使用的是odoo自定义的QWeb模板语法，后面会详细讨论之。首先先修改 `__manifest__.py` 文件中data属性，好把目标模板文件加载进来（这个最新的scaffold 命令已经写好了）：

```
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
```

templates.xml文件内容如下：

```xml
<odoo>
    <template id="index">
        <title>我的第一个模块</title>
        <t t-foreach="fruits" t-as="fruit">
            <p><t t-esc="fruit"/></p>
        </t>
    </template>
</odoo>
```

这里使用了Qweb模板语言，就这里提及的我们可以简单了解下:

```
<t t-foreach="[1, 2, 3]" t-as="i">
<p><t t-esc="i"/></p>
</t>
```

其输出是:

```
<p>1</p>
<p>2</p>
<p>3</p>
```



这里的 `<t t-esc="i"/>` 是先计算 i 的值，然后将其打印出来。

然后在之前controllers那里的main.py文件那里，我们使用这个模板文件。

```python
from odoo import http

class First(http.Controller):
    @http.route('/first/first/', auth='public')
    def index(self, **kw):
        return http.request.render("first.index",
                                   {'fruits': ['apple', 'banana', 'pear']})

```



这里调用 `http.request.render` 函数，可以猜到这是一个网页模板渲染输出函数。这次运行你需要加上 `-u first` 来update 目标模块。



### models

熟悉django的同学应该知道这里的models是什么东西，同样odoo也是自己写的ORM接口，废话少说，看代码写法吧：

```python
from odoo import models, fields, api

class Fruits(models.Model):
    _name = 'first.fruits'

    name = fields.Char()

```

### security

security文件夹里面已经有一个 `ir.model.access.csv` 文件了，其对模型的访问权限进行管理，加上记录：

```
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_first_fruits, access_first_fruits,model_first_fruits,,1,0,0,0

```

`group_id:id` 留空，这给所有用户对该模型读的权限。 

然后在 `__manifest__.py` 那里把这个文件挂上：

```
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],

```

### demo

在 `demo.xml` 上加上一些演示数据，方便测试我们写得模块。

```xml
<odoo>
  <record id="apple" model="first.fruits">
    <field name="name">apple</field>
  </record>
  <record id="banana" model="first.fruits">
    <field name="name">banana</field>
  </record>
  <record id="pear" model="first.fruits">
    <field name="name">pear</field>
  </record>
</odoo>

```

这种定义数据的方式是对接之前的模型定义的，也就是上面的 `model` ，然后 `field name="name"` 里面的值就是该记录具体name的值。



然后 `controllers.py` 改成这样了:

```python
from odoo import http

class First(http.Controller):
    @http.route('/first/first/', auth='public')
    def index(self, **kw):
        Fruits = http.request.env['first.fruits']
        return http.request.render("first.index",
                                   {'fruits': Fruits.search([])})

```

而 `templates.xml` 改成这样子了:

```xml
<odoo>
    <template id="index">
        <title>我的第一个模块</title>
        <t t-foreach="fruits" t-as="fruit">
            <p><t t-esc="fruit.id"/> <t t-esc="fruit.name" /></p>
        </t>
    </template>
</odoo>

```

读者可以重启动odoo server来看一下显示效果（请创建一个新的数据库开启了演示模式）。



## 美化网页

odoo有内置模块 `website` ，我们利用它们可以进一步开发出和原odoo网页统一风格的网页界面。

首先我们需要在 `__manifest__.py` 的 "depends" 属性改为:

```
'depends': ['website'],

```

然后是controllers那里加上 `website=True` 这个设置。

```
@http.route('/first/first/', auth='public', website=True)

```

最后是模块文件那里修改为:

```xml
<odoo>
    <template id="index">
        <t t-call="website.layout" >
        <t t-set="title">我的第一个模块</t>
        <div class="oe_structure">
            <div class="container">
                <t t-foreach="fruits" t-as="fruit">
                    <p><t t-esc="fruit.id"/> <t t-esc="fruit.name" /></p>
                </t>
            </div>
        </div>
        </t>
    </template>
</odoo>

```

然后重启odoo server，然后升级模块之后看一下（更新manifest和template）。

在网站的左边有 HTML编辑和主题选择等，在顶上右边有编辑模型等。**注意：** HTML编辑功能经过实验升级模块后会丢失。 

### url route加入参数

```python
    @http.route('/academy/<name>/', auth='public', website=True)
    def teacher(self, name):
        return '<h1>{}</h1>'.format(name)

```

其他的一些东西和django那边很是类似，这里先略过，后面有需要再详细查阅和讨论之，下面主要把如何定制 odoo 自带的商业系统弄清楚。



## data文件

odoo的视图使用xml数据文件表示的，这一块较为陌生，再熟悉一下。

```xml
<odoo>
  <operation/>
   ...
</odoo>

```

odoo标签下的数据就是送给odoo处理的数据。

其后 `operation` 有：

- record  数据库里面的数据更新或新增操作
  - model 要操作的模型
  - id （也就是external id，external id 是存储在 `ir.model.data` 里面的字符串，可用于快速引用某条记录。）
- field  用来给record定义字段数据的
- delete 用来数据库删除数据的
- function 在某个模型上调用某个方法

### 快捷标签

#### menuitem

快速定义一个 `ir.ui.menu` 记录，也就是一个菜单。

#### template

快速创建一个 QWeb 视图，一般继承自别的视图的修改操作推荐使用template。

- id (external id 或者说 xml id)

- inherit_id （继承自，比如是external id）

  

#### report

快速创建一个 `ir.actions.report` 记录。

 

## 定制odoo

本文主要讨论如何深度定制odoo现有的商业体系。

首先是一个菜单（菜单可以有子菜单），然后这个菜单下面是某个模型的记录。那么这个菜单在odoo框架中是如何生成的呢？前面谈到odoo的模型具体的对象实际上就是SQL表格的一条记录，而odoo框架具体显示的菜单也是一个odoo中的一个模型对象，其对应的表格是 `ir_ui_menu` （对应的模型名 `IrUiMenu` ，`_name` 是 `ir.ui.menu` ），其在xml中的声明是通过 `menuitem` 标签来完成的，具体细节等下再讲。然后菜单需要连接一个动作，这样用户点击这个菜单的时候，这个动作将会触发。

这些动作对象是存放在 `ir_act_window` （对应模型名是 `IrActionsActWindow` `_name` 是 `ir.actions.act_window` ）表格中的。动作触发之后接下来是要处理视图问题。

视图这边有所变动，具体视图都是存放在 `ir_ui_view` （对应的模型名是 `View` `_name` 是 `ir.ui.view` ）表格中的，然后找到视图是根据具体的模型和视图类型来的，视图类型默认是列表，还有表单，kanban等等。视图的解析过程是查找目标视图的 primary 视图的 arch 里面的内容，如果目标视图有parent，那么parent的视图也将解析，如果目标视图没有parent，那么arch里面的内容是什么就是什么，子视图也将逐步展开。

比如：

```
select * from public.ir_ui_view where model = 'res.company' ;
```

就会找到和 `res.company` 相关的视图，具体显示要根据目标类型对应的动作的 `view_mode` 这个字段来确定最优先的显示方案。

具体研究对象的模型，视图，菜单，动作等，这些实际上都是odoo里面的模型，也就是具体对象的值是存放在某个具体的SQL表格里的，然后程序完成一系列的索引，取值等操作，并最终生成显示结果，这大概就是odoo框架里面发生的故事概貌了。



### 定制菜单

修改 `views/views.xml` 文件来定义具体的菜单对象：

#### 加入菜单

```xml
<!-- 加入菜单 -->
    <menuitem id="menu_qingjia" name="请假" sequence="0"></menuitem>
    <menuitem id="menu_qingjia_qingjiadan" name="请假单" parent="menu_qingjia"></menuitem>
    <menuitem id="menu_qingjia_qingjiadan_qingjiadan" parent="menu_qingjia_qingjiadan" action="action_qingjia_qingjd"></menuitem>

```

#### 加入动作

```xml
<!-- 打开请假单动作 -->
    <act_window id="action_qingjia_qingjd"
        name="请假单"
        res_model="qingjia.qingjd"
        view_mode="tree,form" />
```

#### menuitem

- name 具体这个菜单在视图中显示的名字。
- sequence 是显示排序。
- parent 是本菜单的父菜单。如果是子菜单则需要指定，只有顶级菜单不需要指定。
- action 指定本菜单连接的动作。如果连接动作了那么name属性可以不用指定了，系统会直接引用动作的name属性的。这里菜单和某个动作关联起来了。和前面联系起来，那么就是具体某个子菜单和某个数据模型关联起来了。

#### act\_window

- name 具体act\_window动作在UI中显示的名字（类似于QT中动作作为菜单中的项目的情况）。
- res\_model act\_window动作对应的某个数据模型（这里动作和数据模型关联在一起了）
- view\_mode act\_window动作打开后支持的视图模式。

### 定制视图

具体可以用的视图定义动作的时候设置：

```xml
    <act_window id="action_qingjia_qingjd"
        name="请假单"
        res_model="qingjia.qingjd"
        view_mode="tree,form" />
```

设置 `view_mode` ，下面定义视图的时候注意声明好模型名即可。

#### 表单视图

```xml
<!--
表单视图
-->
    <record id="qingjia_qingjd_form" model="ir.ui.view">
    <field name="name">qing jia dan form</field>
    <field name="model">qingjia.qingjd</field>
    <field name="arch" type="xml">
        <form>
        <header>
            <button name="btn_confirm" type="workflow" states="draft"
            string="发送" class="oe_highlight" />
            <button name="btn_accept" type="workflow" states="confirmed"
            string="批准" class="oe_highlight"/>
            <button name="btn_reject" type="workflow" states="confirmed"
            string="拒绝" class="oe_highlight"/>
            <field name="state" widget="statusbar" statusbar_visible="draft,confirmed,accepted,rejected" class="oe_highlight" type="workflow"/>
        </header>

        <sheet>
            <group name="group_top" string="请假单">
                <group name="group_left">
                <field name="name"/>
                <field name="beginning"/>
                </group>
                <group name="group_right">
                <field name="manager"/>
                <field name="ending"/>
                </group>
            </group>
            <group name="group_below">
            <field name="reason"/>
            </group>
        </sheet>

        </form>
    </field>
    </record>
```

#### tree视图

```xml
<!--
tree视图
-->
    <record id="qingjia_qingjd_tree" model="ir.ui.view">
    <field name="name">qing jia dan tree</field>
    <field name="model">qingjia.qingjd</field>
    <field name="arch" type="xml">
        <tree>
            <field name="name"/>
            <field name="beginning"/>
            <field name="ending"/>
            <field name="state"/>
        </tree>
    </field>
    </record>
```



### 定义模型

```python
from odoo import models, fields, api

class Qingjd(models.Model):
    _name = 'qingjia.qingjd'

    name = fields.Many2one('res.users', string="申请人", required=True)
    days = fields.Float(string="天数", required=True)
    startdate = fields.Date(string="开始日期", required=True)
    reason = fields.Text(string="请假事由")
    
    def send_qingjd(self):
        self.sended = True
        return self.sended
    
    def confirm_qingjd(self):
        self.state = 'confirmed'
        return self.state
```



- `_name`  定义了本模型具体对应SQL表格的名字，
- `name` odoo模型还需要一个name字段，很多显示和搜索行为都依赖于它。
- `required` 如果设置为True则该字段为必填项
- `string` 不写的话第一个参数就是这个，具体就是这个字段在用户界面的显示文字
- `default` 默认值

- `Char` 具体定义了一个字符串输入字段，Char() 函数可以接受一些可选参数，比如 `string` 表示本模型为用户可见的名字； `required`； `help` 在用户UI界面下的帮助信息； `index` 布尔值，默认是False，如果为True则要求在数据库中为这列创建一个索引(index)。
- `Boolean` 布尔值 
- `Integer` 整数值 
- `Float` 浮点数值
- `Text` 大段文本输入
- `Selection` 几个值的选择
- `Html`
- `Date`
- `Datetime`
- `Many2one` 关系 many to one 字段
- `One2many` 关系one to many 字段
- 

然后我们在pgadmin3前面的介绍中也看到了，此外还有创建一些其他的表头字段:

- `id` 在表格中一条记录的独特id
- `create_date` 创建日期
- `create_uid` 谁创建的
- `write_date` 最后修改日期
- `write_uid` 谁最后修改的

odoo8之后推出了新的ORM api语法，下面详细讨论之。这块内容主要参考了 [odoo new api guideline](https://github.com/nbessi/odoo_new_api_guideline) 这个项目。

#### 什么是Recordset

新的API引入一个核心的概念就是 Recordset ，Recordset是个什么东西呢？就是前面讲的某一个模型（类）的所有对象（具体的实例）的集合就是一个Recordset对象。——这是recordset最大的情况，一个重要的限定条件就是其内元素必定是相同模型的，由这个最大的集合情况然后删除过滤掉一些元素（记录）之后仍然是recordset对象。

按照官方文档的描述是，一个Recordset对象应该是已经排序了的同一模型的对象的集合。他还指出虽然现在还可以存放重复的元素，这个以后可能会变的。同时你从名字可能猜到这个Recordset对象应该支持集合的一些操作，事实确实如此。

比如Recordset支持如下运算:

```
record in recset1     # include
record not in recset1 # not include
recset1 + recset2     # extend 
recset1 | recset2     # union
recset1 & recset2     # intersect
recset1 - recset2     # difference
recset.copy()         # copy the recordset (not a deep copy)
```

上面的操作只有 `+` 还保留了次序，不过recordset是可以排序的，关于次序比如使用:

```
for record in recordset:
    print(record)

```

具体的次序是否像集合set一样是不一定的还是如何呢？这里需要进一步的讨论。





#### `@api.multi`

默认行为就是这个，比如要返回一个 RecordSet，那么就返回RecordSet，并没有额外的操作。



#### `@api.one`

如果加上这个装饰器，那么方法里面的 `self` 是具体对应的本模型 RecordSet 的一条记录（也就是在multi装饰器的基础上，使用这个one装饰器，将自动循环每条记录）。

```python
    @api.one
    def do_toggle_done(self):
        self.is_done = not self.is_done
        return True

    @api.multi
    def do_clear_done(self):
        done_recs = self.search([('is_done', '=', True)])
        done_recs.write({'active': False})
        return True

```



#### domain语法

本小节主要参考了 [这个网页](http://stackoverflow.com/questions/14608775/how-to-filter-datas-in-openerp-using-domain-list) 。

Odoo里面的domain语法使用比较广泛，其就好像一个过滤器，应该对应的是SQL的SELECT语句。最基本的语句形式是 `[('field_name', 'operator', value)]`



- field\_name 必须是目标模型的有效field名字。
- operator 比如是一个字符串，可用的值有: `= != > >= < <= like ilike` , 此外还有"in", "not in", "parent\_left", "child\_of", "parent\_right"。这里的parent和chind似乎是某种记录的关系，先暂时略过。其他的意义都是很明显的。
- value 必须是和前面的field\_name类型相同的某个值。

然后这些圆括号包围的基本语句可以用以下几个逻辑运算符连接: `&  | !` ，其中 `&` 是默认的逻辑运算连接符，也就是你看到两个圆括号表达式中间没有逻辑运算连接符，则要视作其间加入了 `&` 。具体形式大概类似这样:

```
[('field_name1', 'operator', value), '!',  
    ('field_name2', 'operator', value), '|', 
    ('field_name3', 'operator', value),('field_name4', 'operator', value)]

```

多个逻辑运算符的情况有点复杂，具体是 `!` 先解析，其只作用于后面的第一个元素；然后 `&` 和 `|` 作用于后面的两个元素。一个简单的解析步骤是先将 `!` 解析进去，比如是解析为不是等，然后再将 `|` 解析进去，相当于一个并联电路接进来，然后所有的过滤条件组成一个大的串联过滤线路。这样上面的表达式就解析为:

```
1表达式 and 2表达式否 and 3表达式或4表达式

```

然后前面的那个domain:

```
domain = [('is_done', '=', True),
'|', ('user_id', '=', 'self.env.uid'),
('user_id','=',False)]

```

应该解析为:

```
is_done是True and user_id 是self.env.uid 或 user_id是False

```

#### search方法

一个recordset对象调用其search方法还是返回一个recordset对象。

search方法接受一个参数，这个参数就是前面谈论的基于odoo domain语法的过滤器表达式。

所以下面这个表达式:

```
self.env[’res.users’].search([(’login’, ’=’, ’admin’)])

```

的含义就是调用 `res.users` 这个表格或者说recordset，然后执行search方法，具体选中的record是login这个字段等于admin的。

接下来执行search方法，返回的done\_recs也是一个recordset对象，对于这些recordset对象执行了 write 方法，其接受一个字典值，就是直接更改SQL表格里面的某个表头（属性），将其改为某个值。值得一提的是，recordset调用write方法会将本recordset内所有的record都进行修改操作的。

前面讲到通过 super() 来继承修改原模型的某个方法，请看下面的例子:

```python
@api.one
def do_toggle_done(self):
    if self.user_id != self.env.user:
        raise Exception('Only the responsible can do this!')
    else:
        return super(TodoTask, self).do_toggle_done()

```

这里 `@api.one` 自动遍历目标recordset，然后方法里面的self就是一个record。这里程序的逻辑很简单，就是如果用户名不是当前登录用户（因为todo task管理只是自己管理自己的任务计划），那么将会报错。如果是那么就调用之前的方法。

#### write方法

```
done_recs.write({'active': False})

```

在 `api.one` 方法下，每一次对属性的修改都将产生一次Record的write行为:

```
@api.one
def dangerous_write(self):
  self.x = 1
  self.y = 2
  self.z = 4

```

推荐如下进行 write 操作：

```python
def better_write(self):
   for rec in self:
      rec.write({'x': 1, 'y': 2, 'z': 4})

# or

def better_write2(self):
   # same value on all records
   self.write({'x': 1, 'y': 2, 'z': 4})

```

#### `self.env`

- `self.env.user` 当前用户
- `self.env.lang` 当前语言
- `self.env['res.users']` 获取某个模型对象
- `self.env.cr.execute` 执行sql语句







## 继承修改odoo

### 扩展现有模块

即使是对于现有的模块，推荐的做法也是通过新建一个模块来达到扩展和修改现有模块的目的。具体方法就是在python中的类里面使用 `_inherit` 属性。这标识了将要扩展的模块。新的模型继承了父模型的所有特性，我们只需要声明一些我们想要的修改就行了。通过这种继承机制的修改可从模型到视图到业务逻辑等对原模块进行全方位的修改。

实际上，Odoo模型在我们定义的模型之外，它们都在注册中心注册了的，所谓全局环境的一部分，可以用 `self.env[model name]` 来引用之。比如要引用 `res.partner` 模型，我们就可以写作 `self.env['res.partner']` 。

#### 给模块增加field

如下代码就是首先通过 `_inherit` 继承原模块，然后再增加一些field:

```
from odoo import models, fields, api

class TodoTask(models.Model):

	_inherit = 'todo.task'

	user_id = fields.Many2one('res.users',string='Responsible')
	date_deadline = fields.Date('Deadline')

```

关于 `res.users` 和 `res.partner` 具体是雇员还是合作伙伴什么的，这个以后再摸清楚，这里先简单将其看作一个SQL表格，然后Many2one前面讲过了就是根据某个给定的SQL表格来生成一个下拉选单，具体是引用的该SQL表格的那个表头属性，这里应该还有一个细节讨论。

不管怎么说，现在我们通过新建一个模块 todo\_user ，如前面描述的将模块设置配置好之后，原模块 todo\_app 的todo.task模型就增加了新的两个field了，也就是两个新的表头了。

#### 修改已有的field

按照上面的继承机制，我们可以如上类似处理，只修改你希望更改的某个field的某个属性即可。如下:

```
name = fields.Char(help="can I help you")


```

这样原模型的namefield额外增加了help帮助信息了。



#### 重载原模型的方法

读者一定已经想到了，类似的在这种继承机制下，可以通过重写原模型的方法来重载该方法。事实上确实可以这样做，而这里要讲的是还有一种更加优雅的继承原模型的方法，那就是通过 `super()` 来调用父类的方法。

首先我们看到下面这个例子:

```python
@api.multi
def do_clear_done(self):
    domain = [('is_done', '=', True),
    '|', ('user_id', '=', 'self.env.uid'),
    ('user_id','=',False)]
    done_recs = self.search(domain)
    done_recs.write({'active':False})
    return True


```





### 视图的继承修改

本小节主要参考了 [这篇文章](http://www.jeffzhang.cn/Odoo-Notes-2/) ，一个简单的例子如下所示：

```xml
        <template id="product_item_hide_no_price" inherit_id="website_sale.products_item">
            <xpath expr="//div[hasclass('product_price')]/b" position="attributes">
                <attribute name="t-if">product.price > 0</attribute>
            </xpath>
        </template>

```

其大体分为三步：

1. 推荐使用 template 标签来创建一个 QWeb 对象
2. 用 `inherit_id` 来描述继承关系
3. 实际修改，修改有三种方法，下面具体描述之。

#### xpath+expr

xpath用 expr 来进行xpath语法定位，找到的第一个将用于下面的修改操作。

#### field+name

field 用 name 来过滤属性，对找到的第一个field进行操作

#### 其他

第一个元素有相同的name和属性的将进行操作

#### position

position 决定对选中的节点如何操作

- inside 默认，附加在选中的节点上
- replace 替换
- after 作为选中节点的兄弟节点附加进来
- before 作为选中节点的兄弟节点插入之前
- attributes 

- `attributes` 修改选中节点的属性值 后面必须跟着 `<attribute> ` 标签。

## 定制odoo实战

### 寻根问底第一谈



res.company 模型对应的 

```
select * from public.ir_ui_menu where parent_id is null  ;
```

我们看到 settings -> 4  ，然后我们继续：

```
select * from public.ir_ui_menu where parent_id = 4  ;
```

看到 User & Company 的 id 是 7 ，

然后继续我们找到 Company 子菜单的 id 是54，其对应的action是 `"ir.actions.act_window,44"` ， 也就是其对应的是 第 44  号 动作，然后我们继续：

```
select * from public.ir_act_window where id = 44 ;
```

我们看到这个动作对应的 模型就是 `res.company` 。启动的 `view_mode` 定义显示方案。具体视图是

```
select * from public.ir_ui_view where model = 'res.company' ;
```

就会找到和 `res.company` 相关的视图。

现在假设我们我要定义res.company 的某个视图，首先我们激活开发者模式，然后到目标视图那里，点击 `Fields View Get` ，我们看到 `form` 开头，也就是当前是表单视图。于是我们继续：

```
select name,arch_db from public.ir_ui_view where model = 'res.company' and 
        type = 'form' order by priority ;
```

具体视图的名字只是方便描述记忆用的，也不是xml里面方便引用的external id，priority这个字段也定义了继承关系的顺序。

首先我们看到第一个视图内容：

```xml
<?xml version="1.0"?>
<form string="Company">
<sheet>
<field name="logo" widget="image" class="oe_avatar"/>             
<div class="oe_title">
<label for="name" class="oe_edit_only"/> (...)"
```

这应该内容还没有定义完，不会这么短，所以我们还是要在xml那边查找定义，现在我们可以根据name来查找xml了。我们首先获得下面这两个xml：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<odoo>
    <data>
        <record id="view_company_form" model="ir.ui.view">
            <field name="name">res.company.form</field>
            <field name="model">res.company</field>
            <field name="arch" type="xml">
                <form string="Company">
                  <sheet>
                    <field name="logo" widget="image"  class="oe_avatar"/>
                    <div class="oe_title">
                        <label for="name" class="oe_edit_only"/>
                        <h1>
                            <field name="name"/>
                        </h1>
                    </div>
                    <notebook colspan="4">
                        <page string="General Information">
                            <group>
                                <group>
                                    <field name="partner_id" readonly="1" required="0" groups="base.group_no_one"/>
                                    <label for="street" string="Address"/>
                                    <div class="o_address_format">
                                        <field name="street" placeholder="Street..." class="o_address_street"/>
                                        <field name="street2" placeholder="Street 2..." class="o_address_street"/>
                                        <field name="city" placeholder="City" class="o_address_city"/>
                                        <field name="state_id" class="o_address_state" placeholder="State" options='{"no_open": True}'/>
                                        <field name="zip" placeholder="ZIP" class="o_address_zip"/>
                                        <field name="country_id" placeholder="Country" class="o_address_country" options='{"no_open": True}'/>
                                    </div>
                                    <field name="report_header" placeholder="e.g. Global Business Solutions"/>
                                </group>
                                <group>
                                    <field name="website" widget="url" placeholder="e.g. www.odoo.com"/>
                                    <field name="phone"/>
                                    <field name="email"/>
                                    <field name="vat"/>
                                    <field name="company_registry"/>
                                    <field name="currency_id" options="{'no_create': True, 'no_open': True}" id="company_currency"/>
                                    <field name="parent_id"  groups="base.group_multi_company"/>
                                    <field name="sequence" invisible="1"/>
                                    <field name="report_footer" placeholder="e.g. Your Bank Accounts, one per line"/>
                                </group>
                                <group name="social_media"/>
                            </group>
                        </page>
                    </notebook>
                    </sheet>
                </form>
            </field>
        </record>
     
```

```xml
        <record id="action_view_company_form_link_2_currencies" model="ir.ui.view">
            <field name="name">res.company.form</field>
            <field name="model">res.company</field>
            <field name="inherit_id" ref="base.view_company_form"/>
            <field name="arch" type="xml">
                <xpath expr="//field[@id='company_currency']" position="after">
                    <label for="id" invisible="1"/>
                    <p class="text-muted">
                        <a href="" type="action" name="%(base.action_currency_all_form)d">Activate more currencies</a>.
                    </p>
                </xpath>
            </field>
        </record>
```

然后我们对照 `Fields View Get` 看一下，大体就是这些内容了。然后我们再来分析一下第二个xml的视图继承修改动作。去看看，果然 `<field name="currency_id"` 后面插入了这些内容。



### pruchase模块研究

#### 删除询价单子菜单

这边直接创建采购单即可，不需要询价单，首先将询价单子菜单去除。我们找到采购的子菜单id 号是 265，然后继续：

```
select * from public.ir_ui_menu where parent_id = 265  ;

```

我们看到目标子子菜单是：

```
id parent_left parent_right name   active sequence parent_id web_icon action
278;206;207;"Requests for Quotation";t;0;265;"";"ir.actions.act_window,375"

```

然后我们需要把这个子子菜单的menuitem记录删除掉，具体查询到的是xml语句：

```xml
        <menuitem action="purchase_rfq" id="menu_purchase_rfq"
            parent="menu_procurement_management"
            sequence="0"/>

```

于是有：

```xml
<delete id="purchase.menu_purchase_rfq" model="ir.ui.menu"></delete>

```

#### 采购订单直接生成采购单

然后我发现现在点击了之后还是生成的询价单，我希望是开始编辑采购单，也就是彻底取消询价单功能。之前我注意到下面 376 动作就是对应的就是采购单那边的。然后采购订单这边的试图还需要进一步研究，我们已经明确了要研究的模型的 `purchase.order` 。

我们先查看视图那边的情况：

```sql
select * from public.ir_ui_view where model = 'purchase.order' ;

```

深感现在要自如定制，还欠缺一点火候，下面继续深入学习odoo内部视图模型等等各方面的机制，然后再回到这个问题上来。

------



## 继续深入学习odoo内部机制

### controller

```python
class Academy(http.Controller):
    @http.route('/first/teachers/', auth='public', website=True)
    def index(self, **kw):
        Teachers = http.request.env['academy.teachers']
        return http.request.render("first.index",
                                   {'teachers': Teachers.search([])})

```

1. 通过`http.request.env` 来获取模型对象，通过调用 `search` 方法来获取所有记录。
2. 通过 `http.route` 装饰器来指定url分发规则，通过auth来指定认证规则，通过website来使用QWeb模版。
3. 通过 `http.request.render` 来通过模版渲染网页，第一个参数是本模块的名字加上template id来选定模版，后面的字典值来返回一些参数供网页模版调用。

url接受参数和类型限定，

```python
    @http.route('/academy/<int:id>/', auth='public', website=True)
    def teacher(self, id):
        return '<h1>{} ({})</h1>'.format(id, type(id).__name__)

```

或者指定odoo内部的某个模型：

```python
    @http.route('/first/<model("academy.teachers"):teacher>/', auth='public', website=True)
    def teacher(self, teacher, **kw):
        return http.request.render('first.biography', {
            'person': teacher
        })

```

### security

```
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_first_teachers, access_first_teachers,model_academy_teachers,,1,0,0,0

```

前面的id和name名字都不是特别限定死，关键是 `model_id:id` 这个字段，名字一定是 `model_<model_name>` 这个里面的 `model_name` 和 `request.env` 或者在定义模型的时候 `self.env` 的引用都是一样的，只是这里的  `model_name` 只是将点号换成了下划线。

### template

QWeb那边继续学习，QWeb里面原html标签直接写上就是了，区别就是 `t-` 开头的那些 QWeb 属性，或者 `t` 标签在条件渲染中不会渲染出来：

#### t-if

```
<t t-if="condition">
    <p>Test</p>
</t>

```

若条件符合，也只是输出：

```
<p>Test</p>

```

而：

```
<div t-if="condition">
    <p>Test</p>
</div>

```

的输出是：

```
<div>
    <p>Test</p>
</div>

```

#### t-call

```
<t t-call="website.layout" >

```

调用子模板，

#### 循环渲染

```xml
                <t t-foreach="teachers" t-as="teacher">
                    <p><t t-esc="teacher.id"/>
                        <a t-attf-href="/first/{{slug(teacher)}}">
                             <t t-esc="teacher.name" />
                        </a>
                    </p>
                </t>

```

对某个参数递归，每个递归值由 `t-as` 指定，然后获取数值。 `t-esc` 接受一个表达式，然后估值然后打印出其内容。

#### t-attf-*

渲染某个属性，其值是个字符串 format 语句。





# 库存管理

1. 创建供应商
2. 创建产品：
   1. 库存产品，可消耗产品，服务类产品
   2. 供应链 制造： 内部制造或者内部服务；购买，通过采购订单从供应商处购买；MTS 仓库有足够的货物满足客户，
   3. 在手产品，可用产品
3. 初始库存 创建一个库存调整，然后点击开始盘点
4. 和销售流程的集成，选择一个客户，创建一个报价单，添加产品，确认销售，点击交货
   库存那边如果产品的供应链可用，则显示调拨单，手工检查可用，处理产品，完成数量，验证交货 确认
5. 和采购流程的集成，采购那边，创建询价，确认订单，询价单变成采购单之后同时调拨单也生成了，点击发货。库存那边，查找入库送货，然后点击处理产品，然后通过扫描枪扫描或者odoo确认来验证收货单。
6. 确立订货规则，一个好的仓管系统会让你的货物存量既不要太低也不要太高，通过odoo的订货规则，来做到这点。在可库存产品中输入最小和最大数量
7. 



# 采购

[TOC]

采购必然有一个采购单（Purchase Order），也可能是由询价单或者采购招标自动生成出来。

销项税 销售额*税率

进项税 购买货物支付的税额

应缴税 = 销项税 -  进项税 

条形码 barcode 

产品模版 野马牌T恤衫， S 蓝色 是产品变量 具体的尺寸和颜色是属性，每一个产品变量都对应一个barcode条形码

每一个产品变量都有自己的price 价格，具体是 price = template price + variant price

存货（Inventory）

Picture （和每个产品变量绑定）

Other Field 大部分field和产品模版关联，如果你改变他们，所有的相关产品变量都将改变

## 激活产品变体特性

销售- 设置- 产品变体

添加产品 - 



## 采购

1. 创建询价单 -  保存 - 确认询价单 -  创建采购订单 保存 
2. 接受产品的时候要点击 **接受产品**  （确认送货）
3. 供应商账单 （登记付款）



# 会计



## 会计学入门

会计系统反映了企业的两个基本方面: 自己有什么和欠别人什么。资产(assert)是企业拥有或控制的能够给企业带来未来经济效益的资源。例如: 现金，物料，设备和土地等。负债(liabilities)是企业欠非其所有者（债权人）的债务，未来需要用现金、产品或服务来偿还。权益(equity)是指企业所有人对企业资产所享有的求偿权。

总的来说有:

```
资产 = 负债 + 所有者权益
```

负债已经放在所有者权益前面，因为负债应该先被满足。此外还有一个扩展的会计公式:

```
资产 = 负债 + 所有者名下的资本 - 所有者提取 + 收入 - 费用
```

其中收入减去费用的部分便是净利润(net income)，如果费用大于收入，则会产生净损失(net loss)。

常见的经济业务:

- 所有者投资 谁成立了一家公司，然后以该公司的名义存了多少钱，创始人的这笔钱叫做所有者投资，属于前面的所有者权益中的所有者名下的资本。
- 用现金采购物料 这是将公司的现金资产转变成为另一种资产(物料)，这项经济业务仅仅改变了资产形式。
- 用现金购买设备 这和上面类似，也仅仅改变了资产形式，公司资本总数量还是没变。
- 赊购物料 公司资产增加，赊的钱属于公司的负债。
- 提供服务赚取现金 资产现金部分增加，右边属于收入增加。
- 用现金支付费用 资产现金部分减少，右边费用增加，然后减去。
- 用赊销的方式提供服务或出租设备 左边资产应收款项部分增加，右边收入部分增加。
- 应收账款变现 左边资产由应收款变为现金，右边没有变化。
- 支付应付款项 应付款项在左边属于现金减少，在右边属于负债减少。
- 所有者提取现金 在左边资产现金减少，右边所有者权益减少。



## 财务报表

利润表
所有者权益表
资产负债表
现金流量表

## 原始凭证

原始凭证可以是纸质的也可以是电子版的，主要有: 销售发票，支票，订货单，供货商签发的账单，员工收入记录，银行对账单等。

## 账户

资产类账户 = 负债类账户 + 所有者权益账户

### 资产类账户

资产是指企业拥有或控制的预计在未来能够给企业带来一定的经济效益的资源。大多数会计系统都包含以下账户:

- 现金账户(cash) 反映企业的现金金额，现金的增减变动情况都要记录在现金账户中。

- 应收款项(account receivable) 是指卖方持有的买房对卖方的付款承诺。
- 应收票据(note receivable) 也称为期票，是一种书面承诺，承诺在未来某个特定时间还款。

- 预付款项(prepaid accounts) 代表着提前支付的未来费用。
- 物料(supplies) 在被使用完之前属于资产，使用完之后成本将被记入费用账户。

- 设备(equipment) 也是一项资产，随着设备的使用和耗费，其成本将一点点列为费用，这种费用成为折旧。
- 建筑物(buildings)

- 土地(land)

### 负债类账户

比较常见的负债类账户有:

- 应付款项(account payable) 口头的或暗含以后要付款的承诺。
- 应付票据(note payable) 较为正式的未来付款承诺。
- 预收账款(unearned revenues) 未来企业提供产品或劳务才能清偿的负债。
- 应计负债(accrued liabilities) 企业所欠的尚未偿还的负债。

### 所有者权益账户

按照前面提及的扩展会计公式，所有者权益账户分为: 所有者名下资本，所有者提取，收入和费用。

## 分类帐

信息系统中所有账户的集合叫做分类帐。

## 会计科目表

企业所使用的所有账户名称及其编号的列表叫做会计科目表。

具体编号中的科目号有国标的规定，然后子目号有的省市有规定，如果没有则自己内定。 比如按照 \href{http://blog.sina.com.cn/s/blog_60dc73f50100kq6l.html}{这个网页} 的介绍，资产类编号首位科目号是1，负债是2，所有者权益是3等等。

## 报告期间

比如有年度财务报表，报告期为一年的会计报告，或者还有一个月，一季度等中期财务报告。



1. 设置公司信息
2. 设置银行账户 （科目编号翻译应改为银行帐号） 银行识别码实际上就是银行的swift code  或者称之为 BIC bank identifier code
3. 科目表 安装中国科目表
4. 税 创建税项，设置销售和采购的默认税项，当公司开发票的时候，系统会自动考虑这些税项。
5. 多币种支持，这个暂时不用考虑
6. 一旦开始一项新的业务，需要创建客户和供应商
7. 然后公司运营的实物或者服务称之为产品，需要创建公司的产品



## 用户角色权限

1. 专员 限制访问级别，专门处理开单
2. 经理 完全访问，有会计应用的全部权限，
3. 主管 高级访问，记录发票，管理银行费用，核销日记账分录



## 客户流程

### 转账付款

1. 创建一个客户发票
2. 登记银行对账单
3. 核销银行对账单

### 支票付款

1. 创建一个客户发票
2. 在发票界面登记付款
3. 创建存款单
4. 登记银行对账单
5. 已有交易核销

### 客户催款

1. 核销银行对账单
2. 查看未付款发票
3. 发催款信



## 供应商流程

### 登记账单

1. 创建账单
2. 现金交易
3. 审核账单



### 账单付款

1. 标记账单为待付款
2. 打印支票或生成付款单

### 核销银行对账单

自动核销银行对账单



# 附录





## 模型表格清单

### 本页使用说明

子标题为模型具体通过 `self.env[name]` 可调用的名字，然后通过代码演示了该模型的具体代码定义的模型名或者也写上表格名。

### base.language.install

```
class BaseLanguageInstall(models.TransientModel):
    _name = "base.language.install"
```

### res.company

```
class Company(models.Model):
    _name = "res.company"
```

### purchase.order

```
class PurchaseOrder(models.Model):
    _name = "purchase.order"
```



### res.users

res.uses 在网页视图下对应的菜单是: 设置→用户。 这个表格（或说模型）存储着一些登录用户的信息，比如用户名或密码等。



## 参考资料



1. [wiki商业智能](https://zh.wikipedia.org/wiki/\%E5\%95\%86\%E4\%B8\%9A\%E6\%99\%BA\%E8\%83\%BD) [wiki ERP](http://en.wikipedia.org/wiki/Enterprise_resource_planning)
2. ERP不花钱, 作者: 老肖（OSCG）, 版本:  1.0 
3. Odoo Development Essentials , author: Daniel Reis , date: April 2015
4. [OdooV10 官方文档](https://www.odoo.com/documentation/user/10.0/zh_CN)
5. Odoo new API guideline Documentation , author: Nicolas Bessi , date: April 13, 2015 .
6. 会计学原理 第19版 作者: John J.Wild , Ken W. Shaw 等. 崔学刚译, 中国人民大学出版社.













