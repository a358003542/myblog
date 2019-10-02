Title: luigi模块
Slug: luigi-module
Date: 2018-01-13 20:56
Modified: 2018-01-13 20:56
Tags: luigi, workflow,
Status: draft

[TOC]

## 简介

luigi模块其实很早以前就接触过，但因为当时没有特别的需求所以对这个模块还是处于一种浅尝辄止的状态。到现在因为各种数据处理任务，开始强烈感觉到需要一个大的框架来管理这些小的数据处理脚本任务，使之更加的自动化和流程化。然后我开始找相应的软件，最后发现相关的软件不是少而是杂而多，请读者参看 [这篇文章](http://ju.outofmemory.cn/entry/221885) 。

首先有这么多项目证明程序员对于这个软件需求是很强烈的，但是如此的杂乱，大概两三百个，没有像scrapy或者django那种特别出色脱颖而出的项目，这多少是令人遗憾的。这也间接反应了这个问题，那就是这方面任务，恐怕最后还是要靠程序员自己编写大量定制代码来完成任务，而不能完全依靠某个工具。

我选luigi学习的原因无非有二：

1.  python
2.  github星数靠前

其实之前对luigi似乎是不太满意的，官方文档是一部分原因，可能以前对这块需求也不是特别强烈是一部分原因，或者还有其他？但还是决定硬着头皮学习，然后再慢慢定制吧。

## 定义任务

首先当然是定义任务，其继承自 `luigi.Task` ，其内有特殊含义的方法有： 

-   run 实际执行任务的动作
-   output 描述任务的输出对象
-   requires 描述任务的依赖

### requires

返回某个任务对象或者某些任务对象列表，作为本任务的前置任务。看得出来作为任务对象的一些参数是区别对待的，比如即使是依赖于本对象，如果参数是前一日期时间，则需要上一任务完成之后再执行本任务。

### 依赖于某个Target

可以如下创建一个 `ExternalTask` ：

```python
class LogFiles(luigi.ExternalTask):
    date = luigi.DateParameter()
    def output(self):
        return luigi.contrib.hdfs.HdfsTarget(self.date.strftime('/log/%Y-%m-%d'))
```

然后依赖于这个外部文件对象，当目标文件对象创建之后，才会进行下面的任务。

### Parameter对象

任务类里面可以定义一些 Parameter 对象，当我们通过命令行调用该任务的时候，可以提供这些参数。

```
date = luigi.DateParameter(default=datetime.date.today())
date_interval = luigi.DateIntervalParameter()
use_hadoop = luigi.BoolParameter()
```

### input方法

input方法是luigi框架里面任务对象调用本任务的前依赖输出对象的便捷方法，比如你使用 `self.input` ，就对应本任务的 requires Target 对象，或者说当你调用 `self.input()` 实际上得到的就是 `self.requires()` 的输出。

## 运行任务

```
luigi --module autowriting.workflow examples.HelloWorldTask --local-scheduler
```

一般生产环境会去掉 `--local-scheduler` 然后使用中央调度器，你需要用 

```
luigid
```

来开启它。

默认你可以在localhost的 `8082` 端口看到监视任务的画面。






## Target对象

描述任务的观察对象，比如硬盘里的某个文件或者数据库里的某条记录，其内部唯一具有特殊含义的方法就是 `exists` ，其用来判断目标对象是否存在，如果存在则返回True，如果不存在则返回False。



-   LocalTarge 描述本地磁盘文件对象
-   `luigi.contrib.mongodb.MongoTarget` mongodb target
-   `luigi.contrib.mongodb.MongoCellTarget` 具体到mongodb的某个doc的某个属性
-   `luigi.contrib.mongodb.MongoRangeTarget` mongodb的某些doc的某个属性
-   

## 日志管理

luigi 的日志不做任何调配的话，就是默认的 `luigi-interface` 然后流打印到终端。如下所示：

```python

def setup_interface_logging(conf_file='', level_name='DEBUG'):
    # use a variable in the function object to determine if it has run before
    if getattr(setup_interface_logging, "has_run", False):
        return

    if conf_file == '':
        # no log config given, setup default logging
        level = getattr(logging, level_name, logging.DEBUG)

        logger = logging.getLogger('luigi-interface')
        logger.setLevel(level)

        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(level)

        formatter = logging.Formatter('%(levelname)s: %(message)s')
        stream_handler.setFormatter(formatter)

        logger.addHandler(stream_handler)
    else:
        logging.config.fileConfig(conf_file, disable_existing_loggers=False)

    setup_interface_logging.has_run = True
```

如果我们在运行luigi命令的工作目录下写上配置文件 `luigi.cfg` :

```
[core]
logging_conf_file=luigi_logging.cfg
```

然后在 `luigi_logging.cfg` 里面写上一些logging的配置：

```
[loggers]
keys=luigi,root

[logger_luigi]
handlers=custom
qualname=luigi
level=DEBUG
propagate=0

[logger_root]
handlers=output

[formatters]
keys=simple

[formatter_simple]
format=%(asctime)s %(name)s [%(levelname)s] %(thread)d %(module)s %(funcName)s %(lineno)s: %(message)s

[handlers]
keys=output,custom

[handler_output]
class=StreamHandler
formatter=simple
args=(sys.stdout,)

[handler_custom]
class=FileHandler
formatter=simple
args=('logs/luigi.log',)
```

这样所有的日志将输出到你指定的文件下。

具体请进一步 参看 `logging.config.fileConfig` 中配置文件的写法。具体在luigi的任务脚本中如下使用 logger：

```python
import logging
logger = logging.getLogger('luigi')
```

遗留的问题有：

1.  更多的logger -> 多些几个就是了。
2.  RotateFileHandler 怎么加载 -> 如下写法： 

```
class=logging.handlers.RotatingFileHandler
args=('logs/elasticsearch_sync.log', 'a', 200000)
```

3.  经过测试每个logger的 `qualname` 参数不能省略。


**NOTICE** : logger最好放在任务类里面，否则你彼此引用任务脚本会把环境污染了。




## 所有任务集中于一个任务

所有的任务每天都执行一次。

```
class AllReports(luigi.WrapperTask):
    date = luigi.DateParameter(default=datetime.date.today())
    def requires(self):
        yield SomeReport(self.date)
        yield SomeOtherReport(self.date)
        yield CropReport(self.date)
```

## 执行循环任务

```
luigi --module all_reports RangeDailyBase --of AllReports --start 2015-01-01
```

