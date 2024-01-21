
"""
模块功能说明：
logging模块是Python内置的标准模块，主要用于输出运行日志，
可以设置输出日志的等级、日志保存路径、日志文件回滚等, 记录运行时的过程
"""

import logging
from logging import handlers
import sys

level_relations = {
'''日志事件级别，日志级别关系映射
级别排序：CRITICAL > ERROR > WARNING > INFO > DEBUG
默认等级： WARNING
1.默认的级别为”warning“,只会追踪该级别及以上的事件，除非更改日志配置。
2.处理形式：1）最简单方式输出到控制台 2）常用方式写入磁盘文件
'''
    'debug': logging.DEBUG,  #等级1，细节信息，仅当诊断问题时适用
    'info': logging.INFO, #等级2，确认程序按预期运行
    'warning': logging.WARNING, #等级3，表明有或即将发生的意外（例如：磁盘空间不足），程序按预期运行
    'error': logging.ERROR,  #等级4，由于严重的问题，程序某些功能已经不能正常执行
    'crit': logging.CRITICAL #等级5，严重的错误，表明程序已经不能继续执行
    }

def _get_logger(filename, level='info'):
    #1.创建logger对象，返回一个日志器
    log = logging.getLogger(filename)
    #2.设置日志等级
    log.setLevel(level_relations.get(level))
    #4.创建一个格式器对象
    fmt = logging.Formatter('%(asctime)s %(thread)d %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')  # 控制台输出参数格式
    """控制台输出参数（日志输出格式）
    name 日志的名称%s                                              例如：E:\pythonProject\testlog.log
    asctime 可读时间2023-06-14 16:17:36,020 ，逗号之后是毫秒%s        例如：2023-06-14 17:32:56,616
    filename 文件名，pathname的一部分%s                             例如：日志模块.py
    pathname 文件的全路径名称%s                                     例如：E:\pythonProject\Controlled Library 受控库\日志打印\日志模块.py
    funcName 调用日志多对应的方法名%s                                例如：<module>
    levelname 日志的等级%s                                         例如：INFO
    levelno 数字化的日志等级%s                                      例如：20
    lineno 被记录日志在源码中的行数%d                                 例如：82
    module 模块名%s                                               例如：日志模块
    msecs 时间中的毫秒部分%d                                        例如：859.8983287811279
    process 进程的ID %d                                           例如：36852 动态值
    processName 进程的名称 %s                                      例如：MainProcess
    thread 线程的ID %d                                            例如：21820 动态值
    threadName 线程的名称%s                                        例如：MainThread
    relativeCreated 日志被创建的相对时间，以毫秒为单位%d               例如：14.00899887084961
    """

    #Handler处理器
    # StreamHandler 屏幕输出(输出到控制台)
    console_handler = logging.StreamHandler(sys.stdout)  #sys.stdout默认是映射到控制台
    console_handler.setFormatter(fmt)# 设置写到日志文件格式，fmt控制台输出参数格式
    # ①BaseRotatingHandler 标准的分割文件日志
    #file_handler = handlers.BaseRotatingHandler
    # ②RotatingFileHandler 按文件大小记录日志（按照大小自动分割日志文件，一旦达到指定的大小重新生成文件）
    #maxBytes：单位bit 1*1024*1024*1024=1G , backupCount=0 保存几天的日志
    # file_handler = handlers.RotatingFileHandler(filename=filename, maxBytes=1*1024*1024*1024, backupCount=1, encoding='utf-8')
    # ③TimedRotatingFileHandler 按时间记录日志（日志文件按天进行保存，每天一个日志文件）
    # when:h(时)/m(分)/s(秒)/d(天)/midnight(凌晨)等等,  interval:间隔时间, backupCount=0 保存几天的日志
    file_handler = handlers.TimedRotatingFileHandler(filename=filename, when='D',interval=1, backupCount=3, encoding='utf-8')
    file_handler.setFormatter(fmt)   # 设置写到日志文件格式，fmt控制台输出参数格式
    #file_handler.suffix = '%Y-%m-%d_%H_%M_%S'  # 日志文件后缀,开启后会导致backupCount参数失效

    # 6.为日志器添加处理方式,将设置格式后的处理器对象给日志器“吞吃”，使日志器有处理日志的能力
    log.addHandler(console_handler)  #将日志输出到屏幕,
    log.addHandler(file_handler)   #将日志输出到日志文件
    return log


if __name__ == "__main__":
    logger = _get_logger(R'logger_test.log', 'info')  # 明确指定日志输出的文件路径和日志级别
    logger.info('日志输出测试') #7.调用日志器对象，生成日志





