# class one:
#     two=2
#     three=3
#
#     def four(self):
#         return ('四')
#     def five(self):
#         return ('五')
#
# # a=one().two                    #调用类里的值
# #
# # b=one().four()                #调用类里的方法
#
# a=one().four()
# print(a)






# #如果不想要那个self,可以在函数前面加一个@staticmethod,就不用加self了(不推荐，因为不能用类里的属性值)
# class one:
#     two=2
#     three=3
#
#     @staticmethod                     #加一个@staticmethod,就不用加self了
#     def four():
#         print ('四')
#
#     @staticmethod                     #加一个@staticmethod,就不用加self了
#     def five():
#         print('五')
#
# one().four()
#
# one().five()






#提高属性值的复用性：初始化函数，在java里叫构建函数

class one():


    def __init__(self,name,age):
        self.name=name
        self.age=age

    def two(self):
        return (self.name,'名字1')

    def three(self):
        return (self.name,'名字2')

    def four(self):
        return (self.age,'年龄1')

    def five(self,):
        return (self.age,'年龄2')

    def six(self,*a):
        for item in a:
            print(self.name+'会'+item)

a=one(20,'小红').two()              #这里的参数是在类后面的参数，所以是传到class的初始化参数，而不是def
b=one(20,'小红').three()
c=one(20,'小红').four()
d=one(20,'小红').five()
e=one('jiaming','27').six('打篮球')

print(a)
print(b)
print(c)
print(d)









