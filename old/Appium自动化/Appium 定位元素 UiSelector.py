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

'''---------------------------------------通过 UiSelector 这个类里面的方法实现元素定位---------------------------------------------'''
'''固定写法：driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,"new UiSelector().方法("value")")'''
'''https://developer.android.google.cn/reference/androidx/test/uiautomator/UiSelector#public-constructors
    .index(3)       #元素index索引
    .text("健康管理") #text
    .resourceId     #resource-id
    .className      #class
    .childSelector  #父元素的子元素  
    .instance(0)    #排在第一个的控件
    
'''

code = 'new UiSelector().resourceId("com.huawei.health:id/hw_main_tabs").childSelector(new UiSelector().className("android.widget.LinearLayout").index(3))'
els=driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code)
print(els.get_attribute("text"))
l = []
print(l)
l.append(els.get_attribute("text"))
print(l)


'''----------------------------------------------------------------------------------------------------------------'''
# 1.className定位
# UISelector.className方法：通过ClassName找到所有的TextView控件，然后再在这些TextView控件查找text是”Add note“的控件
#driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.widget.TextView").text("重置")')
# els=driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.widget.TextView").text("健康管理")')
'''--------------------------------------------------------------------------------------------------------------'''
# # UISelector.classNameMatches方法：通过正则表达式判断className是否和预期的一致
# driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().classNameMatches(".*TextView$")')


# # 2.通过文本信息来定位：
# # UISelector.text方法 ：通过直接查找当前界面上所有的控件来比较每个控件的text属性是否如预期值来定位控件
# driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("重置")')
# el =driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("健康管理")')
# print('1',el.get_attribute("text"))
'''----------------------------------------------------------------------------------------------'''
# # ，跟以上方法类似，但是不需要输入控件的全部text信息，如例子，只要写“重”或“置”即可。
# driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().textContains("重")')
# driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,new UiSelector().textContains("健"))
# print('2',el.get_attribute("text"))
'''-----------------------------------------------------------------------------------------------'''
# # UISelector.textStartsWith方法 通过判断一个控件的text的开始是否和预期的字串相吻合来获得控件
# driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().textStartsWith("重置")')
# el= driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,new Uiselector().textStartsWith("健"))
# print('3',el.get_attribute("text"))
'''-----------------------------------------------------------------------------------------------'''
# # UISelector.textMatches方法 通过正则表达式的方式来比较控件的text来定位控件
# # driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().textMatches("^重.*")')
# el=driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().textMatches("^健.*")')
# print('4',el.get_attribute("text"))



# # 3.通过控件ID定位。
# # UiSelector.resourceId方法
# elss = driver.find_elements(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.huawei.health:id/item_function_menu_title")')

# # UiSelector.resourceIdMatches方法
# driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceIdMatches(".+id/title")')

'''--------------------------------------------------------------------------------------------------------------'''
# # 4.通过控件contentDescription定位。即是 content'desc ：contentDescription 一直是强调开发人员需要添加进去的
# # UiSelector.description方法
# driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().description("lmappDesc")')
# # UiSelector.descriptionContains方法
# driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().descriptionContains("lmapp")')
# # UiSelector.descriptionStartWith方法
# driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().descriptionStartsWith("lmapp")')
# # UiSelector.descriptionMatches方法
# driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().descriptionMatches("^lmapp.*$")')
'''-----------------------------------------------------------------------------------------------------------------'''

# # 5.1滑动屏幕查找 适用于 ANDROID 本身的滑动 存在滚动条的滑动，那么不显示滚动条执行报错!
# e = 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).'+'scrollIntoView(new UiSelector().text("Popup Menu").instance(0));'
# driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,e).click()
#
# # 5.2滑动屏幕查找：
# ele = 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().description("活动中心").instance(0));'
# driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, ele).click()
#
# # 6.组合应用
# driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("重置").resourceId("com.android.settings:id/title")')

# for el in els:
#   print(el.get_attribute("className"))
