Title: corenlp研究
Slug: corenlp-research
Date: 2018-01-21 09:36
Modified: 2018-01-21 09:36
Tags: corenlp,
Status: draft

## 安装corenlp server

非java语言还是推荐先配置好Stanford 的 corenlp server，然后再通过api来调用之。具体java 的server端先到 [官网](https://stanfordnlp.github.io/CoreNLP/index.html) 下载，然后解压，下载好中文模型jar文件然后扔进去，然后还需要写个文件

 `StanfordCoreNLP-chinese.properties` ，具体内容请参看 [这个网页](https://stanfordnlp.github.io/CoreNLP/human-languages.html) 然后运行：

```
java -Xmx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -serverProperties StanfordCoreNLP-chinese.properties -port 9000 -timeout 15000
```

设置JAVA环境和 `JAVA_HOME`  变量这些就不多说了。

服务器启动后，在 `localhost:9000` 那里，打开浏览器我们可以看到一些有趣的东西。

## pycorenlp

python的简单对接如下所示，pycorenlp的github项目在 [这里](https://github.com/smilli/py-corenlp) 。目前确定的 annotators 有：
```python
from pycorenlp import StanfordCoreNLP

CORENLP_URI = 'http://192.168.0.109:9000'

class CoreNLP():
    def __init__(self,corenlp_uri=CORENLP_URI):
        self.nlp = StanfordCoreNLP(corenlp_uri)


    def read_text(self, text, annotators='tokenize,ssplit, pos, ner, depparse, parse', outputformat='json'):
        output = self.nlp.annotate(text, properties={
            'annotators': annotators,
            'outputFormat': outputformat
        })
        self.output = output
```

1. tokenize,ssplit, 基本辅助
2. pos part of speech 做词性分析
3. ner 命名实体（效果并不是很好）
4. depparse（依赖分析，也就是那个依赖图）
5. parse（句法分析，也就是那个树形图）


### nlp.output的结构
- `nlp.output['setences'][0]` 第一句话
- `nlp.output['setences'][1]` 第二句话

- `nlp.output['setences'][0]['tokens']`

```
{'index': 1, 'word': '猴子', 'originalText': '', 'lemma': '猴子', 'characterOffsetBegin': 0, 'characterOffsetEnd': 2, 'pos': 'NN', 'ner': 'O'}, 
```

里面装着具体 分词，从那里开始，到那里结束，pos 词性，ner 命名实体

- `nlp.output['setences'][0]['parse']`
  该句话的句法分析


- `nlp.output['setences'][0]['basicDependencies']` 
  该句话的句子依赖分析

## POS

POS是 part of speech 也就是对已经分好词的中文文本进行词性标注，[参考论文](https://web.stanford.edu/~jurafsky/sighan_pos.pdf) ，目前暂时感兴趣的是分析出来的英文缩写的含义，下面列表之：

-   AD adverb 副词
-   CC 连接词
-   CD 基数词
-   DT 限定词
-   FW 外语词
-   JJ 其他名词修饰符
-   LC 方位词
-   M 量词
-   NN common noun 一般名词
-   NR 专有名词
-   NT 时间名词
-   OD 序数词
-   P 介词
-   PN 代词
-   PU 标点符号
-   SP 句末助词
-   VA 表语形容词
-   VV 其他动词



## Named Entity Recognizer

命名实体识别，主要以下几个输出：

-   O
-   ORG
-   LOC
-   PER
-   GPE

## ParserAnnotator

parse 句法分析：

-   root 根
-   IP 从句
-   NP 名词短语
-   VP 动词短语
-   PP 介词短语
-   前面在POS中提到的词性，在具体词的上一节点。
-   PU 断句符号
-   ​

## CoreNLP加速

本小节主要参看了 [CoreNLP的官方介绍](https://stanfordnlp.github.io/CoreNLP/memory-time.html) ，其中最核心的一个点就是慎重选择你的 annotators ，不需要就不选。

如果只是想要词性标注和ner功能，那么推荐的annotators设置为：

```
tokenize, ssplit, pos, lemma, ner
```

如果命名实体识别ner你只需要 person location organization ，那么你的annotators只需要设置为：

```
tokenize,ssplit,pos,ner
```

然后还可以进一步设置：

```
ner.useSUTime false 
ner.applyNumericClassifiers false 
```

