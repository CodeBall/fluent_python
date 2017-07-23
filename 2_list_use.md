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
## 序列的+和*
## 序列的增量赋值
## list.sort() and sorted()

