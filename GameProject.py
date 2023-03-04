class Tuong:
    def __init__(self):
        pass
    ExtraHP = 0
    ExtraSPD = 0
    equipment = []
class Extra_Skill(Tuong):
    type = "Extra skill"

    def __init__(self,BasicHP,BasicATK,BasicSPD,EnemyHP,EnemySPD):
        self.BasicHP = BasicHP
        self.BasicSPD = BasicSPD
        pass
    def HPBoost(self):
        self.ExtraHP += (self.BasicHP/100)*15
        print (self.ExtraHP + self.BasicHP)
    
    def SpeedBoost(self):
        for i in range(5,0,-1):
            self.ExtraSPD = self.BasicSPD *(i/10)
            print (self.BasicSPD + self.ExtraSPD)

