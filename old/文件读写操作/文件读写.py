# coding:utf-8

"""文件读写---笔记
原理：读写文件首先通过内置函数open打开一个文件，
    open函数会返回一个对象，我们称之为文本对象，
    返回的文件对象包含读取文件内容和写入文件内容的方法。
注意事项：要写入字符串的文件，需要将字符串编码为字节串，
        从文本文件中读取的文件信息都是字节串，在处理之前，必须将字节串解码为字符串。
------------------------------------------------------------------


----------------------------文本文件读写-----------------------------
open(
    file,            
    mode='r',         
    buffering=-1,
    encoding=None,
    errors=None,
    newline=None,
    closefd=True,
    opener=None
    )
-----
解析：

1）参数file
file参数指定要打开文件的路径。可以是相对路径（当前工作目录）或绝对路径。
2）参数mode
mode参数指定文件打开的模式。（打开文件的模式决定可以怎么操作文件）
常用打开模式：
r 只读文本模式打开（最常用的方式，如果没有指定参数mode的值，就使用缺省值‘r’）
w 只写文本模式打开（创建一个新文件写入内容，或者清空某个文本文件重新写入内容）
a 追加文本模式打开（文件末尾添加内容）

3）参数encoding
encoding参数指定了读写文件时，使用的字符编解码方式。
调用.write()写入字符串到文件中，open函数会使用指定encoding编码为字节串
调用read从文件中读取内容，open函数会使用指定encoding解码为字符串对象
如果调用的时候没有传入encoding参数值，open函数会使用系统缺省字符编码方式（Windows系统上，使用gbk编码）
-------------------------------以下内容为实操-----------------------------------"""


"""-----------------写文件----------------------"""
###会覆盖原来的内容,使用要特别注意

"""代码1
f = open('tmp.txt','w',encoding='utf8') #指定编码方式为utf8
# f = open('tmp.txt','w',encoding='gb2312') #指定编码方式为utf8
f.write('hello\ncHl0aG9uMy52aXAgYWxsIHJpZ2h0cyByZXNlcnZlZA==')  #将字符串编码为utf8字节串写入文件
f.close()  #关闭文件对象
"""

"""-----------------追加文件----------------------"""

"""代码1
f = open('tmp.txt','a',encoding='utf8') #指定编码方式为utf8
# f = open('tmp.txt','a',encoding='gb2312') #指定编码方式为utf8
f.write('\n填入写入的内容')  #将字符串编码为utf8字节串写入文件
f.close()  #关闭文件对象
"""

"""-----------------读文件read()----------------------"""

"""代码1
# 因为是读取文本文件的模式， 可以无须指定 mode参数
# 因为都是 英文字符，基本上所以的编码方式都兼容ASCII，可以无须指定encoding参数
f = open('tmp.txt')

tmp = f.read(3)  # read 方法读取3个字符
print(tmp)       # 返回3个字符的字符串 'hel'

tmp = f.read(3)  # 继续使用 read 方法读取3个字符
print(tmp)       # 返回3个字符的字符串 'lo\n'  换行符也是一个字符

tmp = f.read()  # 不加参数，读取剩余的所有字符
print(tmp)       # 返回剩余字符的字符串 'cHl0aG9uMy52aXAgYWxsIHJpZ2h0cyByZXNlcnZlZA=='

# 文件操作完毕后， 使用close 方法关闭该文件对象
f.close()
"""

"""-----------------读文件readlines()-按行读取----------------------"""

""">>>1
f = open('tmp.txt')
linelist = f.readlines()   #内置函数readlines()按行读取
f.close()

for line in linelist:  #for循环
    print(line)      
>>>"""
#结果
#hello
#
#cHl0aG9uMy52aXAgYWxsIHJpZ2h0cyByZXNlcnZlZA==

""">>>2
f = open('tmp.txt')
content = f.read()
f.close()
print(content)

linelist = content.splitlines(True) #按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。
for line in linelist:
    print(line)
>>>"""
#结果
#hello
#cHl0aG9uMy52aXAgYWxsIHJpZ2h0cyByZXNlcnZlZA==


url ="https://img-blog.csdnimg.cn/211f7b2e28c04eca97b3c8d9106dd148.png"
path = url.split('/',10)
print(path)

# f =open('tmp.txt','wb')
# content ='大的'
# f.write(content.encode('utf8'))
# f.close()
# f=open('tmp.txt','rb')
# con = f.read()
# print(con)
#
# con=b'\xe5\xa4\xa7\xe7\x9a\x84'
# f = open('tmp.txt','ab')
# f.write(con)
