Title: neo4j图数据库
Date: 2018-08-07
Modified: 2018-08-08
Slug: neo4j
Tags: 数据库, 图数据库
Status: draft
[TOC]



## 前言

图数据库是什么的就多说了吧，一般想到要学习neo4j图数据库的读者，对图和图数据库应该有了一个简单的了解了。图数据库更侧重于描述事物之间的关系。



## Cypher查询语言

cypher可以说是最容易学的图查询语言了，一旦你学会的cypher，学其他图查询语言也会很容易的。如下一个cypher例子：

```cypher
MATCH:  (a:Person {name: 'Jim'}) -[:KNOWS]-> (b) -[:KNOWS] -> (c), (a)-[:KNOWS]-(c)
RETURN: b,c
```

里面的a,b,c你定义的节点名字，具体是寻找一个Person节点，其有属性 `{name: 'Jim'}` ，其有关系（KNOWS）指向b节点，然后a节点有关系（KNOWS）指向c节点，b节点有关系（KNOWS）指向c，要求返回b节点和c节点。

上例还可以写做如下形式：

```cypher
MATCH:  (a:Person) -[:KNOWS]-> (b) -[:KNOWS] -> (c), (a)-[:KNOWS]-(c)
WHERE: a.name  = 'Jim'
RETURN: b,c
```



### CREATE

```cypher
CREATE (shakespeare:Author {firstname:'William', lastname:'Shakespeare'}),
(juliusCaesar:Play {title:'Julius Caesar'}),
(shakespeare)-[:WROTE_PLAY {year:1599}]->(juliusCaesar)
...
```



MERGE



DELETE



SET



FOREACH 



UNION



WITH





## py2neo

neo4j的python接口，但不仅仅是接口，而是做了很多高层封装。











## 一些名词术语

### The labeled property graph model

最常见的一种图模型，标签属性图模型。一般有如下特征：

- 它包含节点和关系
- 节点含有一些属性（key-value对）
- 节点可以有一个或多个标签
- 关系有名字和方向，总是有一个起点节点和一个终点节点
- 关系也可以包含属性







### RDF

Resource Description Framework 







## 参考资料

1. graph databases 2nd edition by Ian Robinson, Jim Webber, Emil Efrem


