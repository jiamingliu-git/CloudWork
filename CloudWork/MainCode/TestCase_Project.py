import unittest
from CloudWork.MainCode.TestMethod import TestMethod_Box_01
import configparser
from CloudWork.TestData.LoadFile_Method import LoadFile
from CloudWork.TestData.TestConfigData import *
from ddt import ddt,data


#获取测试用例
alldata=LoadFile(TestCase_Path, 0).get_data_auto()

#获取配置文件
cf=configparser.ConfigParser()
cf.read('F:\pyfile\CloudWork\TestData\\Testcase.config',encoding='UTF-8')

@ddt
class TestCase_Box_Project(unittest.TestCase):

# 登录
    def setUp(self):
        global login_headers

        url=cf['login']['url']
        data=cf['login']['data']
        headers = getattr(LoginToken,'headers')
        login_res=TestMethod_Box_01().login('post',url=eval(url),data=eval(data),headers=headers)
        print('登录结果：',login_res.json())

        try:
            self.assertEqual(login_res.json()['code'],'0000')
            TestReasult = 'Pass'
            print('断言结果：', TestReasult)
        except AssertionError as e:
            print('用例执行出错：{0}'.format(e))
            raise e
#保存登录后token
        setattr(LoginToken,'token',login_res.json()['value'])



#6-15用例执行
    @data(*alldata[5:15])
    def test_Project(self,project_data):
        getattr(LoginToken,'headers')['Authorization']=getattr(LoginToken,'token')     #拼接成带token的headers
        headers = getattr(LoginToken, 'headers')

        # project_data['Data']['projectId']=getattr(ProjectId,'projectid')
        # projectid=getattr(ProjectId, 'headers')

        project_res = TestMethod_Box_01().project(str(project_data['Method']),project_data['Url'],eval(project_data['Data']),headers=headers)
        print('用例执行结果:',project_res.json())
        if project_res.json()['value']:
            setattr(ProjectId,'projectid',project_res.json()['value'])

        try:
            self.assertEqual(project_res.json()['code'],str(project_data['Expect']))
            TestReasult = 'Pass'
            print('断言结果：',TestReasult)
        except AssertionError as e:
            print('断言结果：'.format(e))
            raise e

        LoadFile(TestCase_Path, 0).write_back(project_data['CaseNum'] + 1, str(project_res.json()))


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
        get_projectlist_url='https://testscp-ms.xgjk.info/scp-work/project/findByCondition'
        get_projectlist_data={"currentPage": 1,
                                "headEmployeeIds": [],
                                "introduce": "",
                                "pageSize":50,
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
        get_projectlist_headers = {'Content-Type':'application/json;charset=UTF-8','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)','Authorization':login_token}
        get_projectlist_res=TestMethod_Box_01().get_projectlist('get',get_projectlist_url,get_projectlist_data,get_projectlist_headers)
        values=get_projectlist_res.json()["result"]
        projectid_list=[]
    #取到所有项目id(未发布)
        for i in values:
            allprojectid=i['projectId']
            projectid_list.append(allprojectid)
    #删除项目
        for b in projectid_list:
            delete_project_url='https://testscp-ms.xgjk.info/scp-work/project/deleteById?projectId={0}'.format(b)
            delete_project_headers = {'Content-Type':'application/json;charset=UTF-8','Authorization':TestCase_Box_Project().setUp()}
            delete_project_res=TestMethod_Box_01().delete_unpublish_project('delete',delete_project_url,delete_project_headers)
            print('删除未发布项目结果：',delete_project_res.json())
            self.assertEqual(delete_project_res.json()['code'], '0000','删除未发布项目失败')


if __name__ == '__main__':
    unittest.main()