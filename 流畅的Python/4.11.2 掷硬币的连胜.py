# coding=utf-8
import random

# 初始化正反面次数为0, 设置循环次数time
head = 0
tail = 0
time = 100

# 列表存放正反面次数的结果,随机生成0和1，代表正反面
coin = [random.choice([0, 1]) for i in range(time)]

# 循环即抛硬币
for n in range(len(coin)):
    # 设置判断条件，将正反面次数存到变量，并存放到列表中
    if n == 0:
        head += 1
        coin.append(n)
    elif n == 1:
        tail += 1
        coin.append(n)
print('正面的概率', head/time)
print('反面的概率', tail/time)

# 计算本次硬币面和上一次是否相同，x正，y反
x = 0
y = 0

# 计算6正6反各自概率的和
a = 0
b = 0
