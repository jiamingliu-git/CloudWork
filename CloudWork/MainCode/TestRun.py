import unittest
import HTMLTestRunner
from CloudWork.MainCode.TestCase_Task import *
from CloudWork.MainCode import TestCase_Task
from CloudWork.MainCode import TestCase_Project
from CloudWork.TestData.TestConfigData import *
from CloudWork.MainCode.TestCase_Project import *
from BeautifulReport import BeautifulReport
import time

loader=unittest.TestLoader()                                                     #用例加载器
casebag=unittest.TestSuite()                                                     #创建一个容器:casebag

# #多条加用例(精确至：类名)
# casebag.addTest(loader.loadTestsFromTestCase(TestCaseBox_Task))
casebag.addTest(loader.loadTestsFromTestCase(TestCaseBox_Project))

# #多条加用例(精确至：文件名)
# casebag.addTest(loader.loadTestsFromModule(TestCase_Task))

# #单条加用例(精确至： 类名 -- 方法名)
# casebag.addTest(TestCase_Box_AddTask('test_a_add_task'))                         #往casebag里加用例。。。。
# casebag.addTest(TestCase_Box_SaveTask('test_b_savetask'))
# casebag.addTest(TestCase_Box_Project('delete_all_unpublish_project'))



# #测试报告一
# with open(TestReport_Path,'wb') as report:                                                    #新建一个文件：report.html,命名为report,
#     runer=HTMLTestRunner.HTMLTestReportEN(stream=report,                                         #引用HTMLTestReportEN,把测试报告写进这个文件
#                                           verbosity=2,
#                                           title='协同办公项目接口自动化测试报告',
#                                           description='描述内容:无',
#                                           tester='LAU')
#     runer.run(casebag)                                                                           #调用runer中run方法，运行casebag(casebag里面已经加了用例了)


#测试报告二（需要将BeautifulReport包放在python3.8\Lib\site-packages下才可以使用）
from CloudWork.TestData.TestConfigData import *
now = time.strftime("%Y-%m-%d %H_%M_%S")
filename = now + r'report.html'
desc = '协同办公项目接口自动化测试报告'
result = BeautifulReport(casebag)
result.report(filename=filename, description=desc, log_path=TestReport_Path)








#情况二
#加载TestCase文件里的所有用例:                                 #没有test开头的用例不执行
# from CloudWork_Project.MainCode import TestCase
# loader=unittest.TestLoader()
# casebag.addTest(loader.loadTestsFromModule(TestCase))



# ##
# suite1 = unittest.TestLoader().loadTestsFromTestCase(TestCase_Box_Project().test_a_add_project())               #使用unittest中的TestLoader加载用例（类名），放入suite1
# suite2 = unittest.TestLoader().loadTestsFromTestCase(TestCase_Box_Project().test_b_add_projectemployee())               #使用unittest中的TestLoader加载用例（类名），放入suite1
#
# casebag = unittest.TestSuite().addTests([suite1,suite2])