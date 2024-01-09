import matplotlib.pyplot as plt

# 使用 scatter() 绘制一系列点
# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]
# 自动计算数据，将系列点连成一条线
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

# 使用内置样式
plt.style.use('seaborn')
fig, ax = plt.subplots()
# 绘制散点图
# ax.scatter(x_values, y_values, s=100)

# 创建一个由红色的点组成的散点图。定制颜色，方案1
# ax.scatter(x_values, y_values, color='red', s=10)
# 使用 RGB 颜色模式定制颜色，创建一个由浅绿色的点组成的散点图。定制颜色，方案2
# ax.scatter(x_values, y_values, color=(0, 0.8, 0), s=10)
# 颜色映射。定制颜色，方案3
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# 设置图题并给坐标轴加上标签
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
# 设置刻度标记的样式
ax.tick_params(labelsize=14)

# 设置每个坐标轴的取值范围
ax.axis([0, 1100, 0, 1_100_000])
# 刻度标记使用常规表示法（定制刻度标记）
# ax.ticklabel_format(style='plain')
# 保存绘图
# plt.savefig('scatter_squares_plot.png', bbox_inches='tight')
# 显示绘图
plt.show()
