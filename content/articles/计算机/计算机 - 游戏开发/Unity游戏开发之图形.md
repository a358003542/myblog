Tags: unity

[TOC]

## 前言

本文是Unity游戏开发系列的图形部分。

### 本系列内容的取舍

- 因为笔者开发的是3D游戏，因此专属于2D游戏的那些内容将不会在这里讨论。
- 笔者使用的是Unity 2020.3 LTS版本，之前的版本被废弃的特性或者之后的版本新增的特性将不会在这里讨论。
- 笔者在行文上会尽可能节省笔墨，只是标出官方参考文档的引用出处，但在某些地方会额外花费笔墨来说明，比如个人觉得官方文档文字可能不是很好懂，某些内容很重要需要再特别强调一遍等。
- 一般来说官方文档里面有的不会在这里赘述，不过有时某些内容会特别重要而会再强调一遍。

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





## LOD技术

unity的LOD技术可以根据游戏对象与摄像机的距离来选择性地使用游戏对象不同的渲染模型。

具体就是创建一个空的游戏对象，添加LOD group组件。然后将blender建模的不同精细度的模型导入到该游戏对象，并拖动到LDO group那里对应不同的LOD显示级别。其中LOD0是精细度最高的模型。

blender那边需要建模不同精细度的模型，导出的时候名字一般规范为： `Name_LOD0` 等。一个简单的做法是对网格体使用精简修改器，刚开始调配的多边形数目小的不能再小的建模再网上抬高一点为LOD0，然后再继续降低多边形数目，这个时候你会发现模型出现了一些瑕疵或缺陷，这是可以容忍的，因为LOD1是摄像机距离有点远的时候了，这个时候玩家一般不会太注意这些模型的小瑕疵了。



## 粒子系统

粒子系统可以制作出很多种效果，比如爆炸，火焰，烟雾，烟花，施法效果等。粒子系统就是空间中的一个点，从这个点出发发射一些粒子对象，从而制造出一些视觉效果。

### 新建一个粒子系统

新建一个粒子系统，右键在世界大纲视图下新建->效果->粒子系统。你也可以将粒子系统作为某个对象的组件添加进去。

从粒子系统属性面板可以看到很多属性调配参数，这些更规范的叫法叫做模块，默认启用的模块有默认模块和发射模块和形状模块。除了默认模块其他模块都是可选可启用也可停用的。这么多模块和参数，慢慢熟悉吧。

### 默认模块

显然至少默认模块的一些参数要先熟悉清楚。

- Duration 持续时间 粒子系统的运行时间
- Looping 是否循环播放
- Prewarm 预热 粒子系统从上次的循环中开始播放
- Start Delay 启动延迟 发射粒子之前等待的时间，不能和预热共存。
- Start Lifetime 每个粒子的存活时间，单位是秒
- Start Speed 粒子的初始速度
- Start Size 粒子的初始大小
- Start Rotation 粒子的初始旋转角度
- 翻转旋转 某些粒子向反方向旋转
- Start Color 粒子的起始颜色
- 重力修改器 应用于粒子的重力修改器，0是没有重力。
- 模拟空间 指定坐标是本地局部坐标系还是世界坐标系
- 模拟速度 微调粒子系统的播放速度
- 时间差 粒子系统的时间是基于缩放时间还是非缩放时间
- 缩放模式 缩放是基于游戏对象的父对象还是发射器的形状
- 唤醒时播放 粒子系统Awake就开始播放，如果关闭则需要手动开启粒子系统。
- 发射器速度 速度的计算是基于对象的变换还是它的刚体
- 最大粒子 粒子可以存在的最大数目，如果达到最大数目，粒子系统将暂停新粒子生成。
- 自动随机种子 每次播放粒子系统选择不同的随机种子
- 停止行动 如果粒子系统停止或所有粒子消亡，是否禁用或销毁自身。

### 发射模块

- Rate over time 随单位时间产生的粒子数，即每秒发射的粒子数目
- Rate over distance 每Unit单位发射的粒子数目
- bursts 爆发，突变。在某个特定时间内突然发射额外的粒子

### 形状模块

这个确定的是发射器，或者说发射的粒子们组成的形状。





## Shader

### 绘图管线

