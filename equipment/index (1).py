
import pygame
from pygame.locals import *
pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))



price = 0
atk = 0 #sat thuong
hp = 0 #mau 
ats = 0 #toc danh (%) 
spd = 0 #toc chay 

lendo = [] 





class Equipment(pygame.sprite.Sprite): 
    def __init__(self, price, atk, hp, ats, spd): 
        super(Equipment, self).__init__() 
        #self.surf = pygame.image.load(link) 
        self.price = price 
        self.atk = atk 
        self.hp = hp 
        self.ats = ats
        self.spd = spd


thuong_longinus = Equipment(2030, 80, 0, 15, 500, 0, 0) 

kiem_fafnir = Equipment(2040, 60, 0, 0, 0, 30, 0) 

thanh_kiem = Equipment(2120, 90, 0, 0, 0, 0, 0)

kiem_muramasa = Equipment(2020, 75, 0, 10, 0, 0, 0) 

quy_kiem = Equipment(1740, 100, 0, 0, 0, 0, 0) 

phuc_hop_kiem = Equipment(2150, 70, 0, 10, 400, 15, 0) 

guom_sam_set = Equipment(1780, 50, 0, 0, 0, 35, 1.05)

song_dao_bao_tap = Equipment(1920, 0, 0, 0, 0, 35, 1.07) 

nanh_fenrir = Equipment(2950, 200, 0, 0, 0, 0, 0)

cung_ta_ma = Equipment(2300, 90, 0, 0, 0, 0, 0) 

vuot_hung_tan = Equipment(1960, 0, 0, 0, 0, 30, 1.05)

thuong_xuyen_pha = Equipment(2020, 110, 0, 0, 0, 0, 0) 

ngoc_dai_phap_su = Equipment(2010, 0, 140, 10, 0, 0, 0) 

truong_bung_no = Equipment(2000, 0, 240, 0, 0, 0, 0) 

mat_na_berith = Equipment(2120, 0, 140, 10, 225, 0, 0) 

truong_bang = Equipment(2020, 0, 140, 0, 850, 0, 1.05) 

bang_nhan_skadi = Equipment(2150, 0, 160, 0, 500, 0, 0) 

xuyen_tam_lenh = Equipment(1980, 0, 120, 10, 500, 0, 0) 

qua_cau_bang_suong = Equipment(2000, 0, 220, 0, 0, 0, 0)

vuong_mien_hecate = Equipment(2300, 200, 0, 0, 0, 0, 0) 

quyen_truong_rhea = Equipment(2220, 0, 140, 10, 0, 0, 0) 

guom_tan_the = Equipment(2190, 0, 200, 10, 0, 0, 0) 

guom_hien_triet = Equipment(2100, 0, 140, 0, 1050, 0, 0) 

thap_tu_kiem = Equipment(1970, 0, 180, 0, 0, 0, 1.08) 

sach_thanh = Equipment(2990, 0, 400, 0, 1400, 0, 0) 

ao_choang_than_ra = Equipment(1950, 0, 0, 0, 1200, 0, 0) 

khien_huyen_thoai = Equipment(2180, 0, 0, 20, 360, 0, 0) 

ao_choang_bang_gia = Equipment(1970, 0, 0, 10, 1000, 0, 0) 

giap_thong_kho = Equipment(1940, 0, 0, 0, 1500, 0, 0) 

riu_hyoga = Equipment(1920, 0, 0, 0, 1400, 0, 0) 

giap_gaia = Equipment(1960, 0, 0, 0, 1440, 0, 1.05) 

khien_that_truyen = Equipment(2100, 0, 0, 0, 1560, 0, 0) 

huan_chuong_troy = Equipment(2320, 0, 0, 10, 1360, 0, 0) 

phu_chu_truong_sinh = Equipment(1980, 0, 0, 0, 1800, 0, 0) 

thuan_nham_thach = Equipment(1980, 0, 0, 0, 1300, 0, 0) 

giap_ho_menh = Equipment(2400, 100, 100, 0, 120, 0, 0) #chien luc +10% 

giay_ho_ve = Equipment(700, 0, 0, 0, 110, 0, 60) 

giay_kien_cuong = Equipment(690, 0, 0, 0, 100, 0, 60) 

giay_thuat_si = Equipment(710, 0, 0, 15, 0, 0, 60) 

giay_phu_thuy = Equipment(710, 0, 75, 0, 0, 0, 60) 

giay_du_muc = Equipment(660, 0, 0, 0, 0, 25, 60) 

giay_hermes = Equipment(580, 0, 0, 0, 0, 0, 120) 








#price, stvl, stp, ghc, m, td, tc
class Player(pygame.sprite.Sprite): 
    def __init__(self, money, atk, hp, ats, spd): 
        super(Player, self).__init__() 
        self.surf = pygame.Surface((20, 20)) 
        self.surf = pygame.image.load('girl.png')  
        self.money = 0 
        self.atk = atk 
        self.hp = hp 
        self.ats = ats
        self.spd = spd
        self.equip = []

    def buy(self, equip):
        """
        class equipment: price, atk... rồi

        """
        if self.money >= equip.price:
            self.monney -= equip.price
            self.equip.append(equip)
        
    def update(self):
        temp_hp = 0
        temp_atk = 0
        temp_spd = 0
        temp_ats = 0
        for i in self.equip:
            temp_hp += i.hp
            temp_atk += i.atk
            temp_spd += i.spd
            temp_ats += i.ats
        self.hp = temp_hp + basic_hp


player = Player(price, stvl, stp, ghc, m, td, tc)

player.buy(thuong_longinus)

running = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Draw the player on the screen
    screen.blit(player.surf, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))


    # Update the display
    pygame.display.update()









