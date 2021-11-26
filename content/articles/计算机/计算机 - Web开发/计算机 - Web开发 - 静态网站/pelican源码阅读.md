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
- 忽略了程序运行计时和相关日志的输出讨论
- 忽略了一些程序运行统计信息和相关日志输出的讨论



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

这个 `load_plugins` 首先做的工作是试着加载pelican模块里面的plugins文件夹下的插件，因为pelican模块默认里面什么都没有，所以这一块等于什么都没做，就略过讨论了。

然后 `load_plugins` 开始分析配置的 `PLUGINS` ，然后根据配置 `PLUGIN_PATHS` 来试着加载插件。具体加载过程以最简单的情况来说就是执行：

```
spec = importlib.machinery.PathFinder.find_spec(plugin, plugin_paths)
```

find_spec是一个类方法，其返回的spec是一个特别的对象，经过module_from_spec函数处理就能转成module对象。这里的 `plugin_paths` 是一个类似 `sys.path` 的列表值：`['path']` 。

剩下的加载模块动作如下

```python
        # Avoid loading the same plugin twice
        if spec.name in sys.modules:
            return sys.modules[spec.name]
        # create module object from spec
        mod = importlib.util.module_from_spec(spec)
        # place it into sys.modules cache
        # necessary if module imports itself at some point (e.g. packages)
        sys.modules[spec.name] = mod
        try:
            # try to execute it inside module object
            spec.loader.exec_module(mod)
        except Exception:  # problem with import
            try:
                # remove module from sys.modules since it can't be loaded
                del sys.modules[spec.name]
            except KeyError:
                pass
            raise
```

关于上面的代码最核心的是 `mod = importlib.util.module_from_spec(spec)` 这一句，通过这一句我们就获得了对应插件，也就是python的module对象，后面的这一句：

```
sys.modules[spec.name] = mod
```

只是对于某些插件可能需要 `import` 操作才有用，然后后面的 `spec.loader.exec_module(mod)` 更多的是去试着执行module对象，是一个试着核对插件正确性的手段。

再回到最开始讨论的 `init_plugins` 方法上，这里有一句：

```
plugin.register()
```

这个是在说所有的pelican的插件都应该定义 **register** 函数，插件被加入进来都会先执行这个register函数。

### 信号

在讲到插件就必须讲到信号了，pelican利用blinker这个第三方模块来实现一种信号-函数的执行机制，上面讲的插件要和pelican的具体事务发生关系就需要通过信号来绑定上行为。简单来说就是pelican自身处理事物流程到了一定阶段就会发送一个信号，pelican的插件，具体就是register函数哪里，将这些信号也就是pelican的处理事物流程哪里，再扩展出另外一些额外的函数执行行为。

因为本文关注于pelican的源码阅读，所以这些信号就要详细解读一下，虽然pelican的核心执行流程还没有说明清楚，不过这里就预先讲一点，后面再有涉及到的地方再继续补充之。

```
initialized = signal('pelican_initialized')
```

Plican对象的 `__init__` 构造方法执行完毕会发送这个信号。发送的附带参数，也就是信号connect的执行函数的接受参数为Pelican对象。

```
finalized = signal('pelican_finalized')
```

Plican对象的 `run` 方法主要工作运行完毕之后会发送这个信号。发送的附带参数是Pelican对象。

```
readers_init = signal('readers_init')
```

Readers类 `__init__` 构造方法主要工作执行完毕之后会发送这个方法，Readers类在autoreload哪里的讨论提到，pelican需要清楚自己支持的后缀名的时候就需要先执行，所以这个信号发送是很早的。一般新增的Reader按照官方文档的讨论，也就是如果新增扩展名的，都应该和这个信号绑定起来，早早地执行起来。

下面这些信号后面再适当的时候引入进来再讨论之。

