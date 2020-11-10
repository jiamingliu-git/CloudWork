# # import configparser
# # from CloudWork.TestData.LoadFile_Method import DoExcel
# # from CloudWork.MainCode.TestMethod import TestMethod_Box_01
# #
# # cf=configparser.ConfigParser()
# # cf.read('F:\pyfile\CloudWork\TestData\\Testcase.config',encoding='UTF-8')
# # alldata = DoExcel('F:\pyfile\CloudWork\TestData\data_task.xlsx', 0).get_data_auto()
# # Headers = {'Content-Type':'application/json;charset=UTF-8'}
# # res=TestMethod_Box_01().login('post',url=eval(cf['login']['url']),data=eval(cf['login']['data']),headers=Headers)
# # print(res.json())
# #
# # print('******************************************************************************************')
# # print(cf['login']['url'])
# # print(cf['login']['data'])
# # print(type(cf['login']['url']))
# # print(type(cf['login']['data']))
# # print('********************')
# # a=alldata[0]['Url']
# # b=alldata[0]['Data']
# # print(a)
# # print(b)
#
#
# # import unittest
# # from CloudWork.MainCode.TestMethod import TestMethod_Box_01
# # from ddt import ddt,data
# # from CloudWork.TestData.LoadFile_Method import LoadFile
# # from CloudWork.TestData.Login_Token import LoginToken
# # import configparser
# # import requests
# # import unittest
# # #获取excel里所有数据（测试用例）
# # alldata = LoadFile('F:\pyfile\CloudWork\TestData\data_task.xlsx', 0).get_data_auto()
# # a=alldata[0:4]
# # print(len(a))
# # @ddt
# # class TestCase_Box_Task():
# #
# #     @data(*alldata[0:4])
# #     def test_a_addtask(self,addtask_data):
# #             print(alldata[0:4])
# #
# #
# # TestCase_Box_Task().test_a_addtask()
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# import unittest
# from CloudWork.MainCode.TestMethod import TestMethod_Box_01
# from ddt import ddt,data
# from CloudWork.TestData.LoadFile_Method import LoadFile
# import configparser
# import requests
#
# cf=configparser.ConfigParser()
# cf.read('F:\pyfile\CloudWork\TestData\\Testcase.config',encoding='UTF-8')
# # #获取excel里所有数据（测试用例）
# # alldata = LoadFile(TestCase_Path, 0).get_data_auto()
# # headers=alldata[0]['Headers']
# # headers['Authorization']=
# # print(headers)
#
#
#
