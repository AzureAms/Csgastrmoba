# import time
# from time import sleep
# class Tuong:
#     def __init__(self, Basic_Hp, Basic_Damage, Level, Run_speed, Attack_speed):
#         self.Basic_Hp = Basic_Hp
#         self.Basic_Damage = Basic_Damage
#         self.level = Level
#         self.Run_speed = Run_speed
#         self.Attack_speed = Attack_speed
#         extra_hp = 0
#         equipment = []
#         pass
# class Dich(Tuong):
#     def __init__(self, Current_Enemy_Hp, Current_Enemy_Damage):
#         self.Enemy_Hp = Current_Enemy_Hp
#         self.Enemy_Damage = Current_Enemy_Damage
#         pass
# class Hero_A(Tuong):
#     def __init__(self):
#         self.Basic_Hp = 500 #máu gốc
#         self.Basic_Damage = 50 #dame gốc
#         self.Attack_speed = 10 #tốc đánh gốc
#         self.Run_speed = 50  #tốc chạy gốc
#         self.Level = 1 #level tướng A
#         pass
#     def upgrade(self):
#         while self.Level <= 15:
#             time.sleep(30)
#             self.Basic_Hp = self.Basic_Hp + 75
#             self.Basic_Damage = self.Basic_Damage + 10
#             self.Level = self.Level + 1
#     def update(self):
#             self.Current_Run_speed = self.Run_speed + (self.Run_speed * 30) / 100
#     def skill_1(self):
#         Activate_Skill = True        