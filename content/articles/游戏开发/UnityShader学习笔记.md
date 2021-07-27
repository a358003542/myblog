## 基础

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

1. Unity Shader入门精要 by 冯乐乐
2. Mastering Unity Shaders and Effects by Jamie Dean