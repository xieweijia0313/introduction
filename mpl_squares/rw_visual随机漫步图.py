import matplotlib.pyplot as plt
from random_walk import RandomWalk


# 只要程序处于活动状态，就不断地模拟随机漫步
while True:
    # 创建一个RandomWalk实例，并将其所包含的点都绘制出来
    rw = RandomWalk(50000)
    rw.fill_walk()

    # 设置绘图窗口的尺寸
    plt.figure(dpi=128, figsize=(10, 6))
    # 设置图标样式
    plt.style.use('classic')
    fig, ax = plt.subplots()
    point_numbers = list(range(rw.num_points))
    # 绘制漫步图
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors="none", s=5)
    # 突出起点和终点
    ax.scatter(0, 0, c="green", edgecolors="none", s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c="red", edgecolors="none", s=100)

    # 绘制花粉在水滴表面的运动轨迹
    # ax.plot(rw.x_values, rw.y_values, linewidth=2)

    # 坐标轴隐藏
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    # x和y轴的刻度间距相等
    ax.set_aspect('equal')
    # 显示图形
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == "n":
        break
