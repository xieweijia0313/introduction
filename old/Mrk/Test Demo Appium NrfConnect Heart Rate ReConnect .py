# coding:utf-8
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
import os
import logging
from logging import handlers
import timeit
from tkinter import messagebox  #弹窗
'''
脚本概述：
    V1.0 实现功能：
        

'''
Bl_de= "hw807"
# Bl_de= input('请输入蓝牙广播名: ')


file = 'E:\logger' #日志文件保存路径

#使用wifi连接时，填写设备ID;使用数据线连接时，注释
# os.system('adb connect 192.168.160.112')

#初始化Appium 参数配置
des = {
    "platformName": "Android",  # 被测手机是安卓
    "platformVersion": "12",  # 手机安卓版本
    "deviceName": '192.168.10.97:5555',  # 设备名，安卓手机可以随意填写，IOS根据具体手机填写
    "appPackage": "no.nordicsemi.android.mcp",  # 启动APP Package名称,cmd命令【no.nordicsemi.android.mcp】
    "appActivity": ".DeviceListActivity",  # 启动APP Activity名称,cmd命令【adb shell dumpsys activity recents | find “intent={”】
    # "unicodeKeyboard":True,  # 使用自带输入法，输入中文时填True
    "resetKeyboard": True,  # 程序执行完毕恢复原来输入法,默认为Unicode IME
    "noReset": True,  # 不要重置app
    "newCommandTimeout": "9000",  # 应用的最大超时响应时间
    "automationName": "UiAutomator2",  # 使用的自动化引擎的名称
    "skipServerInstallation": True # 解决uiautomator2重复安装问题
}

# 连接Appium Server，初始化自动化环境
driver = webdriver.Remote('http://localhost:4723/wd/hub', des)
driver.implicitly_wait(5) # 设置缺省等待时间
time.sleep(5)

# 日志级别关系映射。
level_relations = {
    'debug': logging.DEBUG,    #调试 ，打印详细信息
    'info': logging.INFO,      #一般信息，打印关键信息，证明程序按预定轨迹执行。
    'warning': logging.WARNING,#警告信息，未预料到的 及可能出现问题和错误的提示信息，但是软件还是会照常运行    例如：磁盘空间不足。
    'error': logging.ERROR,    #程序出现错误，可能会波及一些功能的使用
    'crit': logging.CRITICAL   #严重错误，软件不能正常执行
}

#打印以及保存日志
def _get_logger(path,filename, level='info' ):
    #检查创建日志文件夹
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)

    # 创建日志对象
    log = logging.getLogger(filename)
    # 设置日志级别
    log.setLevel(level_relations.get(level))
    # 日志输出格式
    fmt = logging.Formatter('%(asctime)s %(thread)d %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
    # 输出到控制台
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(fmt)

    # 输出到文件
    # 文件保存方式一,日志文件按天进行保存，每天一个日志文件
    file_handler = handlers.TimedRotatingFileHandler(filename=filename, when='D', backupCount=1, encoding='utf-8')
    # 文件保存方式二,按照大小自动分割日志文件，一旦达到指定的大小重新生成文件,maxBytes=1*1024*1024*1024 单个文件上限1G
    # file_handler = handlers.RotatingFileHandler(filename=filename, maxBytes=1*1024*1024*1024, backupCount=2, encoding='utf-8')

    file_handler.setFormatter(fmt)
    log.addHandler(console_handler)
    log.addHandler(file_handler)
    return log



'''手机操作模块'''
#获得屏幕大小宽和高
def getSize(driver):
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)  #返回一个元组（）

#屏幕向下滑动
def swipeDown(driver,t=2000):
    l = getSize(driver)
    # print(l)
    x1 = int(l[0] * 0.5)    #x坐标
    y1 = int(l[1] * 0.38)   #起始y坐标
    y2 = int(l[1] * 0.58)   #终点y坐标
    driver.swipe(x1, y1, x1, y2,t)

#屏幕向上滑动
def swipeUp(driver, t=2000):
    l = getSize(driver)
    # print(l)
    x1 = int(l[0] * 0.5)  # x坐标 856.1095
    y1 = int(l[1] * 0.98)  # 起始y坐标
    y2 = int(l[1] * 0.38)  # 终点y坐标
    driver.swipe(x1, y1, x1, y2, t)


