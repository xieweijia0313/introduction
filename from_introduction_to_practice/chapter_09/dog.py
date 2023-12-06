class Dog:
    """一次模拟小狗的简单尝试"""

    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗收到命令时坐下"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """模拟小狗收到命令时打滚"""
        print(f"{self.name} rolled over!")


my_dog = Dog("Willie", 6)
you_dog = Dog("luck", 3)

print(f"my_dog's name is {my_dog.name}")
print(f"my_dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()

print(f"my_dog's name is {you_dog.name}")
print(f"my_dog is {you_dog.age} years old.")
you_dog.sit()
you_dog.roll_over()
