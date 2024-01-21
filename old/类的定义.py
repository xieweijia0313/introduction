#定义一个类
class BenCar:
    brand = '奔驰'  #类的属性
    country = '德国' #类的属性

    #以下是行为的定义
    @staticmethod  #装饰器，下面的函数是这个类静态的方法
    def pressHorn(): #自定义pressHorn，函数名称
        print('嘟嘟嘟~~~~')

    #类的实例属性（每个实例独有的属性），在类的初始化方法__init__里面定义
    def __init__(self,color,esn): #晒儿服
        self.color = color
        self.engineSN = esn

    def changeColor(self,newColor):
        self.color = newColor


'''类的继承，定义之类'''
class Benz2016(BenCar):  #Benzz2016继承父类BenCar的属性
    price = 580000       #新增类的属性
    model = 'Benz2016'   #新增类的属性

    def __init__(self,color,esn,weight):

        #先调用父类的初始化方法
        # BenCar.__init__(self,color,esn)
        super().__init__(color,esn)


        self.weight = weight  #新增实例对象
        self.oilweight = 0    #新增实例对象

    def fillOil(self,oilAdded):
        self.oilweight += oilAdded
        self.weight    += oilAdded

class Benz2018(Benz2016):
    price = 88888
    model = 'Benz2018'




car1 = Benz2016('green','sn2323432',1000) #实例化对象
car1.changeColor('black')
car1.fillOil(10)

BenCar.pressHorn() #执行静态方法

print(car1.brand)  #得到属性的值
print(car1.model)  #得到属性的值

print(car1.color)
print(car1.engineSN)

print('车的重量',car1.weight)
print('油的重量',car1.oilweight)

car2 = Benz2018('green','sn2323432',1000)
print(car2.model)
