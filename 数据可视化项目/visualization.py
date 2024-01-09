from die import Die
import plotly.express as px

die_1 = Die()
die_2 = Die(10)


#  掷几次骰子，并将结果存储在一个列表中
results = []
for foll_num in range(50000):
    result = die_1.roll() + die_2.roll()  # 返回 一个随机数
    results.append(result)

# 分析结果
frequencies = []  # 将分析后的数据依次存入
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result+1)
for value in poss_results:  # 循环骰子的面数+1次
    frequency = results.count(value)  # 统计列表指定数值出现的次数
    frequencies.append(frequency)

# 对结果进行可视化
title = "Results of rolling two D6 and D10 50,000 times."  # 标题
labels = {'x': "Result", 'y': "Frequency of Result"}  # x,y轴标题
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)  # 生成一个127.0.0.1网页
# 进一步定制图形
fig.update_layout(xaxis_dtick=1)  # 刻度标签的间距指定为1
fig.show()  # 查看网页
# fig.write_html('dice_visual_d6d10.html')  # 保存图像
