#
#
#
# total=int(input('请输入购买金额'))
#
# if total>=0 and total<=50:
#     total=total*0.9
#     print('您的折扣是让利10%，需要支付{}'.format(total))
# elif total>50 and total<=100:
#     total2 = total * 0.8
#     print('您的折扣是让利20%，需要支付{}'.format(total2))




# import random                    #生成随机数
#
# num1=random.randint(1,9)        #1到9随机生成一个数
# num2=int(input("请输入数字"))
# if num2>num1:
#     print("您输入的数字太大了")
# elif num2<num1:
#     print("您输入的数字太小了")
# elif num2==num1:
#     print("您输入的数字与随机生成数刚好相等")



# #取值
#
# gg={'key':'value','key2':'value2'}
# b=gg.values()
# for ss in b:
#     print(ss)



# L=[['a','b','c','d','e'],['f','g','h','i','j'],['k','o','p','q'],['23'],['456']]
# for s in L:                                #拿到的值是：一个个列表
#     for ab in s:                           #拿到的值是：列表里的每个值
#         print(ab)




# #for循环
# gg=['a',1,[3,4],(5,6,'qwer'),{'key':'value','key2':'value2'}]
# for zz in gg[4]:
#     print(zz)
#
#
# L=[5,6,9,3,7]
# sum=0
# for a in L:
#     sum=sum+a
# print(sum)




# #range
# range(1,6)
#
# a=list(range(1,6))   #转换成list列表
# print(a)
#
# b=list(range(1,6,2))  # 跳一个数字（步长2）
# print(b)

#
# for item in range(3):#循环3次
#     print('@@@')




# L=[5,6,9,3,7]
#
# for a in range(5):
#     print(L[a])

#
#
# sum=0
# for a in range(1,101):
#     sum=sum+a
# print(sum)




# name = ['a','b','c','d','e','f','g']
# for a in name:
#     newname=str(input('请输入英文字母'))
#     if newname in name:
#         print('ok')
#         break
#
#     elif newname not in name:
#         print('not in name')






# #while
#
# while True:            #死循环
#     print('a')

#-----------------------------------------------------
# a=0
# sum=0
# while a<=100:
#     sum=sum+a
#     a=a+1
# print(sum)



# num=9
# newnum=int(input('请计算3*3的值'))
# if newnum==num:
#     print('答对了')
# elif newnum !=num:
#     while True:
#         print('拜拜')



user={'admin':123456,'LAU':123456}

aa=10
while aa>0:
    username = str(input('输入用户名'))
    if username in user.keys():
        while True:
            userpwd=int(input('请输入密码'))
            if userpwd==user[username]:
                print('登录成功')
                break
            else:
                print('密码错误')
                continue
    elif username not in user.keys():
        print('用户名输入错误或不存在')
    aa=aa-1


