

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

可能已经设置好了，如果没有设置好，可以去 `Edit->首选项->外部工具->外部脚本编辑器` 那里设置。

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




## Unity Editor的使用

关于Unity Editor的基本使用请读者自行熟悉软件界面，然后试着自己慢慢搭建起，比如一个平面作为一个基本的游玩空间，平面由四面墙围起来，然后等等其他立方体等等。移动缩放旋转和复制等等。

推荐是找个相关的入门视频看看，当然喜欢自己摸索的多接触接触也就可以了。

### 预制件

预制件Perfab非常的有用，可以说是Unity开发里面很重要的一个核心概念了。可以将Perfab理解为编程中的类，而场景中的各个对象在没有perfab之前属于游离的实例，在创建perfab之后才真正可以称之为根据某个perfab类在场景中创建的实例。所以一般来说Unity开发中场景的大部分GameObject都应该perfab化。

嵌套预制件，多个perfab形成嵌套关系并没有改变原perfab和场景中实例间的继承关系。

预制件变体，你可以根据某个perfab来创建某个预制件变体，这些预制件变体更类似于类的继承关系，比如你改变原预制件的某个属性，之后创建的预制件变体的某个属性也会对应发生更改。【变种属性应该继续保持原有的继承更改关系。】

**需要注意的是在项目间重复使用，Perfab和Perfab之间和各个资产之间的引用关系必须是一致的，也就是原Asset资产的文件夹层次是保持一致的。**

### 解压缩Perfab

是由原场景中GameObject转成Perfab的反向操作，也就是该GameObject成为一个常规的GameObject了。

### 练习题1

请读者随便新建一个场景，新建一个平面，命名为ground，预制件化，然后在该平面的两角放置两个立方体，两个立方体是根据一个预制件perfab而来，然后将该立方体拖动为ground的子辈。然后将ground预制件化。然后再根据ground预制件再新建一个平面再将这两个平面对接。

经过试验我们可以发现，嵌套预制件也有一种继承层次在里面。比如现在假设有 boxBase，boxRight，box3这三个材质，其中boxBase作用于box perfab，boxRight作用于ground perfab的右角盒子，box3作用于场景中某个特别的盒子。

以左角的盒子为例，不受ground perfab的修改影响，不受box3修改的影响，所以最终颜色是boxBase决定的。以第二个盒子为例，受boxBase修改影响，然后再受ground perfab右角修改影响，最终颜色是boxRight。而第三个盒子的颜色则就是box3材质颜色。

简单来说嵌套Perfab有一种类似编程上的继承关系在里面，

### 如何将某个摄像头调到当前视角

首先在编辑器上调整好开发者视角，然后选中某个摄像头，然后选择 `游戏对象-> align with view` 。

## blender和unity的协作

虽然Unity的ProBuilder和PloyBrush提供了一定的模型建立和地形构建的能力，但这主要还是用于原型开发，一般建模当然还是推荐在blender上完成，然后可能Unity的terrian地形工具搭建某些简单的地形有用，不过就成熟的项目来说地形构建也推荐是通过blender建模来实现。

首先Unity的地形工具是有局限性的，某些封闭的如洞穴场景或者如同minecraft需要和地形的元素进行交互的场景是不应该使用Unity的terrian地形工具的，而应该通过blender建模来导入到Unity场景中来。其次即使是那些似乎看起来Unity地形工具勉强能够应付的场景，如果后续对地形在表现细节上有更多的要求，那么也应该通过blender建模来实现。

### blender建模

blender建模导入Unity下面说一下基本的流程思路，可能有时会有一些细节上的问题。

1. 按A全选你想要导出的元素，主要是网格体和骨架。选择导出到FBX，然后选择网格体，如果有骨骼的话也推荐将骨架选上。然后导出。
2. 将FBX文件移动到你的Unity项目中，Unity会自动检测导入，但一般来说你还需要对模型导入配置参数进行一些调整。比如材质，比如如果是人形模型，而你希望根据该人形模型构建动画还需要自动创建Avatar。
3. FBX模型最好是另外单独一个地方存放，导入的模型参数配置好之后，拖入场景，然后拖动制成Perfab预制件，然后解压缩预制件，再对该预制件进行一些你想要的修改，比如有的加上碰撞器和行为脚本之类的。在更新预制件。

### blender动画

blender里面的动画导出到Unity也是类似上面的导出FBX，实际上就是导出的你的模型的骨架的一些移动变换数据，然后Unity接受成为动画Clips。

1. 按A全选你想要导出的元素，主要是网格体和骨架。选择导出到FBX，然后选择骨架，和导出一般模型不同，如果你只希望导出动画的话这里只选择骨架即可。
2. FBX动画文件导入Unity项目中，然后对动画Animation这一栏一些参数做出一些调配，还有Avatar选择Copy from之前本模型创建的那个Avatar。

个人测试相同的人形模型差异不太大的话即使是原来不同的Avatar动画文件里面的内容也是可以复制，大体可以参考的。这一块主要是动画姿态的不匹配问题，如果是自己很粗略弄的动画反倒是泛用性会很强，而那些动捕或者调配的很好的姿态，泛用性会很差，比如一个女性角色的走路姿态套用到一个男性角色上然后出来的效果你懂的。

简单的Unity动画就在Unity那边编辑即可，但有些动画文件很复杂，而Unity那边的动画文件编辑功能并不是很强大，可能还是要继续再blender那边修改之后再应用到Unity那边。

最后提醒一点blender那边的骨架的各个名字最好先就定义好，从blender到unity预制件这条线路各个骨架的名字基本上不会再修改了，修改只会造成各种麻烦。



## 输入

### input system

new unity input system 更多地多设备输入兼容。文档在 [这里]([Installation guide | Input System | 1.1.0-preview.3 (unity3d.com)](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.1/manual/Installation.html)) 。

激活新的输入系统： `Edit->Project settings->Player-> Active Input Handling` 。

