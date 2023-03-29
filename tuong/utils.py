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

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


class Projectile(pygame.sprite.Sprite):
    def __init__(self, speed, start_pos, target_pos, image):
        super().__init__()
        self.surf = pygame.image.load(image).convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(center=start_pos)
        self.speed = speed
        self.start_pos_x = start_pos[0]
        self.start_pos_y = start_pos[1]
        self.dx = target_pos[0] - start_pos[0]
        self.dy = target_pos[1] - start_pos[1]
        self.distance = math.hypot(self.dx, self.dy)
    def update(self):
        # Calculate the new position of the sprite based on the distance and speed
        # new_x = self.rect.centerx
        # new_y = self.rect.centery
        if self.distance != 0:
            new_x = self.rect.centerx + (self.dx / (self.distance)) * self.speed
            new_y = self.rect.centery + (self.dy / (self.distance)) * self.speed
        else:
            new_x = 0
            new_y = 0
        self.rect.center = (new_x, new_y)
        if math.hypot(new_x - self.start_pos_x, new_y - self.start_pos_y) > 200:
            self.kill()

class Player():
    def __init__(self, image):
        self.x = 960
        self.y = 540
        self.ats = 1
        self.extra_ats = 1
        self.extra_hp = 0
        self.extra_speed = 0
        self.extra_dam = 0
        self.hp_lost = 0
        self.equipment = []
        self.level = 1
        self.max_level = 10
        super(Player, self).__init__()
        self.surf = pygame.image.load(image).convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        # self.surf = pygame.Surface((75,25))
        self.rect = self.surf.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.angle = 0
        self.speed = 2
        self.stunned = False
        self.stunned_time = 0
        self.time = -500
    def level_up(self, lvlup_health, lvlup_atk):
        if self.level < self.max_level:
            self.level += 1
            self.health += lvlup_health
            self.max_health += lvlup_health
            self.atk += lvlup_atk
    def temp_health(self, health, duration):
        original_health = self.health
        self.health += health
        if self.health >= original_health:
            self.health = original_health

    def is_stunned(self):
        if self.stunned and time.time() < self.stunned_time:
            return True
        else:
            self.stunned = False
            return False
        
    def stun(self, duration):
        self.stunned = True
        self.stunned_time = time.time() + duration

    #mua do
    def buy(self, equip):
        # class equipment: price, atk, hp, ats, spd; 
        if self.money >= equip.price:
            self.monney -= equip.price
            self.equipment.append(equip)

    
    #di chuyen
    
    def draw(self, win):
        # print(self.x, self.y)
        cx, cy = pygame.mouse.get_pos()
        dx, dy = cx - self.x, cy - self.y
        if abs(dx) > 0 or abs(dy) > 0:
            cx, cy = pygame.mouse.get_pos()
            dx, dy = cx - self.x, cy - self.y
            if abs(dx) > 0 or abs(dy) > 0:
                self.angle = math.atan2(-dx, -dy)*57.2957795

            img_copy = pygame.transform.rotate(self.surf, self.angle)
            rotated_rect = img_copy.get_rect(center = (round(self.x), round(self.y)))
            
            win.blit(img_copy, rotated_rect)

    def move(self):
        cx, cy = pygame.mouse.get_pos()
        dx, dy = cx - self.x, cy - self.y
        if abs(dx) > self.speed * 10 or abs(dy) > self.speed * 10:
            dist = math.hypot(dx, dy)
            self.x += min(dist, self.speed) *10*dx/dist
            self.y += min(dist, self.speed) *10*dy/dist
            self.rect.center = (round(self.x), round(self.y))
        if abs(dx) < 10 and abs(dy) < 10:
            self.rect.center = (self.x,self.y)
    def update(self, left_click, middle_click, right_click):
        if left_click:
            pass

        if right_click:
            # Z.normal_attack()
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Calculate the angle between the player's position and the mouse position
            dx = mouse_x - self.rect.centerx
            dy = mouse_y - self.rect.centery

            distance = math.hypot(dx, dy)
            if dx != 0 and dy != 0:    
                self.rect.move_ip((200*self.speed * dx/50)/distance,(200*self.speed * dy/50)/distance)
            elif dx == 0 and dy == 0:
                self.rect.center = pygame.mouse.get_pos()
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

# Setup the clock for a decent framerate