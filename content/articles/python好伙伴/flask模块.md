Title: flask模块
Slug: flask-module
Date: 2019-01-03
Modified: 2019-07-22
Tags: flask

[TOC]

## 前言

django是一种构建大型商务网站的解决方案，除非目前贵公司的技术栈是已经架构在django之上的，否则不管是个人性质的小项目，或者刚刚开始的新的项目，个人推荐flask多于django的。当然在flask和tornado之间如何选择上，个人觉得更多的是在你对python的异步这一块的理解上，如果你懂python的异步，并且也知道你要做的api对并发和速度都有很高的要求，那么就应该选择tornado，否则就选择flask。

比如作为个人爱好去搭建的小网站或者api服务，那么选择flask是很适合的。本文也是作者有时鼓捣个人的小网站慢慢积累的一些东西。

## 推荐的启动方式

目前flask推荐的启动方式是通过：

```
flask run
```

或者

```
python -m flask run 
```

来启动flask。【这个方式很适合开发和测试，实际部署还是WSGI server来进行】

要正常执行上面的命令，你需要设置好一些环境变量，最主要的是 `FLASK_APP` 这个变量：

windows 

```
set FLASK_APP=hello.py
flask run
```
linux 

```
export FLASK_APP=hello.py
flask run
```

推荐是通过在当前工作目录下加上 `.env` 这个文件，里面定义：

```
FLASK_APP=myapp.py
FLASK_ENV=development
FLASK_DEBUG=1
```

环境变量，在运行 flask 命令的时候会自动加载这些环境变量。【这种加载行为只是针对flask命令，load_dotenv 模块之前该做的还是要做，不受影响。】

### FLASK_DEBUG

如果设置为1则开启flask调试模式：

- 重载器 所有源码文件变动自动重启服务器
- 调试器 出现异常在浏览器中显示异常信息

生产环境一定要把调试模式关闭！

### pycharm启动

pycharm现在有专门的flask启动支持，不过也可以继续采用如上描述的启动方式，这样会更加接近服务器那边的部署环境。

![img]({static}/images/python_third_party/pycharm_flask.png)

选择启动python脚本，选择 `Module name` ，这样就对应 `python -m flask` 命令的效果，然后加上参数 `run` ，环境变量如上所示，不用再特别调配了，工作目录设置下即可。

类似的你还可以再加上一个 `python -m flask shell` 命令。




## flask的请求分发

查看flask当前app的url分发情况
```
app.url_map
```
默认flask有个额外的路由
```
/static/<filename>
```



## flask的请求对象

request请求对象有：

- form dict 存储请求的表单字段
- args  dict 存储URL上传递的参数
- values form和args的合集
- cookies dict 存储请求的所有cookies
- headers dict 存储http的headers
- files dict 存储请求上传的所有文件
- get_data 返回请求主体缓冲的数据
- get_json return dict 包含解析请求主题后得到的json
- blueprint 处理请求的Flask蓝本
- endpoint 处理请求的Flask端点名称
- method HTTP请求方法
- scheme http或https
- is_secure 通过HTTPS发送的请求返回True
- host  请求主机名
- path 请求URL路径
- query_string URL查询字符串部分
- full_path URL 路径和查询字符串部分
- url 完整URL
- base_url 同url但没有查询字符串部分
- remote_addr 远程IP地址
- environ dict 请求原始WSGI环境 



## flask的请求钩子

请求钩子用装饰器来实现，flask有以下四种钩子：

- before_request 请求之前执行
- before_first_request 只在第一次请求前执行
- after_request 每次请求后执行 如果程序没有抛出异常的话
- teardown_request 每次请求之后执行，即使抛出异常

请求钩子和视图函数之间变量互通一般用上下文全局变量 g ，比如 `before_request` 处理的时候设置 `g.user` 为登录用户，后面视图函数可以调用 `g.user` 来得知当前登录用户。

## flask的响应对象

```
response = make_response(content, status_code)
response.set_cookie('a',1)
```

响应对象有以下属性或方法：

- status_code
- headers
- set_cookies 设置cookies
- delete_cookies 删除一个cookies
- content_length 内容长度
- content_type 响应主体的媒体类型
- set_data  
- get_data

特殊的响应： 重定向响应 状态码 302 Location部分写上目标URL flask提供 redirect函数快速生成这个重定向响应对象。

abort函数 其返回的是状态码404 其是抛出异常 



## 加入错误页面

```
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404
```



## url_for

```
url_for('index', _external=True)
```

1. 名字，
2. 送入一些参数进去
3. `_external` 绝对路径 ，一般使用相对路径即可，浏览器之外的某些链接一定要使用绝对路径

## 静态文件

```
url('static', filename='favicon.ico')
```



## flask-moment

Moment JS 送入UTC时间会自动转换成为本地时间，服务器那边的时间戳最好是记录UTC时间。用户则应该看到本地时间。

```jinja2
{% block scripts %}
    {{ super() }}
    {{ moment.include_moment() }}
    {{ moment.lang("zh-cn") }}
{% endblock %}
```



在模板上使用：

```jinja2
    <p>当前时间是： {{ moment(current_time).format('LLLL') }}.</p>
    <p>{{ moment(current_time).fromNow(refresh=True) }}刷新过.</p>
```

