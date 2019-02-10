Title: java语言之-junit4单元测试
Slug: junit4
Date: 2018-08-05
Modified: 2018-08-05
Tags: junit
Status: draft

[TOC]

## maven安装junit

```xml
<dependency>
  <groupId>junit</groupId>
  <artifactId>junit</artifactId>
  <version>4.12</version>
  <scope>test</scope>
</dependency>
```



## 基本例子

junit4 的新写法不需要用类extends Testcase 那种写法了，而是采用如下含注释的写法 

```java
import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class CalculatorTest {
  @Test
  public void evaluatesExpression() throws Exception {
    Calculator calculator = new Calculator();
    int sum = calculator.evaluate("1+2+3");
    assertEquals(6, sum);
  }
}
```







## 参考资料

1. 官方文档
2. [深入探索junit4](https://www.ibm.com/developerworks/cn/education/java/j-junit4/index.html)