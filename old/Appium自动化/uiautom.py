#coding:utf-8
import os
import time
import uiautomator2 as u2
import timeit
num=10


d = u2.connect()
# 有多台设备，指定设备ip,通过USB链接， 我的设备序列号是127.0.0.1
# device = u2.connect_wifi('192.168.160.112')
# 获取正在运行的apk的包名
# pkgname = d.app_current
# print(pkgname)
# print(d.app_current())
# print(d.device_info)
d.app_stop('com.huawei.health')
d.app_start('com.huawei.health','.MainActivity')
time.sleep(8)
d.implicitly_wait(5)
try:
    d.xpath('//*[@resource-id="com.huawei.health:id/hw_main_tabs"]/android.widget.LinearLayout[4]/android.widget.ImageView[1]').click()
except:
    pass
try:
    d.xpath('//*[@resource-id="com.huawei.health:id/card_device_list"]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[2]').click()
except:
    pass

for i in range(0,num):
   time.sleep(10)
   try:
       start = timeit.default_timer()
       d(resourceId="com.huawei.health:id/tv_device_start").click()
   except:
       end = timeit.default_timer()
       print('Running time: %s Seconds' % (end - start))
       pass
   time.sleep(1)
   try:
      d(resourceId="android:id/button1").click()
   except:
        pass
   print('01')
   time.sleep(3)
   try:
      d(resourceId="com.huawei.health:id/dialog_one_btn").click()
   except:
        pass
   print('02')
   time.sleep(10)
   d.long_click(547,2076,0.8)
   print('03')
   d(resourceId="com.huawei.health:id/hwappbarpattern_cancel_icon").click()



