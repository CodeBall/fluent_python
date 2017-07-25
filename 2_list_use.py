# 列表推导
def symbol2ascii(symbols):
    ascii_codes = [ord(symbol) for symbol in symbols]
    print(ascii_codes)


# 生成器表达式
def symbol2ascii_by_generator(symbols):
    ascii_codes_generator = (ord(symbol) for symbol in symbols)
    ascii_codes_tuple = tuple(ord(symbol) for symbol in symbols)
    ascii_codes_list = list(ord(symbol) for symbol in symbols)
    print(type(ascii_codes_generator))
    print(type(ascii_codes_tuple))
    print(type(ascii_codes_list))


# 切片的使用
def split_for_object(object_ex):
    print(object_ex)
    print(object_ex[2:5])
    print(object_ex[:4])
    print(object_ex[::3])
    print(object_ex[::-1])
    print(object_ex[::-2])


# 序列的+运算
def do_add(a, b):
    print(a + b)


# 序列的*运算
def do_mul(a, n):
    print(a * n)


# 建立由列表组成的列表
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


# symbol2ascii("ABCDabcdEF")
# symbol2ascii_by_generator("ABCDabcdEF")
# split_for_object("abcdefghijklmn")
# do_add("hello ", "world!")
# do_mul("ABB-", 4)
# wrong_ex()
# right_ex()
# iadd_ex()
