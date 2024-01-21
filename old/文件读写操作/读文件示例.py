"""创建一个文本文件
hello
cHl0aG9uMy52aXAgYWxsIHJpZ2h0cyByZXNlcnZlZA==
"""
f = open('tmp.txt','w',encoding='utf8')
f.write('hello' #第一行
        '\n'    #回车
        'cHl0aG9uMy52aXAgYWxsIHJpZ2h0cyByZXNlcnZlZA==') #第二行
f.close()

#读取文本文件
f = open('tmp.txt','r')
tmp = f.read(3) #read方法读取3个字符
print(tmp) #返回3个字符的字符串，'hel'

tmp = f.read(3) #继续使用read方法读取3个字符
print(tmp)  #返回3个字符的字符串 'lo\n'  换行符也是一个字符

tmp = f.read() #返回剩余字符的字符串 'cHl0aG9uMy52aXAgYWxsIHJpZ2h0cyByZXNlcnZlZA=='
print(tmp)

f.close() #文件操作完毕，使用close方法关闭文件对象
print('----------------------------------1---------------------------------------')

#使用功能readlines方法，该方法会返回一个列表
f =open('tmp.txt')
linelist = f.readlines()  #返回一个列表['hello\n', 'cHl0aG9uMy52aXAgYWxsIHJpZ2h0cyByZXNlcnZlZA==']
print(linelist)
f.close()
for line in linelist:
    print(line)

print('----------------------------------2---------------------------------------')
f = open('tmp.txt')
content = f.read() #读取全部内容
f.close()

linelist = content.splitlines() #按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。
for line in linelist:
    print(line)

