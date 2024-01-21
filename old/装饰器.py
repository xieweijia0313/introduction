import time

# 定义一个装饰器函数
def sayLocal(func):
    def wrapper():
        curTime = func()
        return f'当地时间： {curTime}'
    return wrapper


#以 @sayLocal 开头后面接装饰器函数 的这种写法，是一种 语法糖 ，也就是便捷写法
@sayLocal  #装饰器，等价于getXXXTime = sayLocal(getXXXTime)
def getXXXTime():
    return time.strftime('%Y_%m_%d %H:%M:%S',time.localtime()) #当前时间2023_07_10 21:32:45

# 装饰 getXXXTime
# getXXXTime = sayLocal(getXXXTime)

print (getXXXTime())

print('------------------------------------------')

def sayLocal(func):
    def wrapper(*args,**kargs):
        curTime = func(*args,**kargs)
        return f'当地时间： {curTime}'
    return wrapper

@sayLocal
def getXXXTimeFormat1(name):
    curTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    return f'{curTime} ，数据采集者：{name} '

def getXXXTimeFormat2(name,place):
    curTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    return f'{curTime} ，数据采集者：{name} , 采集地：{place}'

print(getXXXTimeFormat1('张三'))
print(getXXXTimeFormat2('李四','杭州'))