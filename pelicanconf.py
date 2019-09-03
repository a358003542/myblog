#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import sys

AUTHOR = 'cdwanze'
SITENAME = "cdwanze的博文"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'



if sys.platform == 'win32':
    DEFAULT_LANG = 'zh'
else:
    DEFAULT_LANG = 'zh_CN'
    LOCALE='zh_CN'
DEFAULT_DATE_FORMAT = '%Y年 %b %-d日'

# set default date
DEFAULT_DATE = 'fs'
# set default category
DEFAULT_CATEGORY = 'others'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# 不要自动删除的文件
OUTPUT_RETENTION = [".git"]


# Blogroll
LINKS = (('MyGitHub', 'http://www.github.com/a358003542'),
         ('MyEmail', 'a358003542@gmail.com'),)


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['images',
                'pdfs',
                'data',
                'extra',
                'typeset']

EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/CNAME': {'path': 'CNAME'},
}

# foler as category
USE_FOLDER_AS_CATEGORY = True

ARTICLE_URL = 'articles/{slug}.html'  # articles 里面的内容
ARTICLE_SAVE_AS = ARTICLE_URL
PAGE_URL = '{slug}.html'  # pages 文件夹里面的内容
PAGE_SAVE_AS = PAGE_URL
CATEGORY_URL = 'categorys/{slug}/index.html'
CATEGORY_SAVE_AS = CATEGORY_URL
TAG_URL = 'tags/{slug}.html'
TAG_SAVE_AS = TAG_URL

# disable author page
AUTHOR_URL = 'author/{slug}.html'
AUTHOR_SAVE_AS = ''
# disable parse html
READERS = {'html': None}

MARKUP = ('md', 'ipynb')
IGNORE_FILES = ['.ipynb_checkpoints']

# changing theme
THEME = 'mytheme'


# the plugin
PLUGIN_PATHS = ['myplugins']

PLUGINS = ['pelican_javascript', 'extract_toc', 'pelican_ipynb', 'tipue_search', 'render_math']

MATH_JAX = {'tex_extensions': ['mhchem.js']}

DIRECT_TEMPLATES = ['index', 'categories', 'archives', 'tags', 'search']

DEFAULT_PAGINATION = 20

# auto toc support
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.toc': {},
        'markdown.extensions.fenced_code': {},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}
