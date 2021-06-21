#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import sys

# set the author metadata
AUTHOR = 'wanze'

# the filename decide the title metadata
FILENAME_METADATA = '(?P<title>.*)'

# set default category
DEFAULT_CATEGORY = 'archived'
# the sub folder name not decide the category name
USE_FOLDER_AS_CATEGORY = True
# show the pages
DISPLAY_PAGES_ON_MENU = True

SITENAME = "万泽的博客"
SITEURL = ''

PATH = 'content'
ARTICLE_EXCLUDES= ['articles\\python\\algorithm\\examples']

TIMEZONE = 'Asia/Shanghai'

# set default date
DEFAULT_DATE = 'fs'
DEFAULT_LANG = 'Chinese (Simplified)'

DEFAULT_DATE_FORMAT = '%Y年 %b %-d日'

#  disable feed generation
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# 不要自动删除的文件
OUTPUT_RETENTION = [".git"]

# Blog roll
LINKS = (('MyGitHub', 'http://www.github.com/a358003542'),
         ('MyEmail', 'a358003542@outlook.com'),)

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# static path copy it to the destination
STATIC_PATHS = ['images',
                'data',
                'extra']

EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/ads.txt': {'path': 'ads.txt'},
}

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
# READERS = {'html': None}


######################### MARKDOWN CONFIG #################
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight',
                                           'guess_lang': False},
        'markdown.extensions.toc': {},
        'markdown.extensions.fenced_code': {},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.footnotes': {}
    },
    'output_format': 'html5',
}
#############################################################


################## theme ##########################
# changing theme
THEME = 'mytheme'

SITE_DESCRIPTION = '欢迎来到本网站，希望本网站的文章能够对您有所帮助。'

TEMPLATE_PAGES = {'404.html': '404.html'}

######################################################


################################### plugin #################
PLUGIN_PATHS = ['myplugins']

PLUGINS = ['pelican_javascript', 'extract_toc',
           'tipue_search', 'render_math', 'sitemap', 'pandoc_html']

MATH_JAX = {'tex_extensions': ['mhchem.js']}

DIRECT_TEMPLATES = ['index', 'categories', 'archives', 'tags', 'search']

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.8,
        'indexes': 0.2,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'weekly',
        'indexes': 'weekly',
        'pages': 'monthly'
    },
    'exclude': ['tags/', 'categorys/']
}

##################################################################
