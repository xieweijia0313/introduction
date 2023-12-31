import collections

# 初始化一个具名元组对对象Card
Card = collections.namedtuple('Card', ['rank', 'suit'])

# 实例化对象
beer_card = Card('7', 'diamonds')

# 获取所有字段名和字段值
print(beer_card)  # Card(rank='7', suit='diamonds')

# 获取所有字段名构成的tuple//('rank', 'suit')
print(beer_card._fields)  # ('rank', 'suit')

"""函数支持的3个方法"""
# 使用list实例化一个新的对象，原namedtuple不变
beer_card21 = beer_card._make([5, "kk园区"])
print(beer_card21)  # Card(rank=5, suit='kk园区')

# 使用关键字参数修改并实例化一个新对象
beer_card22 = beer_card._replace(suit="kk战区")
print(beer_card22)  # Card(rank='7', suit='kk战区')

# 将 namedtuple 对象转换为 OrderedDict 有序字典对象
print(beer_card._asdict())  # {'rank': '7', 'suit': 'diamonds'}
