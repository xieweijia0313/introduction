from pathlib import Path
import plotly.express as px


class DataConversion:
    """解析数据的类"""

    def __init__(self, file_path):
        self.file_path = file_path
        self.anal_path = '解码数据.txt'
        self.I_data, self.I_UTC_8 = [], []  # I_data瞬时数据，I_UTC_8系统时间
        self.CUM_data, self.CUM_UTC_8 = [], []  # CUM_data累计数据， CUM_UTC_8系统时间
        # 瞬时数据
        self.instantaneous_speeds, self.resistance_levels, self.step_per_minutes = [], [], []
        # 累计数据
        self.elapsed_times, self.total_distances, self.total_energys, self.stride_counts = [], [], [], []

    def run_data(self):
        """主程序"""
        self._up_data_16()
        self._anal_data_10()
        self.data_visualisation_entity()

    def _up_data_16(self):
        """提取原始数据"""
        data_up_path = Path(self.file_path)
        # 逐行读取，放到列表中
        content = data_up_path.read_text().splitlines()

        # 提取有效数据到列表
        for i in content:
            if i.startswith("I"):
                i = i.split()
                # print(i)  # 打印瞬时+累计数据
                # 提取瞬时数据
                if not i[-1].find('02-42'):
                    self.I_data.append(i[-1])
                    self.I_UTC_8.append(i[1])
                # 提取累计数据
                else:
                    self.CUM_data.append(i[-1])
                    self.CUM_UTC_8.append(i[1])

    def _anal_data_10(self):
        # "瞬时速度instantaneous_speed": [3, 4], "当前阻力resistance_level": [5],  "瞬时踏频step_per_minute": [6, 7]
        anal_data_path = Path(self.anal_path)
        anal_data_path.write_text('')

        for i in self.I_data:
            i = i.split('-')
            # print(i)  # 打印原始瞬时数据
            instantaneous_speed = int(i[4] + i[3], 16) / 100
            resistance_level = int(int(i[5], 16) / 10)
            step_per_minute = int(i[7] + i[6], 16)
            self.instantaneous_speeds.append(instantaneous_speed)
            self.resistance_levels.append(resistance_level)
            self.step_per_minutes.append(step_per_minute)

            with anal_data_path.open('a') as file_obj:
                file_obj.write(f'瞬时踏频:{step_per_minute}\n')

        # print(self.instantaneous_speeds)  # 打印瞬时速度
        # print(self.resistance_levels)  # 打印瞬时速度
        print(self.step_per_minutes)  # 打印瞬时踏频

        # date_dicts = {
        #     "运行时间elapsed_time": [3, 4],
        #     "距离total_distance": [5, 6],
        #     "卡路里total_energy": [7, 8],
        #     "计数stride_count": [9, 10]
        # }
        for cum in self.CUM_data:
            cum = cum.split('-')
            # print(cum)  # 打印原始累计数据
            elapsed_time = int(cum[4] + cum[3], 16)
            total_distance = int(cum[6] + cum[5], 16)
            total_energy = int(cum[8] + cum[7], 16)
            stride_count = int(cum[10] + cum[9], 16)
            self.elapsed_times.append(elapsed_time), self.total_distances.append(total_distance), \
                self.total_energys.append(total_energy), self.stride_counts.append(stride_count)
            with anal_data_path.open('a') as file_obj:
                file_obj.write(f'运行时间:{elapsed_time}, 距离:{total_distance}, '
                               f'卡路里:{total_energy}, 计数:{stride_count}\n')
            print(f'运行时间:{elapsed_time}, 距离:{total_distance}, 卡路里:{total_energy}, 计数:{stride_count}\n')
        # print(self.I_UTC_8)

    def _anal_data_write_file(self):
        pass

    def data_visualisation_entity(self):
        """数据可视化"""
        title = "踏频"
        labels = {'x': 'Time', 'y': ''}
        fig1 = px.line(x=self.I_UTC_8, y=self.step_per_minutes, title=title, labels=labels)
        fig1.show()


if __name__ == "__main__":
    path = '原始数据.txt'
    data = DataConversion(path)
    data.run_data()
