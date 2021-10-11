Tags: unity

[TOC]

## 前言

本文是Unity游戏开发系列的输入部分。

### 本系列内容的取舍

- 因为笔者开发的是3D游戏，因此专属于2D游戏的那些内容将不会在这里讨论。
- 笔者使用的是Unity 2020.3 LTS版本，之前的版本被废弃的特性或者之后的版本新增的特性将不会在这里讨论。
- 笔者在行文上会尽可能节省笔墨，只是标出官方参考文档的引用出处，但在某些地方会额外花费笔墨来说明，比如个人觉得官方文档文字可能不是很好懂，某些内容很重要需要再特别强调一遍等。
- 一般来说官方文档里面有的不会在这里赘述，不过有时某些内容会特别重要而会再强调一遍。

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

**NOTICE:**  详细阅读上面的case判断，如果不加上case判断，一般的行为会触发三次，一次started = 1，一次performed = 1，一次canceld = 0。 

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

按照传统输入系统的方法读取值会在Update方法那边编写，现在在回调方法上对应地如上写上读取值之后，就类似传统输入在Update方法那里获取到目标值了，然后后面的都是类似的了。



#### 判断本帧某个键位是否按下了

这个键位判断不需要去设置Actions的配置对于任何按键都可以如下直接去判断。

```
  Keyboard.current.space.wasPressedThisFrame
```

### Input.mousePosition

获取当前鼠标在屏幕上的坐标，返回一个Vector3值，z值总为0，x和y都等于0时表示左下角，右上角是 `(Screen.width, Screen.height)` 。





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

