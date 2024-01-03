from pathlib import Path
# import matplotlib.pyplot as plt
import plotly.express as px

file_path = Path("S28_data.txt")
path = Path("S28.txt")
path.write_text("")
# 打开文件，逐行读取，组成一个列表
content = file_path.read_text().rstrip().splitlines()

rpm_lists = []
time_lists = []
data_bike_lists = []
for cont in content:

    find_idx = cont.find("02-42")
    # print(find_idx)
    if find_idx == 90:
        data_bike = cont[90:].split('-')
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
    date_0x01 = int(contents[4] + contents[3], 16) * 0.01
    date_0x02 = int(contents[5], 16)
    date_0x03 = f"{int(contents[7] + contents[6], 16)}"
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
    rpm_lists.append(int(float(date_0x03)))

title = "踏频"
labels = {'x': 'Time', 'y': 'RPM'}
fig1 = px.line(x=time_lists, y=rpm_lists, title=title, labels=labels)
fig1.write_html('S28.html')
fig1.show()
