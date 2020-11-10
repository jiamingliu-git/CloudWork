class PlayOne():
    def __init__(self,year,contry,name):
        self.year=year
        self.name=name
        self.contry=contry

    def WalkGround(self):
        print(self.name+'行走不太平稳')

    def info(self):
        print('{0}年生产，{1}研发，名字叫{2}'.format(self.year,self.contry,self.name))


class PlayTwo(PlayOne):                                   #继承了PlayOne

    def WalkGround(self):
        print(self.name+'平稳行走')

    def AvoidBlock(self):
        print(self.name+'可以避开障碍物')

#
# PlayTwo(2020,'俄国','JM').info()
#
# PlayTwo(2020,'俄国','JM').WalkGround()



#-------------------------------------------------------------------------------
                                                 #注意：
class PlayThree(PlayOne,PlayTwo):                #继承了两个，那么优先使用PlayOne的函数
                                                 #如果要继承两个，那么要保证这两个没有继承关系
    def Jump(self):
        print(self.name+'可以跳了')

PlayThree(2020,'俄国','JM').Jump()
PlayThree(2020,'俄国','JM').WalkGround()