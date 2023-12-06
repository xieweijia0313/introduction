import pygal
from die import Die

die = Die()

#  掷几次骰子，并将结果存储在一个列表中
results = []
for foll_num in range(100):
    result = die.roll()  # 返回一个随机数
    results.append(result)

# 分析结果
frequencies = []  # 将分析后的数据依次存入
for value in range(1, die.num_sides+1):  # 循环骰子的面数+1次
    frequency = results.count(value)  # 统计列表指定数值出现的次数
    frequencies.append(frequency)

# 对结果进行可视化
hist = pygal.Bar()  # 创建Bar类的实例

hist.title = "Results of rolling one D6 1000 times."  # 标题
hist.x_labels = ['1', '2', '3', '4', '5', '6']  # x轴刻度标签
hist.x_title = "Result"  # x轴标题
hist.y_title = "Frequency of Result"  # y轴标题
hist.add('D6', frequencies)  # 数据指定的标签，输入的数据列表
hist.render_to_file('die_visual.svg')  # 图表渲染为SVG文件