添加Player Input 组件

编写Action输入键位绑定

如果设置的是Send Message，则假设有Move Action，则对应该GameObject的`OnMove` 方法，Move发送的是一个Vector2值。x对应的是该GameObject Right方向上的位移，y对应的是该GameObject forward方向上的位移，有一个中间值(0.7,0.7) ，是45度的方向，你可以简单理解为right方向移动了0.7个单位，forward方向移动了0.7个单位，0.7这个数字的含义表示目标方向的移动长度还是大约1个单位。

另外一个是单键位绑定，返回的是float值，1表示键位触发。

如果设置的是InVoke Unity Events，则需要下面写上对应Action的回调方法，似乎InVoke Unity Events功能更强大一些，其支持对按键动作多种状态的判断。

```c#
    public void OnFire(InputAction.CallbackContext context)
    {
        switch (context.phase)
        {
            case InputActionPhase.Performed:
                if (context.interaction is SlowTapInteraction)
                {
                    StartCoroutine(BurstFire((int)(context.duration * burstSpeed)));
                }
                else
                {
                    Fire();
                }
                m_Charging = false;
                break;

            case InputActionPhase.Started:
                if (context.interaction is SlowTapInteraction)
                    m_Charging = true;
                break;

            case InputActionPhase.Canceled:
                m_Charging = false;
                break;
        }
    }
```

上面Started最先触发，然后再触发Performed。如果你的context设置了SlowTapInteraction也就是一定时间的按键判断等，这块后面再详细了解。

**NOTICE:**  详细阅读上面的case判断，如果不加上case判断，一般的行为会出发三次，一次started = 1，一次performed = 1，一次canceld = 0。 

#### 读取值

上面started，performed和canceld只是针对更复杂的按键情况，如果只是一般的使用则如下读取值然后大致类似传统输入系统那样去做即可。

首先Move和Look读取Vector2的值：

```
Vector2 m_Movement = context.ReadValue<Vector2>();
```

然后对于一般按键值读取为bool值：

```
bool m_Attack = context.ReadValueAsButton();
```

按照传统的方法这些都应该在Update方法里面写上的，现在在对应的OnMove之类的方法写上然后各个键值每帧都会更新的，也就是相当于Update上执行了这些命令。



#### 判断本帧某个键位是否按下了

这个键位判断不需要去设置Actions的配置对于任何按键都可以如下直接去判断。

```
  Keyboard.current.space.wasPressedThisFrame
```

### Input.mousePosition

获取当前鼠标在屏幕上的坐标，返回一个Vector3值，z值总为0，x和y都等于0时表示左下角，右上角是 `(Screen.width, Screen.height)` 。







## 物理系统

### 碰撞器

#### 碰撞器组件的是否是触发器属性

默认是否，如果勾选，则该碰撞器不具有物体碰撞功能而只有碰撞事件触发功能，也就是你可以穿模进去了。比如某些液体就可以勾选这个选项这样玩家既可以进入该液体同时也可以跟踪玩家进入该液体的事件。

### Character Controller组件

一般第一人称或第三人称角色控制玩家会需要更灵活地控制角色，这种情况下玩家角色如果加入物理系统的刚体会有一种操作上的不顺畅感，但此时仍然希望保留碰撞的物理效果，可以加入Character Controller组件来实现这点。

我们看到角色控制器下面有三个参数：center控制胶囊碰撞体的中心位置，半径控制胶囊碰撞体的宽度，height控制胶囊碰撞体的高度。大体可以猜到角色控制器就是通过这个胶囊碰撞体来和环境交互的。

#### isGrounded

本角色控制器组件在上一次移动中是否接触到了地面。



### 射线投射

```
public static bool Raycast(Vector3 origin, Vector3 direction, float maxDistance = Mathf.Infinity, int layerMask = DefaultRaycastLayers, QueryTriggerInteraction queryTriggerInteraction = QueryTriggerInteraction.UseGlobal);
```

从origin向这direction方向发射一个射线，如果射线和某个碰撞体相交则返回true，否则返回false。

这个射线投射很有用，物理系统里面的很多功能都是基于这个射线投射，比如碰撞判断。此外还可以基于这个射线投射来构建出很多有用的功能：

- 比如想要确定玩家当前的选择交互对象，视窗中心射出一个射线，和什么GameObject相交则认为该GameObject是当前玩家的选择对象。
- 然后再比如射击游戏可以用射线投射来模拟射击动作，并利用RayCatHit返回对象来获取被击中物体的很多信息，从而来更好地构建射击动作。



### Physics.CheckCapsule

这个可以用来测试玩家角色是否接触地面，具体这个方法参数官方文档读起来也不是很直观，具体来说其定义了这样一个胶囊：

![img]({static}/images/2021/unity_capsule.png)

其中的layer层一般将地形GameObject放入该层。

```
public static bool CheckCapsule(Vector3 start, Vector3 end, float radius, int layerMask = DefaultRaycastLayers, QueryTriggerInteraction queryTriggerInteraction = QueryTriggerInteraction.UseGlobal);
```

### 图层

图层的创建和将某个GameObject分配给某个图层在Unity Editor那边操作熟悉下即可。

图层在某些特定的地方会很有用，比如摄像机渲染和物理系统的射线碰撞判断，否则不要创建一些无谓的图层。



#### 摄像机的剔除遮罩属性

Culling Mask 用来设置本摄像机想要渲染的图层，默认是Everything。

现在假设有两个摄像机，一个摄像机对着一个红色的立方体，该红色的立方体在RED图层；另外一个摄像机对着蓝色的立方体，该蓝色的立方体在BLUE图层。第一个摄像机的剔除遮罩没有选择BLUE图层，则该摄像机的渲染图像里面没有蓝色的立方体；第二个摄像机的剔除遮罩没有选择RED图层，则该摄像机的渲染图像里面没有红色的立方体。

