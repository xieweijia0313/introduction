import csv
from datetime import datetime
from matplotlib import pyplot as plt

# filename = 'sitka_weather_07-2021_simple.csv'
filename = 'death_valley_2021_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)  # 调用函数csv.read(),将f存储的文件对象当作实参传递给他，创建一个与文件相关联的阅读器对象
    header_row = next(reader)  # 调用函数next()，将阅读器对象传递给他，返回文件中的下一行，调用1次返回1行

    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)
    dates, highs, lows = [], [], []  # dates, highs存储时间和温度
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        dates.append(current_date)

        high = int(row[4])
        highs.append(high)

        low = row[5]
        lows.append(low)

# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)  # alpha颜色的透明度;0表示完全透明，1（默认设置）表示完全不透明
plt.plot(dates, lows, c='blue', alpha=0.5)
# 给图表区域着色
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# 设置图形的格式
plt.title("Daily high temperatures, July 2014", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()  # 绘制斜的日期标签
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=10)

plt.show()
