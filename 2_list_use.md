# 列表的使用
## 序列
按照存放的数据，序列可以分为容器序列和扁平序列，区别在于容器序列存放的是他们所包含的任意类型的对象的引用，扁平序列存放的是值，因此扁平序列其实是一段连续的内存空间，但是扁平序列只能存放像字符，字节和数值这种基本类型。容器序列和扁平序列的举例如下：

+ 容器序列： list, tuple, collections.deque
+ 扁平序列： str, bytes, bytearray, array.array

按照存放数据能否被修改可以分为可变序列和不可变序列，顾名思义，可变序列就是存放的数值是可以被改变的，不可变序列就是值是不可以被改变的，如果被改变了，将会得到一个新的对象。可变序列和不可变序列的举例如下：

+ 可变序列： list, bytearray, array.array, collections.deque, memoryview
+ 不可变序列： tuple, str, bytes


## 列表推导
列表推导是构建列表的快捷方式。废话不多说，直接上列表推导的示例：

```Python
def symbol2ascii(symbols):
    ascii_codes = [ord(symbol) for symbol in symbols]
    print(ascii_codes)


symbol2ascii("ABCDabcdEF")
```

列表推导虽然可读性更好，代码运行更高效，但也不能够滥用，如果列表推导的代码超过了两行，就应该考虑使用for循环代替了。一般的原则是：只用列表推导来创建新的列表，并且尽量保持简短。

## 生成器表达式
列表推倒的作用只是生成列表，如果希望生成其他类型的序列，可以使用生成器表达式，它能够创建其它任何类型的序列。另外，生成器表达式背后遵守了迭代器协议，可以逐个地产出元素，而不是先建立一个完整的列表，然后再把这个列表传递到某个构造函数里。
生成器表达式的语法和列表很相似，不同之处是把方括号换成圆括号，并指明要生成的序列类型。

```Python
def symbol2ascii_by_generator(symbols):
    ascii_codes_generator = (ord(symbol) for symbol in symbols)
    ascii_codes_tuple = tuple(ord(symbol) for symbol in symbols)
    ascii_codes_list = list(ord(symbol) for symbol in symbols)
    print(type(ascii_codes_generator))
    print(type(ascii_codes_tuple))
    print(type(ascii_codes_list))

symbol2ascii_by_generator("ABCDabcdEF")
```
## 切片
### 为什么切片和区间会忽略最后一个元素
这样做的好处有以下几点：

+ 当只有最后一个位置时，我们也可以快速看出切片和区间有多少个元素，比如`my_list[:5]`有5个元素
+ 当起止位置信息都可见的时候，我们可以快速计算出区间的长度，即后一个数减去第一个数
+ 可以让我们使用任意一个数把区间分成两个部分，比如`my_list[:x]`和`my_list[x:]`

### 切片的使用方法
可以使用`my_list[a:b]`的形式对序列进行基本的切片操作，也可以用`my_list[a:b:c]`的形式对列表my_list在a和b之间以c间隔进行取值，c的值也可以是负值，代表反向取值，如下所示：

```python
def split_for_object(object_ex):
    print(object_ex)
    print(object_ex[2:5])
    print(object_ex[:4])
    print(object_ex[::3])
    print(object_ex[::-1])
    print(object_ex[::-2])

split_for_object("abcdefghijklmn")
```
程序运行的返回结果如下：

```Python
abcdefghijklmn
cde
abcd
adgjm
nmlkjihgfedcba
nljhfdb
```

## 序列的+和*

+可用于两个序列的拼接操作，*用于一个序列重复n次的操作，这两个运算符都不修改原有的序列，而是产生一个新的序列。示例如下所示：

```python
# 序列的+运算
def do_add(a, b):
    print(a + b)


# 序列的*运算
def do_mul(a, n):
    print(a * n)

do_add("hello ", "world!")
do_mul("ABB-", 4)
```

*的运用有一个需要注意的地方，即在执行`a*n`的过程中，如果a中有元素是对其他可变对象的引用，则运算完成之后就得到n个同样的引用，修改一处则会有多处进行修改。比如下面这个示例：

