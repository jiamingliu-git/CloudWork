# import unittest
# from CloudWork.MainCode.TestMethod import TestMethod_Box_01
# import configparser
# from ddt import ddt,data
# from CloudWork.TestData.LoadFile_Method import LoadFile
# from CloudWork.TestData.TestConfigData import *
# import requests
#
#
# Alldata=LoadFile(TestCase_Path,0).get_data_auto()
# print(Alldata[5])

from CloudWork.TestData.TestConfigData import *
import logging

class Mylog:
    def mylog(self,msg,level):
        #设定级别
        my_logger=logging.getLogger('名字')
        my_logger.setLevel('DEBUG')

        #设置输出格式
        formatter = logging.Formatter('%(asctime)s -- %(levelname)s -- %(filename)s -- %(module)s -- %(lineno)s -- 日志信息:%(message)s')

        #创建输出渠道
        ch=logging.StreamHandler()
        ch.setLevel('DEBUG')
        ch.setFormatter(formatter)

        fh=logging.FileHandler(Testlogs_Path,encoding='UTF-8')
        fh.setLevel('DEBUG')
        fh.setFormatter(formatter)

        #两者对接
        my_logger.addHandler(ch)
        my_logger.addHandler(fh)


        #收集日志
        level = level.upper()
        if level == 'DEBUG':
            my_logger.debug(msg)
        elif level == 'ERROR':
            my_logger.error(msg)
        elif level == 'INFO':
            my_logger.info(msg)
        elif level == 'WARNING':
            my_logger.warning(msg)
        elif level == 'CRITICAL':
            my_logger.critical(msg)

        #关闭渠道
        my_logger.removeHandler(ch)
        my_logger.removeHandler(fh)

    def debug(self,msg):
        self.mylog(msg,'DEBUG')

    def info(self,msg):
        self.mylog(msg,'INFO')

    def error(self,msg):
        self.mylog(msg,'ERROR')

    def warning(self,msg):
        self.mylog(msg,'WARNING')

    def critical(self,msg):
        self.mylog(msg,'CRITICAL')


if __name__ == '__main__':
    pass
