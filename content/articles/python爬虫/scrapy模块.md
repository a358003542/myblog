Title: scrapy模块
Slug: scrapy-module
Date: 2017-10-11 07:04 
Tags: python, 网络抓取,
[TOC]

## 简介
老实说Scrapy模块和Django模块在实用上包括在内容目录结构上都很相似，当然这两个项目干的完全是两个不同的事情，我想这种相似性更多的可以描述为类似于大多数GUI界面的那种类似。

我之前尝试过写过一个小的Spider网络爬虫程序，其实网络爬取大体过程都是类似的，因此我学习Scrapy项目大体只是一些基本配置的了解，对于其内部原理已经很熟悉了，所以本文不会在这些地方赘述了。

scrapy就是一个python模块，可以通过 `pip` 安装之，所以安装这块也不多说了。


### 新建一个项目

```
scrapy startproject project_name  [path] 
```

因为我喜欢创建python的venv虚拟环境，所以上面最后path设置为 `.` 当前目录下的意思。

然后接下来就是编写爬虫Spider脚本还有等等其他一些配置了。



## 第一个例子
下面是一个简单的例子：

```python
class MySpider(scrapy.Spider):
    user_agent = get_random_user_agent()
    name = "7yrt"
    start_urls = ['http://7yrt.com/html/rhrt/']
    allowed_domains = ['http://7yrt.com/']


    def parse(self, response):
        url = response.url
        html = response.text
        
        ## do something
        if re.match('http://7yrt.com/html/rhrt/[\d]+/[\d]+/[\d_]+.html', url):
            images = parse_webpage_images(url, html, name='div', class_='imgview')
            title = response.xpath('//h1/text()').extract_first()
            for index,image in enumerate(images):
                yield MyItem(uuid=get_item_uuid(url, str(index)),
                            image_url=[image],
                            name = title)


        ##### get next page
        links = parse_webpage_links(url, html)

        for next_page in links:
            yield scrapy.Request(next_page, callback=self.parse)
        
```

- `user_agent` 属性改变你爬虫情况的USER_AGENT HTTP头，这通常需要设置一下，防止你的爬虫被ban。

- `name` 你的爬虫的名字，等下你要具体运行某个爬虫的名字是 `scrapy crawl spider_name` ，用的就是这里定义的名字。然后 `scrapy list` 显示的也是这些爬虫名字。

- `start_urls` 你的爬虫起始开爬点，官方教程提到过 `start_requests` 这个方法，一般就定义 `start_urls` 还是很简便的。

- `allowed_domains` 你可以在 `parse` 方法获取 `next_page` 的时候自己定义过滤行为，更简单的就是定义站点内这个行为，这个熟悉点网络爬虫基本编写原理的都会了解这个概念，不过记得你还需要在 `settings.py` 那边设置：

```
SPIDER_MIDDLEWARES = {
    'scrapy.spidermiddlewares.offsite.OffsiteMiddleware': None,
}
```

### parse方法
parse方法类似于Django也有request请求和response的概念，简单来说每一个URL（按照基本网络爬虫模型）最后都会送入到这个方法，其要完成的工作有：

- 针对某些特定的url获取数据
- 添加next page行为（其内暗含的行为有去重，舍弃，过滤等）


### response对象
response对象可以获取 `response.text` 然后送给beautifulsoup来处理，比如上面的 `parse_webpage_images` 和 `parse_webpage_links` 就是这样做的，主要是这两个以前写的函数还是很简便的，所以就没考虑效率问题了，有的时候真的不在乎那么一点，因为后面还会讨论减缓爬虫爬取速度的问题。

然后官方教程提到的response对象可以调用 `css` 或 `xpath` 方法来进行一些信息提取工作，这个简单了解下xpath语法，还是很便捷的。

### MyItem对象
MyItem对象是在 `items.py` 哪里定义的，很简单，没啥好说的，就是一个简单的python对象罢了，方便存储数据用。你若不喜欢，就临时定义一个字典值也是可以的。


## settings.py里面的配置

### 减缓访问速度
在网络爬取中，防止被ban（一般403错误就是由此而来）一直是个大问题。开代理换IP要求挺高的，不过下面这些手段一般还是能够实现的，这些都在settings.py里面就有了，只需要去注释就是了。大体有下面这些：