``` python
def wrong_ex():
    weird_board = [['_'] * 3] * 3
    print(weird_board)
    weird_board[0][2] = 'A'
    print(weird_board)


def right_ex():
    weird_board = [['_'] * 3 for i in range(3)]
    print(weird_board)
    weird_board[0][2] = 'A'
    print(weird_board)

wrong_ex()
right_ex()
```

上面示例的运行结果如下：

```python
[['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
[['_', '_', 'A'], ['_', '_', 'A'], ['_', '_', 'A']]
[['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
[['_', '_', 'A'], ['_', '_', '_'], ['_', '_', '_']]

```


## 序列的增量赋值
### 就地加法
增量赋值的写法就是类似于`a += b`的样子，+=背后用到的特殊方法是`__iadd__`，但是如果一个类没有实现这个方法，python就会退而求其次，使用`__add__`方法。这两个方法还是有根本的区别的：

+ `__iadd__`方法也称‘就地加法’，因为在做运算的时候，a会就地改动，效果就像`a.extend(b)`一样，不会出现新的对象。
+ `__add__`方法在做加法运算的时候，会先计算`a + b`，然后将结果存到一个新的对象中，再将这个对象赋值给a。

需要注意的是，就地加法只能运用在可变序列中，不可变序列不会在原地进行修改。如下示例所示：

```python
# 就地加法在可变序列和不可变序列中的应用
def iadd_ex():
    a = [1, 2, 3]
    b = (4, 5, 6)
    c = [7, 8, 9]
    d = (10, 11, 12)
    print("id for a :{}".format(id(a)))
    print("id for b :{}".format(id(b)))

    a += c
    b += d
    print("id for a after run a += c : {}".format(id(a)))
    print("id for b after run b += c : {}".format(id(b)))

iadd_ex()
```

示例结果如下：

```python
id for a :4324181576
id for b :4324140952
id for a after run a += c : 4324181576
id for b after run b += c : 4324209000
```

由此可见：对不可变序列进行重复拼接操作的话，效率会变得很低，因为解释其需要把原来对象中的元素拷贝到新的位置，然后在执行拼接操作。

**注意，str作为不可变序列，重复操作时没有效率降低的说法，因为对str类型数据做+=操作太普遍，python就对其进行了优化，在申请空间时，程序会预留可扩展空间给str，因此不会涉及到复制的操作，而是直接执行拼接**

### 就地乘法
就地乘法的使用和就地加法很相似，只不过就地乘法用到而特殊方法是：`__imul__`

## list.sort() and sorted()

+ list.sort()方法是就地排序，执行完这个方法后，原对象有可能发生了变化，同时，这个方法也不会返回任何值。
+ sorted()方法做排序操作时，会新建一个列表作为返回值，这个方法可以接受任何形式的可迭代对象作为参数，也可以包括不可变对象和生成器，只是最后返回的都会是一个列表。

list.sort()方法和sorted()方法虽然实现不同，但都有两个可选的关键字参数：

+ reverse： 指明最终序列是升序还是降序，这个参数的默认值是False，代表升序。
+ key： 一个只有一个参数的函数，这个函数会被用在序列里的每一个元素上，函数所产生的结果就是排序算法依赖的对比关键字。默认用元素自己的值来排序。

```python
# list.sort()方法和sorted()方法的使用
def sort_and_sorted():
    fruits = ['grape', 'watermelon', 'apple', 'banana']
    # 通过下面两个输出可以证明sorted()方法不改变原来的序列
    print(sorted(fruits))
    print(fruits)

    # 按照元素本身进行降序排序,这里就是字母顺序
    print(sorted(fruits, reverse=True))

    # 按照长度进行升序排序
    print(sorted(fruits, key=len))

    # 按照长度进行降序排序
    print(sorted(fruits, key=len, reverse=True))

    # 通过下面两个打印可以证明list.sort()方法是就地排序
    print(fruits)
    fruits.sort()
    print(fruits)

sort_and_sorted()
```
程序的运行结果如下：

```python
['apple', 'banana', 'grape', 'watermelon']
['grape', 'watermelon', 'apple', 'banana']
['watermelon', 'grape', 'banana', 'apple']
['grape', 'apple', 'banana', 'watermelon']
['watermelon', 'banana', 'grape', 'apple']
['grape', 'watermelon', 'apple', 'banana']
['apple', 'banana', 'grape', 'watermelon']
```

