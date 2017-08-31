from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')


class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:

    def __init__(self, customer, cart, promotion = None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)

        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)

        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


def fidelity_promo(order):
    """为积分达到1000以上的客户提供5%折优惠"""
    return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0


def bulk_item_promo(order):
    """为单个商品达到20个的客户提供10%折优惠"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1

    return discount


def large_order_promo(order):
    """订单中的不同商品达到10个的客户提供7%折优惠"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07

    return 0


joe = Customer('joe', 0)
ann = Customer('ann', 1100)
cart = [LineItem('banana', 4, .5),
        LineItem('apple', 10, 1.5),
        LineItem('mellon', 5, 5.0)
        ]

# print(Order(joe, cart, fidelity_promo))
# print(Order(ann, cart, fidelity_promo))

banana_cart = [LineItem('banana', 30, .5),
               LineItem('apple', 10, 1.5)
               ]

# print(Order(joe, banana_cart, bulk_item_promo))

long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]

# print(Order(joe, long_order, large_order_promo))
# print(Order(joe, cart, large_order_promo))


# promos = [fidelity_promo, bulk_item_promo, large_order_promo]
promos = [globals()[name] for name in globals() if name.endswith('_promo') and name != 'best_promo']
# import inspect
# 注意,这里的promotions是我们存放策略函数的模块,该代码示例把策略放在了同一个模块中,
# 如果想正确运行以下语句,还需摘出所有策略方法,放在外部的promotions模块中,并且引入该模块。
# promos = [func for name, func in inspect.getmembers(promotions, inspect.isfunction)]


def best_promo(order):
    """从所有折扣策略中选择最佳的"""

    return max(promo(order) for promo in promos)

# print(best_promo(Order(joe, long_order)))

