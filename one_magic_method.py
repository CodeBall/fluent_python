#-*- coding:utf-8 -*-

import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(i) for i in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(suit, rank) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

# 初始化一个FrenchDeck的对象,这时会调用__init__方法
deck = FrenchDeck()

# 可以使用len()方法查看deck的长度,此时会调用__len__方法
print(len(deck))

# 如果想获取deck中某个元素,可以使用下标索引法,此时会调用__getitem方法
print(deck[0])
print(deck[-1])

# 如果想随机抽取某一个元素,可以结合random中的choice方法
for i in range(0, 5):
    print(choice(deck))

# 在初始化的过程中,可以看到生成的对象其实是一个列表, 那么可以向操作列表一样操作deck

# 切片操作☞取出第二个到第八个元素,左闭右开
print(deck[2:8])

# 切片操作☞取出第一个元素,然后每隔13个元素取一次
print(deck[1::13])

# 迭代以及反向迭代取出所有元素,此时会调用__getitem__方法
for d in deck:
    print(d)

for d in reversed(deck):
    print(d)
