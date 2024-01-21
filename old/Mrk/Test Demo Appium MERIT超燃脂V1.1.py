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


num = 100               #循环次数'''
'''脚本概述：
    实现功能：
        1、实现MERIT超燃脂 自动连接设备
        2、自动调节阻力循环测试
'''

levadd = 16            #最大阻力
levsub = 1             #最小阻力
flaglevel = False       #当flaglevel为True时，无限循环阻力levadd~levsub
# os.system('adb connect 192.168.160.16')

#初始化Appium 参数配置
des = {
    "platformName": "Android",  # 被测手机是安卓
    "platformVersion": "12",  # 手机安卓版本
    "deviceName": '192.168.10.97:5555',  # 设备名，安卓手机可以随意填写，IOS根据具体手机填写
    "appPackage": "uni.UNIE7FC6F0",  # 启动APP Package名称,cmd命令【no.nordicsemi.android.mcp】
    "appActivity": ".view.logo.SplashActivity",  # 启动APP Activity名称,cmd命令【adb shell dumpsys activity recents | find “intent={”】
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

'''APP控制模块'''
def DdviceModule():  #切到设备界面
    try:
        # code = 'new UiSelector().resourceId("uni.UNIE7FC6F0:id/tvManageTitle")'
        # el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code)
        driver.find_element(AppiumBy.ID,"uni.UNIE7FC6F0:id/ivFatBurner").click()
        time.sleep(1)
        driver.find_element(AppiumBy.ID, "uni.UNIE7FC6F0:id/tv_continue").click()
    except:
        logger.info('Not Location DdviceModule 404')
        sys.exit() #结束python脚本

def ConnectDevice(): #连接设备
    try:
        code = 'new UiSelector().resourceId("uni.UNIE7FC6F0:id/tvStart")'
        el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,code)
    except:
        logger.info('Connect Failed 404')
        sys.exit()
    else:
        el.click()

def Start(): #开始运动
    try:
        el = driver.find_element(AppiumBy.ID, "uni.UNIE7FC6F0:id/ivFatBurner")
    except:
        logger.info('Start Failed 404')
        sys.exit()
    else:
        el.click()

def Stop():  #结束运动
    try:
        driver.find_element(AppiumBy.ID,'uni.UNIE7FC6F0:id/tvEnd').click()
    except:
        logger.info('not find stop')
        sys.exit()
    try:  #确认结束训练弹框
        code = 'new UiSelector().text("确定结束训练吗?")'
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code)
    except:
        logger.info('没有找到"确定结束训练"弹框')
        sys.exit()
    else:
        code = 'new UiSelector().text("确定")'
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code).click()

def OutFitrep():  #退出结算报告
    try:
        driver.find_element(AppiumBy.ID, "uni.UNIE7FC6F0:id/delete_iv").click()
        time.sleep(2)
    except:
        print('退出结算报告出错')
        sys.exit()

def levelAdd():  #增加阻力
    for i in range(1, levadd):
        TouchAction(driver).press(x=943, y=1400).release().perform()
        logger.info('阻力%s' % (i+1))
        time.sleep(1)

def levelSub(): #减小阻力
    levsubs = int(levadd)-int(levsub)+1
    for i in range(1, levsubs):
        TouchAction(driver).press(x=136, y=1400).release().perform()
        logger.info('阻力%s' % (levadd-i))
        time.sleep(1)

def level():
    while flaglevel == True:
        levelAdd()
        time.sleep(2)
        levelSub()
    else:
        levelAdd()
        time.sleep(2)
        levelSub()

def tvSubmit(): #跳过点亮新勋章
    flag = True  # 标志位
    while flag == True:
        try:
            code = 'new UiSelector().text("开心收下")'
            el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code)
        except:
            flag = False
        else:
            el.click()
            continue
    pass

if __name__ == "__main__":
    # 明确指定日志输出的文件路径和日志级别
    logger = _get_logger(R'E:\logger\test.log', 'info')
    DdviceModule()   #切到设备界面
    ConnectDevice() #连接设备

for i in range(0,num):
    start = timeit.default_timer()
    Start()      #开始运动
    time.sleep(5)
    level()      #阻力调节
    Stop()       #结束运动
    tvSubmit()   #勋章弹框跳过
    OutFitrep()  #退出结算报告
    end = timeit.default_timer()
    logger.info('Running time: %s Seconds' % (end - start))
    logger.info('第%s次测试完成' % (i + 1))
    time.sleep(5)

