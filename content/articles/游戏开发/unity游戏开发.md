### 前言

本文主要写着一些笔者在进行Unity游戏开发时的实践经验分享。



### 翻译插件遇到的一个问题

个人编写的小型翻译插件没太多花里胡哨的东西，反而很好用，不过遇到了一个问题，那就是不管是设置 `.text` 还是通过 `SetText` 方法都有可能让原Text对象的原始文本内容给永久修改掉。这个似乎有时并没有修改，有时会修改，可能和退出机制有关，但不管怎么说这个是不可控的。

只好每个text下面再另外新增一个脚本用来保留该text的字典key。

### UI图像类型属性和sprite导入设置

UI图像类型有一个已切片sliced属性，假设你的sprite图像分为九个区域，其中四个角落是那种圆角，然后你希望你的图像有很好地拉伸扩展性能并保留四个圆角的显示效果，则可以选择这个sliced属性。具体来说这九个区域的设置和你的sprite导入设置有关系。

sprite是单一还是多个都是可以的，不过推荐还是用外部编辑器将周边的多余的透明区块剔除掉，能够选择单一就选择单一。然后就是sprite图片从个人实践经验来看并不是像素越高越好，比如这里讨论的四个圆角，四个圆角加上一定的周边区域，32*32的图片大小就够用了，因为sprite作用在UI上缩放，直线或者涂满颜色的区块缩放显示效果都还是挺不错的。

然后网格类型mesh type一定要选择 **全矩形** 。然后进入sprite editor：

![img]({static}/images/2021/sprite_sliced.png)

注意拖动要拖动中间的绿色方块，其他位置是调整整个sprite大小的。然后点击应用。



### 场景里面东西太多，如何选择性地显示

参考官方文档的这里： [Unity - Manual: Scene visibility (unity3d.com)](https://docs.unity3d.com/Manual/SceneVisibility.html)

世界大纲视图对象左侧有个眼睛的形状可以切换该对象在场景中的可见性，不影响实际游戏中的效果。

如果是只想观察场景中的某个或某些对象其他对象都希望隐藏则选中那些你想要显示的对象，然后按键 `Shift+H` 进入Isolation view模式，再按键 `Shift+H` 退出Isolation view模式。

### 怎么我的场景看上去有点暗

在窗口-渲染那些烘焙下光照，一般Build项目之前是需要烘焙下光照的。

### 怎么修改动画的播放速度

可以通过某个参数来控制动画的播放速度，具体如下图所示：

![img]({static}/images/2021/unity_animation_speed.png)

### Audio mixer是做什么的

请参看这个视频： [Audio Mixer and Audio Mixer Groups - Unity Official Tutorials - YouTube](https://www.youtube.com/watch?v=vOaQp2x-io0&ab_channel=Unity)



### URP

Universal Render Pipeline，除非是很高画面要求的游戏，则推荐使用HDRP，否则一般项目推荐使用URP。

URP的安装就是安装URP包，因为URP包内置了post process功能，所以原来的Post Processing Stack包可以删掉了。

然后需要在` 项目设置->Player->其他设置` 那里，将Color Space颜色空间设置为线性，意义不明，[参考网页](https://learn.unity.com/tutorial/introduction-to-urp)。

然后需要创建一个URP asset，具体是

```
Assets > Create > Rendering > Universal Render Pipeline > Pipeline Asset
```

然后是启用该asset，具体是在 `项目设置->图形` 那里选择该asset文件。

至此原有项目就已经升级为URP项目了。

#### 升级你的着色器

项目升级为URP项目，会自动升级你的着色器，后面你也可以手工选择那些旧有的着色器来升级为URP支持的着色器，具体就是选择：

```
Edit > Render Pipeline > Universal Render Pipeline
```

然后选择 ` Upgrade Project Materials to URP Materials` 或者  `Upgrade Selected Materials to URP Materials` 。

不是所有的旧有着色器都能成功升级为URP支持的着色器的。

### null check

在C#那边推荐的null检查语法是 `is null` ，当时说的是可以规避掉 `==` 被重载的情况，null 检查会更严谨些，但在unity这边，似乎unity对象的 `==` 运算符已经被重载了，所以 `is null` 检查会失效。而unity的官方2020版推荐的null check语法是这样的：

```c#
using UnityEngine;
using System.Collections;

public class Example : MonoBehaviour {

    void Start () {
        GameObject go = GameObject.Find("wibble");
        if (go) {
            Debug.Log(go.name);
        } else {
            Debug.Log("No game object called wibble found");
        }
    }

}
```

对于unity的对象可以这样判断，但对于C#的其他对象还是推荐使用 `is null` 。个人实践unity的null对象通过 `is null` 判断并不是一个c#的null对象，而如果通过 `go == null` 是可以判断的，然后unity的null对象能够用上面的写法，也说明了它不是一个c#的null，而是一个对象，并且这个对象还支持转bool类型的方法。个人推断这种转bool和 `== null` 写法内部区别不是太大。

但这种情况是令人沮丧的，不说还需要额外区分哪些对象是不是unit对象，因为null在C#中的普遍存在，经常你编写的函数和某些地方可能返回null或者unity空对象或者unity对象，所以更推荐的做法都写成

```c#
        if (go != null) {
            Debug.Log(go.name);
        } else {
            Debug.Log("No game object called wibble found");
        }
```



### 地形环境的开发

笔者经过摸索并没有找到特别好的地形环境搭建工具，至少免费的没有。那个L3DT并不是很好用，还将很多问题弄复杂了。地形环境开发最关键的问题不是要弄出一个随机的看上去还行的地形环境出来，那随便怎么弄一下就行，而是要首先用绘画工具加上游戏设计思路将地图的大概形状和玩家活动区域分块和玩家可行走区域等设计规划出来。然后才是实际搭建unity的Terrian。

游戏设计阶段对地图的大概情况也就是等高线的手绘是一个很重要的一环，我想在这一环之上，试着完善等高线图然后使用用unity的terrian地形生成，也就是基于等高线图来自动生成地形，实际输出效果不是很好。等高线边缘通过光滑倒是可以微调，等高线的相对高度通过绘制图形是利用灰度的百分比也可以做到一个大概的效果。但仍然有太多地方需要优化了，比如规划的玩家可行走路线的斜坡表达，比如河道边的效果表现，比如等高线区域太过于平坦。

这些微调整优化里面有一些倒是不那么紧要的，毕竟Unity的地形仍然只是一个原型工具，比如等高线区域太过于平坦，加入岩石模型就可以改变这点，但有一些则是需要立刻在地形上进行微调的，一个是河道边路斜面优化，一个是玩家可行走路线上一些斜坡的优化等。

Unity的灰度百分比推荐8位灰度，0%白表示z=0，然后100%白表示你的地形的最大高度，然后进行百分比划分。Unity接受的Terrian必须是正方形的raw图片格式。

整个地形环境的开发如上描述从地图等高线手绘，到玩家活动区域和行走路线设定到Unity的Terrian，再就是构想玩家于某一点的视觉呈现概念图到Unity的terrian地形微调，再到各个岩石，地面，树木等模型的建模，再到模型制成unity的预制件和根据terrian来放置，然后后期还有根据地图设计对石头树木矿石等各个资源型预制件的微调。这一流程虽然繁琐但每一步都是必要的，可见一个游戏的地形环境开发也不是一蹴而就的事。
