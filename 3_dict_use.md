# 字典
## 可散列的数据类型
### 定义
如果一个对象是可散列的，那么在这个对象的生命周期中，它的散列值是不变的，而且这个对象需要实现`__hash()__`方法。
另外，可散列对象还要有`__qe()__`方法，这样才能跟其他键作比较。
如果两个可散列对象是相等的，那么它们的散列值一定是一样的。
### 可散列数据举例
+ str,bytes和数值类型等原子不可变数据类型都是可散列的类型。
+ 对于元组来说，只有当一个元组包含的所有元素都是可散列类型的情况下，该元组才是可散列类型。
+ 自定义对象都是可散列的，散列值就是该对象的id()函数返回的值


## 字典的构造方法
构造字典的方式有很多种，如下所示：

```python
# 字典的构造方法
dict1 = {"name": "Alice", "age": 23, "email": "test@126.com"}
dict2 = dict(name="Alice", age=23, email="test@126.com")
dict3 = dict([("name", "Alice"), ("age", 23), ("email", "test@126.com")])
dict4 = dict(zip(["name", "age", "email"], ["Alice", 23, "test@126.com"]))
dict5 = dict({"email": "test@126.com", "age": 23, "name": "Alice"})

print(dict1 == dict2 == dict3 == dict4 == dict5)
```

这个示例的输出结果会是`True`，由此可以看出,无论我们用什么方法、以什么顺序创造字典,在基本的字典类型中,只要字典中元素的键和值都是相等的,创造出来的字典都是相同的。

### 字典推导(ﾉ*･ω･)ﾉ
和列表一样,字典也可以使用字典推导的方法来构建新的字典,来看下面两个例子：

```Python
# 示例一
dial_codes = [(86, 'China'), (91, 'India'), (1, 'Unit States'), (62, 'Indonesia'), (55, 'Brazil'), (92, 'Pakistan'),
              (880, 'Bangladesh'), (234, 'Nigeria'), (7, 'Russia'), (81, 'Japan')]
country_code1 = {country: code for code, country in dial_codes}
print(country_code1)
```

```python
# 示例二
codes = [86, 91, 1, 62, 55, 92, 880, 234, 7, 81]
countries = ["China", "India", "Unit States", "Indonesia", "Brazil", "Pakistan", "Bangladesh", "Nigeria", "Russia",
             "Japan"]
country_code2 = {country: code for country in countries for code in codes}
country_code3 = [{country: code} for country in countries for code in codes]
print(country_code2)
print(country_code3)
```

在示例二中,给出了两种推导的方法,一种是字典推导,会得到一个字典,另一种是列表推导,该示例和1_magic_method.py中生成纸牌的示例很相似,这里计算的是codes和countries的笛卡尔积。可以自己运行程序查看结果。

## 常见的映射方法
collections模块中有两个字典的变种类型，分别是defaultdict和OrderedDict，它们和dict类型也是有共同的方法。具体可以看下表的内容：

  方法列表 | dict | defaultdict | OrderedDict | 备注
  ---- | ---- | ---- | ---- | ----
  `d.clear()` | ✅ | ✅ | ✅ | 移除所有的元素
  `d.__contains__(k)` | ✅ | ✅ | ✅ | 检查k是否在d中
  `d.copy()` | ✅ | ✅ | ✅ | 浅复制
  `d.__copy__()` | | ✅ | | 用于支持浅复制
  `d.default_factory` | | ✅ | | 在`__mising__`函数中被调用的函数，用于给未找到的元素设置值
  `d.__delitem__(k)` | ✅ | ✅ | ✅ | `del d(k)`, 移除键为k的元素
  `d.fromkeys(it, [initial])` | ✅ | ✅ | ✅ | 将迭代器it里的元素设置为映射里的键， 如果有initial参数，就把它设为这些键对应的值，默认为None
  `d.get(k, [default])` | ✅ | ✅ | ✅ | 返回键k对应的值，如果字典中没有该键，则返回default的值或者None
  `d.__getitem__(k)` | ✅ | ✅ | ✅ | 让字典d能用`d[k]`的形式返回k对应的值，如果k找不到会报错
  `d.items()` | ✅ | ✅ | ✅ | 返回d中所有的键值对
  `d.__iter__()` | ✅ | ✅ | ✅ | 返回键的迭代器
  `d.keys()` | ✅ | ✅ | ✅ | 返回字典的所有键
  `d.__len__()` | ✅ | ✅ | ✅ | 可以使用`len(d)`的形式得到字典的键值对数量
  `d.__missing__(k)` | | ✅ | | 当`__getitem__()`找不到相应的值时，会调用该方法
  `d.move_to_end(k, [last])` | | | ✅ | 把键为k的元素移动到字典的最前面或者最后面， last默认为True
  `d.pop(k, [default])` | ✅ | ✅ | ✅ | 返回键k所对应的值，然后移除这个键值对，如果k没有找到，则返回default的值或者None
  `d.popitem()` | ✅ | ✅ | ✅ | 随机返回一个键值对，并在字典中移除掉
  `d.__reversed__()` | | | ✅ | 返回倒序的键的迭代器
  `d.setdefault(k, [default])` | ✅ | ✅ | ✅ | 若字典中有键k，则把它对应的值设定为default的值，然后返回这个值若无，则让`d[k] = default`，然后返回default
  `d.__setitem__(k, v)` | ✅ | ✅ | ✅ | 实现d[k] = v的操作
  `d.update(m, [**kargs])` | ✅ | ✅ | ✅ | m可以是映射或者键值对迭代器，用来更新d中对应的条目
  `d.values()` | ✅ | ✅ | ✅ | 返回字典中的所有值

