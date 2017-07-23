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


symbol2ascii("ABCDabcdEF")
symbol2ascii_by_generator("ABCDabcdEF")
