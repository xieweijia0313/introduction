"""绘制简单的散点图"""
import matplotlib.pyplot as plt

# 使用 scatter() 绘制一系列点
# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]

# 自动计算数据，将系列点连成一条线
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=100)
# 设置图题并给坐标轴加上标签
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
# 设置刻度标记的样式
ax.tick_params(labelsize=14)

# 设置每个坐标轴的取值范围
ax.axis([0, 1100, 0, 1_100_000])
# 保存绘图
plt.savefig('scatter_squares_plot.png', bbox_inches='tight')
# 显示绘图
plt.show()