## 处理找不到的键的方法
从上面的表中可以得知，查找一个字典的键对应的值有多种方法

+ `d[k]`方法在找不到键k时，Python会直接抛出异常
+ `d.get(k, [default])` 方法在找不到键k时，会返回None, 如果default参数被设定了，则会返回该参数的值

### 使用setdefault
如果除了拿到这个值外，还想对该值进行更新操作，并且在没有键的情况下，则执行添加操作，那么setdefault方法是最好的选择

`d.setdefault()`方法的使用十分简单，下面来看使用这个方法和不使用的代码对比：

```python
# 从字典country_code1中搜索Korea对应的号码, 如果没有则赋值为99999
import time
start_time = time.time()
if "Korea" not in country_code1:
    country_code1["Korea"] = 99999
    print((time.time() - start_time)*10000)

# 从字典country_code1中搜索Canada对应的号码, 如果没有则赋值为251
start_time = time.time()
country_code1.setdefault("Canada", 251)
print((time.time() - start_time)*10000)
print(country_code1)
```

在上述示例中，计算出了两种方法的执行时间，从时间来看，使用`setdefault()`方法所用的时间会更短。

### 自定义__missing__方法
如果只是单纯的查找取值，除了`d[k]` 和 `d.get(k, [default])` 两种方法，defaultdict类型还提供了`__missing__`方法。

defaultdict类型的基本使用示例：

```python
import collections
dd = collections.defaultdict(tuple, **country_code1)
print(dd['China'])
print(dd.get("C"))
print(dd["C"])
print(dd["B"])
print(dd.get("B"))
```

从上示例的结果可以看出，当从字典中查询一个不存在的键时，defaultdict会对该键初始化一个空的tuple作为值，之后在查询该键，则会返回空的tuple。
并且，`__missing__`方法只会在`__getitem__`里被调用，其他方法是不会发挥作用的。

如果觉得defaultdict中的`__missing__`太有局限性了，可以自己定义一个雷然后实现该方法，从而达到目的。
比如以下示例：

```Python
class StrKeyDict0(dict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, item):
        return item in self.keys() or str(item) in self.keys()

d = StrKeyDict0([('2', 'two'), ('4', 'four')])
print(d['2'])
print(d[4])
print(d.get('2'))
print(d.get(4))
print(d.get(1))
print(2 in d)
print(1 in d)
print(d[1])
```

自定义类实现的功能是当请求的键是其他类型时，转换成字符串类型再去获取值。该类的实现有以下几点值得注意：

+ get()方法把查找的工作以`self[key]`的形式进行处理，这样做可以在取值的时候调用`__getitem__()`方法，当获取不到键的时候，该方法会去调用`__missing__()`方法，于是就会触发将键的类型转换成字符串形式的操作。
+ 关于`__missing__()`方法中为什么还要判断key的类型是否是字符串，则是为了防止掉进无限递归的陷阱。`__missing__()`方法的返回还是使用`self[key]`的格式，该方法在获取不到键的时候会调用`__missing__()`方法，因此会形成一个无限递归。
+ 关于为什么会有`__contains__`方法，是因为在执行`in`操作的时候会用到该方法，但是dict中提供的这个方法不会在找不到键的时候调用`__missing__`方法。另外，在实现这个方法的时候，使用的是`key in self.keys()`的形式而不是`key in d`的形式，也是为了防止掉进无限递归的陷阱中。

## 字典的变种
标准库collections模块中，有以下几种不同的映射类型：

+ collections.OrderedDict
+ collections.ChainMap
+ collections.Counter
+ collections.UserDict

除此之外，Python3.3之后，types模块引入了一个封装类名叫`MappingProxyType`的不可变映射类型。如果给这个类一个映射，他会返回一个只读视图，但是这个视图也是动态的。因此可以直接对原映射做出改变，但是不能通过视图对原映射做出改变。

