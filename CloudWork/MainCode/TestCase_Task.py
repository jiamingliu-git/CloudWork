# import unittest
# from CloudWork.MainCode.TestMethod import TestMethod_Box_01
# from ddt import ddt,data
# from CloudWork.TestData.LoadFile_Method import LoadFile
# from CloudWork.TestData.TestConfigData import *
# import configparser
#
#
# #获取excel里所有数据（测试用例）
# alldata = LoadFile(TestCase_Path, 0).get_data_auto()
#
# #获取配置文件
# cf=configparser.ConfigParser()
# cf.read('F:\pyfile\CloudWork\TestData\\TestAccount.config',encoding='UTF-8')
#
#
# @ddt
# class TestCase_Box_Task(unittest.TestCase):
#
# # 登录
#     def setUp(self):
#         #global login_headers
#
#         url=cf['login']['url']
#         data=cf['login']['data']
#         headers = getattr(LoginToken,'headers')
#
#         login_res=TestMethod_Box_01().login('post',url=eval(url),data=eval(data),headers=headers)
#         print('登录结果：',login_res.json())
#
#         try:
#             self.assertEqual(login_res.json()['code'],'0000')
#             TestReasult = 'Pass'
#             print('断言结果：', TestReasult)
#         except AssertionError as e:
#             print('用例执行出错：{0}'.format(e))
#             raise e
# #保存登录后token
#         setattr(LoginToken,'token',login_res.json()['value'])
#
#
# #1-5用例执行
#     @data(*alldata[0:5])
#     def test_task(self,addtask_data):
#         headers={'Content-Type': 'application/json;charset=UTF-8', 'Authorization':getattr(LoginToken,'token')}
#         test_res=TestMethod_Box_01().task(str(addtask_data['Method']),addtask_data['Url'],eval(addtask_data['Data']),headers=headers)
#         print('用例执行结果:',test_res.json())
#
#         try:
#             self.assertEqual(test_res.json()['code'], str(addtask_data['Expect']))
#             TestReasult = 'Pass'
#             print('断言结果：',TestReasult)
#         except AssertionError as e:
#             print('断言结果：'.format(e))
#             raise e
#         LoadFile(TestCase_Path,0).write_back(addtask_data['CaseNum']+1,str(test_res.json()))
#
#
#
# # 退出登录
#     def tearDown(self):
#         logout_res = TestMethod_Box_01().logout('get',eval(cf.get('logout','url')))
#         print('退出登录结果：', logout_res.json())
#         self.assertEqual(logout_res.json()['code'],'0000', '退出登录出错')
#
#
# #
# #
# #
# #
# #
# #
# #
# # #----------------------------------以上区域为插入用例位置-------------------------------------------------------------
# #
# #删除所有任务（未发布）
#
#     def delete_all_unpublish_task(self):
#     # 获取第一页的所有未发布任务id
#         find_taskid_url = 'https://testscp-ms.xgjk.info/scp-work/task/findByCondition'
#         find_taskid_data = {'currentPage': 1,
#                             'headEmployeeIds': [],
#                             'name': "",
#                             'pageSize': 50,
#                             'priorities': [],
#                             'startCreateTime': "",
#                             'startEndTime': "",
#                             'stopCreateTime': "",
#                             'stopEndTime': "",
#                             'taskClassIds': [],
#                             'taskCreatorIds': [],
#                             'taskEmployeeIds': [],
#                             'taskStates': ['DRAFT'],
#                             'taskViewQuery': "MY_HEAD"}
#         header = {'Content-Type': 'application/json;charset=UTF-8', 'Authorization': getattr(LoginToken,'token')}
#         get_task_id_res = TestMethod_Box_01().get_all_task_id('post',find_taskid_url,find_taskid_data,header)
#         self.assertEqual(get_task_id_res.json()['code'],'0000','获取第一页的所有任务id出错')
#         taskidlist = []                                                 #新建一个列表
#         for i in get_task_id_res.json()['value']['result']:             #在json响应结果里的value里的result获取所有taskId
#             all_taskid = i['taskId']
#             taskidlist.append(all_taskid)                               #把所有taskId存在一个列表里
#
#     #删除所有未发布任务
#         header = {'Content-Type': 'application/json;charset=UTF-8', 'Authorization': getattr(LoginToken,'token')}
#         for i in taskidlist:
#             delete_task_url = 'https://testscp-ms.xgjk.info/scp-work/task/deleteById?taskId={0}'.format(i)
#             delete_task_res=TestMethod_Box_01().delete_unpublish_task('delete',delete_task_url,header)
#             print('删除所有未发布任务结果',delete_task_res.json())
#             self.assertEqual(delete_task_res.json()['code'],'0000','删除所有未发布任务出错')
# #
# #
# #
# if __name__ == '__main__':
#      unittest.main()
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
