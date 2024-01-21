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

'''
脚本概述：
    实现功能：
        1、实现MERIT超燃脂 自动连接设备
        2、自动调节阻力循环测试
'''

num = 10               #循环次数
Manufacturer = "Merach"
# Manufacturer = "MRK"



# Bl_de = "Merach-Swan-75"  #14
# Bl_de = "MRK-K60-C523"
# Bl_de = "Merach-MR581-E7"
Bl_de = "MRK-K60-A800"

# Model = "K60"
# Model = "MR581"
# Model = "Swan"
Model = "K60"

# Bl_de = "MRK-K60-C523"      #12

#使用wifi连接时，填写设备ID;使用数据线连接时，注释掉
# os.system('adb connect 192.168.160.112')

#初始化Appium 参数配置
des = {
    "platformName": "Android",  # 被测手机是安卓
    "platformVersion": "10",  # 手机安卓版本
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
driver.implicitly_wait(2) # 设置缺省等待时间
time.sleep(5)

'''日志模块'''
level_relations = { # 日志级别关系映射
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warning': logging.WARNING,
    'error': logging.ERROR,
    'crit': logging.CRITICAL
}
def _get_logger(filename, level='info'):
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
    # 日志文件按天进行保存，每天一个日志文件
    file_handler = handlers.TimedRotatingFileHandler(filename=filename, when='D', backupCount=1, encoding='utf-8')
    # 按照大小自动分割日志文件，一旦达到指定的大小重新生成文件
    # file_handler = handlers.RotatingFileHandler(filename=filename, maxBytes=1*1024*1024*1024, backupCount=1, encoding='utf-8')
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

'''APP模块''' #开始搜索蓝牙广播
def Scan_start():
    try:
        #判断当前刷新状态
        code = 'no.nordicsemi.android.mcp:id/action_scan_stop'
        WebDriverWait(driver, 2).until(EC.presence_of_element_located((AppiumBy.ID, code)))
    #scan_start当前未搜索蓝牙广播
    except:
        logger.info('没有找到scan_stop')
        try:
            code2='no.nordicsemi.android.mcp:id/action_scan_start'
            WebDriverWait(driver, 2).until(EC.presence_of_element_located((AppiumBy.ID, code2)))
        except:
            logger.info('没有找到scan_start')
            sys.exit()
        else:
            driver.find_element(AppiumBy.ID, code2).click()
            print('正在搜索蓝牙广播中...')
    #scan_stop当前正在搜索蓝牙广播
    else:
        print('正在搜索蓝牙广播中...')

#定向搜索蓝牙设备
def Sel_Bl_dev():
    try:
        code = 'no.nordicsemi.android.mcp:id/filter_header'
        driver.find_element(AppiumBy.ID,code).click() #点击搜索框，打开搜索页面
        code = 'new UiSelector().className("android.widget.EditText").index(1)'
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,code).clear().send_keys(Bl_de)
        code = 'no.nordicsemi.android.mcp:id/filter_header'
        driver.find_element(AppiumBy.ID, code).click()  #点击搜索框，关闭搜索页面，开始搜索
    except:
        logger.info('定向搜索蓝牙广播出错了。')
        sys.exit()
    else:
        print('定向搜索指定蓝牙广播%s中' %Bl_de)

#连接设备
def Con_Bl_dev():
    try:
        code = 'new UiSelector().text("CONNECT")'
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,code).click()
    except:
        logger.info('蓝牙连接失败了')
        sys.exit()

#获取全部设备数据
def Get_Data():
    try:
        code = 'new UiSelector().resourceId("no.nordicsemi.android.mcp:id/action_more")'
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, code))).click()
        # driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,code).click()
        code = 'new UiSelector().text("Read characteristics")'
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code).click()
    except:
        logger.info('获取全部数据失败了')
        sys.exit()

#展开/关闭0x1800,Generic Access数据
def Expansion_Generic_Access():
    try:  #展开Generic Access窗口
        code = 'new UiSelector().text("Generic Access")'
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code).click()
    except:
        logger.info('展开/关闭0x1800,Generic Access 出错了')
        sys.exit()

