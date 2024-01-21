#-*- coding: utf-8 -*-
import os
import time

if __name__ == "__main__":
    os.system('adb kill-server')
    time.sleep(2)
    os.system('adb start-server')
    time.sleep(2)
    # os.system('adb connect 192.168.31.48')    #家
    # os.system('adb connect 192.168.160.16')   #公司
    # os.system('adb devices')  # 查看已连接的设备
