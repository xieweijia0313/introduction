from random import choice


class RandomWalk:
    """一个生成随机漫步数据的类"""
    def __init__(self, num_points=5000):  # num_points书记漫步包含的默认点数
        """初始化随机漫步的属性"""
        self.num_points = num_points

        # 所有随机漫步都始于（0，0）
        self.x_values = [0]
        self.y_values = [0]
        self.x_step = ""
        self.y_step = ""

    def fill_walk(self):
        """计算随机漫步所包含的各种点"""

        # 不断漫步，直到列表达到指定的长度
        while len(self.x_values) < self.num_points:

            # 决定前进的方向以及沿这个方向前进的距离
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance
            self.x_step = x_step

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance
            self.y_step = y_step
            # 拒绝原地踏步
            if self.x_step == 0 and self.y_step == 0:
                continue
            self.get_step()

    def get_step(self):
        # 计算下一个点的x和y值
        next_x = self.x_values[-1] + int(self.x_step)
        next_y = self.y_values[-1] + int(self.y_step)
        # 将下一个点加入列表中
        self.x_values.append(next_x)
        self.y_values.append(next_y)
