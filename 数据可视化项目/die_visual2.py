import plotly.express as px
from die import Die

# 创建一个D6
die_1 = Die(8)
die_2 = Die(8)

#  掷2个骰子，并将结果存储在一个列表中
# results = []
# for foll_num in range(50_000):
#     result = die_1.roll() + die_2.roll()  # 返回一个随机数
#     results.append(result)

# 将for循环替代为列表推导式
results = [die_1.roll() + die_2.roll() for foll_num in range(50_000)]

# 分析结果
# frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result+1)
# for value in poss_results:
#     frequency = results.count(value)
#     frequencies.append(frequency)

# 将for循环替代为列表推导式
frequencies = [results.count(value) for value in poss_results]


# 对结果进行可视化
title = "Results of Rolling Two D6 Dice 50,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
# fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)  # 直方图
# fig = px.scatter(x=poss_results, y=frequencies)  # 散点图
fig = px.line(x=poss_results, y=frequencies)  # 折线图

# 进一步定制图形
# 将x轴的标签间距设为1
fig.update_layout(xaxis_dtick=1)
# fig.write_html('dice_visual_d6d10.html')
fig.show()
