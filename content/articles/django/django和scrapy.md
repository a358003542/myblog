Title: django后台api编写之-django和scrapy
Date: 2018-05-26

[TOC]

## django和scrapy

django也可以和scrapy集成起来，简单来说就是通过 `scrapyd` ，django发送一个信号，然后scrapyd 后台启动一个爬虫任务。本小节主要参考了 [这篇文章](https://medium.com/@ali_oguzhan/how-to-use-scrapy-with-django-application-c16fabd0e62e) ，谢谢作者。

这样做有什么好处？大体有以下好处：

1.  爬虫的运行状态信息可查询可操作
2.  爬虫后台爬取不卡顿前台显示
3.  以信号为基础可以和celery结合起来从而建立更加复杂的基于简单的HTTP信号机制的爬虫系统（包括周期性任务或者其他任务等等）

读者请参看上面这篇文章，下面我就一些最核心的点来描述之。

### 从views开始说起

```python
from scrapyd_api import ScrapydAPI
scrapyd = ScrapydAPI('http://localhost:6800')

@api_view(['POST'])
def crawl_article(request):
    """
    POST : 传递公众号和文章title，然后运行spider去爬取。
    GET ; 查询某个爬虫进行到了什么状态
    :param request:
    :return:
    """

    if request.method == 'POST':
        mode = int(request.data.get('mode', 1))

        if mode == 1:
            gzh_id = request.data.get('gzh_id', None)
            if not gzh_id:
                return OurResponse.fail_missing_paras(msg="missing gzh_id")

            settings = {
                'gzh_id': gzh_id,
                'mode': mode,
            }

            task = scrapyd.schedule('default', 'article', settings=settings, **settings)

            return OurResponse.sucess_response(task_id=task, gzh_id=gzh_id, status='started')


```

你需要安装的pypi包有：`django` ，当然，`python-scrapyd-api` 同scrapyd交谈的python api接口。`Scrapy` 和 `scrapyd` 。

最核心的就是 `scrapyd.schedule()` 这个函数，`default` 是projecet name，意义有待进一步阐明。然后 `article` 就是具体你写的爬虫名字，然后还可以传递一些参数进去，这些参数实际传到了scrapy爬虫那边，简单来说就是你如果要手工模拟的话加上 `-a mode=1` 也是一样的效果。这些参数到了爬虫类那里可以直接 `self.mode` 调用那是后话了。 

所以scrapyd，ok，后台开了一个爬虫，还有什么要说的吗？没了。就django和scrapy集成知识来说没了，scrapy那边数据怎么存等等那都是scrapy那边的问题了。

最后粘贴个查看spider运行状态的视图函数吧，之所以粘贴出来是因为其和本文讨论的 `python-scrapyd-api` 有关，暴漏了很多api操作，可以简单看下了解下。



```python

@api_view(['GET', 'POST'])
def crawl_index(request):
    """
    task_id # 如果有则根据task_id 来查询

    或者根据 status 来过滤查询 '' running pending finished

    project_name 参数默认 default
    :param request:
    :return:
    """
    if request.method == 'GET':
        project_name = request.query_params.get('project_name', 'default')
        task_id = request.query_params.get('task_id', None)

        if task_id:
            status = scrapyd.job_status(project_name, task_id)
            if not status:
                return OurResponse.fail_uri_not_found(msg='task_id not found')
            else:
                return OurResponse.sucess_response(task_id=task_id, status=status)

        status_filter = request.query_params.get('status', '')
        data = scrapyd.list_jobs(project_name)

        if status_filter:
            data = scrapyd.list_jobs(project_name)
            data = {status_filter: data.get(status_filter)}

        return OurResponse.sucess_response(**data)

    elif request.method == 'POST':
        task_id = request.data.get('task_id', None)
        if not task_id:
            return OurResponse.fail_missing_paras(msg='missing task_id')

        status = scrapyd.cancel('default', task_id, signal='TERM') # kill it twice
        status = scrapyd.cancel('default', task_id, signal='TERM')

        return OurResponse.sucess_response(task_id=task_id, status=status)
```









