class Car:
    """一次模拟哦汽车的简单尝试"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回格式规范的描述性"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车行驶里程的消息"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        将里程表读数设置魏指定的值
        禁止将里程表读数往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading += mileage
        else:
            print("You can't roll back an odometer！")

    def increment_odometer(self, miles):
        # 让里程读数增加相应的值
        if miles >= self.odometer_reading:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer！")


class Battery:
    """电池类"""

    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条电池容量的消息"""
        print(f"This car has a {self.battery_size} -kWh battery.")

    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65


class ElectricCar(Car):

    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)
        self.battery = Battery(65)
        self.range = 0

    def get_range(self):
        """打印电池续航里程"""
        # self.battery.upgrade_battery()
        self.battery.describe_battery()
        if self.battery.battery_size == 40:
            self.range = 150
        elif self.battery.battery_size == 65:
            self.range = 225
        print(f"This car can go about {self.range} miles on a full charge")


my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.get_range()
