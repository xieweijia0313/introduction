from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path('sitka_weather_07-2021_simple.csv')
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)
print(header_row)
# 获取每个元素的索引及其值
for index, column_header in enumerate(header_row):
    print(index, column_header)

dates, highs, lows = [], [], []
for row in reader:
    # 提取日期
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    # 提取最高温度
    high = int(row[4])
    # 提取最低温度
    low = int(row[5])
    dates.append(current_date)
    highs.append(high)
    lows.append(low)

# 根据数据绘图
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, linewidth=3, color='red')
ax.plot(dates, lows, linewidth=3, color='blue')
# 传递一组x坐标值和两组y坐标值;实参facecolor指定填充区域的颜色;实参alpha指定颜色的透明图,0完全透明,1完全不透明
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# 设置绘图的格式
ax.set_title("Daily High Temperatures, July 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)

# 绘制倾斜的日期标签
fig.autofmt_xdate()

ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=14)
plt.show()
