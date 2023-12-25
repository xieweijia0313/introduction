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

    find_idx = cont.find("AA-27")
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
        "设备状态0x01": [4], "设备模式0x02": [5, 6], "瞬时速度0x03": 7, "瞬时踏频0x06": 10, "平均踏频0x0C": 13,
        "总距离0x0F": 16, "阻力等级0x17": 21, "瞬时功率0x08": 24, "平均功率0x0E": 27, "总消耗卡路里0x12": 30,
        "坡度值0x18": 33, "运动时间0x1E": 36
    }
    # 逐行将列表中的数据取出，并转成十进制
    date_0x01 = int(contents[4], 16)
    date_0x02 = int(contents[6], 16)
    date_0x03 = f"{contents[9] + contents[8]}, {int(contents[9] + contents[8], 16) * 0.01}"
    date_0x06 = f"{int(contents[12] + contents[11], 16) * 0.5}"
    date_0x0C = int(contents[15] + contents[14], 16) * 0.5
    date_0x0F = f"{contents[20] + contents[19] + contents[18] + contents[17]}, " \
                f"{int(contents[20] + contents[19] + contents[18] + contents[17], 16)}"
    date_0x17 = f"{int(int(contents[23] + contents[22], 16) * 0.1)}"
    date_0x08 = f"{int(contents[26] + contents[25], 16)}"
    date_0x0E = int(contents[29] + contents[28], 16)
    date_0x12 = f"{int(contents[32] + contents[31], 16)}"
    date_0x18 = contents[35] + contents[34]
    date_0x1E = f"{int(contents[38] + contents[37], 16)}"
    date_dict_keys = list(date_dicts.keys())

    date = [date_0x01, date_0x02, date_0x03, date_0x06, date_0x0C, date_0x0F,
            date_0x17, date_0x08, date_0x0E, date_0x12, date_0x18, date_0x1E]
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
    rpm_lists.append(int(float(date_0x06)))


# fig, ax = plt.subplots()
# ax.plot(time_lists, rpm_lists, linewidth=5)
# ax.set_title("", fontsize=12)
# ax.set_xlabel("Time", fontsize=12)
# ax.set_ylabel("RPM", fontsize=12)
# plt.show()
# time.sleep(1)

title = "踏频"
labels = {'x': 'Time', 'y': 'RPM'}
fig1 = px.line(x=time_lists, y=rpm_lists, title=title, labels=labels)
fig1.write_html('S28.html')
fig1.show()
