from pathlib import Path


path = Path("log_2023.txt")
# 读取全部内容
contents = path.read_text()
# 按行读取并存放到一个列表中
lines = contents.splitlines()


class StatusDataProcessing:
    """这是一个处理设备状态数据的类"""

    def __init__(self, files):
        self.lines = files
        # 存放原始数据
        self.initial_datas_list = []

        # 存放处理后的数据
        self.processing_datas_list = []
        self.rpm = []

    def start(self):
        status_data_processing.initial_data()
        status_data_processing.processing_datas()



    def initial_data(self):
        """原始(0x) 02-42设备状态数据"""

        for line in self.lines:
            if "value: (0x) 02-42" in line:
                self.initial_datas_list.append(line)

    def processing_datas(self):
        """处理后的(0x) 02-42设备状态数据"""

        for initial_datas in self.initial_datas_list:
            message = initial_datas[-44:].replace('-', '')
            self.processing_datas_list.append(message)
            # 取踏频
            rpm_num = message[14:16] + message[12:14]
            status_data_processing.base_conversion(rpm_num)

    def base_conversion(self, rpm_num):
        # 踏频数据-16进制→10进制
        hex_num = f"0x{rpm_num}"
        dec_num = int(hex_num, 16)  # 16进制数
        self.rpm.append(dec_num)


status_data_processing = StatusDataProcessing(lines)
