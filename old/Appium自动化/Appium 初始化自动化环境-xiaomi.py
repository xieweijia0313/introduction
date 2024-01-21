#coding:utf-8
#-*- coding: utf-8 -*-
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

des = {
  "platformName": "Android", #被测手机是安卓
  "platformVersion": "6", #手机安卓版本
  "deviceName": '9599f8fd',  # 设备名，安卓手机可以随意填写，IOS根据具体手机填写
  "appPackage": "uni.UNIE7FC6F0",  # 启动APP Package名称,cmd命令【no.nordicsemi.android.mcp】
  "appActivity": ".view.logo.SplashActivity", # 启动APP Activity名称,cmd命令【adb shell dumpsys activity recents | find “intent={”】
  "unicodeKeyboard": True,  #使用自带输入法，输入中文时填True
  "resetKeyboard": False,   #程序执行完毕恢复原来输入法,默认为Unicode IME
  "noReset": True,   #不要重置app
  "newCommandTimeout": "9000",  #应用的最大超时响应时间
  "automationName" : "UiAutomator2",   # 使用的自动化引擎的名称
  "skipServerInstallation": True  #解决uiautomator2重复安装问题，需已安装uiautomator2包
    }
# 连接Appium Server，初始化自动化环境
driver = webdriver.Remote('http://localhost:4723/wd/hub', des)
# 设置缺省等待时间
driver.implicitly_wait(5)