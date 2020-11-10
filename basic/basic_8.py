class PlayOne():
    def __init__(self,year,contry,name):
        self.year=year
        self.name=name
        self.contry=contry

    def WalkGround(self):
        print(self.name+'行走不太平稳')

    def info(self):
        print('{0}年生产，{1}研发，名字叫{2}'.format(self.year,self.contry,self.name))


class PlayTwo(PlayOne):

    def WalkGround(self):
        super(PlayTwo,self).WalkGround()          #超继承：在PlayTwo找到PlayOne，然后用PlayOne的WalkGround
        print(self.name+'平稳行走')

    def AvoidBlock(self):
        print(self.name+'可以避开障碍物')

PlayTwo(2020,'china','jm').WalkGround()