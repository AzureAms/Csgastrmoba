import pygame
import math
import time

pygame.init()

time = pygame.time.get_ticks()

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Setup the clock for a decent framerate
clock = pygame.time.Clock()

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Player():
    def __init__(self, image):
        self.ats = 1
        self.extra_ats = 1
        self.extra_hp = 0
        self.extra_speed = 0
        self.extra_dam = 0
        self.hp_lost = 0
        self.equipment = []
        self.level = 1
        super(Player, self).__init__()
        self.surf = pygame.image.load(image).convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        # self.surf = pygame.Surface((75,25))
        self.rect = self.surf.get_rect()
        self.angle = 0
        self.speed = 2
    
    #mua do
    def buy(self, equip):
        # class equipment: price, atk, hp, ats, spd; 
        if self.money >= equip.price:
            self.monney -= equip.price
            self.equipment.append(equip)
    
    #di chuyen
    def update(self, left_click, middle_click, right_click):
        if left_click:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Calculate the angle between the player's position and the mouse position
            dx = mouse_x - self.rect.centerx
            dy = mouse_y - self.rect.centery

            distance = math.hypot(dx, dy)
            if dx != 0 and dy != 0:    
                self.rect.move_ip((200*self.speed * dx/50)/distance,(200*self.speed * dy/50)/distance)
            elif dx == 0 and dy == 0:
                self.rect.center = pygame.mouse.get_pos()

        if right_click:
            pass
        if middle_click:
            pass

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

        #update hp, atk, ...
        self.extra_hp = sum([equip.hp for equip in self.equipment])
        self.extra_atk = sum([equip.atk for equip in self.equipment])
        self.extra_spd = sum([equip.spd for equip in self.equipment])
        self.ats = sum([equip.ats for equip in self.equipment])

# money = 0
# atk = 0 #sat thuong
# hp = 0 #mau 
# ats = 0 #toc danh (%) 
# spd = 0 #toc chay 