'''APP模块'''
def Search_for_Bluetooth_radio(): #搜索蓝牙信号
    try:
        #检查当前是否在检测蓝牙信号
        code = 'no.nordicsemi.android.mcp:id/action_scan_stop'  #判断是否在检测中
        WebDriverWait(driver, 2).until(EC.presence_of_element_located((AppiumBy.ID, code)))

    except: #未在检测蓝牙广播，进行如下操作，开启检测
        logger.info('蓝牙初始化成功，当前未在搜索蓝牙广播')
        try:
            code2='no.nordicsemi.android.mcp:id/action_scan_start'
            WebDriverWait(driver, 2).until(EC.presence_of_element_located((AppiumBy.ID, code2)))
        except:
            logger.info('蓝牙初始化成功，但是没有找到SCAN搜索按钮')
            sys.exit()
        else:
            driver.find_element(AppiumBy.ID, code2).click()
            print('蓝牙初始化成功，正在搜索蓝牙广播中...')

    else: #当前正在搜索蓝牙广播信号
        print('正在搜索蓝牙广播中...')
def Search_for_Bluetooth_radio_device():  #搜索指定蓝牙设备
    try:
        # 点击搜索框，打开搜索页面
        code = 'no.nordicsemi.android.mcp:id/filter_header'
        driver.find_element(AppiumBy.ID,code).click()

        # 输入蓝牙设备名称
        code = 'new UiSelector().className("android.widget.EditText").index(1)'
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,code).clear().send_keys(Bl_de)

        # 点击搜索框，关闭搜索页面，开始搜索
        code = 'no.nordicsemi.android.mcp:id/filter_header'
        driver.find_element(AppiumBy.ID, code).click()

    except:
        logger.info('搜索指定蓝牙，初始化失败')
        sys.exit()
    else:
        print(f'搜索指定蓝牙{Bl_de}')
def Connect_for_BLuetooth__radio_device(): #连接蓝牙设备
    try:
        #点击CONNECT按钮
        code = 'new UiSelector().text("CONNECT")'
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, code))).click()
    except:
        logger.info(f'连接{Bl_de}超时')
        sys.exit()
    else:
        try:
            code = 'new UiSelector().resourceId("no.nordicsemi.android.mcp:id/action_disconnect")'
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, code)))
        except:
            logger.info(f'连接{Bl_de}失败了')
        else:
            logger.info(f'恭喜，连接{Bl_de}成功了')
    finally:
        time.sleep(10)

def Heart_Rate(): #心率服务
    try:
        #展开心率服务
        code = 'new UiSelector().text("0x180D")'
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code).click()

    except:
        logger.info("Heart_Rate出错了")
        sys.exit()

    try:  #订阅Heart_Rate
        code = 'new UiSelector().resourceId("no.nordicsemi.android.mcp:id/action_start_notifications")'
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,code).click()
    except:
        logger.info("订阅Heart_Rated出错了")
        sys.exit()
    try: #读取Heart_Rate值
        code = 'new UiSelector().resourceId("no.nordicsemi.android.mcp:id/value").instance(0) '
        el =driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,code)
    except:
        logger.info("读取Heart_Rated出错了")
        sys.exit()
    else:
        time.sleep(3)
        return el.get_attribute("text")


def ReConnect():
        try:   #重新连接
            #断开蓝牙
            code = 'new UiSelector().resourceId("no.nordicsemi.android.mcp:id/action_disconnect")'
            driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code).click()
            logger.info("断开蓝牙")
            time.sleep(10)
            #连接蓝牙
            code = 'new UiSelector().text("CONNECT")'
            driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code).click()
            logger.info("连接蓝牙")

        except:
            logger.info("重连出错了")
            sys.exit()
        finally:
            time.sleep(8)


if __name__ == "__main__":
    # 明确指定日志输出的文件路径、日志名称、日志级别。
    logger = _get_logger(R'E:\logger', R'E:\logger\test.log', 'info')
    logger.info('日志输出测试')
    Search_for_Bluetooth_radio()
    Search_for_Bluetooth_radio_device()
    time.sleep(3)
    Connect_for_BLuetooth__radio_device()

for i in range(100):
    logger.info(f'第{i+1}次连接测试 {Heart_Rate()}')
    time.sleep(3)
    ReConnect()
    time.sleep(3)


    # driver.quit()


