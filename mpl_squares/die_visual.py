import plotly.express as px
from die import Die

# 创建一个D6
die = Die()

#  掷几次骰子，并将结果存储在一个列表中
results = []
for foll_num in range(100):
    result = die.roll()  # 返回一个随机数
    results.append(result)

# 分析结果
frequencies = []
poss_results = range(1, die.num_sides+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
title = "Results of Rolling One D6 1,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)  # 直方图
# fig = px.scatter(x=poss_results, y=frequencies)  # 散点图
# fig = px.line(x=poss_results, y=frequencies)  # 折线图
fig.show()
