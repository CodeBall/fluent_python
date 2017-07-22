# Python的特殊方法
Python提供了各种各样的特殊方法,使用这些方法可以实现自定义的类。
## 特殊方法的基本使用
特殊方法是给Python解释器调用的，我们不需要使用my_object.__len__()这种方法进行调用，而是写作len(my_object)的形式。

很多时候，特殊方法的调用是隐式的，比如我们使用for对某个对象进行迭代的时候，会优先调用iter()方法，而iter()方法的背后是`__iter__`方法。

### 利用特殊方法可以做哪些事情
不同的特殊方法可以实现不同的功能，下面列举一些简单的示例
#### 模拟数值类型
如果我们想实现向量的各种运算，可以创建一个向量类，利用特殊方法进行实现，如下代码所示：

```
from math import hypot

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)

    def __abs__(self):
        # hypot 用来返回向量的模
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __repr__(self):
        return "Vector ({}, {})".format(self.x, self.y)
```

#### 字符串表示形式
有时候，我们在控制台打印某个对象的时候，我们得到的会是类似于`<Vector object at ...>`的形式，因为该对象没有实现__repr__的方法。
`__repr__`方法的作用是把一个对象用字符串的方式表示出来，当使用交互式控制台或者调试程序的时候会调用这个方法。
`__str__`方法也会实现类似的功能，与`__repr__`方法不同的是该方法会被str()函数 ，或者使用print时调用，并且一个对象如果没有实现`__str__`方法，则会使用`__repr__`方法代替，反之则行不通。

#### 算术运算符
可以使用`__add__`，`__mul__`等方法实现运算符的操作，例如Vector的示例

#### 自定义布尔值
python自定义的bool类型还是有一定的局限性，比如我们自己定义的类总会被认为真，如果我们对类的bool判断有新的规则，则可以使用`__bool__`方法进行实现，例如Vector的示例。

**注意 如果我们自定义的类中实现了__len__方法，使用python自带的bool进行判断时，该方法会调用__len__方法，如果__len__的返回值为0，则为假，其他的值返回真**

### python 特殊方法一览

![](http://cdn.blog.yanzl.net/2017-07-22-095117.jpg)

![](http://cdn.blog.yanzl.net/2017-07-22-magic_method2.png)

![](http://cdn.blog.yanzl.net/2017-07-22-magic_method3.png)





