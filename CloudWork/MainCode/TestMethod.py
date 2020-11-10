import requests
from CloudWork.MainCode.RequestMethod import Http_Request
###post请求json=用字典传参,data就的把字典通过json.dumps()转换成字符串


class TestMethod_Box_01():

#用户登录
    def login(self,method,url,data,headers):
        login_res = Http_Request().http_request(method,url,data,headers)     #可以加verify=False：加了这个才可以抓到https
        return login_res

#退出登录
    def logout(self,method,url):
        logout_res=Http_Request().http_request(method,url,data=None,headers=None)
        return logout_res

#获取所有任务id
    def get_all_task_id(self,method,url,data,headers):
        get_all_task_id_res=Http_Request().http_request(method,url,data,headers)
        return get_all_task_id_res

#新建任务(未发布)
    def add_unpublish_task(self,method,url,data,headers):
        add_task_res = Http_Request().http_request(method,url,data,headers)
        return add_task_res

#任务接口
    def task(self,method,url,data,headers):
        task_res=Http_Request().http_request(method,url,data,headers)
        return task_res

#删除任务(未发布)
    def delete_unpublish_task(self,method,url,headers):
        delete_unpublish_task_res = Http_Request().http_request(method,url,data=None,headers=headers)
        return delete_unpublish_task_res

#新建项目(未发布)
    def project(self,method,url,data,headers):
        add_project_res=Http_Request().http_request(method,url,data,headers)
        return add_project_res

#添加项目成员
    def add_projectEmployee(self,method,url,data,headers):
        add_projectEmployee_res=Http_Request().http_request(method,url,data,headers)
        return add_projectEmployee_res

#获取项目列表
    def get_projectlist(self,method,url,data,headers):
        get_projectlist_res=Http_Request().http_request(method,url,data,headers)
        return get_projectlist_res

#暂存项目
    def save_project(self,method,url,data,headers):
        save_project_res=Http_Request().http_request(method,url,data,headers)
        return save_project_res

#添加项目状态
    def add_projectstate(self,method,url,headers):
        add_projectstate_res=Http_Request().http_request(method,url,data=None,headers=headers)
        return add_projectstate_res

#删除项目状态
    def delete_projectstate(self,method,url,headers):
        delete_projectstate_res=Http_Request().http_request(method,url,data=None,headers=headers)
        return delete_projectstate_res

#删除项目(未发布)
    def delete_unpublish_project(self,method,url,headers):
        delete_project_res=Http_Request().http_request(method,url,data=None,headers=headers)
        return delete_project_res

#删除项目成员
    def delete_projectuser(self,method,url,headers):
        delete_projectuser_res=Http_Request().http_request(method,url,data=None,headers=headers)
        return delete_projectuser_res


# class TestMethod_Box_02():
#
# #后台管理系统
#     def login(self):




if __name__ == '__main__':
    print('------------------------------------------------------------------------------------------------------------')

# add_project_url = 'https://testscp-ms.xgjk.info/scp-work/project/add'
# add_project_data = {
#                     "classId": 112994949267456,
#                     "name": "aip_auto_project",
#                     "templateId": None
#                     }
# add_project_headers = {'Content-Type':'application/json;charset=UTF-8','Authorization':'eyJhbGciOiJIUzUxMiJ9.eyJjb21wYW55SWQiOjEsImxvZ2luVHlwZSI6IlBDIiwiY29tcGFueU5hbWUiOiLmtYvor5Xlhazlj7giLCJtb2JpbGUiOiIxMzY0MDk4MTIxOSIsImVtcGxveWVlSWQiOjExMjk5NTc2NzE1NjczNiwidXNlck5hbWUiOiJMQVUiLCJleHAiOjE2MDMzMzA5NzgsInVzZXJJZCI6MTEyOTk1NzY3MTU2NzM2fQ.8hfpCQdccaHVUecSJWYtNC9bd477k2dq8tjomaHVW83wPNPIwM5QcluTJ8RFZAGBwOyj9i7tMjYPisnWwN7zCA'}
# add_project_res=TestMethod_box_01().add_unpublish_project(add_project_url,add_project_data,add_project_headers)
# print('添加草稿项目结果',add_project_res.json())






