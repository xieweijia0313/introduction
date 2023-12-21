from pathlib import Path

file_path = Path("S28_data.txt")
# 打开文件，逐行读取，组成一个列表
content = file_path.read_text().rstrip().splitlines()
# 将每行转成一个列表，并用-分割元素
for con in content:
    contents = con.split('-')
    # 每一个字节位，代表的数据
    date_dicts = {
        "设备状态0x01": 3, "设备模式0x02": 5, "瞬时速度0x03": 7, "瞬时踏频0x06": 10, "平均踏频0x0C": 13,
        "总距离0x0F": 16, "阻力等级0x17": 21, "瞬时功率0x08": 24, "平均功率0x0E": 27, "总消耗卡路里0x12": 30,
        "坡度值0x18": 33, "运动时间0x1E": 36
    }
    # 逐行将列表中的数据取出，并转成十进制
    date_0x01 = int(contents[4], 16)
    date_0x02 = int(contents[6], 16)
    date_0x03 = f"{contents[9] + contents[8]}, {int(contents[9] + contents[8], 16) * 0.01} km"
    date_0x06 = f"{int(contents[12] + contents[11], 16) * 0.5} RPM/min"
    date_0x0C = int(contents[15] + contents[14], 16) * 0.5
    date_0x0F = f"{int(contents[20] + contents[19] + contents[18] + contents[17], 16)} M"
    date_0x17 = f"{int(int(contents[23] + contents[22], 16) * 0.1)}"
    date_0x08 = f"{int(contents[26] + contents[25], 16)} W"
    date_0x0E = int(contents[29] + contents[28], 16)
    date_0x12 = f"{int(contents[32] + contents[31], 16)} kcal"
    date_0x18 = int(contents[35] + contents[34], 16)
    date_0x1E = f"{int(contents[38] + contents[37], 16)} s"
    date_dict_keys = list(date_dicts.keys())
    date = [date_0x01, date_0x02, date_0x03, date_0x06, date_0x0C, date_0x0F,
            date_0x17, date_0x08, date_0x0E, date_0x12, date_0x18, date_0x1E]
    i = 0
    for date_dict_key in date_dict_keys:
        print(date_dict_key, date[i])
        i += 1
    print()
