# from basic.basic_4 import add
#
# print(add(3,4))



# file=open('F:\\pyfile\\mainfile\\data\\practice.txt','r+',encoding='UTF-8')    #打开一个文件
#
# res=file.read(100)                 #读这个文件     读100个字符
# file.write("世界")
# file.writelines(['777','999'])
# print(res)


#  r:       只读
#  w:       只写
#  a:       可读可写
#  r+:      可读可写                                     *常用
#  w+:      清空重写，不存在就新建
#  a+:      追加写，原来的内容不清空                        *常用
#  \n:    换行符


#   file.write:         写字符串
#   file.writelines():   写列表， 例：file.writelines(['777','888'])




import os

# os.mkdir('a')                              #在同级目录下新建文件夹a     ：相对路径
#
# os.mkdir('F:\\pyfile\\mainfile\\data\\a')    #创建文件夹a             ：绝对路径
#
# os.rmdir('F:\\pyfile\\mainfile\\data\\a')    #删除文件夹a             ：绝对路径
#
#
# res=os.getcwd()                                    #获取当前文件夹路径
# print('路径：',res)
#
# res=os.path.realpath(__file__)                      #获取本身文件路径
# print(res)



# #异常处理
# import os
# try:
#     os.mkdir('F:\\pyfile\\mainfile\\data')        # 试一下新建文件夹
# except Exception as e:                           # 如果出错了就把错误存在 e 里
#     a=open('F:\\pyfile\\mainfile\\data\\errorfile','a+',encoding='utf-8')          #新建一个文件夹叫：errorfile
#     a.writelines(str(e))                               # 把错误写进e里（写进去的内容一定要是字符串，所以转换成str）
#     a.close()
# else:
#     print("+++")                                 # try成功了才执行
# finally:
#     print('***')                                 # 无论如何都会执行finally




