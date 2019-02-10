Title: 机器学习第六谈之pipeline
Slug: machine-learning-talk-six
Date: 2018-12-26
Modified: 2018-12-26
Tags: machine-learning

[TOC]

## 机器学习第六谈之pipeline

前面的学习讨论从keras到numpy，从验证测试到各个算法，大概讨论是很零零碎碎的。甚至会让人产生机器学习内容太多了，太难了的感觉。前面的那些基础知识很多都是可以后面再慢慢补充学习的，说到底机器学习应用属于工程领域，工程上的思维更多的偏向用，偏向从顶向下的学习方法——即不是从底向上的，学习基础知识一步步上的，而是先跟着已经成熟的项目来学习，来看看别人是怎样做的，最好马上手头上就能编写出一个针对某个问题的某个粗糙的解决方案，然后再针对性的学习和一步步地优化。

在之前的学习中应该说那个数据处理流如何去做的思考还是藏在脑子里面的，而慢慢接触到sklearn项目的pipeline概念，我们就会发现这个问题sklearn不说很完美地解决了，至少已经是部分解决了。并且在理解这个pipeline概念之后，我发现我的视角似乎更加的宏观和开阔了，甚至之前似乎分裂了的神经网络领域知识也融合进来了。下面是重点理解sklearn的Pipeline这个概念，然后试着在自己的机器学习项目中加以实践。



sklearn的pipeline是进行机器学习数据处理流的很重要的一个工具，下面的这个图很重要，大概说明了pipeline的主要工作原理。



【pipeline工作流程图】

