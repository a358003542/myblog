Slug: pelican-source-code





[TOC]



### 前言

本文的讨论基于pelican version **4.7.1** 。

本文主要以pelican命令为切入口来对pelican模块的核心内容进行讨论，其他辅助性质的工具和其他细枝末节的内容将会忽略掉，忽略讨论的内容有：

- pelican-import 
- pelican-quickstart
- pelican-themes
- pelcan-plugins
- 命令行listen参数，这个只是pelican额外提供的辅助工具，自己另外再用python的 `http.server` 模块启动一个效果都是一样的。

### 初始化日志

这是进入pelican模块必做的第一件事情。

```
def init(level=None, fatal='', handler=RichHandler(console=console), name=None,
         logs_dedup_min_level=None):
```

fatal参数另外封装了一下LimitLogger来实现的，主要是实现warning或者error日志的时候程序就终止。

logs_dedup_min_level默认是 `logging.WARNING` ，也就是warning级别之上的日志都会打印出来。

然后是利用 `logging.basicConfig` 进行了一些基本的日志打印格式调整。

`RichHandler` 利用的是另外一个rich模块，主要是美化终端输出格式，这些简单了解下即可。

pelican的log.py里面最核心的内容就是LimitLogger加载了LimitFilter，其filter函数实现了日志过滤功能。

1. 日志级别大于`logging.WARNING` 的必打印
2. 如果该日志文件编号`record.levelno` 和 日志信息重复，则不再打印。
3. 对接 `LOG_FILTER` 配置。填写的这些日志将会被过滤。
4. 如果日志接受额外的参数 `limit_msg` ，默认阈限是5，也即是报告五次之后不再报告。

日志这块pelican就是做了上面所述的这些调整，简单了解下即可。

### 命令行参数和配置文件加载

命令行参数和配置文件加载这里就不专门讨论了，这些内容有些在pelican的使用中已有所接触，有些后面提到什么参数什么配置就默认加载进来了。

配置的相关选项和默认值在 `settings.py` 哪里有，这块查看源码或者查看文档的说明即可，不作过多讨论了。

### autoreload

pelican命令行对应的`__main__`里面的main函数，里面最核心的逻辑，在忽略掉listen之后就是两个分支：一个是autoreload参数填入，则执行：

```
autoreload(args)
```

一个是没有autoreload参数则为：

```
	watcher = FileSystemWatcher(args.settings, Readers, settings)
	watcher.check()
	with console.status("Generating..."):
		pelican.run()
```

这两个过程的主要区别是autoreload会监控文件的变化，如果文件发生了变化则会重新执行 `pelican.run()` 。下面详细讨论下文件监控行为，也就是FileSystemWatcher类里面的细节。后面只关注 `pelican.run()` 了。

查看了一下`pelican.run()`后面的代码，后面的文件列表还会另外生成的，也就是可以确定这个FileSystemWatcher的用途仅仅只是用来判断监控的文件或文件夹里面的内容是否发生了变化。

其维护了这样一个字典值：

```
	self.watchers = {
		'settings': FileSystemWatcher.file_watcher(settings_file)
	}
```

后面还会根据配置来更新一些监控项：

- content 根据 `PATH` 配置来。
- theme 根据 `THEME` 配置来。
- 此外还会根据 `STATIC_PATHS` 来增加静态资源监控，从代码来看这些静态文件是必须在 `PATH` 下面的。

其会利用 `get_watcher` 方法来自动判断给定的path是文件还是文件夹，来分配 `file_watcher` 或者 `folder_watcher` 。

这个 `file_watcher` 和`folder_watcher` 是一个生成器函数，其中 `file_watcher` 的内部逻辑是 判断该文件的

```
os.stat(path).st_mtime
```

如果大于函数内部记录的 `LAST_MTIME` ，则认为该文件已发生修改，然后 `yield True` ，否则 `yield False` 。

FileSystemWatcher在每次判断前需要前支持`check` 方法：

```python
    def check(self):
        result = {key: next(watcher) for key, watcher in self.watchers.items()}
```

其核心就是那个`next`函数，其会再次执行目标生成器函数。

 `file_watcher` 和`folder_watcher` 内部都是`While True` 的循环，好在python的迭代器的惰性运算机制，使得这个监控设计实现起来很简单。

`folder_watcher` 当然需要进行文件夹迭代，监控的文件要满足两个条件：

1. 是有效的扩展名，有效的扩展名是根据 `Readers` 类来的，其是根据这个来的：

```python
        for cls in [BaseReader] + BaseReader.__subclasses__():
            if not cls.enabled:
                logger.debug('Missing dependencies for %s',
                             ', '.join(cls.file_extensions))
                continue

            for ext in cls.file_extensions:
                self.reader_classes[ext] = cls
```

pelican的所有Reader都需要继承自 `BaseReader` 这个类，上面完成了对 BaseReader所有子类的迭代查询，以`MarkdownReader`为例子：

```
class MarkdownReader(BaseReader):
    """Reader for Markdown files"""

    enabled = bool(Markdown)
    file_extensions = ['md', 'markdown', 'mkd', 'mdown']
```

如果你没有安装 `Markdown` 模块，则enabled就为False，那么其就不是有效扩展，其不会进入Readers类的reader_classes和readers这两个字典值中。这样这些相关的扩展名也不会被视作有效扩展名。

2. 不是忽略的文件。忽略逻辑是由配置的 `IGNORE_FILES` 来定义的，默认值是 `['.#*']` 。具体匹配是由python的fnmatch模块定义的语法：

```
fnmatch.fnmatch(f, ignore)
```

其对文件名提供了一种比正则表达式更简单点的匹配模式，具体是匹配的文件的后缀名。比如默认的 `['.#*']` 就是任何以 `.#` 开头的扩展名文件都将被忽略。

`folder_watcher` 对整个文件夹是否发生了更新采取了一种很聪明的方法，取 `max(file_times(path))` 其内所有文件修改时间的最大值，如果该时间大于记录的上次最大时间，那么文件夹里面的内容肯定发生修改了。

`update_watchers` 在初次运行或者配置发生变化之后需要运行一次，其内有些小细节处理，这里就忽略讨论了。

`theme` 和静态文件的文件夹监控的有效扩展是直接赋值 `['']` ，这里我注意到 `f.endswith(tuple(extensions))` ，python的字符串的endswith方法还可以接受一个字符串元组，只要以其中任一个结尾即返回`True` 。然后有：

```
>>> '.abc'.endswith('')
True
```

也就是静态文件夹里面没有是有效扩展名这个判断逻辑。

### 加载插件

在运行 `pelican.run()` 之前还有一件事，那就是实例化 `Pelican` 类，从代码中看，这里面最重要的一项工作就是加载插件。

```python
    def init_plugins(self):
        self.plugins = []
        for plugin in load_plugins(self.settings):
            name = get_plugin_name(plugin)
            logger.debug('Registering plugin `%s`', name)
            try:
                plugin.register()
                self.plugins.append(plugin)
            except Exception as e:
                logger.error('Cannot register plugin `%s`\n%s',
                             name, e)

        self.settings['PLUGINS'] = [get_plugin_name(p) for p in self.plugins]

```

这个 `load_plugins` 有一个