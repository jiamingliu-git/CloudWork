import os

'''读取文件路径'''
project_path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
print(project_path)

#测试用例路径
TestCase_Path=os.path.join(project_path,'TestData','CloudWork_TestCase.xlsx')
print(TestCase_Path)

#测试报告路径
TestReport_Path=os.path.join(project_path,'TestReport','report09.html')
print(TestReport_Path)

class LoginToken():
    headers = {'Content-Type': 'application/json;charset=UTF-8'}
    token=None      #token=

class ProjectId():
    data =None
    projectid=None