```
all_generators_finalized = signal('all_generators_finalized')

article_generator_pretaxonomy = signal('article_generator_pretaxonomy')
article_generator_finalized = signal('article_generator_finalized')
article_generator_write_article = signal('article_generator_write_article')
article_writer_finalized = signal('article_writer_finalized')

page_generator_finalized = signal('page_generator_finalized')
page_generator_write_page = signal('page_generator_write_page')
page_writer_finalized = signal('page_writer_finalized')

static_generator_init = signal('static_generator_init')
static_generator_finalized = signal('static_generator_finalized')

# Page-level signals

article_generator_preread = signal('article_generator_preread')
article_generator_context = signal('article_generator_context')

page_generator_preread = signal('page_generator_preread')
page_generator_context = signal('page_generator_context')

static_generator_preread = signal('static_generator_preread')
static_generator_context = signal('static_generator_context')

content_object_init = signal('content_object_init')

# Writers signals
content_written = signal('content_written')
feed_generated = signal('feed_generated')
feed_written = signal('feed_written')
```

### run

终于要到Pelican核心工作流程，也就是Pelican对象的run方法的讨论了。pelican的核心工作流程如下：

1. 收集各个Generator类
2. 如果各个Generator有 `generate_context` 方法，则执行之。
3. 如果各个Generator有 `refresh_metadata_intersite_links` 方法，则执行之。
4. 如果各个Generator有 `generate_output` 方法，则执行之。



在收集完各个Generator类之后有额外的逻辑：

```python
        if (self.delete_outputdir
                and os.path.commonpath([os.path.realpath(self.output_path)]) !=
                os.path.commonpath([os.path.realpath(self.output_path),
                                    os.path.realpath(self.path)])):
            clean_output_dir(self.output_path, self.output_retention)
```

也就是如果配置定义了 `DELETE_OUTPUT_DIRECTORY`  ，并且不是源或者父文件夹，则执行删除动作。删除动作不会删除配置 `OUTPUT_RETENTION` 定义的文件夹。

这是额外的一个优化逻辑，这里就不深入讨论了。



#### 收集各个Generator类

默认 `ArticlesGenerator` 和 `PagesGenerator` 都要加入进来。在 `ArticlesGenerator` 类初始化的时候还有一些细节，先讨论之。

ArticlesGenerator类继承自 `CachingGenerator` ，`CachingGenerator` 继承自 `Generator, FileStampDataCacher` 。

先看到 `Generator` 类，其 `__init__` 构造方法执行完毕之后会发送 `generator_init` 信号。

```
generator_init = signal('generator_init')
```

Generator类构造方法里面进行了很多Jinja2相关的配置，如果你自己定义的Generator类不需要Jinja2那么则不需要继承自Generator。

```python
        self._templates_path = list(self.settings['THEME_TEMPLATES_OVERRIDES'])

        theme_templates_path = os.path.expanduser(
            os.path.join(self.theme, 'templates'))
        self._templates_path.append(theme_templates_path)
        theme_loader = FileSystemLoader(theme_templates_path)

        simple_theme_path = os.path.dirname(os.path.abspath(__file__))
        simple_loader = FileSystemLoader(
            os.path.join(simple_theme_path, "themes", "simple", "templates"))

		self.env = Environment(
            loader=ChoiceLoader([
                FileSystemLoader(self._templates_path),
                simple_loader,  # implicit inheritance
                PrefixLoader({
                    '!simple': simple_loader,
                    '!theme': theme_loader
                })  # explicit ones
            ]),
            **self.settings['JINJA_ENVIRONMENT']
        )
```

Jinja2的ChoiceLoader工作原理是如果一个template找不到则会尝试下一个loader。

Jinja2的FileSystemLoader是试着从文件系统中查找一个template。

PrefixLoader是根据前缀限定来查找loader，默认的`delimiter='/'` ，也就是假设你指定template名字是 `!simple/index.html` ，则会试着用simple_loader来查找index.html模板。

现在总结到pelican里面jinja2模板引擎查找模板的逻辑是：

