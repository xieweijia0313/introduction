from pathlib import Path
import plotly.express as px
import matplotlib.pyplot as plt


class DataConversion:
    """解析数据的类"""

    def __init__(self, file_path, anal_file_name):
        self.file_path = file_path
        self.anal_path = anal_file_name
        # 原始累计数据
        self.CUM_DATA_16 = []
        # 原始瞬时数据
        self.I_DATA_16 = []

        # 累计数据系统时间
        self.CUM_UTC_8 = []
        # 瞬时数据系统时间
        self.I_UTC_8 = []

        # 瞬时数据,instantaneous_speeds速度, resistance_levels阻力, step_per_minutes踏频
        self.instantaneous_speeds, self.resistance_levels, self.step_per_minutes = [], [], []
        #
        self.elapsed_times, self.total_distances, self.total_energys, self.stride_counts = [], [], [], []

        # 所有数据
        self.more_data_lists = []

    def run_data(self):
        """主程序"""
        self._up_data_16()
        self._anal_data_10()
        # self.data_visualisation_entity()
        self.data_visualisation_entity_2()


    def _up_data_16(self):
        """提取原始数据"""
        data_up_path = Path(self.file_path)
        # 逐行读取，放到列表中
        content = data_up_path.read_text().splitlines()

        # 提取有效数据到列表
        for i in content:
            if i.startswith("I	"):
                i = i.split()
                # print(i)  # 打印原始的瞬时+累计数据
                self.more_data_lists.append(str(i[-1]))
                if not i[-1].find('02-42'):
                    self.I_UTC_8.append(i[1])
                # 提取累计数据
                else:
                    self.CUM_UTC_8.append(i[1])

    def _anal_data_10(self):
        """运动数据解析"""
        # "瞬时速度instantaneous_speed": [3, 4], "当前阻力resistance_level": [5],  "瞬时踏频step_per_minute": [6, 7]
        anal_data_path = Path(self.anal_path)
        # 请空文件
        anal_data_path.write_text('')
        num = 0
        for more_data in self.more_data_lists:
            more_data = str(more_data)

            if more_data.startswith('02-42'):  # 瞬时数据

                self.I_DATA_16.append(more_data)
                i_data = more_data.split('-')
                instantaneous_speed = int(i_data[4] + i_data[3], 16) / 100
                resistance_level = int(int(i_data[5], 16) / 10)
                step_per_minute = int(i_data[7] + i_data[6], 16)
                self.instantaneous_speeds.append(instantaneous_speed)
                self.resistance_levels.append(resistance_level)
                self.step_per_minutes.append(step_per_minute)

                with anal_data_path.open('a') as file_obj:
                    file_obj.write(f'系统时间：{self.I_UTC_8[num]}, 瞬时踏频:{step_per_minute},')
                    print(f'系统时间：\n{self.I_UTC_8[num]}, 瞬时踏频:{step_per_minute}')
                for i in range(1):
                    num += 1

            elif more_data.startswith('02-43'):  # 累计数据
                self.CUM_DATA_16.append(more_data)
                cum_data = more_data.split('-')
                elapsed_time = int(cum_data[4] + cum_data[3], 16)
                total_distance = int(cum_data[6] + cum_data[5], 16)
                total_energy = int(cum_data[8] + cum_data[7], 16)
                stride_count = int(cum_data[10] + cum_data[9], 16)
                self.elapsed_times.append(elapsed_time), self.total_distances.append(total_distance),\
                    self.total_energys.append(total_energy), self.stride_counts.append(stride_count)

                with anal_data_path.open('a') as file_obj:
                    file_obj.write(f'运动时间:{elapsed_time}, 距离:{total_distance},卡路里:{total_energy}, 计数:{stride_count}\n')
                print(f'运行时间:{elapsed_time}, 距离:{total_distance},卡路里:{total_energy}, 计数:{stride_count}')

    def _anal_data_write_file(self):
        pass

    def data_visualisation_entity(self):
        """数据可视化"""
        title = ''
        labels = {'x': 'Time', 'y': ''}
        fig1 = px.line(x=self.I_UTC_8, y=self.step_per_minutes, title=title, labels=labels)
        fig1.show()

    def data_visualisation_entity_2(self):
        plt.style.use('seaborn')
        fig, ax = plt.subplots()
        ax.plot(self.I_UTC_8, self.step_per_minutes, linewidth=5)
        # ax.scatter(self.I_UTC_8, self.step_per_minutes, s=10)

        # 设置图题并给坐标轴加上标签
        ax.set_title("", fontsize=24)
        ax.set_xlabel("", fontsize=14)
        ax.set_ylabel("", fontsize=14)
        # 设置刻度标记的样式
        # ax.tick_params(labelsize=14)
        plt.show()


if __name__ == "__main__":
    path = 'S12.txt'
    # path = 'R06.txt'
    file_name = '解码_' + path
    data = DataConversion(path, file_name)
    data.run_data()

