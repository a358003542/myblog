Title: mindmaptree
Slug: mindmaptree
Date: 2017-11-24 18:03
Modified: 2017-11-24 18:03
[TOC]

如下思维导图，我们如何设计一种数据格式来便捷的进行后续csv或者json操作？

![img]({static}/images/arithmetic/mindmaptree.png)

然后其对应的csv格式如下：

```
奴隶社会,非洲,古埃及文明,金字塔
,亚洲,两河流域文明,汉谟拉比法典
,,古印度,种姓制度
,,,佛教的创立
,欧洲,希腊,希腊城邦
,,,雅典民主
,,罗马,城邦
,,,帝国的征服与扩展
,,希腊罗马古典文化,建筑艺术
,,,公历
```

这个问题实际上和前面谈论的二叉搜索树有点类似，只是那个问题的变种罢了，同样在这种树形结构下不可避免要用到递归思维。下面是一个很粗糙版本的实现，其中最核心的一个点就是我这个Node只做好自己的分内事情就行了，然后放到整体的支持功能递归展开即可。

## 基本类的设计

```python

import logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


class MindMapTree(object):
    def __init__(self, data=None, parent=None):
        self.data = data
        self.parent = parent
        self.children = []

    def introspection(self):
        """
        核心内省函数，返回我和我的所有children。
        """
        stack = []
        tree = self
        if tree.data is not None:
            logger.debug('intorspection add node:{0}'.format(tree))
            stack.append(tree)

            for child in tree:
                stack += child.introspection()
        return stack

    def __str__(self):
        if self.children:
            return '<MindMapTree:{0}> has children: {1}'.format(self.data, self.children)
        else:
            return '<MindMapTree:{0}>'.format(self.data)

    def __repr__(self):
        if self.children:
            return '<MindMapTree:{0}> has children: {1}'.format(self.data, self.children)
        else:
            return '<MindMapTree:{0}>'.format(self.data)

    def append(self, child_data):
        child = MindMapTree(child_data, parent=self)
        self.children.append(child)

    def remove(self, child_data):
        child = MindMapTree(child_data, parent=self)
        self.children.remove(child)

    def insert(self, parent_data, child_data):
        for target in self.introspection():
            if target.data == parent_data:
                target.append(child_data)

    def find(self, key):
        for target in self.introspection():
            if target.data == key:
                return target
        raise KeyError

    def set_nodedata(self, data):
        self.data = data

    def __iter__(self):
        if self.children is not None:
            for child in self.children:
                yield child

    def to_json(self):
        return {self.data: [i.to_json() for i in self.children]}

    def get_path(self):
        res = []
        while True:
            res.append(self.data)
            if self.parent is None:
                break
            else:
                self = self.parent
        return res[::-1]


if __name__ == "__main__":
    tree = MindMapTree("奴隶社会")
    tree.append("非洲")
    tree.append("亚洲")
    tree.insert("非洲", "古埃及文明")
    tree.insert("古埃及文明", "金字塔")
    tree.insert("亚洲", "两河流域文明")
    tree.insert("两河流域文明", "汉谟拉比法典")
    tree.insert("亚洲", "古印度")

    print(tree)
    print('######################')
    stack = tree.introspection()

    print(stack)

    yazhou = tree.find("亚洲")

    print(yazhou.introspection())
    print(yazhou.parent)
    print(yazhou.children)

    print(tree.to_json())

    print(tree.get_path())
```

## csv的读写

```python


import csv
from collections import defaultdict


class MindMapCSV(csv.Dialect):
    delimiter = ','  # 分隔符
    quotechar = '"'  # quote符号
    doublequote = True  # 双引号在字符中的情况
    skipinitialspace = True  # 分隔符后空白忽略
    lineterminator = '\n'  # 换行符
    quoting = csv.QUOTE_MINIMAL  # 最小quote


csv.register_dialect("MindMapCSV", MindMapCSV)


import logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)
from mindmaptree import MindMapTree


class MindMapReader():
    def __init__(self, f, dialect='MindMapCSV'):
        self.data = MindMapTree()

        last_stack = {}
        first = True  # 根元素，目前还只处理一个根元素的情况
        for line in csv.reader(f, dialect):
            logger.debug('got original line data: {0}'.format(line))

            for index, item in enumerate(line):
                if item:
                    if first:
                        last_stack[index] = item
                        self.data.set_nodedata(item)
                        first = False
                    else:
                        last = last_stack[index - 1]
                        last_stack[index] = item
                        self.data.insert(last, item)
                else:  # ""
                    continue

        logger.debug('init data: {0}'.format(self.data.introspection()))

    def getdata(self):
        return self.data


class MindMapWriter():
    def __init__(self, f, dialect='MindMapCSV'):
        self.data = MindMapTree()

        self.writer = csv.writer(f, dialect)

    def setdata(self, data):
        self.data = data
```



## 其他函数接口

```python

def read_csv(f):
    with open(f, newline='', encoding='utf8') as f:
        reader = MindMapReader(f)
        data = reader.getdata()

        return data


def csv2json(f):
    with open(f, newline='', encoding='utf8') as f:
        reader = MindMapReader(f)
        data = reader.getdata()

        res = data.to_json()
        import json
        res = json.dumps(res, sort_keys=True, indent=2, ensure_ascii=False)
        return res


def find(mindmaptree, key):
    try:
        target = mindmaptree.find(key)
        return '.'.join(target.get_path())
    except KeyError:
        return'找不到关键字：{0}'.format(key)


if __name__ == '__main__':

    data = read_csv('history.csv')
    print(data)

    json_data = csv2json('history.csv')
    print(json_data)

    find_res = find(data, "汉谟拉比法典")
    print(find_res)

    find_res = find(data, "美洲")
    print(find_res)

```

