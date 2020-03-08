Title: tarfile和zipfile模块
Date: 2017-05-05
Status: draft
[TOC]





tarfile和zipfile模块
--------------------

tarfile是gzip，bz2和lzma压缩文件读写的解决方案，zipfile模块是zip压缩文件的解决方案，。

### 制作gz压缩文件

请看下面的例子：

    import tarfile
    with tarfile.open("skeleton.tar.gz", "w:gz") as tar:
        for name in ["setup.py","LICENSE","README.md","skeleton", "docs"]:
            tar.add(name)

这里首先用tarfile模块的**open**函数来返回一个TarFile对象，其中第一个参数是你的压缩文件的名字，第二个参数是处理模式。

模式可接受的参数如下：

r

:   默认值是r，就是只读某个压缩文件。类似有**r:gz**，**r:bz2**和**r:xz**，这里的意思就是具体设置好要读的压缩文件的格式（gzip，bzip2和lzma）。

w

:   类似的还有**w:gz**，**w:bz2**，**w:xz**。这里**w**或者**w:**官方文档的说明是（Open
​    for uncompressed writing），我对这个无压缩方式写不是很理解。

a

:   还有**a:**， Open for appending with no compression.
​    文件如果不存在将被创建。

#### TarFile的add方法

然后接下来就是往压缩文件里面添加内容（文件或者整个目录），具体就是用创建的TarFile对象的add方法，如上例子所示。

### 解压缩gz压缩文件

最简单的例子如下所示：

    with tarfile.open("skeleton.tar.gz") as tar:
        tar.extractall()

#### TarFile的extractall方法

用tarfile模块的open函数打开那个压缩文件，用返回的TarFile对象的extractall方法解压缩这个文件，注意用os.chdir来控制当前工作目录。

更多tarfile模块内容请参见[官方文档](https://docs.python.org/3.4/library/tarfile.html)。

### 提取egg文件中的内容

简单的例子如下所示：

    zip=zipfile.ZipFile("test.egg")
    zip.extract('test.txt')

这里用zipfile模块的ZipFile构造函数创建了一个ZipFile对象，然后用ZipFile的**extract**方法提取出了test.txt文件在当前工作目录。

相关的**extractall**方法将会提取出压缩文件中所有的内容。

### 制作zip压缩文件

简单的示例如下：

    with zipfile.ZipFile('test.zip','w') as zip:
        zip.write('test2.png')

首先用zipfile模块的ZipFile构造函数创建一个ZipFile对象，这里mode需要使用**'w'**，然后使用ZipFile对象的write方法来添加内容。你可以猜到如果模式是**'a'**的话write方法是给这个压缩文件添加内容（a模式同文件操作含义如果原压缩文件不存在也是可以创建的）。

更多zipfile模块内容请参见[官方文档](https://docs.python.org/3.4/library/zipfile.html)。

