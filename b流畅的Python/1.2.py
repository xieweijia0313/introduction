import collections
# from random import choice

# 初始化一个具名元组对对象Card
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    # 生成序列'2'~'A'
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    # 字符串转字符列表
    # print(list('JQKA'))  # ['J', 'Q', 'K', 'A']
    # 数字序列列表
    # print([n for n in range(2, 11)])
    # 数字转字符串
    # print([str(n) for n in range(2, 11)])
    # 字符串分隔
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


# 实例化对象
beer_card = Card('7', 'diamonds')

deck = FrenchDeck()
# print(len(deck))
# print(deck[0])  # 抽取第一张
# print(choice(deck))  # 随机抽一张

# 迭代纸牌
# for card in deck:
#     print(card)
# 反向迭代纸牌
# for card in reversed(deck):
#     print(card)


suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    # 检测字符串中是否包含子字符串card.rank
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


for card in sorted(deck, key=spades_high):
    print(card)