#### 物理系统的图层碰撞矩阵

在 `Edit->Project settings->Physics` 那里，有一个Layer collision Matrix，用来设置你的项目里面各个图层中的各个GameObject是否有物理系统的碰撞判断。

此外物理系统的射线投射函数`Raycast` 里面有个 `layerMask` 参数就是设置你希望该射线和那些图层交互的。比如：

```
int layerMask = 0;
```

则射线不会和任何东西发生碰撞。

如果：

```
int layerMask = 1<<8;
```

则射线会和第8图层的GameObject发生碰撞。

如果：

```
int layerMask = ~(1<<8);
```

则射线会和其他图层的GameObject发生碰撞除了第8图层。

看到这里读者可能已经明白了，一共32个图层，第一图层是 `00...00001` ，第二图层是`000...00010` ，比如我现在希望取第一图层和第二图层，就是 `00...0001 | 000...00010`  ，也就是 `00...11` 。

但个人还是不喜欢这种写法，还是推荐多使用 `LayerMask.GetMask` 这个方法，这个方法接受一个图层或者多个图层的名字，然后返回也就是类似上面描述的layermask的数值：

```
LayerMask.GetMask("UserLayerA", "UserLayerB");
```

## 序列化

序列化是理解Unity Editor如何工作的关键，这当然对你后面更好地使用Unity Editor从而更好地进行游戏开发很重要，但更重要的是Unity Editor可以看作利用Unity技术实现的第一个游戏，因此Unity Editor广泛使用的序列化技术对你的游戏代码开发同样具有参考价值，这点我们后续会看到。

