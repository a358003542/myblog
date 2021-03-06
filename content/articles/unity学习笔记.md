

[TOC]

## 开发环境

1. 安装visual studio
2. 选择安装 `使用unity的游戏开发`
3. 去unity官网下载安装 `unity hub`



## 入门功课

### 新建一个C#脚本

该脚本名字随意，但需要遵守如下规范：

1. 因为该脚本的名字就是类的名字，所以一般开头大写，然后在写法上遵守驼峰规则。
2. 该脚本的名字和里面类的名字一致。

### 双击脚本自动打开visual studio

可能已经设置好了，如果没有设置好，可以去Edit->首选项->外部工具->外部脚本编辑器那里设置。

设置好了就可以双击打开visual studio了。

### 将脚本作为组件挂在摄像头上

记得visual studio那边修改名字之后要保存下，然后点击摄像头，添加组件，选择脚本。

### 入门Debug

你的脚本类需要继承自 `MonoBehaviour` ，这样unity才能知道那个是一个脚本类。

Start方法每个组件游戏开始时就会执行，在这个方法里面写上这样的Debug语句：

```
    void Start()
    {
        Debug.Log("hello world!");
    }
```

保存运行游戏，如果没有问题的话，你在控制台那边应该看到一个hello world的消息。入门第一课算是完成了。

加分项，熟悉下面的LogFormat方法的用法，以后某些情况会很方便的。

```
Debug.LogFormat("{0} + {1} = {2}", 2,3,2+3);
```

## 引用Unity对象

### GetComponet generic method

GetComponet方法是一个generic method，需要指定查找的组件类型，查找只限于本GameObject的组件。

```
private Transform camTransform;
camTransform = this.GetComponent<Transform>();
Debug.Log(camTransform.localPosition);
```

### Find方法

Find方法可以用于查找不是本GameObject的其他GameObject，具体名字就是Unity面板上显示的那个名字。

```
private GameObject directLight;
private Transform lightTransorm;

directLight = GameObject.Find("Directional Light");
lightTransorm = directLight.GetComponent<Transform>();
Debug.Log(lightTransorm.localPosition);
```



### 引用脚本类

如果某个脚本类挂载在某个GameObject上，那么如下就可以引用该脚本类：

```
gameManager = GameObject.Find("GameManager").GetComponent<GameBehavior>();
```

上面代码的意思是有一个 `GameBehavior.csharp` 文件里面有 `GameBehavior` 类挂载在GameManager这个GameObject上，那么按照上面的语句就可以引用该脚本类对象了。



## Unity Editor基本的使用

关于Unity Editor的基本使用请读者自行熟悉软件界面，然后试着自己慢慢搭建起，比如一个平面作为一个基本的游玩空间，平面由四面墙围起来，然后等等其他立方体等等。移动缩放旋转和复制等等。

如果对这种类似的软件不太熟悉的话，推荐是找个相关的入门视频看看，如果对这类软件有点熟悉的，可能左看看右点点就大体能够掌握了。

## GameObject

 一个空的GameObject就是一个容器，其可以用于在Unity Editor的世界大纲视图中进行层级管理。一个GameObject下面管理的多个物体，如果将这个GameObject拖动到项目文件夹视图下，则将会创建一个Perfab预制件。预制件Perfab可以重复只用，并且改变基础Perfab属性会影响所有相关场景中的由此Perfab实例化的对象。

## animation clip

制作动画片段：

1. 新建一个Animations文件夹等下放动画片段资源
2. 选中你想要有动画效果的那个组件，选定window->Animation->Animation。
3. 选择启用关键帧记录模式，然后在每个帧上修改物体组件的某个属性

动画的开头和结尾常常有卡顿现象，哪怕你设置的旋转动作是0度到360度数值上是无缝对接的，仍然会有卡顿现象，你可以在曲线那里看到数值的变动是有一个切线变化率的，每一个帧都有两个切线，左切线是进入，右切线是离开，从头帧到结尾帧要想不卡顿，左右两个切线斜率必须是相同的，也就是co-linear的。

对于旋转动作可以将头尾两帧的双切线都改为线性。对应官方文档的 Broken-Linear模式。这样帧与帧之间是线性变化的，也就不存在那个变动斜率问题了。

## particle system

制作粒子系统：

1. 右键在世界大纲视图下新建->效果->粒子系统
2. 将粒子系统和你想要有该粒子系统效果的物体组件XYZ值设为一样
3. 调配你的粒子系统的各个属性

## 移动控制

`Input.GetAxis(axis_name)` 获取当前控制轴的值，比如Horizontal axis 方向left和 a键为-1，right和d为1。



## Update和FixedUpdate

Update是每帧执行，一般键盘输入放在这里。

FixedUpDATE是每个固定时间段执行，一般物理模拟内容放在这里。

## transform.Translate和Rigidbody.MovePosition

经过试验结论如下，在速度特别快的情况下两个都可能发生避开物理碰撞系统而发生穿模，速度很低的情况下两个也都不会穿模。不过在速度中等的情况下，用Transform的translate方法移动物体仍时不时会避开物理刚体碰撞系统，而在这种情况下刚体的MovePosition就表现要好一下。

此外FixUpdate的固定时间设定也会很好地防止物体移动速度不可捉摸的突变情况。

## transform的层级树

unity的每一个gameObject都有transform这个属性，transform的parent和child概念就是来自你在世界大纲视图上定义的GameObject的层级。

你可以通过transform的层级数来定位某个gameObject的transform，然后通过 `.gameObject` 这个属性来获得具体该gameObject对象。

## 碰撞器组件的是否是触发器属性

默认是否，如果勾选，则该碰撞器不具有物体碰撞功能而只有碰撞事件触发功能，也就是你可以穿模进去了。

## Physics.CheckCapsule

这个可以用来测试玩家角色是否接触地面，具体这个方法参数官方文档读起来也不是很直观，具体来说其定义了这样一个胶囊：

![img]({static}/images/2021/unity_capsule.png)

## 如何将某个摄像头调到当前视角

首先在编辑器上调整好开发者视角，然后选中某个摄像头，然后选择 `游戏对象-> align with view` 。

## 其他

`Ctrl+Shift+M` 在visual studio 上调出Unity快速方法输入。

