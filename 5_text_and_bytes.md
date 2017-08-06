# 文本和字节序列

写在前面：这篇笔记只是简单地记录一下，因为对编码问题了解的比较少，所以在看的过程中并不算太懂，这里只把能够理解的以及应该记忆的列举出来。

## 字符

字符的标识，即码位，是0~1114111的数字。
字符的具体表述取决于编码，编码是在码位和字节序列之间转换时的算法。
把码位转换成字节序列的过程是编码，把字节序列转换成码位的过程是解码。简单粗暴的来说，编码就是把人类可读的文本字符串转换成传输需要的字节序列，解码就是把字节序列转换成人类可读的本文字符串。

## 字节
二进制序列各个字节的值可能会使用下列三种不同的方式展示：

+ 可打印的ASCII范围内的字节，使用ASCII字符本身。
+ 制表符、换行符、回车符和\对应的字节，使用转义序列\t、\n、\r和\\
+ 其它字节的值使用十六进制转义序列（例如 \x00是空字节）

### 构建bytes 和 bytearray实例

构建bytes 和 bytearray实例可以调用各自的构造方法，传入一下参数

+ 一个str对象和一个encoding关键字参数
+ 一个可迭代对象，提供0~255之间的数值
+ 一个实现了缓冲协议的对象（如：bytes, bytearray, memoryview, array.array()）;此时，把源对象中的字节序列复制到新建的二进制序列中

## 处理UnicodeEncodeError
多数非UTF编解码器只能处理Unicode字符的一小部分，当我们把文本转换成字节序列时，如果目标编码中没有定义某个字符，就会抛出UnicodeEncodingError异常，除非把errors参数传给编码方法或函数。就像示例一样。

```python
city = 'São Paulo'
print(city.encode('utf_8'))

print(city.encode('utf_16'))

print(city.encode('iso8859_1'))

print(city.encode('cp437'))
```

上述示例在运行到最后一个`print`语句的时候，程序会抛出UnicodeEncodeError，然后终止运行。如果希望程序能够自己解决这种编码问题。可以传递errors参数,告诉程序遇到无法编码的字符时的处理方法，如下面示例：

```python
city = 'São Paulo'

print(city.encode('cp437', errors='ignore'))

print(city.encode('cp437', errors='replace'))

print(city.encode('cp437', errors='xmlcharrefreplace'))
```

上面示例的errors参数中的值都是已经注册好的，该参数的默认值是“strict”，该默认值的意思是直接抛出异常。另外，当遇到编码错误时，还可以使用自己注册的额外的字符串，方法是把一个名称和一个错误处理函数传给`codecs.register_error`函数。

## 处理UnicodeDecodeError

不是每个字节都包含有效的ASCII字符，也不是每一个字符序列都是有效的UTF_8或UTF_16,当把二进制序列转换成文本时，如果是这两个编码中的一个，遇到无法转换的字节序列时，程序会抛出UnicodeDecodeError错误。

```python
octet = b'Montr\xe9al'
print(octet.decode('cp1252'))

print(octet.decode('iso8859_7'))

print(octet.decode('koi8_r'))

print(octet.decode('utf_8'))
```