参看资料wiki ：[Graphics pipeline - Wikipedia](https://en.wikipedia.org/wiki/Graphics_pipeline)

计算机图形学中，绘图管线描述了图像系统通过一系列步骤来将3D场景渲染为2D图像的这一过程。更具体来说这一过程就是我们游戏中的3d场景投射到摄像机上的过程。

绘图管线大体分为三个主要阶段：应用阶段，几何阶段和光栅化阶段（rasterization）。

### Shader

上面的应用阶段是在CPU上进行的，而几何阶段和光栅化阶段是在GPU上进行的，基本上绘图管线上定义的工作就是GPU要做的事情。然后GPU那边的工作大概也是一系列的工作流，这其中情况各不相同，有的是固定不变的，有的是可配置的，有的是可编程的。然后这里面有一些重要的工作节点称之为什么着色器Shader。常常听到什么Shader比如片元着色器就是对应GPU的某个Shader工作节点。

所以简单来说谈到Shader实际上指的是GPU上的某段程序。

### ShaderLab

所谓的编写Shader其实只是因为GPU上的某个Shader提供了可配置接口或者可编程入口，然后再通过某种语言来对这个Shader进行编程或者说编写。这个语言很多GPU厂商都提供了自己特定的语言，Unity提供了两种Shader编码语言，然后会将其根据不同的GPU转成对应的它支持的语言。其中ShaderLab是Unity专门开发出来的专门写Shader的一门语言。此外Unity还支持HLSL语言，这些就不做过多讨论了。

### 标准表面着色器

新建一个标准表面着色器，这个选项放在最上面，应该是最常用的，其他什么Shader后面再了解。其内容如下：

```c#
Shader "Custom/NewSurfaceShader"
{
    Properties
    {
        _Color ("Color", Color) = (1,1,1,1)
        _MainTex ("Albedo (RGB)", 2D) = "white" {}
        _Glossiness ("Smoothness", Range(0,1)) = 0.5
        _Metallic ("Metallic", Range(0,1)) = 0.0
    }
    SubShader
    {
        Tags { "RenderType"="Opaque" }
        LOD 200

        CGPROGRAM
        // Physically based Standard lighting model, and enable shadows on all light types
        #pragma surface surf Standard fullforwardshadows

        // Use shader model 3.0 target, to get nicer looking lighting
        #pragma target 3.0

        sampler2D _MainTex;

        struct Input
        {
            float2 uv_MainTex;
        };

        half _Glossiness;
        half _Metallic;
        fixed4 _Color;

        // Add instancing support for this shader. You need to check 'Enable Instancing' on materials that use the shader.
        // See https://docs.unity3d.com/Manual/GPUInstancing.html for more information about instancing.
        // #pragma instancing_options assumeuniformscaling
        UNITY_INSTANCING_BUFFER_START(Props)
            // put more per-instance properties here
        UNITY_INSTANCING_BUFFER_END(Props)

        void surf (Input IN, inout SurfaceOutputStandard o)
        {
            // Albedo comes from a texture tinted by color
            fixed4 c = tex2D (_MainTex, IN.uv_MainTex) * _Color;
            o.Albedo = c.rgb;
            // Metallic and smoothness come from slider variables
            o.Metallic = _Metallic;
            o.Smoothness = _Glossiness;
            o.Alpha = c.a;
        }
        ENDCG
    }
    FallBack "Diffuse"
}

```

- Shader "Custom/NewSurfaceShader" 这里定义了你的着色器名字，后面选择着色器在Custom的NewSurfaceShader那里。
- Properties 定义属性，这些属性在材质面板那里可以看到。`_Color ("Color", Color) = (1,1,1,1)` ，`_Color` 是Shader内部使用该属性的调用名，后面一个元组第一个是材质那边的显示名字，第二个是该变量的类型，最后等号后面是该属性的默认值。
- SubShader 至少要定义一个SubShader区块，多个SubShader的意思是针对不同的硬件。
- FallBack 含义很明显，如果所有的SubShader都失败了则回滚到某个着色器。

这里就简单讨论下，更详细的讨论在后面。





## 参考资料

1. Unity官方文档
2. Stack overflow
3. 其他模块文档
4. Unity商城Free资源
5. Learning c# by developing games with unity 2019 by Harrison Ferrone
6. Unity 游戏开发 by  Mike Geig
7. Mastering UI Development with Unity by Asheley Godbold
8. Unity in Action by Joseph Hocking
9. Unity Shader入门精要 by 冯乐乐
2. Mastering Unity Shaders and Effects by Jamie Dean