推荐读者参考阅读 [这篇文章](https://blogs.unity3d.com/2014/06/24/serialization-in-unity/) 。

以下是Unity序列化技术中涉及到的一些场景：

- Unity Editor会将属性面板的一些属性进行序列化存储起来。
- perfab预制件也是一种序列化手段。
- 当unity实例化一个对象时，首先是把该对象序列化，然后新建一个对象，然后反序列化获得的数据打入新的对象中。
- Unity Editor执行保存动作也加载场景是利用了yaml进行的序列化和反序列化动作。
- Unity Editor的热重载：代码发生变动，首先序列化所有编辑器窗体，再销毁窗体，再更新旧的C#代码，再加载新的C#代码，再重新创建窗体。



Unity会对以下属性进行序列化：

- public
- [SerializeField] 属性
- not static
- not readonly
- not const
- unity能够序列化的

unity能够序列化的属性：

- 自定义的non abstract class有[SerializeField] 属性标注
- 自定义的结构有[SerializeField] 属性标注
- 由UntiyEngine.Object衍生出来的类
- C#的基本数据类型（int, float, double, bool, string etc.）
- 可以序列化对象组成的array
- `List<T>`  T是可序列化的类型。

### SerializeField

上面序列化一节提到，一个私有字段如果加上 `[SerializeField]` 标识，Unity对该私有字段也将使用序列化技术。

以编辑器脚本的某个公有字段来说，unity会将其序列化存储在硬盘中从而实现热重载，也就是下次启动游戏之后还会将你修改的这些参数填上去。如下加入 SerializeField 之后，该私有字段一样也会进入unity的序列化管理。

```
[SerializeField] private AssetReference _persistentManagersScene = default;
```

### ScriptableObject

ScriptableObject继承自UntiyEngine.Object，按照上面序列化一小节的描述，ScriptableObject是可序列化的对象。

ScriptableObject的作用是充当一个数据容器。Unity的预制件实例化，里面的数据将会产生多个副本，所以对于重复使用的公有数据一般是推荐使用ScriptableObject来存储数据，然后预制件来访问这些数据。

#### ScriptableObject的唯一性

ScriptableOjbect的唯一性是根据你创建的asset文件唯一性来的，只要保证是引用的同一asset文件，则生成类的实例都是一样的，个人测试也是实例id都是一样的。

如果是和Unity Addressable Asset system相结合，如果你的ScriptableObject是通过 `LoadAssetAsync` 加载进来的，那么在引用Asset的时候实际上都是在使用一个ScriptableObject，你可以将这个ScriptableObject看作类似perfab预制件一样的东西，直接使用该数据对象就是直接使用预制件，都是在用同一个东西。

而如果你调用 `InstantiateAsync` 来对ScriptableObject进行了实例化，则就是不同的数据对象了。[参考网页](https://docs.unity3d.com/cn/2019.4/Manual/class-ScriptableObject.html)。

经过个人试验发现：

```
		bool t1 = _menuToLoad[0] == _menuToLoad[1];
		bool t2 = _menuToLoad[1] == _menuToLoad[2];
		Debug.Log($"{_menuToLoad[0].GetHashCode()}");
		Debug.Log($"{_menuToLoad[1].GetHashCode()}");
		Debug.Log($"{_menuToLoad[2].GetHashCode()}");
		Debug.Log($"test:      {t1}");
		Debug.Log($"test:      {t2}");

		return;
```

上面代码`_menuToLoad` 列表一号和二号是不同的scriptableobject，二号和三号是相同的scriptableobject。然后scrptableobject的相等性可以使用 `==` 运算符来进行，然后通过HashCode发现相同的scriptableobject的哈希值也是相同的。

#### 创建一个ScriptableObject对象

```
[CreateAssetMenu(fileName = "PersistentManagers", menuName = "Scene Data/PersistentManagers")]
public class PersistentManagersSO : GameSceneSO { }
```

fileName是点击菜单按钮之后默认保存的文件名，menuName是在Unity Editor对应的菜单按钮位置，上面的例子是：`资源->创建->场景数据->PersistentManagers` 。

## Unity协程

如果读者之前接触过协程概念，对于这里的协程的理解会很快，但有一点是需要特别强调的。那就是Unity的协程更多的是一个Unity自身基于逐帧运算然后做出来的概念，和很多编程语言上的协程概念比较起来，其底层甚至可能都不依赖于线程切换。

C#语言那边有异步编程，其使用的async func 和await之类的和python的异步编程很像，这些才是严格意义上的协程概念，Unity协程只是利用了C#的 `IEnumerator` 和 `yield return` 构建起来的类似python的可迭代对象，然后在这个可迭代对象之上构建出来的Unity协程概念。

具体Unity协程的编写如下：

```c#
IEnumerator CoroutineExample(int a){
    // do something 
    yield return null;
    // still do something
    yield return null;
}
```

启动一个Unity协程：

```c#
StartCoroutine(CoroutineExample(1));
```

该CoroutineExample协程会在遇到yield return 那里停止执行，然后下一帧再回来继续执行本协程。

此外可以如下启动协程：

```
StartCoroutine("CoroutineExample", 1);
```

这种指定协程名字符串的启动后面可以指定名字要求停止某个协程：

```
StopCoroutine("CoroutineExample")
```

你还可以让某个协程暂停执行多少秒：

```
yield return new WaitForSeconds(.1f);
```

### 嵌套Unity协程

参考了  [这篇文章](https://www.alanzucconi.com/2017/02/15/nested-coroutines-in-unity/) 。

如下：

```
yield return StartCoroutine(AnotherCoroutine())
```

这种形式，父协程要等待子协程完成才会继续往下走，也就是对于父协程来说，子协程的整个执行过程是同步的。因为子协程仍然是通过 StartCoroutine启动的，其内部的执行是异步的。

### 平行Unity协程

```
IEnumerator A()
{
    
    // Starts B, C, and D as coroutines and continues the execution
    Coroutine b = StartCoroutine( B() );
    Coroutine c = StartCoroutine( C() );
    Coroutine d = StartCoroutine( D() );
    
    // Waits for B, C and D to terminate
    yield return b;
    yield return c;
    yield return d;
    
}
```

B C D这几个子协程从启动开始就执行了，说的再直白点就是正常启动协程则一下就启动起来了，根本花费不了什么时间。

上面两种情况可以总结为那就是嵌套Unity协程中，父协程是同步的。所谓同步就是Unity会一直在这里执行，而Unity协程所谓的异步指的是内部执行了很小碎片的不怎么花费时间的动作，然后就yield return了，然后再等待下一帧再继续执行，并不阻塞主程序。

我们看到Unity协程解决的主要是帧动作太多的问题，通过Update等函数我们可以设计每一帧进行某个动作，然后我们发现对于很多问题并不需要每一帧都做，通过Unity协程可以解决这个问题；还有些过程可能横跨多个帧，但其内部动作可以分解为很多小动作，然后每帧再分别执行这些小动作即可，这可以通过Unity协程解决。

但Unity协程不能解决某个动作就是花费时间太长，从而造成你的游戏进程阻塞这个问题，这还是需要靠多线程或异步来解决，Unity协程在这里的作用主要就是每帧来检查一下这个费时的异步动作完成了没有。



## 摄像机

### 多个摄像机

Unity可以添加多个摄像机组件，摄像机有个参数叫做深度，这个深度值最大的摄像机将是最终显示的那个摄像机【如果两个摄像机在显示上都是全覆盖的】。

### Camera.main

如果你的主摄像机有标签 `MainCamera` ，则可以通过 `Camera.main` 来调用。

### Camera.ScreenPointToRay

定义了一个射线，从摄像机出发射向屏幕的某个坐标点。

```
public Ray ScreenPointToRay(Vector3 pos);
```

该pos的z值将忽略。

### 分屏显示

摄像机的Viewport矩形x和y值决定了显示的起始位置，x值是横向，y值是竖向。比如(0,0) 是最左边那里，`(0.5,0)` 是横向宽度50%竖向继续0%那里。然后w是显示的宽度，0.5就是显示宽度为整个宽度的50%。h是显示高度。

调配两个摄像头的Viewport矩形参数，一个(0,0)显示宽度0.5，显示高度1；一个(0.5,0)显示宽度0.5，显示高度1就可以达到一种横向分两个屏幕显示的效果。

继续调配这个Viewport矩形参数还可以做到另外一个摄像头专门在显示界面右上角来显示，一种类似小地图的功能。

### viewportToWorldPoint

根据摄像机视图空间的一个Vector3坐标转成游戏场景中的Vector3坐标。

```
Vector3 p = camera.ViewportToWorldPoint(new Vector3(1, 1, camera.nearClipPlane));
```

其中Vector3的x和y如果是 `(0,0)` 则是左下角，如果是 `(1,1)` 则是右上角，这个z值设置为 `camera.nearClipPlane` 是摄像机的近裁剪平面，还有一个远裁剪平面，z值也可以设置为0就是紧贴着摄像机。

### cinemachine

cinemachine不是要取代原Unity的摄像机组件，而是新增了一个cinemachine brain组件用于控制原Unity摄像机的位置和Aim，同时还提供了其他一些额外的功能，比如摇动效果。

利用cinemachine创建一个第三人称跟踪式摄像头是很方便的，而后续更多的运镜，包括摇摄，跟摄，多个摄像头视角转换都可以很容易办到。

一般使用就使用virtual camera，其他camera只是在特定应用场景下才好用，可能额外增加的一些特性限定并不适合你的应用需求。

Follow控制的摄像头的跟随对象，Body控制的是摄像头跟随跟随对象的移动行为，但是要注意3rd person follow 似乎还会有额外的摄像头旋转动作。

loot at控制的摄像头的瞄准对象，Aim控制的是摄像头的旋转行为，有可以根据用户行为来旋转摄像头，但只是针对的旧版本的输入控制，如果你希望自己实现根据用户的操作来旋转摄像头，最好是自己编写脚本，那么Aim填上do nothing，免得干扰。

body的Framing transposer很灵活和全面，很好用，摄像头偏移，距离，damping，dead zone，soft zone等概念都是可以调整的。

- dead zone cinemachine会保证那个黄点也就是关注点在dead zone之内
- soft zone 如果黄点在dead zone则不会有动作，如果黄点在soft zone 则摄像头会开始调整，摄像头调整可块可慢，具体可根据damping这个值来设置。



## 脚本

### GameObject

 一个空的GameObject就是一个容器，其可以用于在Unity Editor的大纲视图中进行层级管理。一个GameObject下面管理的多个物体，如果将这个GameObject拖动到项目文件夹视图下，则将会创建一个Perfab预制件。预制件Perfab可以重复只用，并且改变基础Perfab属性会影响所有相关场景中的由此Perfab实例化的对象。

一个GameObject里的组件如果调用`gameObject` 属性，比如transform，或者脚本类this，都会指向这个目标容器GameObject。

```
this.gameObject;
this.transform.gameObject;
```

脚本作为组件绑定在某个GameObject上，如上在脚本中调用 `this.gameObject` 则会引用该GameObject。

所有的GameObject，即使是一个空的GameObject也会有transform属性。



#### GetComponent方法

这个方法在 `GameObject.GetComponent` 上，也就是Unity上的所有游戏对象都是可以调用这个方法的，这既包括脚本组件对象，也包括transform对象。

然后GetComponent方法主要是找目标组件和本脚本组件或者其他组件在同一GameObject之下的情况，当然你也可以直接引用本GameObject来调用这个方法：`gameObject.GetComponent` 。返回的是找到的第一个相同类型的目标组件，如果没有找到则返回null。

```
_rb = this.GetComponent<Rigidbody>();
```

上面假设本脚本和某个刚体组件同在一个GameObject之下，则如上引用该目标组件。其实你在Unity Editor看到的其他组件说白了也是一些脚本，只是说之前Unity官方或者其他库预先帮你写好了。脚本也可以不绑定在GameObject上，这个后面会提到，其叫做 ScriptableObject。

#### 引用其他脚本组件

现在假设你的GameObject下面有多个脚本组件，则引用另一个脚本组件代码如下：

```
gameManager = this.GetComponent<GameBehavior>();
```

上面的意思是本GameObject下还有一个脚本类，其类名叫做 `GameBehavior` ，那么那个刚体组件呢，其对应的就是还有另外一个脚本，其类名叫做Rigidbody。请注意，这里的讨论只是在试图澄清组件和脚本类之间的关系，并不是在说如何使用其他类里面的数据，Unity对于交互数据更推荐使用ScriptableObject或者其他方法来处理，一般来说脚本类里面只放着行为逻辑。

#### Find方法

Find方法可以用于查找不是本GameObject的其他GameObject，具体名字就是Unity面板上显示的那个名字。

```c#
private GameObject directLight;
private Transform lightTransorm;

directLight = GameObject.Find("Directional Light");
lightTransorm = directLight.GetComponent<Transform>();
Debug.Log(lightTransorm.localPosition);
```

##### 更推荐的做法

在实践中如上使用Find方法其实并不是很好用，更推荐的做法是将你需要定位的GameObject做成你的脚本类的公有属性或者序列化属性，值得一提的是这种做法可用于定位目标GameObject，也可用于定位目标组件，目标组件在十万八千里远或者就在旁边都可以这样用。

```
public YouTargetClass object_name;
```

然后在编辑器上选中目标对象或者拖动目标对象到目标输入框。你给定的类名一定要是你想定位的目标的类，这样选择框才会弹出对应的候选项。

这种做法的好处就是编辑器友好和简单，又能少写代码又简单当然是推荐使用的了。一般大部分应用场景都可以用这个推荐做法来解决引用目标对象的问题，只可能在某些极个别的情况需要代码查找。

#### transform的层级树

unity的每一个gameObject都有transform这个属性，这个transform是有一个内在的层级树在里面的，这个层级树也就是里面的parent和child概念是直接对应你在大纲视图上看到的GameObject的层级的。

你可以通过transform的层级数来定位某个gameObject的transform，然后通过 `.gameObject` 这个属性来获得具体该gameObject对象。

你可以通过如下语句来迭代某个GameObject下的子节点：

```c#
foreach (Transform child in parent){
    // do something
}
```

然后有 `transform.parent` 来返回本transform的父节点transform对象。更多的方法请参看 Transform 类。

### 常驻GameObject

你可能希望某些GameObject常驻在游戏里面然后多个场景调用。一个做法是不摧毁原场景，设置一个常驻场景作为该GameObject所在地，这可以通过规范你的项目场景加载卸载逻辑来实现。还有一个做法如下：

#### DontDestroyOnLoad

当加载一个新的场景时会把原场景的所有对象destroy掉，如果加入如下代码：

```
DontDestroyOnLoad(this.gameObject);
```

则本脚本绑定的那个GameObject在场景切换时将不会被删除掉。

### Update和FixedUpdate

Update是每帧执行，一般键盘输入放在这里。

FixedUpdate是每隔一定固定时间段执行，一般物理模拟内容放在这里。

此外还需要了解 `Time.deltaTime` ，其返回的是上一帧到这一帧的时间间隔。以FixedUpdate为例，其内每次调用 Time.deltaTime都是相同的某个时间段，而对于Update则没有这个规律。

### Awake和Start

Awake和Start在脚本组件启动时都会被调用一次，Awake先于Start，脚本组件即使没有Enabled，场景启动时Awake也会执行，而Start只有在该脚本组件Enabled的情况下才会执行。

此外还有一个OnEnable方法，它在Awake之后，如果脚本Enabled则会调用。



### OnTriggerEnter和OnCollisionEnter

OnTriggerEnter 的触发条件是：

- 两个GameObject都有碰撞器组件，其中某个GameObject的碰撞器必须勾选了`isTrigger` ，并包含刚体组件。但是如果两个碰撞器都勾选了 `isTrigger` ，也不会触发。
- 然后就是两个碰撞器发生碰撞则会触发事件。

OnCollisionEnter的触发条件较为宽松，两个GameObject的碰撞器或者刚体发生碰撞则会触发。

### HeaderAttribute

在Unity编辑器那边新增一个标题头

```
	[Header("Persistent managers Scene")]
```

### TextAreaAttribute

在Unity编辑器那里新增一个可编辑文本区域。

```
	[TextArea] public string description;
```

### Tooltip
给Unity编辑器的某个字段增加一个提示信息。
```
[Tooltip("Time that this gameObject is invulnerable for, after receiving damage.")]
```









## Unity Addressable Asset system

Unity的官方包，在包管理里面搜索`addressables` 。这个包可以让你访问资产Asset通过地址访问的方式来进行，从而增加资源访问的灵活性。原asset bundle管理方案已经处于废弃状态。

在 window->addressables groups 那里新增一个group。

然后将资源拖动到这里，第一列就是后面你要使用引用的名字，默认的名字是根据你的资源的本地目录来的，你也可以修改为你想要的名字。

在脚本中使用资源如下，接受的参数是该资产的名字。

```
using UnityEngine.AddressableAssets;
Addressables.LoadAssetAsync<GameObject>("AssetAddress");
Addressables.InstantiateAsync("AssetAddress");
```

如果是`AssetReference` 配置好的资产则可以直接如下调用，：

```
_menuLoadChannel.LoadAssetAsync<LoadEventChannelSO>().Completed += LoadMainMenu;
```

一般的使用大体如下：

```c#
using System.Collections;
using System.Collections.Generic;
using UnityEngine.AddressableAssets;
using UnityEngine;

public class AddressablesExample : MonoBehaviour {

    GameObject myGameObject;

        ...
        Addressables.LoadAssetAsync<GameObject>("AssetAddress").Completed += OnLoadDone;
    }

    private void OnLoadDone(UnityEngine.ResourceManagement.AsyncOperations.AsyncOperationHandle<GameObject> obj)
    {
        // In a production environment, you should add exception handling to catch scenarios such as a null result.
        myGameObject = obj.Result;
    }
}

```

### 异步加载你的场景

addressables 系统可用于异步加载你的场景，非常的方便。

```
using UnityEngine.AddressableAssets;
using UnityEngine.ResourceManagement.AsyncOperations;
using UnityEngine.SceneManagement;
using UnityEngine.ResourceManagement.ResourceProviders;

Addressables.LoadSceneAsync("sceneName", LoadSceneMode.Additive).Completed += SceneLoadComplete;
// if scene is a AssetReference
scene.LoadSceneAsync(LoadSceneMode.Additive).Completed += SceneLoadComplete;

private void SceneLoadComplete(SceneInstance obj)
{
	if (obj.Status == AsyncOperationStatus.Succeeded)
	{
		Debug.Log("scene load succeeded.")
		// do something.
	}

}
```

卸载场景如下：

```
private AsyncOperationHandle<SceneInstance> handle;
handle = obj;

Addressables.UnloadSceneAsync(handle).Completed += SceneUnloadComplete;
```

上面不管是加载还是卸载一旦启动就异步进行了，Completed事件加入回调是一种方法，但你也可以用Unity的协程方法来检查之：

```
private IEnumerator LoadingProcess()
{
	if (obj.Status == AsyncOperationStatus.Succeeded)
	{
		Debug.Log("scene load succeeded.")
		// do something.
	}
	yield return null;
}
```

如果大体每一帧都会检测一次加载是否Succeeded。





## 四元数和欧拉角度

旋转Editor看到的x y z的值就是所谓的欧拉角度，但是如果你要给tranform.rotation赋值的话则需要使用四元数（Quaternion）。

```
transorm.rotation = Quaternion.Euler(0,0,0);
```

上面的过程也可以看做将一个欧拉角度数组转换成Quaternion四元数再赋值给rotation。

四元数访问对应的欧拉角度如下：

```
transform.localEulerAngles
```

在用一个Vector3变量表示游戏里面的方向的时候，现在假定都是全局坐标，则 `(0,0,1)` 也就是所谓的forward方向，即物体的z轴指向表示forword方向，此外还有 `(0,1,0)` 表示物体的Vector3.up方向，即物体的Y轴指向。x轴就是x轴和我们一般常识没有太多出入。

到Vector2坐标输入又有所不同，其x值对应的是水平方向，可以认为影响的是x值，而y值对应的是垂直方向，可以认为影响的是y值。

继续学习，这个四元数确实还是很让人困惑的，手册里面说Unity一般期待四元数是normalized，这个懂点线性代数的大概清楚就是这个矢量的模规约为1。具体调用是 `quaternion.normalized` ，将会返回一个magnitude等于1的四元数。

然后看到四元数乘以一个Vector3，参考 [这个网页](https://answers.unity.com/questions/186252/multiply-quaternion-by-vector.html) 。一个Vector3乘以一个四元数实际上是将这个Vector3进行了该四元数对应的旋转操作，也就是返回的也是一个Vector3变量。那么这又到了这个问题上，四元数表示的是一个什么旋转动作。比如说 `Quaternion.Euler(0,90,0)`  意思是绕着y轴旋转90度，y轴是垂直向上的，绕着y轴旋转90度大概就是一个物体在xy平面的旋转动作。



### Quaternion.AngleAxis

绕某个轴旋转多少角度。

```
transform.rotation = Quaternion.AngleAxis(30, Vector3.up);
```





## 基于事件驱动的Unity编程

作为和桌面端程序类似的存在，成熟的Unity游戏编程必然是基于事件驱动的编程模式。这对于大中小型Unity项目都是有用的和必须的。

C#那边已经有成熟的事件驱动编程解决方案了，拿过来用就是了。因为Unity那边又新增了UnityAction之类的语法糖，但从 [这篇文章](https://www.jacksondunstan.com/articles/3335) 来看，其效率反而不如C#自带的事件驱动解决方案，除非在某些Unity Editor定制人物上，才一定要使用UnityAction之类的，那个时候再使用。

在C#那边我们已经有了EventChannel的概念，现在要做的就是进一步将EventChannel做成ScriptedObject，这样一避免了数据冗余，另外可以很方便实现单例事件通道。

大体操作步骤如下：

1. 定义事件通道

```c#
using System;
using UnityEngine;
using UnityEngine.Events;


public class EventChannelBaseSO<T> : ScriptableObject
{
	[TextArea] public string description;

    public event EventHandler<T> Event;

    public void RaiseEvent(object sender, T args)
    {
        Event?.Invoke(sender, args);
    }

    public void AddHandler(EventHandler<T> handler)
    {
        Event += handler;
    }
    public void RemoveHandler(EventHandler<T> handler)
    {
        Event -= handler;
    }
}


public class LoadEventArgs : EventArgs
{
	public GameSceneSO sceneToLoad { get; private set; }

	public LoadEventArgs(GameSceneSO sceneToLoad)
	{
		this.sceneToLoad = sceneToLoad;
	}
}

[CreateAssetMenu(menuName = "Events/Load Event Channel")]
public class LoadEventChannelSO : EventChannelBaseSO<LoadEventArgs>
{
}
```

2. 生成事件通道的ScriptableObject文件

3. 一般在设计上会增加一个常驻场景，该常驻场景是最先加载的场景，然后该场景对某些事件进行了如下绑定，这些事件一般是最基本的事件，比如场景切换事件等。

   

```c#
[SerializeField] private LoadEventChannelSO _menuLoadChannel = default;

private void OnEnable()
{
_menuLoadChannel.AddHandler(LoadMenu);
}


private void OnDisable()
{
_menuLoadChannel.RemoveHandler(LoadMenu);
}
```

4. 其他地方引用该事件通道都是如下形式：

```c#
[SerializeField] private LoadEventChannelSO _menuLoadChannel = default;
```

然后指定事件通道都是那一个asset文件，则可以保证事件通道的唯一性或者说单例性。

5. 其他地方想调用事件如下：

```c#
_menuLoadChannel.RaiseEvent(this, new LoadEventArgs(_menuToLoad));
```

### UnityAction

UnityAction带来的便利就是Unity Editor那边是支持显示一个按钮方便手工触发该事件的，除此之外UnityAction就是一个有着特定名字的C#委托，并没有什么特殊的。







## UI

UI里面有些地方用的是sprite文件对象，如果你直接导入png图片的话会发现没有对应的选项，需要将导入的png图片的属性那里更改为sprite才可以。

一般来说游戏的UI会放在你的常驻场景里面，和你的其他游戏管理逻辑放在一起，而不是某单个level场景里面。



## 导航系统

Unity内置了一个路径导航系统，首先你需要将你的地形 GameObject 进行烘焙：

1. 选择你的地形GameObject，选择Static菜单的Navigation Static【在烘焙NavMesh的时候只收集标记为Navigation Static的游戏对象数据】
2. 选择Window->AI->导航，选择烘培Bake Tab，然后点击烘培。
3. 你将会在目标场景地图下面看到新建了一个NavMesh对象。

导航系统中你想要移动的目标对象需要绑定Nav Mesh Agent组件。

导航系统中你需要定义一系列的导航路径点，空的GameObject即可。



### 如何移动一个Agent

实际会很简单，就是设定destination属性即可。

```
agent.destination = transform.position;
```

### 巡逻模式

一个agent的巡逻模式可以通过如下类似编码来实现：

```c#
    void Update()
    {
        if (agent.remainingDistance < 0.2f && !agent.pathPending)
        {
            MoveToNextPatrolLocaton();
        }
    }
        private void MoveToNextPatrolLocaton()
    {
        if (locations.Count == 0)
        {
            return;
        }

        agent.destination = locations[locationIndex].position;

        locationIndex = (locationIndex + 1) % locations.Count;
    }
```

上面的 `agent.pathPending` 的意思是当前路径还没有计算好，取值否表示一定要先等路径计算好然后剩余距离只有多少之后继续移动到下一个导航点。

### 烘焙的时候选择高度网格

如果不选择高度网格的话，角色会有一定的悬空浮动问题。高度网络在运行时会占用一些内存和处理资源，只有在必要的时候才开启这个选项。

### NavMesh Surface

这个组件需要在 [这里](https://github.com/Unity-Technologies/NavMeshComponents) 额外下载安装，它可以作为组件附加在游戏对象上，然后可以针对某种特定的NavMesh Agent定义可行走区域。









## 动画

制作动画片段：

1. 新建一个Animations文件夹等下放动画片段资源
2. 选中你想要有动画效果的那个组件，选定window->Animation->Animation。
3. 选择启用关键帧记录模式，然后在每个帧上修改物体组件的某个属性

动画的开头和结尾常常有卡顿现象，哪怕你设置的旋转动作是0度到360度数值上是无缝对接的，仍然会有卡顿现象，你可以在曲线那里看到数值的变动是有一个切线变化率的，每一个帧都有两个切线，左切线是进入，右切线是离开，从头帧到结尾帧要想不卡顿，左右两个切线斜率必须是相同的，也就是co-linear的。

对于旋转动作可以将头尾两帧的双切线都改为线性。对应官方文档的 Broken-Linear模式。这样帧与帧之间是线性变化的，也就不存在那个变动斜率问题了。

### Animator组件

控制GameObject的动画组件，需要指定动画控制器，也就是AnimationController。

Apply root motion：应用根运动。是从动画本身控制角色的移动和旋转还是从脚本。

脚本那边设置这个参数是通过 `animator.applyRootMotion` 。

如果脚本定义了 `OnAnimatorMove` 方法，则applyRootMotion不起作用。

更新模式：

- Normal 法线 Animator和Update同步更新
- Animate Physics Animator和FixUpdate同步更新，即和物理系统步调一致

剔除模式：

- 总是动画化，即使在屏幕外也不剔除。

#### 动画状态判断

动画状态判断推荐使用 `animator.StringToHash("State")` 来获取一个int型hash值然后进行状态判断。

具体比较是：

```
CurrentStateInfo = animator.GetCurrentAnimatorStateInfo(0);
Animator.StringToHash("Run") == CurrentStateInfo.shortNameHash;
```

默认的图层索引是0，上面CurrentStateInfo就是当前的动画状态，`CurrentStateInfo.shortNameHash` 就是当前动画状态的短名字的Hash值，短名字的意思就是你的动画控制器那边显示的名字是Run则就是Run，前面没有默认的图层名字。

#### 标签

动画控制器的标签也是一个有用的字段方便进行一些动画控制上状态的逻辑管理。

## particle system

制作粒子系统：

1. 右键在世界大纲视图下新建->效果->粒子系统
2. 将粒子系统和你想要有该粒子系统效果的物体组件XYZ值设为一样
3. 调配你的粒子系统的各个属性





##  材质

### standard着色器

#### albedo

反射率，定义了材质的基本颜色，纹理也是放在这里设置的。

#### metallic

金属的，定义了材质的金属表现。

#### Smoothness

平滑度，定义了材质的表面光滑性。一般为了看上去更真实不应该设置为0或1而是某个中间值。

#### tiling

平铺，定义了纹理在表面平铺重复的次数。

#### offset

偏移，定义了纹理在表面平铺的偏移量。



## 光源

默认的定向光可以类比太阳光，点光源可以类比灯泡，聚光灯可以类比汽车的前照灯。

需要强调一点的是Unity里面的灯光是游戏对象的组件，当你在空白地方新建一个灯光的时候，实际上是新建了一个空白对象然后包含了一个灯光组件。前面提到的各个灯光类型比如定向光点光源都是灯光组件的类型变量控制的，这都是可以调整的。

以新建一个路灯为例子，路灯有杆子和上面的立方体，给上面的立方体一个灯光组件就有了一个类似路灯的效果。

最后要提醒一点的是灯光只是让这个对象在发光，要让这个对象看起来在发光还需要给这个对象添加对应的发光材质。



## 开始菜单

开始菜单就是另外一个场景地图，其是一个2d场景地图，在开发的时候视图中间偏左有个选项，激活了场景处于2d视图中。然后就是在这个场景中添加一些UI元素即构成了开始菜单。



## 多场景无缝切换



## respawn玩家角色

一般都是如下respawn玩家角色：

```
		player.transform.position = spawnPoint.position;
		player.transform.rotation = spawnPoint.rotation;
```

Unity游戏开发一书就是这样写的，然而现在不可以了。 [这个视频](https://www.youtube.com/watch?v=FPU3uR3HYGo) 说了需要把项目设置的Physics的 `Auto Sync Transforms` 勾选上，一试果然就可以了。看了下Unity文档，Unity的物理系统默认没有勾选上，也就是你的transform属性硬修改Unity的物理系统是没有跟上同步的，然后Unity文档又说了这个自动勾选上开销会有一些，所以最好在需要硬修改的地方加上：

```
		player.transform.position = spawnPoint.position;
		player.transform.rotation = spawnPoint.rotation;
		Physics.SyncTransforms();
```





## 单元测试

按照C#的方法，自动创建了一个单元测试项目。即使是空白单元测试也会报错：

```
CS0006 could not found file Assembly-CSharp.dll
```

大概这个错误，我好不容易才在 [这个网页](https://developercommunity.visualstudio.com/t/vs-doesnt-put-binaries-of-unity-project-to-output/785717) 知道Unity项目在visual studio中默认是不自动完成生成项目的，你需要在：

```
工具 ->  选项 -> 适用于Unity的工具 -> 杂项 -> 禁止完整生成项目
```



## 雾效

在 window->渲染->照明设置那里勾选雾，则可以为你的场景打开雾效。



## skybox

天空盒就是在天空那个巨大盒子上应用你想要的材质。可以新建一个材质，然后这个材质在stardard着色器那里选择skybox，从而快速创建一个skybox材质，然后在 window->渲染->照明设置 那里应用该skybox材质。

## 其他

`Ctrl+Shift+M` 在visual studio 上调出Unity快速方法输入。

### RequireComponent

```
[RequireComponent(typeof(PlayerInput))]
public class PlayerScript : MonoBehaviour
{
//
}
```

脚本将会自动添加给本GameObject添加某个组件来确保本GameObject的组件依赖正确。

### 默认单位

Unity术语里面长度用的是 1unit，比如velocity 用的每秒移动的unit。比如1unit等于多少并没有一个准数的，要看你自己那边的建模规范。



## 备用

### Unity环境和.net core略有不同

不能使用 System.HashCode ？说明Unity虽然基于C#，但底层可能不是基于.net core，在某些地方上是有所差异的。

### 移动控制

`Input.GetAxis(axis_name)` 获取当前控制轴的值，比如Horizontal axis 方向left和 a键为-1，right和d为1。

### transform.Translate和Rigidbody.MovePosition

经过试验结论如下，在速度特别快的情况下两个都可能发生避开物理碰撞系统而发生穿模，速度很低的情况下两个也都不会穿模。不过在速度中等的情况下，用Transform的translate方法移动物体仍时不时会避开物理刚体碰撞系统，而在这种情况下刚体的MovePosition就表现要好一下。

此外FixUpdate的固定时间设定也会很好地防止物体移动速度不可捉摸的突变情况。

### 地形绘制纹理

主要是编辑图形层那里，显示创建图层，再是添加图层。在这些图层里面利用不同的笔刷进行绘制。

笔刷的不透明度是笔刷的力度。



### FMOD音效集成

FMOD集成音效

### Makehuman工具

Makehuman工具
