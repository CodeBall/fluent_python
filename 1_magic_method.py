import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(i) for i in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    # 这个方法是根据下标获取对象
    def __getitem__(self, position):
        print(position)
        return self._cards[position]

    """
    这个方法返回一个迭代器,当遇到需要迭代的情况时,会优先调用这个方法,
    如果该方法不存在,会调用__getitem__方法,如果两个方法都不存在,则代表这不是一个可迭代对象。
    """
    def __iter__(self):
        print("this function")
        return iter(self._cards)

    # 对列表进行排序的规则
    def sort_key(self, card):
        rank_value = self.ranks.index(card.rank)
        return rank_value * len(self.suit_values) + self.suit_values[card.suit]

# 初始化一个FrenchDeck的对象,这时会调用__init__方法
deck = FrenchDeck()


def length():
    # 可以使用len()方法查看deck的长度,此时会调用__len__方法
    print(len(deck))


def get_item():
    # 如果想获取deck中某个元素,可以使用下标索引法,此时会调用__getitem方法
    print(deck[0])
    print(deck[-1])


def random_item():
    # 如果想随机抽取某一个元素,可以结合random中的choice方法
    for i in range(0, 5):
        print(choice(deck))

# 在初始化的过程中,可以看到生成的对象其实是一个列表, 那么可以像操作列表一样操作deck


def slice_list():
    # 切片操作☞取出第二个到第八个元素,左闭右开
    print(deck[2:8])

    # 切片操作☞取出第一个元素,然后每隔13个元素取一次
    print(deck[1::13])


def iteration():
    # 迭代以及反向迭代取出所有元素,此时会调用__getitem__方法
    for d in deck:
        print(d)

    # for d in reversed(deck):
    #     print(d)


# deck既然是一个列表,就可以执行排序操作,具体的排序规则也是可以自己实现的
def sort_list_asc():
    # 对列表进行升序排序
    for card in sorted(deck, key=deck.sort_key):
        print(card)


def sort_list_desc():
    # 对列表进行降序排序
    for card in sorted(deck, key=deck.sort_key, reverse=True):
        print(card)
length()
get_item()
random_item()
slice_list()
iteration()
sort_list_asc()
sort_list_desc()


from math import hypot


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)

    def __abs__(self):
        # hypot 用来返回向量的模
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __repr__(self):
        return "Vector ({}, {})".format(self.x, self.y)