#获取0x2A00,Device Name是Value: 开头的数据
def Get_Device_Name():
    try:
        code = 'new UiSelector().textContains("Value: M")'
        Device_Name = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code).get_attribute("text")
    except:
        logger.info('获取0x2A00,Device Name数据出错了')
    else:
        # print(len(Bl_de))
        if len(Bl_de) == 15: #获取到的数据处理分析
            Device_Name = Device_Name[7:22]
            Device_Name.replace('\t', '')
        elif len(Bl_de) == 14: #获取到的数据处理分析
            Device_Name = Device_Name[7:21]
            Device_Name.replace('\t', '')
        elif len(Bl_de) == 12:
            Device_Name = Device_Name[7:19]
            Device_Name.replace('\t', '')
        else:
            Device_Name = Device_Name[7:20]
            Device_Name.replace('\t', '')

        if Device_Name == Bl_de:  #判断Device_Name是否通过
           logger.info('Device_Name: ' + Device_Name + ' Pass') #测试通过
        else:
           logger.info('Device_Name: ' + Device_Name + ' Fail') #测试失败
    finally: #关闭Generic Access窗口
        code = 'new UiSelector().text("Generic Access")'
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code).click()

#展开0x180A,Device Information数据
def Expansion_Device_Information():
    try:
        time.sleep(2)
        code = 'new UiSelector().text("Device Information")'
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code).click()
    except:
        logger.info('展开/关闭0x180A,Device Information 出错了')
        sys.exit()
    time.sleep(2)
    swipeDown(driver, t=2000)
    time.sleep(1)
    # swipeUp(driver, t=1000)


# Manufacture_Name_String厂家名称
def Get_Manufacture_Name_String():
    try:
        # code = 'new UiSelector().textContains("Value: M")'
        code = 'new UiSelector().resourceId("no.nordicsemi.android.mcp:id/value").index(1).instance(0)'
        Device_Name = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code).get_attribute("text")
    except:
        logger.info('获取0x2A29 Manufacture Name String 数据出错了')
        sys.exit()
    else:
        if len(Manufacturer) == 6: #获取到的数据处理分析
            Device_Name = Device_Name[7:13]
            Device_Name.replace('\t', '')
        elif len(Manufacturer) == 3:
            Device_Name = Device_Name[7:10]
            Device_Name.replace('\t', '')
        else:
            Device_Name = Device_Name[7:20]
            Device_Name.replace('\t', '')

        if Device_Name == Manufacturer:  #判断Device_Name是否通过
           logger.info('Device_Information: ' + Device_Name + ' Pass') #测试通过
        else:
           logger.info('Device_Information: ' + Device_Name + ' Fail') #测试失败

# Model_Number_String 模块编号
def Get_Model_Number_String():
    try:
        code = 'new UiSelector().resourceId("no.nordicsemi.android.mcp:id/value").index(1).instance(1)'
        Device_Name = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code).get_attribute("text")
    except:
        logger.info('获取0x2A24 Model Number String 数据出错了')
        sys.exit()
    else:
        if len(Model) == 5: #获取到的数据处理分析
            Device_Name = Device_Name[7:12]
            Device_Name.replace('\t', '')
        elif len(Model) == 4: #获取到的数据处理分析
            Device_Name = Device_Name[7:11]
            Device_Name.replace('\t', '')
        elif len(Model) == 3:
            Device_Name = Device_Name[7:10]
            Device_Name.replace('\t', '')
        else:
            Device_Name = Device_Name[7:20]
            Device_Name.replace('\t', '')
        if Device_Name == Model:  #判断Device_Name是否通过
           logger.info('Model_Number_String: ' + Device_Name + ' Pass') #测试通过
        else:
           logger.info('Model_Number_String: ' + Device_Name + ' Fail') #测试失败

# Serial_Number_String 序列号
def Get_Serial_Number_String():
    try:
        code = 'new UiSelector().resourceId("no.nordicsemi.android.mcp:id/value").index(1).instance(2)'
        Device_Name = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code).get_attribute("text")
    except:
        logger.info('获取0x2A25 Serial_Number_String 数据出错了')
        sys.exit()
    else:
        Device_Name = Device_Name[7:19]
        Device_Name.replace('\t', '')
        logger.info('Serial_Number_String: ' + Device_Name) #记录序列号

