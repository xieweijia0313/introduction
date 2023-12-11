"""绘制简单的折线图"""
import matplotlib.pyplot as plt

# 切换为图形界面显示的终端TkAgg
# ax.matplotlib.use('TkAgg')

input_values = list(range(1, 6))  # 输入数据
squares = [1, 4, 9, 16, 25]  # 输出数据

# 绘制折线图。

# 使用内置样式
plt.style.use('seaborn')

# 调用subplots()函数，在一个图形（figure）中绘制一或多个绘图（plot）。
# 变量fig 表示由生成的一系列绘图构成的整个图形。
# 变量 ax 表示图形中的绘图，在大多数情况下，使用这个变量来定义和定制绘图。
fig, ax = plt.subplots()
"""输入值x轴, 输出值y轴,linewidth=线条粗细。"""
ax.plot(input_values, squares, linewidth=5)

# 设置图表标题并给坐标轴加上标签。
ax.set_title("Square Numbers", fontsize=24)  # 设置图形标题
ax.set_xlabel("Value", fontsize=14)  # 设置图形x轴标签
ax.set_ylabel("Square of Value", fontsize=14)  # 设置图形y轴标签
ax.tick_params(axis='both', which='major', labelsize=14)  # 设置刻度标记的大小

# ax.savefig('mpl_squares_plot.png', bbox_inches='tight')  # 自动保存图表。
plt.show()  # 打开 Matplotlib 查看器并显示绘图
