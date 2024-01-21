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
    V1.1实现功能：
        1、实现华为运动健康APP自动连接设备
        2、自动开启、结束运动。循环N次
'''

#循环次数
num = 100

#使用wifi连接时，填写设备ID;使用数据线连接时，注释掉
# os.system('adb connect 192.168.160.112')

#初始化Appium 参数配置
des = {
    "platformName": "Android",  # 被测手机是安卓
    "platformVersion": "10",  # 手机安卓版本
    "deviceName": '192.168.10.97:5555',  # 设备名，安卓手机可以随意填写，IOS根据具体手机填写
    "appPackage": "com.huawei.health",  # 启动APP Package名称,cmd命令【no.nordicsemi.android.mcp】
    "appActivity": ".MainActivity",  # 启动APP Activity名称,cmd命令【adb shell dumpsys activity recents | find “intent={”】
    # "unicodeKeyboard": True,  # 使用自带输入法，输入中文时填True
    "resetKeyboard": True,  # 程序执行完毕恢复原来输入法,默认为Unicode IME
    "noReset": True,  # 不要重置app
    "newCommandTimeout": "9000",  # 应用的最大超时响应时间
    "automationName": "UiAutomator2",  # 使用的自动化引擎的名称Uiautomator1
    "skipServerInstallation": True # 解决uiautomator2重复安装问题
}

# 连接Appium Server，初始化自动化环境
driver = webdriver.Remote('http://localhost:4723/wd/hub', des)
driver.implicitly_wait(2) # 设置缺省等待时间
time.sleep(8)


'''日志模块'''
level_relations = {    # 日志级别关系映射
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

'''APP控制模块'''
def DdviceModule(): #切到设备界面
    try:
        code = 'new UiSelector().resourceId("com.huawei.health:id/hw_main_tabs").childSelector(new UiSelector().className("android.widget.LinearLayout").index(3))'
        el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code)
    except Exception as e:
        logger.info('Not Found DdviceModule')
        sys.exit() #结束脚本
    else:
        el.click()
    # 判断是否切换成功
    # 设置显性等待 WebDriverWait(driver,等待时常：10S，轮询周期:默认值0.5S).until()/until_not():条件成立/直到条件不成立
    # 条件 (元素定位为的类型，元素定位的表达式)
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((AppiumBy.ID, 'com.huawei.health:id/device_card_list_more_add')))
    except Exception as e:
        logger.info('Not Found DdviceModule')
        sys.exit()
    else:
        logger.info('DdviceModule Succeeded')
        time.sleep(1)

def DeviceMore(): #进入设备
    try:
        code = 'new UiSelector().resourceId("com.huawei.health:id/personal_equipment_layout").instance(0)'
        el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code)
    except:
        logger.info('Not Found DeviceMore')
        sys.exit()
    else:
        el.click()
    #判断是否切换成功
    try:
        el =WebDriverWait(driver,1).until(EC.presence_of_element_located((AppiumBy.ID,'com.huawei.health:id/tv_device_start')))
    except:
        logger.info('Not Found DeviceMore')
        sys.exit()
    else:
        logger.info('DeviceMore Succeeded')

def Start(): #开始运动
    try:
        el = driver.find_element(AppiumBy.ID, "com.huawei.health:id/tv_device_start")
    except:
        logger.info('Start Sports Fail')
    else:
        el.click()

def Bluetooth(): #蓝牙配对
    time.sleep(3)
    try:
        code = 'android:id/button1'
        Butt = WebDriverWait(driver, 3).until(EC.presence_of_element_located((AppiumBy.ID, code)))
    #没有蓝牙配对请求
    except:
        logger.info('Bluetooth Connect Succeeded Alert N')
    #有蓝牙配对请求
    else:
        Butt.click()
        logger.info('Bluetooth Connect Succeeded Alert Y')

def alert():  #历史运动数据弹框检测
    try:
        time.sleep(3)
        code = 'com.huawei.health:id/dialog_one_btn'
        WebDriverWait(driver, 2).until(EC.presence_of_element_located((AppiumBy.ID, code)))  #
    except:
        logger.info("Data Alert N")
        pass
    else:
        driver.find_element(AppiumBy.ID, code).click()
        logger.info('Data alert Y')

def Stop():  #结束运动
    try:
        #1,通过ID定位。动态界面，耗时久
        # el = driver.find_element(AppiumBy.ID,'com.huawei.health:id/track_main_page_btn_stop')
        # TouchAction(driver).long_press(el, duration=1000).release().perform()
        #2,通过坐标定位
        TouchAction(driver).long_press(x=547, y=2076, duration=1000).release().perform()
    except:
        logger.info('Stop Sports Fail')
        sys.exit()

#退出结算报告
def OutFitrep():
    try:
        driver.find_element(AppiumBy.ID, "com.huawei.health:id/hwappbarpattern_cancel_icon").click()
        time.sleep(2)
    except:
        print('OutFitrep Fail')

if __name__ == "__main__":
    # 明确指定日志输出的文件路径和日志级别
    logger = _get_logger(R'E:\logger\test.log', 'info')
    DdviceModule()
    DeviceMore()

for i in range(0,num):
    start = timeit.default_timer()
    Start()
    Bluetooth()
    alert()
    time.sleep(8)
    Stop()
    OutFitrep()
    end = timeit.default_timer()
    logger.info('Running time: %s Seconds' % (end - start))
    logger.info('第%s次测试完成' % (i + 1))
    time.sleep(5)
