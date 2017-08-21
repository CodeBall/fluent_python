import random

from inspect import signature
from functools import reduce, partial
from operator import add, mul


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


print(reduce(add, range(100)))
# 在计算求和方面,sum函数完全可以代替reduce进行计算
print(sum(range(100)))


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


def f(a, *, b):
    return a, b

print(f(12, b=23))


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


def args_info_by_signature():
    sig = signature(args_info)
    print(sig)
    str(sig)

    for name, param in sig.parameters.items():
        print(param.kind, ':', name, '=', param.default)

args_info_by_signature()


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


def fun_annotation(test:str, max_len:'int > 0'=80) -> str:
    return "just text"


def read_annotation():
    sig = signature(fun_annotation)
    print(sig.return_annotation)

    for param in sig.parameters.values():
        note = repr(param.annotation).ljust(13)
        print(note, ':', param.name, '=', param.default)

read_annotation()



triple = partial(mul, 3)
print(triple(7))


