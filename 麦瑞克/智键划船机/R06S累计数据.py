from pathlib import Path
# import matplotlib.pyplot as plt
import plotly.express as px

file_path = Path("R06原始数据.txt")
path = Path("累计数据解析.txt")
path.write_text("")
# 打开文件，逐行读取，组成一个列表
content = file_path.read_text().rstrip().splitlines()

rpm_lists = []
time_lists = []
data_bike_lists = []
time, distance,  calorie, count = [], [], [], []

for cont in content:

    find_idx = cont.find("02-43")
    # print(find_idx)
    if find_idx == 92:
        data_bike = cont[92:].split('-')
        data_bike_lists.append(data_bike)
        time_lists.append(cont[2:10])
# print(data_bike_lists)

for contents in data_bike_lists:
    print(contents)
    # 每一个字节位，代表的数据
    date_dicts = {
        "时间0x01": [3, 4], "距离0x02": [5, 6],  "卡路里0x03": [7, 8],  "计数0x04": [9, 10]
    }
    # 逐行将列表中的数据取出，并转成十进制
    date_0x01 = int(contents[4] + contents[3], 16)
    date_0x02 = int(contents[6] + contents[5], 16)
    date_0x03 = int(contents[8] + contents[7], 16)
    date_0x04 = int(contents[10] + contents[9], 16)
    date_dict_keys = list(date_dicts.keys())

    date = [date_0x01, date_0x02, date_0x03, date_0x04]

    i = 0
    for date_dict_key in date_dict_keys:
        print(date_dict_key, date[i])
        d = f"{date_dict_key, date[i]}"
        i += 1

        with path.open('a') as file_obj:
            file_obj.write(d)
    with path.open('a') as file_obj:
        file_obj.write(f"\n")
    print()
    time.append(int(float(date_0x01)))
    distance.append(int(float(date_0x02)))
    calorie.append(int(float(date_0x03)))
    count.append(int(float(date_0x04)))

title = "时间"
labels = {'x': 'Time', 'y': '时间'}
fig1 = px.line(x=time_lists, y=time, title=title, labels=labels)
fig1.write_html('S28.html')
fig1.show()

title = "距离"
labels = {'x': 'Time', 'y': '距离'}
fig1 = px.line(x=time_lists, y=distance, title=title, labels=labels)
# fig1.write_html('R.html')
fig1.show()

title = "热量"
labels = {'x': 'Time', 'y': '热量'}
fig1 = px.line(x=time_lists, y=calorie, title=title, labels=labels)
fig1.show()

title = "计数"
labels = {'x': 'Time', 'y': '计数'}
fig1 = px.line(x=time_lists, y=count, title=title, labels=labels)
fig1.show()
