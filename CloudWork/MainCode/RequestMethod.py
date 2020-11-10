import requests

class Http_Request():
    @staticmethod
    def http_request(method,url,data,headers):
        method=method.lower()
        if method == 'get':
            res = requests.get(url,headers=headers)
            return res
        elif method == 'post':
            res=requests.post(url,json=data,headers=headers)
            return res
        elif method == 'put':
            res = requests.put(url,json=data,headers=headers)
            return res
        elif method == 'delete':
            res = requests.delete(url,headers=headers)
            return res
        else:
            print('抱歉，暂不支持这种请求方法')



