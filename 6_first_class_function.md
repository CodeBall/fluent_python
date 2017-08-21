# 一等函数
## 一等对象的定义
把一等对象定义为满足下述条件的程序实体：

+ 在运行时创建
+ 能赋值给变量或者数据结构中的元素
+ 能作为参数传给函数
+ 能作为函数的返回结果

在python中，函数也是一等对象，可看如下示例：

```Python
def factorial(n):
    """
    计算阶乘
    :param n:
    :return:
    """
    return 1 if n < 2 else n * factorial(n-1)

print(factorial(3))
print(factorial.__doc__)
x = factorial
print(x(3))
```

## 高阶函数的定义
接收函数为参数，或者吧函数作为返回值的函数就是高阶函数。
最为人熟知的高阶函数有：`map`, `filter`, `reduce`.

`reduce`在python2中时内置函数，在python3中，放在了functools模块中，这个函数最常用的场景是用来求和，如下示例：

```Python
from functools import reduce
from operator import add

print(reduce(add, range(100)))
# 在计算求和方面,sum函数完全可以代替reduce进行计算
print(sum(range(100)))
```
## 可调用对象列举

+ 用户定义的函数：使用def语句或者lambda表达式创建的函数。
+ 内置函数：使用C语言实现的内置函数，如`len`,`time.strftime`。
+ 内置方法：使用C语言实现的方法，如`dict.get`。
+ 方法：在类的定义中定义的函数。
+ 类：调用类时会运行类的`__new__`方法来创建一个实例，然后运行`__init__`方法，初始化实例，最后把实例返回给调用方。因为Python没有new运算符，所以调用类相当于调用函数。
+ 类的实例：如果定义了`__call__`方法，那么它的实例可以作为函数调用。
+ 生成器函数：使用`yield`关键字的函数或方法。调用生成器函数，返回的是生成器对象。

## 自定义可调用类型
任何Python对象都可以表现的像函数，只需要实现实例方法`__call__`，如下示例所示：

```Python
import random


class BingoCage:
    def __init__(self, items):
        self.items = list(items)
        random.shuffle(self.items)

    def pick(self):
        try:
            return self.items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        return self.pick()

bingo = BingoCage(range(3))
print(bingo.pick())
print(bingo())
print(callable(bingo))
```

## 定位参数和仅限关键字参数
如下示例所示：

+ name是必选参数
+ cls是可选参数，且只能通过关键字参数传入
+ name后面的任意个参数，都会被content捕获，存入一个元组中，直到遇到cls参数，或者关键字参数。
+ 关键字参数必须放在参数列表的最后面，当形参中没有对应的关键字时，会被attr参数捕获，存进一个字典中。关键字参数可以传入一个字典，`**dic`的形式，当形参中含有键名时，会直接赋值，没有对应键名时，会被attr捕获。

```python
def tag(name, *content, cls=None, **attr):
    print("this tag name is : {}".format(name))

    if cls:
        print("the class name is : {}".format(cls))

    if content:
        st = "the content is : "
        for c in content:
            st += "{}, ".format(c)
        print(st)

    if attr:
        st = "the style is : "
        for key, value in attr.items():
            st += "{} = {}, ".format(key, value)
        print(st)


tag("p", "hello", "zerol", cls="class_p", id="p_class", color="red")
tag("p", cls="class_p", id="p_class", color="red")
dic = {"cls": "class_p", "id": "p_class", "color": "red"}
tag("p", **dic)

```

仅限关键字参数是Python3新加的特性，上述示例中的cls就是一个仅限关键字参数，实现仅限关键字参数的方法就是把该参数放在前面有*的参数后面，如果函数中不想支持数量不定的定位参数，但想支持仅限关键字参数，则可以直接写个`*`，如下所示：

```python
def f(a, *, b):
    return a, b

print(f(12, b=23))
```

## 获取参数信息(inspect.signature的使用)
函数对象有个`__defaults__`属性，其值是一个元组，里面保存着定位参数和关键字参数的默认值。仅限关键字参数的默认值在`__kwdefaults__`属性中。但是这里面仅包含了值，不包含参数名称，具体请看下述示例：

```python
def args_info(text, max_len=10, *, kw=17, kw1=23, kw2):

    end = 100

    if len(text) > max_len:
        end = len(text)
    else:
        end = max_len

    return end

print(args_info.__defaults__)
print(args_info.__kwdefaults__)
print(args_info.__code__)
print(args_info.__code__.co_varnames)
print(args_info.__code__.co_argcount)

# 代码运行的结果如下：
(10,)
{'kw': 17, 'kw1': 23}
<code object args_info at 0x1010f4f60, file "6_first_class_function.py", line 77>
('text', 'max_len', 'kw', 'kw1', 'kw2', 'end')
2
```

