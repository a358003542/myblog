Title: mol文件格式
Slug: mol-file
Date: 2017-12-04 14:47
Modified:  2017-12-04 14:47
Tags:  cheminformatics,
[TOC]

## 前言

本文主要参考了Molfile的 [wiki页面](https://en.wikipedia.org/wiki/Chemical_table_file) 。

因为openbabel在heroku上不好安装，其有c依赖，然后pubchem数据库那边是可以输出sdf文件的，然后chemdoodle那边是可以接受mol文件格式从而显示分子的3D图形的，一开始我试着用openbabel将smiles输出到mol file：

```python
def smi2mol(smiles):
    """
    read smiles string , retrun 3d mol file content.
    :param smiles:
    :return:
    """
    mol = pybel.readstring("smi", smiles)
    mol.make3D()
    return mol.write("mol")
```

这大体是没有问题的。后来看到pubchem restful api输出record全记录时有很详细的原子数目和坐标，所以想可不可以根据这些数据自动输出mol file。

目前最简单的方法是，利用pubchem获得目标分子的sdf文件，sdf文件是前兼容mol 文件的，我在前端网页初步测试结果也是将文件前一行到 `M  END` 之间的内容复制粘贴新建成为一个mol file，经过测试是可行的。所以一个最简单的方法就是写一个简单的函数，将这之间的内容返回出去即可。

更复杂点的方法就是深入理解化学信息学的连接表结构，读取pubchem各个原子坐标和键信息，然后本地绘制连接表。



## mol文件具体行信息

1.  第一行说明分子的名字
2.  第二行说明本程序信息
3.  第三行空行或者注释
4.  接下来就是连接表的信息了，到 `M  END` 结束，连接表信息如下： 
    1.  `几个原子`  `几个键` ........ V2000 标准
    2.  第一个原子 `x坐标` `y坐标` `z坐标` `元素符号` ...
    3.  ...
    4.  第一个键 连接了`第几个原子` 到  `第几个原子`  `类型` ...

## sdf文件

sdf文件在连接表内容上是一致的，1-3行header说明修改不影响分子的显示。然后sdf文件最后结尾会加上：

```
$$$$
```

mol file没有这个。之上会会继续写分子的其他属性信息：

```

> <PUBCHEM_IUPAC_OPENEYE_NAME>
1-bromobutane

> <PUBCHEM_IUPAC_CAS_NAME>
1-bromobutane

> <PUBCHEM_IUPAC_NAME>
1-bromobutane

> <PUBCHEM_IUPAC_SYSTEMATIC_NAME>
1-bromanylbutane

> <PUBCHEM_IUPAC_TRADITIONAL_NAME>
1-bromobutane

> <PUBCHEM_IUPAC_INCHI>
InChI=1S/C4H9Br/c1-2-3-4-5/h2-4H2,1H3

> <PUBCHEM_IUPAC_INCHIKEY>
MPPPKRYCTPRNTB-UHFFFAOYSA-N

> <PUBCHEM_XLOGP3>
2.8

> <PUBCHEM_EXACT_MASS>
135.989

> <PUBCHEM_MOLECULAR_FORMULA>
C4H9Br

> <PUBCHEM_MOLECULAR_WEIGHT>
137.02

> <PUBCHEM_OPENEYE_CAN_SMILES>
CCCCBr
```

看的出来这种结构是很方便程序分析的，比pubchem返回的json格式还好分析一点。后面我应该更多的对接和分析sdf文件。





