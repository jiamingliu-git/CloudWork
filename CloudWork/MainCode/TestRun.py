import unittest
import HTMLTestRunner
from CloudWork.MainCode.TestCase_Task import *
from CloudWork.MainCode import TestCase_Task
from CloudWork.MainCode import TestCase_Project
from CloudWork.TestData.ConfigPath import *
from CloudWork.MainCode.TestCase_Project import *
from BeautifulReport import BeautifulReport
import time

loader=unittest.TestLoader()                                                     #用例加载器
casebag=unittest.TestSuite()                                                     #创建一个容器:casebag

'''多条加用例(精确至：类名)'''
casebag.addTest(loader.loadTestsFromTestCase(TestCaseBox_Task))
casebag.addTest(loader.loadTestsFromTestCase(TestCaseBox_Project))

# #多条加用例(精确至：文件名)
# casebag.addTest(loader.loadTestsFromModule(TestCase_Task))

# #单条加用例(精确至： 类名 -- 方法名)
# casebag.addTest(TestCase_Box_AddTask('test_a_add_task'))                         #往casebag里加用例。。。。
# casebag.addTest(TestCase_Box_SaveTask('test_b_savetask'))

# '''删除所有任务与项目（未发布）'''
# casebag.addTest(TestCaseBox_Task('delete_all_unpublish_task'))
# casebag.addTest(TestCaseBox_Project('delete_all_unpublish_project'))




#测试报告一
with open(TestReport_Path,'wb') as report:                                                    #新建一个文件：report.html,命名为report,
    runer=HTMLTestRunner.HTMLTestReportEN(stream=report,                                         #引用HTMLTestReportEN,把测试报告写进这个文件
                                          verbosity=2,
                                          title='协同办公项目接口自动化测试报告',
                                          description='描述内容:无',
                                          tester='LAU')
    runer.run(casebag)                                                                           #调用runer中run方法，运行casebag(casebag里面已经加了用例了)


# #测试报告二（需要将BeautifulReport包放在python3.8\Lib\site-packages下才可以使用）
# from CloudWork.TestData.ConfigData import *
# now = time.strftime("%Y-%m-%d %H_%M_%S")
# filename = now + r'report.html'
# desc = '协同办公项目接口自动化测试报告'
# result = BeautifulReport(casebag)
# result.report(filename=filename, description=desc, log_path=TestReport_Path)





# '''发送邮件'''
# import smtplib
# import time
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.application import MIMEApplication
#
# _user='396627130@qq.com'
# _pwd='vmrmgpvoirpcbjjd'
#
# now = time.strftime("%Y-%m-%d %H_%M_%S")
#
#
# class sendEmail():
#     def send_email(self,email_to,filepath):
#         msg=MIMEMultipart()
#         msg['Subject']=now+'测试报告'
#         msg['From']=_user
#         msg['To'] = email_to
#
#         part = MIMEText('这是自动化测试结果，请查收！')
#         msg.attach(part)
#
#         part =MIMEApplication(open(filepath,'rb').read())
#         part.add_header('Content-Dispositon','attachment',filename=filepath)
#         msg.attach(part)
#         s=smtplib.SMTP_SSL('smtp.qq.com',timeout=50)
#         s.login(_user,_pwd)
#         s.sendmail(_user,email_to,msg.as_string())
#         s.close()
#
# if __name__ == '__main__':
#     sendEmail().send_email('396627130@qq.com',r'F:\pyfile\CloudWork20201124.rar')

