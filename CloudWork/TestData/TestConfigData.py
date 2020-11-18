import os
from CloudWork.TestData.LoadFile_Method import LoadFile
import time
import mysql.connector

project_path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
print(project_path)

'''测试用例路径'''
TestCase_Path=os.path.join(project_path,'TestData','CloudWork_TestCase.xlsx')
print(TestCase_Path)

'''测试报告路径'''
'''报告一'''
# now = time.strftime("%Y-%m-%d %H_%M_%S")
# TestReport_Path=os.path.join(project_path,'TestReport',now + 'report.html')
# print(TestReport_Path)
'''报告二'''
TestReport_Path=os.path.join(project_path,'TestReport')
# print(TestReport_Path)


'''测试配置文件路径'''
TestConfig_Path=os.path.join(project_path,'TestData','TestAccount.config')
# print(TestConfig_Path)

'''测试日志文件路径'''
Testlogs_Path=os.path.join(project_path,'Log','testlog01.txt')
# print(Testlogs_Path)



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




db_config={
            'host':'192.168.8.122',
            'user':'xgjk_w',
            'password':'xgjk@2019',
            'port':3306,
            'database':'scp_basic'
            }

#创建数据库连接
cnn=mysql.connector.connect(**db_config)
#创建游标
cursor=cnn.cursor()
#sql语句
query_sql="SELECT * FROM sys_user WHERE `name`='LAU'"
#执行语句
cursor.execute(query_sql)
#获取结果，打印结果
res=cursor.fetchone()
print(res)
cursor.close()
cnn.close()