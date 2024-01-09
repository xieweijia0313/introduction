from pathlib import Path
# import matplotlib.pyplot as plt
import plotly.express as px

file_path = Path("R06原始数据.txt")
path = Path("瞬时数据解析.txt")
path.write_text("")
# 打开文件，逐行读取，组成一个列表
content = file_path.read_text().rstrip().splitlines()

speed, level, rpm = [], [], []
time_lists = []
data_bike_lists = []
for cont in content:

    find_idx = cont.find("02-42")
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
        "瞬时速度0x01": [3, 4], "当前阻力0x02": 5,  "瞬时踏频0x03": [6, 7]
    }
    # 逐行将列表中的数据取出，并转成十进制
    date_0x01 = int(contents[4] + contents[3], 16) / 100
    date_0x02 = int(int(contents[5], 16) / 10)
    date_0x03 = int(contents[7] + contents[6], 16)

    date_dict_keys = list(date_dicts.keys())
    date = [date_0x01, date_0x02, date_0x03]

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
    speed.append(int(float(date_0x01)))
    level.append(int(float(date_0x02)))
    rpm.append(int(float(date_0x03)))

title = "速度"
labels = {'x': 'Time', 'y': title + ' km/h'}
fig1 = px.line(x=time_lists, y=speed, title=title, labels=labels)
# fig1.write_html('.html')
fig1.show()

title = "阻力"
labels = {'x': 'Time', 'y': title}
fig1 = px.line(x=time_lists, y=level, title=title, labels=labels)
fig1.show()

title = "踏频"
labels = {'x': 'Time', 'y': title}
fig1 = px.line(x=time_lists, y=rpm, title=title, labels=labels)
fig1.show()
