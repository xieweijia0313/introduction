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

code = 'new UiSelector().resourceId("com.huawei.health:id/hw_main_tabs").childSelector(new UiSelector().className("android.widget.LinearLayout").index(3))'
els=driver.find_elements(AppiumBy.ANDROID_UIAUTOMATOR, code)


for el in els :

  '''-----------------------1.获取元素文本------------------------------------------------------------'''
  print('1.获取元素文本',el.text)

  '''-----------------------2.获取元素标签名称------------------------------------------------------------'''
  print('2.获取元素标签名称',el.tag_name)

  '''-----------------------3.获取元素属性------------------------------------------------------------'''
  # print('3.获取元素属性',el.get_attribute('content-desc'))

  '''-----------------------4.元素是否被选中------------------------------------------------------------'''
  print('4.元素是否被选中',el.is_selected())

  '''-----------------------5.元素是否被启用------------------------------------------------------------'''
  print('5.元素是否被启用',el.is_enabled())

  '''-----------------------6.获取元素位置------------------------------------------------------------'''
  print('6.获取元素位置',el.is_displayed())

  '''-----------------------7.获取元素大小------------------------------------------------------------'''
  print('7.获取元素大小',el.location)

  '''-----------------------8.获获取元素的尺寸和坐标------------------------------------------------------------'''
  print('8.获取元素的尺寸和坐标',el.size)

  '''-----------------------9.获取 Web 元素的 CSS 计算属性值------------------------------------------------------------'''
  print('9.获取 Web 元素的 CSS 计算属性值',el.rect)

  '''-----------------------10.元素是否被启用------------------------------------------------------------'''
  # print('10.元素是否被启用',el.value_of_css_property("style"))

  '''-----------------------11.获取搜索的id属性值------------------------------------------------------------'''
  print('11.获取搜索的id属性值',el.get_attribute("resourceId"))

  '''-----------------------12.获取搜索的content-desc值------------------------------------------------------------'''
  print('12.获取搜索的content-desc值',el.get_attribute("name"))

  '''-----------------------13.获取搜索的class属性值------------------------------------------------------------'''
  print('13.获取搜索的class属性值',el.get_attribute("className"))

  '''-----------------------14.获取text值'------------------------------------------------------------'''
  print('14.获取text值',el.get_attribute("text"))




