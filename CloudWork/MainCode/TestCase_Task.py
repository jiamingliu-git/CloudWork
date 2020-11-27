import unittest
from CloudWork.MainCode.TestMethod import TestMethod_Box_01
from ddt import ddt,data
from CloudWork.TestData.LoadFile_Method import LoadFile
from CloudWork.TestData.LoadFile_Method import Write_back
from CloudWork.TestData.ConfigData import *
from CloudWork.TestData.ConfigPath import *
import configparser

#获取excel里所有数据（测试用例）
Alldata = LoadFile(TestCase_Path, 0).get_data_auto()

#获取配置文件
cf=configparser.ConfigParser()
cf.read(TestConfig_Path,encoding='UTF-8')


@ddt
class TestCaseBox_Task(unittest.TestCase):

# 登录
    def setUp(self):
        url=cf['login']['url']
        data=cf['login']['data']
        headers = getattr(Mirror,'headers')
        login_res=TestMethod_Box_01().login('post',url=eval(url),data=eval(data),headers=headers)
        print('登录结果：',login_res.json()['message'])

        try:
            self.assertEqual(login_res.json()['code'],'0000')
        except AssertionError as e:
            print('登录断言报错：{0}'.format(e))
            raise e
#保存登录后token
        setattr(Mirror,'token',login_res.json()['value'])


#1-5用例执行
    @data(*Alldata[0:9])
    def test_task(self,alldata):
        getattr(Mirror,'headers')['Authorization']=getattr(Mirror,'token')     #拼接成带token的headers
        headers = getattr(Mirror, 'headers')

        onetaskdata = eval(alldata['Data'])                     #传入的数据

        if alldata['Form']==None:                               #如果不需要拼接进此区域
            if 'taskId' not in onetaskdata:
                task_res=TestMethod_Box_01().task(str(alldata['Method']),alldata['Url'],eval(alldata['Data']),headers=headers)
                print('执行用例：',alldata['CaseName'])
                print('请求地址：',alldata['Url'])
                print('请求参数：',alldata['Data'])
                print('用例执行结果:', task_res.json())
                if task_res.json()['value']:                                                 #如果有生成新的taskid
                    setattr(Mirror, 'taskid', task_res.json()['value'])                          # 把项目taskid存起来

            #断言
                TestResult = ''
                try:
                    self.assertEqual(str(alldata['Expect']),task_res.json()['code'])
                    TestResult = 'Pass'
                except AssertionError as e:
                    TestResult = 'Failed'
                    print('断言结果：{0}'.format(e))
                    raise e
                finally:
                    Write_back().write_back(TestCase_Path, 0,alldata['CaseNum'] + 1, str(task_res.json()),TestResult)


            elif 'taskId' in onetaskdata:                                            #如果参数需要用到taskid
                setattr(Mirror, 'data', onetaskdata)                                       #把数据存在mirror
                taskdata = getattr(Mirror, 'data')                                             #把数据从mirror拿到给prodata
                taskdata['taskId'] = getattr(Mirror, 'taskid')                             #把prodata中的projectid做替换
                task_res = TestMethod_Box_01().task(str(alldata['Method']), alldata['Url'],taskdata, headers=headers)
                print('执行用例：',alldata['CaseName'])
                print('请求地址：',alldata['Url'])
                print('请求参数：',taskdata)
                print('用例执行结果:', task_res.json())

            #断言
                TestResult = ''
                try:
                    self.assertEqual(task_res.json()['code'],str(alldata['Expect']))
                    TestResult = 'Pass'
                    print('断言结果：',TestResult)
                except AssertionError as e:
                    TestResult = 'Failed'
                    print('断言结果：'.format(e))
                    raise e
                finally:
                    Write_back().write_back(TestCase_Path, 0,alldata['CaseNum'] + 1, str(task_res.json()),TestResult)

        elif alldata['Form'] == 'join':                 #需要拼接进此区域
            setattr(Mirror, 'data', onetaskdata)
            prodata = getattr(Mirror, 'data')
            prodata['projectId'] = getattr(Mirror, 'projectid')
#-------------------------------------------------------参数与url拼接方法-------------------------------------------------------------
            raw_url = alldata['Url']
            raw_data = prodata

            list = []
            for key, values in raw_data.items():
                list.append(key + '=' + str(values))
            query_string = '&'.join(list)
            url = raw_url + '?' + query_string
# ------------------------------------------------------参数与url拼接方法-------------------------------------------------------------------
            task_res = TestMethod_Box_01().task(str(alldata['Method']), url, prodata, headers=headers)
            print('执行用例：', alldata['CaseName'])
            print('请求地址：', url)
            print('请求参数：', prodata)
            print('用例执行结果:', task_res.json())

            #断言
            TestResult = ''
            try:
                self.assertEqual(task_res.json()['code'],str(alldata['Expect']))
                TestResult = 'Pass'
                print('断言结果：{}'.format(TestResult))
            except AssertionError as e:
                TestResult = 'Failed'
                print('断言结果：{}'.format(e))
                raise e
            finally:
                Write_back().write_back(TestCase_Path, 0,alldata['CaseNum'] + 1, str(task_res.json()),TestResult)

# 退出登录
    def tearDown(self):
        logout_res = TestMethod_Box_01().logout('get',eval(cf.get('logout','url')))
        print('退出登录结果：', logout_res.json())
        self.assertEqual(logout_res.json()['code'],'0000', '退出登录出错')


#
#
#
#
#
#
#
# #----------------------------------以上区域为插入用例位置-------------------------------------------------------------
#
#删除所有任务（未发布）

    def delete_all_unpublish_task(self):
    # 获取第一页的所有未发布任务id
        find_taskid_url = 'https://testscp-ms.xgjk.info/scp-work/task/findByCondition'
        find_taskid_data = {'currentPage': 1,
                            'headEmployeeIds': [],
                            'name': "",
                            'pageSize': 50,
                            'priorities': [],
                            'startCreateTime': "",
                            'startEndTime': "",
                            'stopCreateTime': "",
                            'stopEndTime': "",
                            'taskClassIds': [],
                            'taskCreatorIds': [],
                            'taskEmployeeIds': [],
                            'taskStates': ['DRAFT'],
                            'taskViewQuery': "MY_HEAD"}
        header = {'Content-Type': 'application/json;charset=UTF-8', 'Authorization': getattr(Mirror,'token')}
        get_task_id_res = TestMethod_Box_01().get_all_task_id('post',find_taskid_url,find_taskid_data,header)
        self.assertEqual(get_task_id_res.json()['code'],'0000','获取第一页的所有任务id出错')
        taskidlist = []                                                 #新建一个列表
        for i in get_task_id_res.json()['value']['result']:             #在json响应结果里的value里的result获取所有taskId
            all_taskid = i['taskId']
            taskidlist.append(all_taskid)                               #把所有taskId存在一个列表里

    #删除所有未发布任务
        header = {'Content-Type': 'application/json;charset=UTF-8', 'Authorization': getattr(Mirror,'token')}
        for i in taskidlist:
            delete_task_url = 'https://testscp-ms.xgjk.info/scp-work/task/deleteById?taskId={0}'.format(i)
            delete_task_res=TestMethod_Box_01().delete_unpublish_task('delete',delete_task_url,header)
            print('删除所有未发布任务结果',delete_task_res.json())
            self.assertEqual(delete_task_res.json()['code'],'0000','删除所有未发布任务出错')
#
#
#
if __name__ == '__main__':
     unittest.main()










