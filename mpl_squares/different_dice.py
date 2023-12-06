import pygal
from die import Die

die_1 = Die()
die_2 = Die(10)

#  掷几次骰子，并将结果存储在一个列表中
results = []
for foll_num in range(5000):
    result = die_1.roll() + die_2.roll()  # 返回 一个随机数
    results.append(result)

# 分析结果
frequencies = []  # 将分析后的数据依次存入
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):  # 循环骰子的面数+1次
    frequency = results.count(value)  # 统计列表指定数值出现的次数
    frequencies.append(frequency)

# 对结果进行可视化
hist = pygal.Bar()  # 创建类的实例

hist.title = "Results of rolling two D6 + D10 5000 times."  # 标题
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']  # x轴刻度标签
hist.x_title = "Result"  # x轴标题
hist.y_title = "Frequency of Result"  # y轴标题
hist.add('D6 + D10', frequencies)  # 数据指定的标签，输入的数据列表
hist.render_to_file('dice_visual.svg')  # 图表渲染为SVG文件
