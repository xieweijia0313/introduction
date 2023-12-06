"""绘制简单的折线图"""

import matplotlib.pyplot as plt

# 切换为图形界面显示的终端TkAgg
# plt.matplotlib.use('TkAgg')

input_values = list(range(1, 6))
squares = [1, 4, 9, 16, 25]

# 绘制折线图。
"""输入值x轴, 输出值y轴, linewidth=线条粗细。"""
plt.plot(input_values, squares, linewidth=5)

# 设置图表标题并给坐标轴加上标签。
plt.title("Square Numbers", fontsize=24)  # 设置图形标题
plt.xlabel("Value", fontsize=14)  # 设置图形x轴标签
plt.ylabel("Square of Value", fontsize=14)  # 设置图形y轴标签
plt.tick_params(axis='both', which='major', labelsize=14)  # 设置刻度标记的大小

plt.savefig('mpl_squares_plot.png', bbox_inches='tight')  # 自动保存图表。
plt.show()  # 显示图形。
