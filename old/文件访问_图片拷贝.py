#coding:utf-8
def fileCope(srcPath,destPath):
    srcf = open(srcPath,'rb') #以二进制模式读的方式打开文件
    content = srcf.read()   #得到的content是 字节串对象 bytes
    srcf.close()

    destf = open(destPath,'wb') #以二进制模式写的方式打开文件
    destf.write(content)        #写入
    destf.close()

fileCope('1.png','1copy.png')


def fileCope2(srcPath,destPath):
    with open(srcPath,'rb') as scrf:
        content = scrf.read()
    with open(destPath,'wb') as destf:
        destf.write(content)

fileCope2('2.png','2copy.png')




