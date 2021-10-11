Slug: unity-editor
Tags: unity

[TOC]

## 前言

本文是Unity游戏开发系列的编辑器编码部分。

### 本系列内容的取舍

- 因为笔者开发的是3D游戏，因此专属于2D游戏的那些内容将不会在这里讨论。
- 笔者使用的是Unity 2020.3 LTS版本，之前的版本被废弃的特性或者之后的版本新增的特性将不会在这里讨论。
- 笔者在行文上会尽可能节省笔墨，只是标出官方参考文档的引用出处，但在某些地方会额外花费笔墨来说明，比如个人觉得官方文档文字可能不是很好懂，某些内容很重要需要再特别强调一遍等。



## 属性值

### TextAreaAttribute

这会让你的字符串有一个更宽的文本输入区域。

```
using UnityEngine;

public class TextAreaExample : MonoBehaviour
{
    [TextArea]
    public string MyTextArea;
}
```



### TooltipAttribute

给Unity编辑器的某个字段增加一个提示信息，当鼠标悬停的时候会弹出这个提示信息。

```
using UnityEngine;

public class Example : MonoBehaviour
{
    [Tooltip("Health value between 0 and 100.")]
    int health = 0;
}
```



### 自定义属性

如下 `Header` 是自定义的属性：

```
	[Header("Persistent managers Scene")]
```

添加一个属性Header，则会在编辑器的Inspector窗口上添加一个标题头，你也可以自定义自己的属性装饰函数。

```c#
	public class HeaderLineAttribute : PropertyAttribute {

		public readonly string header;
		
		public HeaderLineAttribute(string header)
		{
			this.header = header;
		}
	}
```

如上定义了一个 `HeaderLineAttribute` 属性装饰函数，实际使用是：

```
[HeaderLine("Input")]
```

【似乎如果该类的名字有Attribute则会省略。】

然后该属性装饰函数你可以定义属性绘制类：

```c#
	[CustomPropertyDrawer (typeof(HeaderLineAttribute))]
	public class HeaderLineDrawer : DecoratorDrawer
	{
		public HeaderLineDrawer ()
		{
		}
	}
```

DecoratorDrawer类似PropertyDrawer，区别就是DecoratorDrawer不绘制属性，除了从对应的PropertyAttribute对象那里获取的数据。

具体绘图是根据 `OnGUI`  重载方法来的。

## Editor开发

首先列出一个简单的例子，这个例子是给你的类在编辑器视图下添加一个按钮：

```c#
using UnityEditor;
using UnityEngine;

[CustomEditor(typeof(TestSerializableDict))]
public class TestSerializableDictEditor : Editor
{
    public override void OnInspectorGUI()
    {
        base.OnInspectorGUI();

        TestSerializableDict targetScript = (TestSerializableDict)target;
        if (GUILayout.Button("test"))
        {
            targetScript.Test();
        }
    }
}
```

这个方便有时手工触发事件或者动作或者打印Debug信息都是很有用的。



- `using UnityEditor;` 一般进行Unity Editor开发需要引入这个命名空间。
- 关于Editor的类是继承自 `Editor` 这个类。
- `[CustomEditor(typeof(TestSerializableDict))]` 在你的类上面写上一个标记表明你的这个编辑器类是针对某个类对象进行编辑器显示定制优化的。
- 重载 `OnInspectorGUI` 方法来实现编辑器显示定制。在`OnInspectorGUI` 方法里面 `target` 就是目标类对象。



### 插入一个整数值

```
myLevelScript.experience = EditorGUILayout.IntField("Experience", myLevelScript.experience);
```

上面接受两个参数，第一个参数是显示字符，第二个参数是整数值来源。

上面写成再一次赋值语句，应该是从编辑器那边修改值之后，然后修改值再回写回来。【个人尝试是如果不写成这种赋值语句修改值动作是无效的】

### 插入一个Lable

```
EditorGUILayout.LabelField("Label", myLevelScript.Level.ToString());
```

上面接受两个字符串参数，其中第一个参数是左边的label，第二个参数是右边的label。



### 默认显示动作

```
public override void OnInspectorGUI(){
    DrawDefaultInspector();
}
```

`DrawDefaultInspector` 方法会让你的自定义类显示先绘制默认的显示动作。

估计 `base.OnInspectorGUI` 的写法效果是一样的。











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

