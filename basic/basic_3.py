#
#
# def a(ab,cd):
#     print('{}是nick的{}'.format(ab,cd))
# a('mama','helen')                           #调用函数
#
#
#
#
# def add(newnum):                              #100相加函数
#     num=0
#     for c in range(newnum):
#         num=num+c
#     print(num)
# add(101)
#
#
#
# def add(newnum):                              ##100相加函数，使用input
#     num=0
#     for c in range(newnum):
#         num=num+c
#     print(num)
# add(int(input('请输入你想相加的数字：')))


# def add(m=1,n=9,k=2):                #←←←←←←其次使形式/位置参数
#     sum=0
#     for i in range(m,n,k):
#         sum+=i
#     print(sum)
#
# add()                                #←←←←←←优先使用实参数



# def add(m,n,k):
#     sum=0
#     for i in range(m,n,k):
#         sum+=i
#     return sum                     #只有return了，才可以拿去用，不然没有返回数据
#
# print(add(1,10,2))                 #1、打印这个调用的函数
# res=add(1,10,2)                    #2、 或者把他存在变量res结果里
# print(res)                         #    然后打印这个res结果





# #列表长度如果大于2，返回列表前两个内容：
# list=[1,2,3,4]
# def CheckList():
#     if len(list)>2:                #如果长度大于2
#         newlist=list[0:2]          #一个新的列表产生了，他的内容是0到2
#         return newlist             #返回这个newlist的数据：[1,2]
# print(CheckList())                 #打印这个函数返回的数据:[1,2]



# a=20                         #下面声明了a是10，那么a就不再是20
# def add(b):
#     global a                 #声明a是10
#     a=10
#     sum=a+b
#     print(sum)
# add(2)
# print(a)