1. 试着从配置的 `THEME_TEMPLATES_OVERRIDES` 和 配置的 `THEME/template` 定义的文件系统来查找模板
2. 如果上面找不到则试着从pelican代码自带的simple模板里面查找。
3. 如果上面找不到而且模板名字是以 `!simple` 或者 `!theme` 前缀开头，则去掉前缀和delimiter，从对应的simple模板或者 `THEME/template` 哪里查找对应的。

此外配置的 `JINJA_ENVIRONMENT` 可以传递额外的参数给Jinja2的Environment对象。

```python
        # provide utils.strftime as a jinja filter
        self.env.filters.update({'strftime': DateFormatter()})

        # get custom Jinja filters from user settings
        custom_filters = self.settings['JINJA_FILTERS']
        self.env.filters.update(custom_filters)
```

更新Jinja2的Environment环境下的filters， `self.env.filters` 就是一个字典值，你可以在配置中利用 `JINJA_FILTERS` 来添加更多的filter，具体filter就是一个可调用对象即有 `__call__` 的类或者函数即可。

```
        # get custom Jinja globals from user settings
        custom_globals = self.settings['JINJA_GLOBALS']
        self.env.globals.update(custom_globals)
```

Jinja2模板的一些全局可用变量可利用配置 `JINJA_GLOBALS` 来增加之，也是一个字典值。

```
        custom_tests = self.settings['JINJA_TESTS']
        self.env.tests.update(custom_tests)
```

ArticlesGenerator的初始化另外还声明了一些变量，然后发送信号：

```
article_generator_init = signal('article_generator_init')
```

PagesGenerator和ArticlesGenerator一样也是继承自 `CachingGenerator` ，然后初始化也另外声明了一些变量，然后发送信号：

```
page_generator_init = signal('page_generator_init')
```

关于ArticlesGenerator和PagesGenerator的缓存优化生成策略我决定暂时先略过讨论，后面再另开一小节集中讨论之。这是另外额外添加的优化特性。

如果配置有 `TEMPLATE_PAGES` ，则会再加上 `TemplatePagesGenerator` 。

如果配置有 `OUTPUT_SOURCES` ，则会再加上 `SourceFileGenerator` 。

这两个Generator后面再讨论。

下面这段代码是支持自定义Generator插件的：

```python
        for receiver, values in signals.get_generators.send(self):
            if not isinstance(values, Iterable):
                values = (values,)
            for generator in values:
                if generator is None:
                    continue  # plugin did not return a generator
                discovered_generators.append((generator, receiver.__module__))
```

我粗略看了一下，pelican里面信号send之后还有返回值的就两个，一个是 `get_generators` ，一个是 `get_writer` 。

```
get_generators = signal('get_generators')

get_writer = signal('get_writer')
```

send的返回值结构如下：

```
            return [(receiver, receiver(sender, **kwargs))
                    for receiver in self.receivers_for(sender)]
```

具体blinker内部细节不深究了，不过从这里可以看出blinker的某个信号send之后，之前connect的那些回调函数都会被调用和执行。

```
        # StaticGenerator must run last, so it can identify files that
        # were skipped by the other generators, and so static files can
        # have their output paths overridden by the {attach} link syntax.
        discovered_generators.append((StaticGenerator, "internal"))
```

最后是增加 StaticGenerator ，官方文档说明了一定要最后运行。

收集的Generator最后汇总并实例化：

```python

        context = self.settings.copy()
        # Share these among all the generators and content objects
        # They map source paths to Content objects or None
        context['generated_content'] = {}
        context['static_links'] = set()
        context['static_content'] = {}
        context['localsiteurl'] = self.settings['SITEURL']

        generators = [
            cls(
                context=context,
                settings=self.settings,
                path=self.path,
                theme=self.theme,
                output_path=self.output_path,
            ) for cls in self._get_generator_classes()
        ]
```

path来自配置 `PATH` ，theme来自 `THEME` ，output_path 来自 `OUTPUT_PATH` 。

#### generate_context

