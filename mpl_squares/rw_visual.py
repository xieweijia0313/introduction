import matplotlib.pyplot as plt
from random_walk import RandomWalk


# 只要程序处于活动状态，就不断地模拟随机漫步
while True:
    # 创建一个RandomWalk实例，并将其所包含的点都绘制出来
    rw = RandomWalk(50000)
    rw.fill_walk()
    point_numbers = list(range(rw.num_points))

    # 设置绘图窗口的尺寸
    plt.figure(dpi=128, figsize=(10, 6))

    # 坐标轴隐藏。原始代码，失效
    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_yaxis().set_visible(False)
    # 坐标轴隐藏。
    current_axes = plt.axes()
    current_axes.xaxis.set_visible(False)
    current_axes.yaxis.set_visible(False)

    # 绘制漫步图
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors="none", s=5)
    # 突出起点和终点
    plt.scatter(0, 0, c="green", edgecolors="none", s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c="red", edgecolors="none", s=100)

    """
    # 绘制花粉在水滴表面的运动轨迹
    plt.plot(rw.x_values, rw.y_values, linewidth=2)
    """

    plt.show()  # 显示图形
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == "n":
        break
