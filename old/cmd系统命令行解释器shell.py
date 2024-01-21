"""通过python调用shell脚本的3种常见方式"""
"""1.使用os.system来运行（缺点：需等待外部程序结束，才能运行后续程序）
   2.使用subprocess.run来运行
   3.使用subprocess.Popen来运行"""

'''-----------------------------------------1-------------------------------------------'''
'''1.使用os.system来运行
以下为正文...
--------------------------------------------'''

import os
#解决乱码问题，当pycharm控制台用的是utf-8编码，而cmd控制台返回的是GBK编码
os.system('chcp 65001')  #65001UTF-8 ; 936gbk
#执行cmd控制台指令
os.system('ping www.baidu.com -n 10')



'''-----------------------------------------2-------------------------------------------'''
'''2.使用subprocess.run来运行
以下为正文...


import subprocess
subprocess.getoutput('ping www.baidu.com -t')
--------------------------------------------'''

'''-----------------------------------------3-------------------------------------------'''
'''
解析：
①shell=True打开一个命令行解释器，执行命令'ping www.baidu.com -n 10',  重定向stdout=PIPE指定输出到终端的内容放到一个管道里面。
②通过communicate方法读取管道文件的内容，返回标准输出outinfo和标准错误errinfo（返回格式：字节串bytes）
③decode()方法解码，将标准输出outinfo和标准错误errinfo转成字符串
以下为正文...


from subprocess import PIPE, Popen
# ①返回的是Popen实例对象
proc = Popen('fsutil volume diskfree d:',
             stdin=None,  # 标准输入，键盘设备
             stdout=PIPE,  # 标准输出，显示器窗口/终端设备，指定PIPE输出到管道文件
             stderr=PIPE,  # 标准错误，，指定PIPE输出到管道文件
             shell=True)  #打开命令行解释器

# ②通过communicate方法读取管道文件的内容，返回输出到标准输出和标准错误的字节串内容。并将标准输出, 标准错误赋值给outinfo, errinfo
outinfo, errinfo = proc.communicate()  # 存储到变量中 

# 因为返回的是字节串bytes，使用gbk解码
outinfo = outinfo.decode('gbk')
errinfo = errinfo.decode('gbk')
print(outinfo, errinfo)

#课后练习，判断磁盘剩余空间
outputList = outinfo.splitlines() #分割成列表
#剩余空间
free = int(outputList[0].split()[2].replace(',',''))
# free = outputList[0]  #读取列表的第一行字符串,可用字节总数        : 20,004,405,248 (18.6 GB)
# free = free.split() #分割['可用字节总数        ', ' 20,004,405,248 (18.6 GB)']
# free =int(free[2].replace(',',''))
#总空间
total = int(outputList[1].split()[2].replace(',',''))

if free/total < 0.9 :
    print(f'空间不足，剩余空间:{free}')
else:
    print('空间充足')

--------------------------------------------'''