```
DOWNLOAD_DELAY = 3
CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16
# Disable cookies (enabled by default)
COOKIES_ENABLED = False
```
就是设置下载访问停顿时间和并行请求数还有禁用cookies。除了禁用cookies之外，上面这几个设置可以不用，请看到官方文档的 [这里](https://doc.scrapy.org/en/latest/topics/autothrottle.html) 。

这个在 settings.py 文件的后面些也有，这是一种自动节流机制，它是利用下载延迟还有并行数来自动调节DELAY时间，

```
AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
```

最后要说的是自动节流和前面的 `DOWNLOAD_DELAY` 和 `CONCURRENT_REQUESTS_PER_DOMAIN` 是协作关系。自动节流最小不会小过 `DOWNLOAD_DELAY` ，最大不会大过 `AUTOTHROTTLE_MAX_DELAY` 。 然后 `AUTOTHROTTLE_TARGET_CONCURRENCY` 也只是一个节流建议，并不是最大极限，对于单个域名的最大并行请求数是由 `CONCURRENT_REQUESTS_PER_DOMAIN` 定义的。


### JsonPipeline
`pipelines.py` 文件里面就定义了一些你自己写的Pipeline类，比如下面这个是JsonPipeline类：


```python
class JsonPipeline(object):

    def __init__(self):
        self.file = codecs.open('test.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False, indent=4) + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()

```

大体就是一个简单的类，其中一些特别的方法有特别的用处。这个jsonpipelie并不具有实用价值，简单了解下即可。


### ImagesPipeline
想要自动下载图片，没问题，scrapy已经内置有这个功能了！你需要做的就是收集好图片连接就是了。设置里要加上这样一行：

```
ITEM_PIPELINES = {
    'scrapy.pipelines.images.ImagesPipeline': 1,
}
```

然后设置里还有如下相关配置:
```
IMAGES_STORE = '/path/to/download_images'
IMAGES_URLS_FIELD = 'image_url'
IMAGES_RESULT_FIELD = 'image'
```

这里 `IMAGES_URLS_FIELD` 的默认值是 `image_urls` ，你需要在你的items对象加上这一属性，其是一个列表值。然后 `IMAGES_RESULT_FIELD` 默认值是 `images` ， 这个值ImagesPipeline会自动填充，不需要管的。这里改名字是因为我不喜欢很多图片混在一起，所以做了一些处理分开了。


### MongoDBPipeline
想要把数据直接实时填入到mongodb里面去？用 `MongoDBPipeline` 即可，你需要

```
pip install scrapy-mongodb
```

然后配置加上
```
ITEM_PIPELINES = {
    'scrapy_mongodb.MongoDBPipeline': 400,
}
```

这后面的数字只是执行优先级，没什么特别的含义。

然后还有配置：

```
MONGODB_URI = 'mongodb://localhost:27017'
MONGODB_DATABASE = 'myscrapy'
MONGODB_UNIQUE_KEY = 'uuid'
```

这个插件的 `MONGODB_COLLECTION` 值默认是 `items` 是个死的，我还不是很满意。然后 `MONGODB_UNIQUE_KEY` 我还不清楚是什么，后面有时间继续。





## 测试抓取

```
scrapy shell  url
```

然后进入shell之后，有个 `response` 对象，其对应于之前写爬虫 parse函数时候的那个response对象。进一步可以做一些前期测试抓取的工作。



## settings的传递

爬虫初始化后， `self.settings` 就可以使用了，通过它你就可以调用一些在 `settings.py` 文件里面的配置变量了。然后你在写pipeline的时候，如下：

```python
    def open_spider(self, spider):
        self.client = MongoClient(self.mongo_uri)
        self.mongodb = self.client[self.mongo_dbname]
        spider.mongodb = self.mongodb
```

`open_spider` 是打开爬虫后的动作，定义 `self.mongodb` 是将目标mongodb 数据库对象挂载本 pipeline上，而 `spider.mongodb` 是将这个变量挂在本爬虫上，这样后面你的爬虫类那里都是可以直接用 `self.mongodb` 来调用目标变量的，但说到爬虫类 `__init__` 方法里面还不大确定。然后你写pipeline的时候通过 `crawler.settings` 也可以或者配置变量：

```python
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGODB_URI'),
            mongo_dbname=crawler.settings.get('MONGODB_DATABASE')
        )
```



## xpath语法

下面主要通过各个例子简要介绍xpath语法之，参考了 [阮一峰的这篇文章](http://www.ruanyifeng.com/blog/2009/07/xpath_path_expressions.html) 和菜鸟教程的xpath教程。

### 选择title

```
//title
```

这是选择到了文档中任意位置的 title 标签， `/` 开头的话会选择根节点，这不太好用。

### 选择title包含的文本

```
//title/text()
```

### 按照id选择

```
//div[@id='post-date']/text()
```

上面例子的意思是选择一个div标签，其有id属性 `post-date` ，如果div改为 `*` 则为随便什么标签名字。

### 继续往下选

```
//*[@id='js_profile_qrcode']/div/p[1]/span/text()
```

### 选择目标标签的属性

```
////*[@id='js_profile_qrcode']//a/@href
```

## user agent 设置

你可以设置middlesware来设置useragent：

```python
class MyUserAgentMiddleware(UserAgentMiddleware):
    def __init__(self, user_agent='Scrapy'):
        super(MyUserAgentMiddleware, self).__init__()

        self.user_agent = get_random_user_agent()

    def process_request(self, request, spider):
        if self.user_agent:
            request.headers.setdefault('User-Agent', self.user_agent)

        logger.debug('Using User-Agent:{0}'.format(request.headers['User-Agent']))

```

因为middleware是在你的爬虫开始之前就运行了，所以你的爬虫一开始就有一个 user_agent 属性了。

可能你还有其他需求，需要临时改变user agent，那么在你的爬虫类的属性设置那里可以直接设置：

```
user_agent = what
```

这样将覆写原来middleware指定的self.user_agent，实际上在middleware之前你的settings那里还可以设置user_agent，而那是最先的scrapy默认的useragentMiddleware的行为，本小节的讨论参考了 [这个网页 eLRuLL](https://stackoverflow.com/questions/33444793/how-can-i-change-user-agent-in-scrapy-spider) 的回答和自己的一点小小的print。

## 模拟用户登录

```python
import scrapy

class LoginSpider(scrapy.Spider):
    name = 'example.com'
    start_urls = ['http://www.example.com/users/login.php']

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={'username': 'john', 'password': 'secret'},
            callback=self.after_login
        )

    def after_login(self, response):
        # check login succeed before going on
        if "authentication failed" in response.body:
            self.logger.error("Login failed")
            return

        # continue scraping with authenticated session...
```

## 防止被封的策略

1. 设置随机的user agent策略
2. 禁用cookie `COOKIES_ENABLED = True`
3. 设置下载停顿 `DOWNLOAD_DELAY = n`
4. 使用代理池

