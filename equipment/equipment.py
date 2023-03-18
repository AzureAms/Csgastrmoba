
import pygame
from pygame.locals import *
pygame.init()
from utils import *

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


money = 0
atk = 0 #sat thuong
hp = 0 #mau 
ats = 0 #toc danh (%) 
spd = 0 #toc chay 


class Equipment(pygame.sprite.Sprite): 
    def __init__(self, price, atk, hp, ats, spd): 
        super(Equipment, self).__init__() 
        #self.surf = pygame.image.load(link) 
        self.price = price 
        self.atk = atk 
        self.hp = hp 
        self.ats = ats
        self.spd = spd
player = Player(money, atk, hp, ats, spd)


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


thuong_longinus = Equipment(2030, 80, 500, 0, 0) 

kiem_fafnir = Equipment(2040, 60, 0, 30, 0) 

thanh_kiem = Equipment(2120, 90, 0, 0, 0) #khong chi mang -> phe 

kiem_muramasa = Equipment(2020, 75, 0, 0, 0) 

quy_kiem = Equipment(1740, 100, 0, 0, 0) #khong hut mau -> phe 

phuc_hop_kiem = Equipment(2150, 70, 400, 15, 0) 

guom_sam_set = Equipment(1780, 50, 0, 35, 1.05)

song_dao_bao_tap = Equipment(1920, 0, 0, 35, 1.07) 

nanh_fenrir = Equipment(2950, 200, 0, 0, 0)

cung_ta_ma = Equipment(2300, 90, 0, 0, 0) 

vuot_hung_tan = Equipment(1960, 0, 0, 30, 1.05)

thuong_xuyen_pha = Equipment(2020, 110, 0, 0, 0) 

ngoc_dai_phap_su = Equipment(2010, 140, 0, 0, 0) 

truong_bung_no = Equipment(2000, 240, 0, 0, 0) 

mat_na_berith = Equipment(2120, 140, 225, 0, 0) 

truong_bang = Equipment(2020, 140, 850, 0, 1.05) 

bang_nhan_skadi = Equipment(2150, 160, 500, 0, 0) 

xuyen_tam_lenh = Equipment(1980, 120, 500, 0, 0) 

qua_cau_bang_suong = Equipment(2000, 220, 0, 0, 0)

vuong_mien_hecate = Equipment(2300, 200, 0, 0, 0) 

quyen_truong_rhea = Equipment(2220, 140, 0, 0, 0) 

guom_tan_the = Equipment(2190, 200, 0, 0, 0) 

guom_hien_triet = Equipment(2100, 140, 1050, 0, 0) 

thap_tu_kiem = Equipment(1970, 180, 0, 0, 1.08) 

sach_thanh = Equipment(2990, 400, 1400, 0, 0) 

ao_choang_than_ra = Equipment(1950, 0, 1200, 0, 0) 

khien_huyen_thoai = Equipment(2180, 0, 360, 0, 0) 

ao_choang_bang_gia = Equipment(1970, 0, 1000, 0, 0) 

giap_thong_kho = Equipment(1940, 0, 1500, 0, 0) 

riu_hyoga = Equipment(1920, 0, 1400, 0, 0) 

giap_gaia = Equipment(1960, 0, 1440, 0, 1.05) 

khien_that_truyen = Equipment(2100, 0, 1560, 0, 0) 

huan_chuong_troy = Equipment(2320, 0, 1360, 0, 0) 

phu_chu_truong_sinh = Equipment(1980, 0, 1800, 0, 0) 

thuan_nham_thach = Equipment(1980, 0, 1300, 0, 0) 

giap_ho_menh = Equipment(2400, 200, 120, 0, 0) #atk +10% ?

giay_ho_ve = Equipment(700, 0, 110, 0, 60) 

giay_kien_cuong = Equipment(690, 0, 100, 0, 60) 

giay_phu_thuy = Equipment(710, 75, 0, 0, 60) 

giay_du_muc = Equipment(660, 0, 0, 25, 60) 

giay_hermes = Equipment(580, 0, 0, 0, 120) 
