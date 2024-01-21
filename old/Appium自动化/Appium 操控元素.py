#coding:utf-8
#-*- coding: utf-8 -*-
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
import time
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.mobileby import MobileBy

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
# 设置缺省等待时间,在启动后到启动结束所有进程都保持5S处理
driver.implicitly_wait(5)
time.sleep(8)


# 第三种：显形等待
# 明确等待某个条件的满足之后，再去执行下一步的操作。
# 程序每隔XX秒看一眼，如果条件成立了，则执行下一步，否则继续等待，直到超过设置最长时间，然后抛出TimeoutException。

# 使用之前，引入相关的库




code = 'new UiSelector().resourceId("com.huawei.health:id/hw_main_tabs").childSelector(new UiSelector().className("android.widget.LinearLayout").index(3))'
el=driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code)

# 设置显性等待 WebDriverWait(driver,等待时常：10S，轮询周期:默认值0.5S).until()/until_not():条件成立/直到条件不成立
# 条件 (元素定位为的类型，元素定位的表达式)
WebDriverWait(driver, 2).until(EC.presence_of_element_located((AppiumBy.CLASS_NAME, 'android.widget.LinearLayout')))



'''TouchAction(driver)
TouchAction对象包含（tab）、press（短按）、move_to（滑动到某个坐标）等方法
通过TouchAction对象，添加tap、move_to等操作，然后perform()执行，可以实现解锁屏幕等功能
规范中的可用事件有：

短按 (press)
释放 (release)
移动到 (moveTo)
点击 (tap)
等待 (wait)
长按 (longPress)
取消 (cancel)
执行 (perform)
'''



'''-----------------------1.点击屏幕操作click()方法------------------------------------------------------------'''
# el.click()

'''-----------------------2.手指轻敲屏幕操作tap()方法------------------------------------------------------------'''
'''tap(element,x,y)可以通过元素定位的方式敲击，也可以通过元素坐标的方式'''
# 通过元素定位方式敲击屏幕,driver.tap(el, 持续点击时间/s)
TouchAction(driver).tap(el,count=1).perform()
#perform()方法发送命令到服务器执行操作
'''--------------------------------------------------------------------------------'''
# 通过坐标方式敲击屏幕，元素坐标:x=760,y=2206
# A.点击(轻敲)操作：driver.tap(坐标x，坐标y, 持续点击时间/s)
# TouchAction(driver).tap(x=760,y=2206,count=1).perform()
'''--------------------------------------------------------------------------------'''


'''------------------------3.手指按下操作press()方法-----------------------------------------------------------'''
'''press(elemnet,x,y)可以通过元素定位的方式按下，也可以通过元素坐标的方式按下
  release()方法为结束动作，手指按下之后离开屏幕'''
# 通过元素定位方式按下屏幕
# TouchAction(driver).press(el).release().perform()
#通过坐标的方式，元素坐标x=760,y=2206
# TouchAction(driver).press(x=760,y=2206).release().perform()

'''---------------------------------------------------------------------------'''



'''-----------------------4.模拟手指长按操作long_press()方法-------------------------------------------'''
'''长按相对于按下来说增加了按下的时间长短，所以参数多了一个duration单位是毫秒。
  long_press(elemnet,x,y,duration)也是可以通过元素定位的方式按下，也可以通过元素坐标的方式按下。'''

# 通过元素定位方式长按元素
# TouchAction(driver).long_press(el,duration=1000).release().perform()

'''--------------------------------------------------------------------------'''
# 通过坐标方式长按元素，WiredSSID坐标:x=760,y=2206
#wait(5000)等待五秒
# 添加等待(有长按X效果)／不添加等待(无长按效果)
# TouchAction(driver).long_press(x=760, y=2206, duration=5000).release().perform()

'''--------------------------------------------------------------------------'''

'''-----------------------------------------滑动和拖拽-----------------------------------------------------------'''
# TouchAction(driver).press(x=220,y=700).move_to(x=840, y=700).move_to(x=220, y=1530).move_to(x=840, y=1530).release().perform()
# TouchAction(driver).press(x=700,y=1000).move_to(x=700, y=300).release().perform()

'''---------------------------------------------------------------------'''
# #获取屏幕大小和宽度
# size = driver.get_window_size()
# print(driver.get_window_size())

# print('width' not in size)
# print('width' in size)

# for i in size:
#   # print(i,size[i])   #width 1080
#   print(i, size.get(i))

# 返回的是：{'width': 1080, 'height': 1776}
# 利用 swipe(self, start_x, start_y, end_x, end_y, duration=0)方法：
# start_x = size['width'] * 0.9  # 宽度
# start_y = size['height'] * 0.5  # 高度
# end_x = size['width'] * 0.1
# end_y = size['height'] * 0.5

# 一个屏幕向上下左右活动的方法如下：
# # 获得屏幕大小宽和高
# def getSize(driver):
#   x = driver.get_window_size()['width']
#   y = driver.get_window_size()['height']
#   return (x, y)
# print(getSize(driver))
#
# print('向上滑动')
# # 屏幕向上滑动
# def swipeUp(driver, t=1000):
#   l = getSize(driver)
#   x1 = int(l[0] * 0.5)  # x坐标
#   y1 = int(l[1] * 0.75)  # 起始y坐标
#   y2 = int(l[1] * 0.25)  # 终点y坐标
#   driver.swipe(x1, y1, x1, y2, t)
# #
# #
# swipeUp(driver, t=1000)
#
# # 屏幕向下滑动
# def swipeDown(driver, t=1000):
#   l = getSize(driver)
#   x1 = int(l[0] * 0.5)  # x坐标
#   y1 = int(l[1] * 0.25)  # 起始y坐标
#   y2 = int(l[1] * 0.75)  # 终点y坐标
#   driver.swipe(x1, y1, x1, y2, t)
#
#
# # 屏幕向左滑动
# def swipLeft(driver, t):
#   l = getSize(driver)
#   x1 = int(l[0] * 0.75)
#   y1 = int(l[1] * 0.5)
#   x2 = int(l[0] * 0.05)
#   driver.swipe(x1, y1, x2, y1, t)
#
#
# # 屏幕向右滑动
# def swipRight(driver, t=1000):
#   l = getSize(driver)
#   x1 = int(l[0] * 0.05)
#   y1 = int(l[1] * 0.5)
#   x2 = int(l[0] * 0.75)
#   driver.swipe(x1, y1, x2, y1, t)
#
#
# 调用向下滑动的方法
# swipeDown(driver)

#打系统通知栏open_notifications
# driver.open_notifications()

# driver.get_screenshot_as_file("")

# # 1.获取手机分辨率
# window_size = driver.get_window_size()
# print(window_size)
#
# time.sleep(2)
# #2.手机截图
# driver.get_screenshot_as_file("./touch_action_unlock.png")

#3.常用的三个键值  3 Home , 4 返回键  ， 66 回车键
# driver.press_keycode(4)
# driver.press_keycode(3)
#
# #打开手机通知栏
# driver.open_notifications()
# time.sleep(3)
# # driver.press_keycode(4)
#
# # 或者：点击返回键
# driver.keyevent(4)
