import os
from CloudWork.TestData.LoadFile_Method import LoadFile

project_path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
# print(project_path)

#测试用例路径
TestCase_Path=os.path.join(project_path,'TestData','CloudWork_TestCase.xlsx')
# print(TestCase_Path)

#测试报告路径
TestReport_Path=os.path.join(project_path,'TestReport','report11.html')
# print(TestReport_Path)

#测试配置文件路径
TestConfig_Path=os.path.join(project_path,'TestData','TestAccount.config')
print(TestConfig_Path)



class LoginToken():
#获取excel全部数据
    alldata = LoadFile(TestCase_Path, 0).get_data_auto()

# 获取基础headers
    headers=eval(alldata[0]['Headers'])
    token=None




class Mirror():
    data = None
    projectid = None
    Url = None
    userId = None
    taskid = None