# Model_Number_String硬件版本
def Get_Hardware_Revision_String():
    try:
        code = 'new UiSelector().resourceId("no.nordicsemi.android.mcp:id/value").index(1).instance(3)'
        Device_Name = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code).get_attribute("text")
        # print(len(Device_Name),Device_Name)
    except:
        logger.info('获取0x2A26 Hardware_Revision_String 数据出错了')
        sys.exit()
    else:
        if len(Device_Name)==14: #自研
            Device_Name = Device_Name[7:13].replace('\t','')
            logger.info('Hardware_Revision_String: ' + Device_Name)  # 记录硬件版本号
        else:  #智健
            Device_Name = Device_Name[7:10]
            Device_Name.replace('\t', '')
            logger.info('Hardware_Revision_String: ' + Device_Name) #记录硬件版本号

# Firmware_Revision_String 固件版本
def Get_Firmware_Revision_String():
    try:
        code = 'new UiSelector().resourceId("no.nordicsemi.android.mcp:id/value").index(1).instance(4)'
        Device_Name = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code).get_attribute("text")
    except:
        logger.info('获取0x2A26 Firmware_Revision_String 数据出错了')
        sys.exit()
    else:
        if len(Device_Name) == 15: #自研
            Device_Name = Device_Name[7:14].replace('\t', '')
            logger.info('Firmware_Revision_String: ' + Device_Name)  # 记录固件版本号
        elif len(Device_Name)==14: #智健
            Device_Name = Device_Name[7:13].replace('\t','')
            logger.info('Firmware_Revision_String: ' + Device_Name)  # 记录固件版本号
        else:
            Device_Name = Device_Name[7:20]
            Device_Name.replace('\t', '')
            logger.info('Firmware_Revision_String: ' + Device_Name) #记录固件版本号

def Get_Softmware_Revision_String():
    try:
        code = 'new UiSelector().resourceId("no.nordicsemi.android.mcp:id/value").index(1).instance(5)'
        Device_Name = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code).get_attribute("text")
        # print(len(Device_Name))
    except:
        logger.info('获取0x2A26 Softmware_Revision_String 数据出错了')
        sys.exit()
    else:
        if len(Device_Name) == 15: #自研
            Device_Name = Device_Name[7:14]
            Device_Name.replace('\t', '')
            logger.info('Softmware_Revision_String: ' + Device_Name)  # 记录固件版本号

        elif len(Device_Name) == 14:  #智健
            Device_Name = Device_Name[7:13]
            Device_Name.replace('\t', '')
            logger.info('Softmware_Revision_String: ' + Device_Name) #记录固件版本号
        else:
            Device_Name = Device_Name[7:20].replace('\t','')
            logger.info('Softmware_Revision_String: ' + Device_Name) #记录固件版本号

def Get_System_ID():
    swipeUp(driver, t=2000)
    code = 'new UiSelector().resourceId("no.nordicsemi.android.mcp:id/value").index(1).instance(2)'
    System_ID = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code).get_attribute("text")
    System_ID = System_ID[7:].replace('\t', '')
    logger.info('System_ID: ' + System_ID)  # 记录固件版本号

if __name__ == "__main__":
    # 明确指定日志输出的文件路径和日志级别
    logger = _get_logger(R'E:\logger\test.log', 'info')
    Scan_start()
    time.sleep(2)
    Sel_Bl_dev()
    Con_Bl_dev()
    time.sleep(5)
    Get_Data()
    time.sleep(5)
    Expansion_Generic_Access()
    time.sleep(1)
    Get_Device_Name()
    time.sleep(1)
    Expansion_Device_Information()
    time.sleep(1)
    Get_Manufacture_Name_String()
    Get_Model_Number_String()
    Get_Serial_Number_String()
    Get_Hardware_Revision_String()
    Get_Firmware_Revision_String()
    Get_Softmware_Revision_String()
    Get_System_ID()

    # time.sleep(5)
    # driver.quit()

'''Value: Merach              
Value: Swan                
Value: 4475E23C4475 
Value: 1.0 
Value: 3.4.2 '''

code = 'new UiSelector().resourceId("no.nordicsemi.android.mcp:id/value").index(1).instance(2)'
els = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code).get_attribute("text")

# for el in els:
#     print(el.get_attribute("text"))
#
#     # driver.quit()



# for i in range(0,num):
#     start = timeit.default_timer()
#     time.sleep(1)
#     end = timeit.default_timer()
#     logger.info('Running time: %s Seconds' % (end - start))
#     logger.info('第%s次测试完成' % (i + 1))
#     time.sleep(5)

