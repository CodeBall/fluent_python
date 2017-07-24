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


# symbol2ascii("ABCDabcdEF")
# symbol2ascii_by_generator("ABCDabcdEF")
# split_for_object("abcdefghijklmn")
# do_add("hello ", "world!")
# do_mul("ABB-", 4)
wrong_ex()
right_ex()
