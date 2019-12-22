Title: unity入门学习笔记
Slug: unity-beginning-learning-notes
Date: 2019-12-22
Tags: unity

[TOC]

## 开发环境

1. 安装visual studio
2. 选择安装 `使用unity的游戏开发`
3. 去unity官网下载安装 `unity hub`





## 三连棋游戏

参考了unity学习的 [这篇文章](https://learn.unity.com/tutorial/creating-a-tic-tac-toe-game-using-only-ui-components) 。

1. 创建一个2d项目

2. create -> ui -> panel

3. 修改canvas的 UI scale mode -> scale with screen size 默认的800*600在本例子中是够用的

4. 新建的那个panel命名为 Background 

5. 更改background的color 为 black 即 0 0 0 100

6. 然后在 create -> ui -> panel

7. 新的panel命名为 Board 对齐方式选择 middle center

8. Board定位 X,Y 为 0,0 ，然后宽度高度均为 512

9. Board颜色 33 44  55 255

10. 然后在如同上面再新建一个panel，命名为Grid

11. Grid对齐方式middle center，Grid宽度高度 5,512 Grid X,Y位置 -85.33 0

12. Grid颜色 255 0 102 255

13. 复制之前的Grid再粘贴得到Grid(1) Grid(1) 的X,Y 位置调为 85.33 0

14. 复制之前的Grid得到Grid(2) Grid(2) 的X,Y 位置调为 0 85.33 然后宽度高度调为 512,5

15. 复制上面Grid(2)得到Grid(3) 将Y调为-85.33

16. create->ui->button 将按钮命名为Grid Space 重设位置，宽度高度设为128 128

17. 调 Grid Space 按钮的 normal color 为 0 204 204 255

18. 调 Grid Space 按钮的 highlighted color 为 128 255 255 255 

19. 调 Grid Space 按钮的 pressed color 为 51 102 102 255

20. 调 Grid Space 按钮的 disabled color 为 55 66 77 255

21. 将 Grid Space 按钮下的Text 设为 `X` 大小调为111 颜色调为 255 0 102 255

22. 在下面项目 assets 哪里新建一个文件夹 命名为 prefabs

23. 将 Grid Space 按钮拖动到 下面的 prefabs 文件夹

24.  从prefabs哪里重复拖动，制造9个按钮

25. 调整这些按钮的属性XY值，大约是 170 0 , 0 0, 0,170 之类的，注意调好顺序 铺满

26. 将prefab的text的X文字删除，我们会看到scenes哪里的按钮属性也都发生更改了

27. 在下面assets哪里新建一个文件夹 scripts ，然后选择新建 GridSpace 的 C#文件

28. 双击该C#文件如果你的visual studio和unity联动配置好了，那么是可以直接到visual studio哪里去的

    现在GridSpace脚本文件第一阶段初步版本【未完全版】大致如下所示：

    ```c#
    using System.Collections;
    using System.Collections.Generic;
    using UnityEngine;
    
    using UnityEngine.UI;
    public class GridSpace : MonoBehaviour
    {
        public Button button;
        public Text buttonText;
        public string playerSide;
    
        private GameController gameController;
        public void SetGameControllerReference(GameController controller)
        {
            gameController = controller;
        }
        public void SetSpace()
        {
            buttonText.text = gameController.GetPlayerSide();
            button.interactable = false;
            gameController.EndTurn();
        }
    }
    
    ```

29. 点击prefabs的Grid Space ，然后点击 Add Componet ，选择scripts脚本，选择Grid Space

30. 你会看到脚本加入进来之后，之前你设置的`public Button button;` 变量，这里可以添加按钮了，点击右边的小图标，选择Grid Space （self）

31. 然后上面 On Click哪里有点击行为， 下面有一行小图标哪里选择 Grid Space prefab，然后右上哪里选择 Grid Space的SetSpace方法

32. 下面是为游戏新增一个全局控制对象 ，create -> create Empty ，创建一个空对象

33. 然后在scripts哪里新建一个c#脚本 GameController，初步内容如下：
    ```c#
    using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
public class GameController : MonoBehaviour
{
    public Text[] buttonList;
    private string playerSide;
    // Start is called before the first frame update
    void ChangeSides()
    {
        playerSide = (playerSide == "X") ? "O" : "X";
    }
    public string GetPlayerSide()
    {
        return playerSide;
    }

    public void EndTurn()
    {
        if (buttonList[0].text == playerSide && buttonList[1].text == playerSide && buttonList[2].text == playerSide)
        {
            GameOver();
        }

        if (buttonList[3].text == playerSide && buttonList[4].text == playerSide && buttonList[5].text == playerSide)
        {
            GameOver();
        }

        if (buttonList[6].text == playerSide && buttonList[7].text == playerSide && buttonList[8].text == playerSide)
        {
            GameOver();
        }

        if (buttonList[0].text == playerSide && buttonList[3].text == playerSide && buttonList[6].text == playerSide)
        {
            GameOver();
        }

        if (buttonList[1].text == playerSide && buttonList[4].text == playerSide && buttonList[7].text == playerSide)
        {
            GameOver();
        }

        if (buttonList[2].text == playerSide && buttonList[5].text == playerSide && buttonList[8].text == playerSide)
        {
            GameOver();
        }

        if (buttonList[0].text == playerSide && buttonList[4].text == playerSide && buttonList[8].text == playerSide)
        {
            GameOver();
        }

        if (buttonList[2].text == playerSide && buttonList[4].text == playerSide && buttonList[6].text == playerSide)
        {
            GameOver();
        }

        ChangeSides();
    }

    void SetGameControllerReferenceOnButtons()
    {
        for (int i = 0; i < buttonList.Length; i++)
        {
            buttonList[i].GetComponentInParent<GridSpace>().SetGameControllerReference(this);
        }
    }
    void Awake()
    {
        SetGameControllerReferenceOnButtons();
        playerSide = "X";
    }
    // Update is called once per frame
    void GameOver()
    {
        for (int i = 0; i < buttonList.Length; i++)
        {
            buttonList[i].GetComponentInParent<Button>().interactable = false;
        }
    }
}

    ```
    
34. 这个脚本定义了 `public Text[] buttonList;`  将这个脚本 add component 到 Game controller那个空对象上之后，将Button list的大小设为 9 ，然后逐个将之前定义的那些按钮的文本对象添加进来，注意顺序。

35. 关于C#脚本语言的熟悉和理解这个往后面放一放，关于本例子涉及到的东西的详细了解和本例子的继续完善后面再说，本例子主要是对unity游戏开发大概情况有个了解。 

36. 经过测试发现 EndTurn 方法是每次点一下都会执行一次。

    