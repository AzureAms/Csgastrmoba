class Tuong:
    def __init__(self):
        pass
    extra_hp = 0
    equipment = []

class A(Tuong):
    def __init__(self):
        self.basic_hp = 50
        pass
    def total_hp(self):
        if (khien) in self.equipment:
            self.extra_hp += khien.hp
        print (self.extra_hp + self.basic_hp)

class equipments:
    def __init__(self, hp, atk):
        self.hp = hp
        self.atk = atk
        
khien = equipments(2000, 0)
p1 = A()
p1.equipment.append(khien)
print(p1.basic_hp)

p1.total_hp()