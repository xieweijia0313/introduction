import random, time, copy
WIDTH = 60  # 宽度
HEIGHT = 20  # 高度

# 列表的列表结构，存储活细胞和死细胞
nextCells = []
for x in range(WIDTH):  # 一共有60组数据
    column = []  # 创建一个新列
    for y in range(HEIGHT):  # 每组数据长度20
        if random.randint(0, 1) == 0:
            column.append('#')  # 添加一个活细胞
        else:
            column.append(' ')  # 添加一个死细胞

    nextCells.append(column)  # 加入列表的列表
print(nextCells)

while True:
    """主程序循环"""
    print('\n\n\n')  # 用换行符分隔每一步
    currentCells = copy.deepcopy(nextCells)  # 复制nextCells列表
    for y in range(HEIGHT):  # 20
        for x in range(WIDTH):  # 60
            print(currentCells[x][y], end='')
        print()
