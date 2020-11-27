import unittest
from CloudWork.MainCode.TestMethod import TestMethod_Box_01
import configparser
from ddt import ddt,data
from CloudWork.TestData.LoadFile_Method import LoadFile
from CloudWork.TestData.ConfigData import *
from CloudWork.TestData.ConfigPath import *
from CloudWork.MainCode.LogMethod import Mylogger
from CloudWork.TestData.LoadFile_Method import Write_back

#获取配置文件
cf=configparser.ConfigParser()
cf.read(TestConfig_Path,encoding='UTF-8')
# #获取测试用例
Alldata=LoadFile(TestCase_Path,0).get_data_auto()

@ddt
class TestCaseBox_Project(unittest.TestCase):

# 登录
    def setUp(self):
        global login_headers
        url=cf['login']['url']
        data=cf['login']['data']
        headers = getattr(Mirror,'headers')
        login_res=TestMethod_Box_01().login('post',url=eval(url),data=eval(data),headers=headers)
        print('登录结果：',login_res.json())

        try:
            self.assertEqual(login_res.json()['code'],'0000')
        except AssertionError as e:
            Mylogger().error('登录断言报错：{0}'.format(e))
            raise e
#保存登录后token
        setattr(Mirror,'token',login_res.json()['value'])



# #6-15用例执行
    @data(*Alldata[9:20])
    def test_Project(self,alldata):
        getattr(Mirror,'headers')['Authorization']=getattr(Mirror,'token')     #拼接成带token的headers
        headers = getattr(Mirror, 'headers')

        oneprodata = eval(alldata['Data'])  # 传入的数据

        if alldata['Form']==None:                   #如果不需要拼接进此区域
            if 'projectId' not in oneprodata:
                project_res = TestMethod_Box_01().project(str(alldata['Method']), alldata['Url'],eval(alldata['Data']), headers=headers)
                Mylogger().info('用例执行结果:{}'.format(project_res.json()))
                if project_res.json()['value']:                                                 #如果有生成新的项目id
                    setattr(Mirror, 'projectid', project_res.json()['value'])                          # 把项目id存起来
                    print('新增项目结果:', project_res.json())

            #断言
                TestResult = ''
                try:
                    self.assertEqual(project_res.json()['code'],str(alldata['Expect']))
                    TestResult = 'Pass'
                    Mylogger().info('断言结果：{}'.format(TestResult))
                except AssertionError as e:
                    TestResult = 'Failed'
                    Mylogger().error('断言结果：{}'.format(e))
                    raise e
                finally:
                    Write_back().write_back(TestCase_Path, 0,alldata['CaseNum'] + 1, str(project_res.json()),TestResult)


            elif 'projectId' in oneprodata:                                            #如果参数需要用到projectId
                setattr(Mirror, 'data', oneprodata)                                       #把数据存在mirror
                prodata = getattr(Mirror, 'data')                                             #把数据从mirror拿到给prodata
                prodata['projectId'] = getattr(Mirror, 'projectid')                             #把prodata中的projectid做替换
                project_res = TestMethod_Box_01().project(str(alldata['Method']), alldata['Url'],prodata, headers=headers)
                Mylogger().info('用例执行结果:{}'.format(project_res.json()))

            #断言
                TestResult = ''
                try:
                    self.assertEqual(project_res.json()['code'],str(alldata['Expect']))
                    TestResult = 'Pass'
                    Mylogger().info('断言结果：{}'.format(TestResult))
                except AssertionError as e:
                    TestResult = 'Failed'
                    Mylogger().error('断言结果：{}'.format(e))
                    raise e
                finally:
                    Write_back().write_back(TestCase_Path, 0,alldata['CaseNum'] + 1, str(project_res.json()),TestResult)

        elif alldata['Form'] == 'join':                 #需要拼接进此区域
            setattr(Mirror, 'data', oneprodata)
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
            project_res = TestMethod_Box_01().project(str(alldata['Method']), url, prodata, headers=headers)
            Mylogger().info('用例执行结果:{}'.format(project_res.json()))

        #断言
            TestResult = ''
            try:
                self.assertEqual(project_res.json()['code'], str(alldata['Expect']))
                TestResult = 'Pass'
                Mylogger().info('断言结果：{}'.format(TestResult))
            except AssertionError as e:
                TestResult = 'Failed'
                Mylogger().error('断言结果：{}'.format(e))
                raise e
            finally:
                Write_back().write_back(TestCase_Path, 0, alldata['CaseNum'] + 1, str(project_res.json()), TestResult)



# 退出登录
    def tearDown(self):
        url = cf['logout']['url']
        logout_res = TestMethod_Box_01().logout('get',eval(url))
        print('退出登录结果：', logout_res.json())
        self.assertEqual(logout_res.json()['code'], '0000', '退出登录出错')





#----------------------------------以上区域为插入用例位置-------------------------------------------------------------

#删除所有项目（未发布）

    def delete_all_unpublish_project(self):
        #获取所有项目列表(未发布)
        get_projectlist_url = 'https://testscp-ms.xgjk.info/scp-work/project/findByCondition'
        get_projectlist_data = {"currentPage": 1,
                                "headEmployeeIds": [],
                                "introduce": "",
                                "pageSize": 50,
                                "projectClassIds": [],
                                "projectCreatorIds": [],
                                "projectEmployeeIds": [],
                                "projectState": ["DRAFT"],
                                "projectViewQuery": "MY",
                                "startCreateTime": "",
                                "startStartTime": "",
                                "stopCreateTime": "",
                                "stopStartTime": ""
                                }
        get_projectlist_headers = {'Content-Type': 'application/json;charset=UTF-8',
                                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
                                   'Authorization': 'eyJhbGciOiJIUzUxMiJ9.eyJsb2dpblR5cGUiOiJQQyIsIm1vYmlsZSI6IjEzNjQwOTgxMjE5IiwidXNlck5hbWUiOiLliJhMQVUiLCJleHAiOjE2MDY0NjE3MjksInVzZXJJZCI6MTI2MDM4NDc5NzMyNzM2fQ.VfdQ2YyPCC7EqDohAyi8F0hZ_dExQpFgx7vsv1oyk5At9ZkSK1dUnMr4AFp-Bghi4ZRZ9HVKIloPwODKJ1BUbg'}
        get_projectlist_res = TestMethod_Box_01().get_projectlist('post', get_projectlist_url, get_projectlist_data,
                                                                  get_projectlist_headers)
        values=get_projectlist_res.json()["result"]
        projectid_list=[]
    #取到所有项目id(未发布)
        for i in values:
            allprojectid=i['projectId']
            projectid_list.append(allprojectid)
    #删除项目
        for b in projectid_list:
            delete_project_url='https://testscp-ms.xgjk.info/scp-work/project/deleteById?projectId={0}'.format(b)
            delete_project_headers = {'Content-Type':'application/json;charset=UTF-8','Authorization':getattr(Mirror,'token')}
            delete_project_res=TestMethod_Box_01().delete_unpublish_project('delete',delete_project_url,delete_project_headers)
            print('删除未发布项目结果：',delete_project_res.json())
            self.assertEqual(delete_project_res.json()['code'], '0000','删除未发布项目失败')


if __name__ == '__main__':
    unittest.main()
