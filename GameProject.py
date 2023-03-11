class Tuong:
    def __init__(self):
        pass
    ExtraHP = 0
    ExtraSPD = 0
    Equipment = []
    EquipmentHP = 0
    EquipmentSPD = 0
class Extra_Skill(Tuong):
    type = "Extra skill"

    def __init__(self,BasicHP,CurrentHP,BasicATK,BasicSPD,CurrentSPD,EnemyMaxHP,EnemyCurrentHP):
        self.BasicHP = BasicHP
        self.CurrentHP = CurrentHP
        self.BasicSPD = BasicSPD
        self.CurrentSPD = CurrentSPD
        self.EnemyMaxHP = EnemyMaxHP
        self.EnemyCurrentHP = EnemyCurrentHP
        pass
    def HPBoost(self):
        self.ExtraHP += (self.BasicHP/100)*15
        self.CurrentHP = self.CurrentHP + self.ExtraHP + self.EquipmentHP
    def SpeedBoost(self):
        for i in range (10, -1, -1):
            self.ExtraSPD = self.BasicSPD*(i/20)
            self.BasicSPD = self.CurrentSPD + self.ExtraSPD + self.EquipmentSPD
            #wait(0.5s)
    def Incinerate(self):
        for i in range (0, 4):
            self.EnemyCurrentHP -= self.BasicHP * (8/100)
            #wait(1s)
    def Finish(self):
        self.EnemyCurrentHP -= (15/100)*(self.EnemyMaxHP - self.EnemyCurrentHP)
            
            