具体格式请参看 [MomentJs 官网](http://momentjs.cn/) 。



## 表单

flask-wtf 

```python
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app.config['SECRET_KEY'] = 'hard to guess string'

class NameForm(FlaskForm):
    name = StringField('请输入您的名字？', validators=[DataRequired()])
    submit = SubmitField('提交')
```

WTForms支持的HTML字段

- BooleanField 复选框
- DateField 文本字段 for datetime.date
- DateTimeField 文本字段 for datetime.datetime
- DecimalField 文本字段 for  decimal.Decimal
- FileField 文件上传字段
- HiddenField 隐藏文本字段
- FieldList 一组指定类型的字段
- FloatField 文本字段 for float
- FormField 把一个表单作为字段嵌入另一个表单
- IntegerField 文本字段 for integer
- PasswordField 密码文本字段
- RadioField 单选按钮
- SelectField 下拉列表
- SelectmultipleField 下拉多选列表
- SubmitField 表单提交按钮
- StringField 文本字段
- TextAreaField 多行文本字段

WTForms提供的验证函数

- DataRequired 确保类型转换后字段有数据
- Email 验证电子邮箱
- EqualTo 比较两个字段的值 常用于比较两次密码是否输入一致
- InputRequired 确保类型转换前字段有数据
- IPAddress 验证IPv4地址
- Length 长度验证
- MacAddress 验证MAC地址
- NumberRange 数字范围校验
- Optional 允许字段没有输入，将跳过其他校验函数
- Regexp 正则表达式校验
- URL URL校验
- UUID UUID校验
- AnyOf 输入值在任一可能值中
- NoneOf 输入值不在一组可能值中



## 表单提交模式

一般表单提交模式是 POST 重定向到本视图函数 GET ，POST操作需要保存用户的一些信息则修改session中的值。



## flash消息

flash消息方便让用户知道一些必要的信息。flash函数可以实现这点。然后模板文件上需要加上：

```jinja2
    {% for message in get_flashed_messages() %}
        <div class="alert alert-warning">
            <button type="button" class="close" data-dismiss="alert">&times;</button>
            {{ message }}
        </div>
    {% endfor %}
```

## 对接数据库

`__tablename__` 定义表名，默认的表名没有遵循使用复数命名的约定 like  `users`  。

这一块东西后面会补充一些，但更多的是sqlalchemy和sql那边的知识。



## 集成python shell

```python
@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)
```



运行： 

```
flask shell
```

db那些变量是可以正常使用的。

cmd里面要配置好环境变量 `export FLASK_APP=hello.py` 



## flask-migrate

`flask-migrate` 其基于sqlalchemy 的  alembic ，然后做了一些额外的工作。 主要提供了一些便捷的命令行接口，具体使用还是要熟悉sqlalchemy和alembic。

一个简要的例子如下：

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy()

db.init_app(app)
migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
```

新项目首先要运行：

```
flask db init
```

这对应alembic的 `alembic init` 命令，其将创建 `migrations` 文件夹，里面的文件就是alembic需要的，migrations文件夹是推荐和源代码一起加入版本控制的。

和简单的使用的alembic不同，其新建的 `env.py` 有一些优化，flask的配置环境里只要配置了 `SQLALCHEMY_DATABASE_URI` 这样变量，alembic就能正确找到数据库了。

然后：

```
flask db revision # 对应的是 alembic revison
flask db migrate # 对应的是 alembic revision --autogenerate
flask db upgrade # 对应的是 alembic upgrade
flask db downgrade # 对应的是 alembic downgrade
```

一般工作流程：

1. 修改数据库模型或者说数据库模型发生了变动
2. `flask db migrate` 创建迁移脚本
3. 检查自动生成的脚本，改正不正确的地方
4. `flask db upgrade`  将改动应用到数据库



### 删除无用的迁移脚本

alembic的自动生成脚本并不是万能的，需要人工审核。而就算没问题的某些迁移脚本，如果你觉得已经毫无意义了，那么将那个版本的迁移脚本删除是没有任何问题的。

### 彻底从零开始的迁移脚本

虽然alembic的官方文档觉得没有这个必要，不过我觉得还是很有用的。

1. 首先我们在flask应用下加上这样两个命令，负责最开始的创建数据库和根本代码生成表格工作。
2. 表格生成成功之后后面都用flask-migrate 或者说 alembic来管理，经过测试比如在models.py 哪里新加一列，然后利用 `flask db migrate` 是能够自动检测新加入了一列，从而自动生成的代码会更加精准。

```python
from sqlalchemy_utils import database_exists, create_database, drop_database

@app.cli.command()
def initdb():
    user_input = input('本命令只用于数据库初始化，后续更改请使用alembic来管理，确定请输入 [Y]')

    if user_input.lower() == 'y':
        engine = db.engine

        if not database_exists(engine.url):
            create_database(engine.url)
        else:
            print('db exists...')
            import sys
            sys.exit(-1)

        assert database_exists(engine.url)

        db.create_all()

        from alembic.config import Config
        from alembic import command
        alembic_cfg = Config('migrations/alembic.ini')

        command.stamp(alembic_cfg, "head")


@app.cli.command()
def dropdb():
    """
    TODO 生产环境不允许调用本命令
    :return:
    """
    user_input = input('警告!!! 本操作将删除数据库，数据将完全丢失，确定请输入： [YYY]')

    if user_input == 'YYY':
        engine = db.engine

        db.drop_all()

        if database_exists(engine.url):
            drop_database(engine.url)
        else:
            print('db not exists...')

        assert not database_exists(engine.url)
```



## 电子邮件

flask-mail



## 大型应用结构



