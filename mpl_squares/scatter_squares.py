"""绘制简单的散点图"""

import matplotlib.pyplot as plt

# 切换为图形界面显示的终端TkAgg
# plt.matplotlib.use('TkAgg')

# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]


# 绘制散点图。
"""输入值, 输出值, c=线条颜色, cmap=plt.cm.指定映射的颜色, edgecolor='none'删除数据点轮廓, s=数据点大小。"""
# c='red' //自定义颜色，cmap参数需删除
# c=y_values, cmap=plt.cm.Blues  //颜色映射
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=15)


# 设置图表标题并给坐标轴加上标签。
plt.title("Square Numbers", fontsize=24)  # 设置图形标题
plt.xlabel("Value", fontsize=14)  # 设置图形x轴标签
plt.ylabel("Square of Value", fontsize=14)  # 设置图形y轴标签
plt.tick_params(axis='both', which='major', labelsize=14)  # 设置刻度标记的大小

# 装饰图形。
plt.savefig('scatter_squares_plot.png', bbox_inches='tight')  # 自动保存图表。
plt.show()  # 显示图形。
