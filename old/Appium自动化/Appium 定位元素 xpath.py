#coding:utf-8
#-*- coding: utf-8 -*-
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
import time
from appium.webdriver.common.touch_action import TouchAction

des = {
  "platformName": "Android", #被测手机是安卓
  "platformVersion": "10", #手机安卓版本
  "deviceName": '192.168.10.97:5555',  # 设备名，安卓手机可以随意填写，IOS根据具体手机填写
  #com.huawei.health，no.nordicsemi.android.mcp,uni.UNIE7FC6F0
  "appPackage": "com.huawei.health",  # 启动APP Package名称,cmd命令【no.nordicsemi.android.mcp】
#.MainActivity，.DeviceListActivity,.view.logo.SplashActivity
  "appActivity": ".MainActivity", # 启动APP Activity名称,cmd命令【adb shell dumpsys activity recents | find “intent={”】
  "unicodeKeyboard": True,  #使用自带输入法，输入中文时填True
  "resetKeyboard": False,   #程序执行完毕恢复原来输入法,默认为Unicode IME
  "noReset": True,   #不要重置app
  "newCommandTimeout": "9000",  #应用的最大超时响应时间
  "automationName" : "UiAutomator1",   # 使用的自动化引擎的名称
  "skipServerInstallation": True  #解决uiautomator2重复安装问题，需已安装uiautomator2包
    }

# 连接Appium Server，初始化自动化环境
driver = webdriver.Remote('http://localhost:4723/wd/hub', des)
# 设置缺省等待时间
driver.implicitly_wait(5)
time.sleep(8)

'''----------------------------------------通过xpath定位------------------------------------------------'''
'''方法：find_element_by_xpath(xpath_value) # xpath_value:为可以定位到元素的xpath语句
android端xptah常用属性定位
      1. id ://*[contains(@resource-id,'com.android.settings:id/search')] 
      2. class ://*[contains(@class,'android.widget.ImageButton')]
      3. text ://*[contains(@text,'WLA')]
模糊定位 contains(@key,value): value可以是部分值
'''

# 根据id属性定位
# 表达式：//*[@resource-id='id属性']
# els = driver.find_elements(AppiumBy.XPATH, "//*[@resource-id='com.huawei.health:id/hw_main_tabs']")
# for el in els:
#   print(el.get_attribute("resourceId"))
# print('-------------------------------')

# 根据text属性定位
# 表达式：//*[@text='text文本属性']
# els=driver.find_elements(AppiumBy.XPATH, "//*[@text='健康管理']")
# for el in els:
#   print(el.get_attribute("text"))
# print('-------------------------------')
'''-------------------------------------------------------------------------------------'''
# 根据class属性定位
# 表达式： //*[@class='class属性']
# els =driver.find_elements(AppiumBy.XPATH, "//*[@class='android.widget.LinearLayout']")
# for el in els:
#   print(el.get_attribute("className"))
'''--------------------------------------------------------------------------------'''
# 通过content-desc属性定位
# 表达式： //*[@content-desc='文本']

# driver.find_element(AppiumBy.XPATH, "//*[@content-desc='xxxx']")

