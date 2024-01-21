
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


'''------------------------------------------1.根据ID，resource-id 属性---------------------------------------'''
'''id ：元素功能描述：
1、使用方法：find_element(AppiumBy.ID, ‘com.android.launcher3:id/tv_search’)
2、元素的resource-id
3、唯一标识该元素的值（id有时候并不唯一）'''
# driver.find_element(AppiumBy.ID,resource-id)

'''------------------------------------------2.根据CLASS NAME, class属性---------------------------------------'''
'''class_name ：元素功能描述
1、使用方法：find_element(AppiumBy.CLASS_NAME, ‘android.widget.TextView’)
2、该方法一般不使用，由于界面元素的class重复度太高，基本上不存在唯一值
3、元素的class属性'''
# driver.find_element(AppiumBy.CLASS_NAME,class)

'''------------------------------------------3.根据ACCESSIBILITY ID，content-desc属性-------------------------------'''
'''content-desc ：元素功能描述
1、使用方法：find_element(AppiumBy.ACCESSIBILITY_ID, ‘com.android.launcher3:id/tv_search’)
2、content-desc 属性是用来描述该元素的作用
'''
# driver.find_element(AppiumBy.ACCESSIBILITY_ID,content-desc)

#name ：元素功能描述：注释：Appium1.5及之后的版本废弃了name属性