从上述示例可以得出以下结论：

+ `__defaults__`中存放了定位参数和关键字参数的默认值
+ `__kwdefaults__`中存放了仅限关键字参数的默认值，这是一个字典
+ `__code__.co_varnames`中不仅存放了定位参数和关键字参数的名字，还存放了仅限关键字参数的名字，以及方法中局部变量的名字。
+ `__code__.co_argcount`中存放了定位参数和关键字参数的个数。

上面的示例中，我们如果想得到参数默认值，必须同时知道参数的个数、名字和值，并且是从后向前对应的。这使用起来会很麻烦，所以用到了`inspect`模块中的`signature`方法。

```python
from inspect import signature


def args_info_by_signature():
    sig = signature(args_info)
    print(sig)
    str(sig)

    for name, param in sig.parameters.items():
        print(param.kind, ':', name, '=', param.default)

args_info_by_signature()

# 代码运行的结果如下：
(text, max_len=10, *, kw=17, kw1=23, kw2)
POSITIONAL_OR_KEYWORD : text = <class 'inspect._empty'>
POSITIONAL_OR_KEYWORD : max_len = 10
KEYWORD_ONLY : kw = 17
KEYWORD_ONLY : kw1 = 23
KEYWORD_ONLY : kw2 = <class 'inspect._empty'>
```

kind属性的值是_ParameterKind类中的5个值之一，这5个值分别是：

+ POSITIONAL_OR_KEYWORD:可以通过定位参数和关键字参数传入的形参
+ VAR_POSITIONAL:定位形参元组
+ VAR_KEYWORD:关键字参数字典
+ KEYWORD_ONLY:仅限关键字参数
+ POSITIONAL_ONLY:仅限定位参数

`inspect.Signature`对象有个`bind`方法，可以把任意个参数绑定到签名中的形参上，于是可以使用这个方法在真正调用函数前验证参数。

```python
def use_bind():
    sig = signature(args_info)
    args = {'text': "hello,world", 'max_len': 30, 'kw2': 190}
    bound_args = sig.bind(**args)

    print(bound_args)
    for name, value in bound_args.arguments.items():
        print(name, '=', value)

    del args['text']
    bound_args = sig.bind(**args)

use_bind()

#代码运行的结果如下：
<BoundArguments (text='hello,world', max_len=30, kw2=190)>
text = hello,world
max_len = 30
kw2 = 190
Traceback (most recent call last):
  File "6_first_class_function.py", line 119, in <module>
    use_bind()
  File "6_first_class_function.py", line 117, in use_bind
    bound_args = sig.bind(**args)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/inspect.py", line 2921, in bind
    return args[0]._bind(args[1:], kwargs)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/inspect.py", line 2836, in _bind
    raise TypeError(msg) from None
TypeError: missing a required argument: 'text'
```

可以看到最后程序抛出了参数缺失的错误。这就达到了我们进行参数验证的目的。

## 函数注解

```python
def fun_annotation(test:str, max_len:'int > 0'=80) -> str:
    return "just text"
```

上述示例的函数定义中，就用到了函数注解，有注解的函数声明有以下特点：

+ 函数声明中的各个参数可以在`:`之后添加注解表达式
+ 如果参数有默认值，注解的放在参数名和`=`之间
+ 如果想注解返回值，在`)`和函数声明末尾的`:`之间添加`->`和一个表达式，该表达式可以是任何类型。
+ 注解中最常用的类型是类（如：str，int）和字符串（如 'int > 0'）

**注：注解不会做任何处理，python对注解所做的唯一事情是，把他们存储在函数的`__annotations__`属性里。**

`inspect.signature（）`函数可以提取注解，如下所示：

```python
def read_annotation():
    sig = signature(fun_annotation)
    print(sig.return_annotation)

    for param in sig.parameters.values():
        note = repr(param.annotation).ljust(13)
        print(note, ':', param.name, '=', param.default)

read_annotation()

# 代码运行的结果如下：
<class 'str'>
<class 'str'> : test = <class 'inspect._empty'>
'int > 0'     : max_len = 80
```

## 支持函数式编程的包
### functools.partial
```python
from operator import mul
from functools import partial

triple = partial(mul, 3)
print(triple(7))
```

partial的第一个参数是一个可调用对象，后面跟着任意个要绑定的定位参数或者关键字参数。

