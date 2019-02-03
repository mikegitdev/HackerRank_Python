class Enemy:

    def __init__(self,atkl,atkh):
        self.atkl=atkl
        self.atkh=atkh

    def getAtk(self):
        print(self.atkl)

    def getAtkH(self):
        print(self.atkh)


enemy1 = Enemy(40,49)
enemy1.getAtk()

enemy2 = Enemy(75,90)
enemy2.getAtk()

enemy2.getAtkH()
