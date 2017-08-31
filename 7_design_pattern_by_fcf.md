# 使用一等函数实现设计模式
## 使用函数实现“策略”模式
这里借助电商中的一个案例来实现“策略”模式，这个案例就是根据客户的订单和属性进行折扣的计算。
该示例对具体的策略使用函数进行封装，然后将折扣策略应用到Order实例上，因此只需要将促销函数作为参数传入即可。

```python
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

print(Order(joe, cart, fidelity_promo))
print(Order(ann, cart, fidelity_promo))

banana_cart = [LineItem('banana', 30, .5),
               LineItem('apple', 10, 1.5)
               ]

print(Order(joe, banana_cart, bulk_item_promo))

long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]

print(Order(joe, long_order, large_order_promo))
print(Order(joe, cart, large_order_promo))

```

## 选择最佳策略

在上述实例中，我们手动给每个订单分配了相应的折扣。对客户来讲，他们会希望每次的折扣最大，因此我们需要在诸多的折扣策略中选择一个最优的。最佳策略的查询也可以通过一个简单的方法来实现，如下所示：

```python
promos = [fidelity_promo, bulk_item_promo, large_order_promo]


def best_promo(order):
    """从所有折扣策略中选择最佳的"""

    return max(promo(order) for promo in promos)
```

## 找出全部策略
在选择最佳策略的时候，我们需要把所有的策略都集中在一个列表中，因此每增加一个策略，就要修改一次列表，这是非常麻烦的。
python提供了一个内置函数：`globals`，这个函数会返回一个字典，表示当前的全局符号表，这个符号表始终针对当前模块，对函数或方法来说，当前模块就是定义他们的模块。
该函数的使用方法如下所示：

```python
promos = [globals()[name] for name in globals() if name.endswith('_promo') and name != 'best_promo']
```

另一个解决方法是：将所有的策略方法放在同一个模块中，且该模块的方法只能是策略函数，我们假设这个模块是`promotions`，然后将该模块进入，借助`inspect`模块的`isfunction`方法获取所有的策略方法名。如下所示：

```python
import inspect
promos = [func for name, func in inspect.getmembers(promotions, inspect.isfunction)]
```