本图片摘自 [这篇文章](http://frankchen.xyz/2018/04/08/pipeline-in-machine-learning/)

![](http://frankchen.xyz/images/15231783974167.jpg)


其中pipeline前面的叫做transformer，最后一个叫做estimator。



### transformer

transformer必须要有fit和tranform两个方法，当你调用 `pipeline.fit` 的时候，你的dataset (X, y) --> 会逐个通过前面所有的transformer，其中fit方法是进行一些数据的内部处理，一般会返回self，然后transform方法会返回输出数据集 X ，一般你自定义的transformer都应该继承 `TransformerMixin` 这个类，这样你只需要定义fit和transform方法就有 `fit_transform` 方法了。

下面是一个什么都没做的自定义的transformer的大概样子。

```python
from sklearn.base import TransformerMixin
class MyTransformer(TransformerMixin):
    """
    定义自己的Transformer

    """

    def fit(self, X, y=None, **kwargs):
        """
        :param X:
        :param y:
        :param kwargs:
        :return:
        """
        return self

    def transform(self, X, **kwargs):
        """
        :param X:
        :param kwargs:
        :return:
        """
        return X
```



当你调用 `pipeline.predict` 方法，你的输入X同样也会经过前面所有的transformer的transform方法处理【没有调用fit方法了，因为你之前已经调用pipeline.fit了，然后你的模型或者说你的pipeline中的各个transformer已经处理过了，换句话说，你的pipeline中的各个模型都已经训练好了】，然后再调用的是你最后哪个 estimator的 `predict` 方法再得到结果。

也就是说，我们完全可以将pipeline当做一个更大型的组合模型，现在在这个综合模型下，你输入数据集，训练，然后predict，而数据集的minmax scale或者各个标签标记等等都会自动处理，不需要你再这样考虑问题了：训练集已经scale了，我等下要输入一个实际的数据来使用模型，是不是还要先把数据scale一下，然后输出的结果我该转换成什么标记之类的问题了。

sklearn真的是一个很Great的项目，如果你找到有些老旧教材来学习机器学习的话，你会发现机器学习中存在着太多的通用处理模式，你会考虑该怎么形成一种数据处理流模式，而sklearn的pipeline可以说初步解决这个问题了。在使用pipeline，基于pipeline之上构建你的机器学习项目，你完全可以把最终你搭建起来的某个pipeline当做某个综合模型，最后就剩下很简单的这样一个问题：选择参数，输入数据，训练模型，利用模型进行预测，评估模型。

而关于选择参数，sklearn还基于pipeline提出了GridSearchCV网格搜索的概念，我只能说这是sklearn大成式的豪迈宣言了。通过GridSearchCV，在训练pipeline模型的时候，一些参数结合评估模型是可以自动完成优化工作的。

这里还顺便提一下神经网络框架keras和sklearn的关系，正如机器学习是包含神经网络这门学科一样，sklearn模块在使用上是可以包含keras的，keras只是作为神经网络模型算法里面最核心的一部分，至少从输入数据处理流向上应该是这样的，这方面还要继续尝试——多个神经模型，和传统机器学习算法和其他数据处理等等最终形成一个大型的综合模型。



### estimator

estimator只需要fit方法就可以了，这个fit方法的任务就是通过某种学习算法——从简单的线性回归到神经网络等等，训练好模型。然后其还应该提供 predict方法，这也是学习算法的本质要求，来利用训练好的这个模型。



### 特征的联合

前面提到sklearn的pipeline相当于一个综合模型了，在进一步使用 `FeatureUnion` 之后可以让你对特征的操作和添加新特征更加的灵活，FeatureUnion类其实际上对应于一个 transformer，你可以提取然后组合出你想要的那几个特征。请读者多看看 kaggle 的 [这个小项目](https://www.kaggle.com/baghern/a-deep-dive-into-sklearn-pipelines/notebook) ，个人觉得这种写法风格非常的优雅。

针对每个特征进行了提取和处理工作，然后特征联合。此外FeatureUnion 哪里你当然还可以加上额外的特征，进行额外的运算之后得到的新的特征。

还有这个小项目有一点很值得我们注意，也是这篇文章提醒了我，sklearn的train_test_split 分割pandas的DataFrame之后返回也是pandas的DataFrame或者Series【labels】对象。这种和pandas的无缝对接的写法也是很好的。

我在构建pipeline的时候还参考了 [这篇文章](http://zacstewart.com/2014/08/05/pipelines-of-featureunions-of-pipelines.html) 来更连贯地构建了一个综合模型，大概如下所示：

```python
  text = Pipeline([
        ('selector', TextSelector(key='processed')),
        ('tfidf', TfidfVectorizer(stop_words='english'))
    ])

    length = Pipeline([
        ('selector', NumberSelector(key='length')),
        ('standard', StandardScaler())
    ])

    words = Pipeline([
        ('selector', NumberSelector(key='words')),
        ('standard', StandardScaler())
    ])
    words_not_stopword = Pipeline([
        ('selector', NumberSelector(key='words_not_stopword')),
        ('standard', StandardScaler())
    ])
    avg_word_length = Pipeline([
        ('selector', NumberSelector(key='avg_word_length')),
        ('standard', StandardScaler())
    ])
    commas = Pipeline([
        ('selector', NumberSelector(key='commas')),
        ('standard', StandardScaler()),
    ])

    feats = FeatureUnion([('text', text),
                          ('length', length),
                          ('words', words),
                          ('words_not_stopword', words_not_stopword),
                          ('avg_word_length', avg_word_length),
                          ('commas', commas)])

    pipeline = Pipeline([
        ('features', feats),
        ('classifier', RandomForestClassifier(random_state=42)),
    ])
```



然后pipeline就好像一个大的综合模型一样，fit predict 等等之类的。



### GridSearchCV

网格搜索用于调参，具体pipeline的参数名字是 :

```python
f'{transformer_or_estimator_name}__{parameter_name}'
```

```python
from sklearn.model_selection import GridSearchCV

hyperparameters = { 'features__text__tfidf__max_df': [0.9, 0.95],
                    'features__text__tfidf__ngram_range': [(1,1), (1,2)],
                   'classifier__max_depth': [50, 70],
                    'classifier__min_samples_leaf': [1,2]
                  }
clf = GridSearchCV(pipeline, hyperparameters, cv=5)
 
# Fit and tune model
clf.fit(X_train, y_train)
print(clf.best_params_)
```

上面这个例子名字有点长，因为要往下找，features --> text --> tfidf --> 实际传进去的参数是 max_df

这里运算稍微有点耗时，如果程序化的话可以考虑将这些最佳参数最后保存起来：

```python
from sklearn.externals import joblib
joblib.dump(clf.best_estimator_, 'filename.pkl', compress=1)
```

下次直接使用最佳clf是：

```python
reclf = joblib.load('filename.pkl')
preds = reclf.predict(X_test)
```

还有种保存方法，就是直接保存clf，这更加直观，估计兼容性也更好一点，只是模型文件稍微大了些：

```python
from sklearn.externals import joblib
joblib.dump(clf, 'filename.pkl', compress=1)

reclf = joblib.load('filename.pkl')
```



### 机器学习的一般过程整理

下面将机器学习的一般过程在Pipeline的基础上再整理一下：

- 从各个数据来源中获取数据并汇总，这里pandas的io工具非常好用，没必要拒绝使用它。

- 基于pandas的普遍性数据预处理【这个就要根据实际情况来了】

- 分割训练集和测试集

- 针对训练集编写Pipeline pipeline的过程大致涉及到目标特征的提取或者新特征的计算和特征融合，缩放，特征选择，直到最终算法的选择。

- pipeline.fit  训练模型

- pipeline.predict 使用模型

- K折基于训练数据的验证得分 

```
cross_val_score(pipeline, train_data, train_labels, cv=4)
```
- pipeline.test 基于测试集的测试
- 上面讨论的模型如何保存和再利用
- 绘图表现也很重要，虽然这个工作可以往后面放一放。
- 基于GridSearchCV的参数调优
- 更多更多手段调优



