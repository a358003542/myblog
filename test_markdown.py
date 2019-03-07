#!/usr/bin/env python
# -*-coding:utf-8-*-


from markdown import Markdown

settings =  {'extension_configs': {'markdown.extensions.codehilite': {'css_class': 'highlight'}, 'markdown.extensions.toc': {}, 'markdown.extensions.fenced_code': {}, 'markdown.extensions.extra': {}, 'markdown.extensions.meta': {}}, 'output_format': 'html5', 'extensions': ['markdown.extensions.codehilite', 'markdown.extensions.toc', 'markdown.extensions.fenced_code', 'markdown.extensions.extra', 'markdown.extensions.meta']}
md = Markdown(**settings)


string = """在改变某个ndarray对象的dtype的时候，原ndarray对象实际上被删除了，等于重新创建了一个ndarray对象。可以通过上面的类型声明来直接进行转换，如:
```
    >>> t = np.array([1,2,3],dtype='int8')
    >>> t.dtype
    dtype('int8')
    >>> new_t = np.int32(t)
    >>> new_t.dtype
    dtype('int32')
```
"""

res = md.convert(string)


print(res)