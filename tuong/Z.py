import pygame
import math
import time
from utils import *

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


class make_obj(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.surf = pygame.image.load("ZZ.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(center=pos)

class Projectile(pygame.sprite.Sprite):
    def __init__(self, speed, start_pos, target_pos):
        super().__init__()
        self.surf = pygame.image.load("assets\Attacks\Z.png").convert()
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
        if self.distance != 0:
            new_x = self.rect.centerx + (self.dx / self.distance) * self.speed
            new_y = self.rect.centery + (self.dy / self.distance) * self.speed
        self.rect.center = (new_x, new_y)
        if math.hypot(new_x - self.start_pos_x, new_y - self.start_pos_y) > 200:
            self.kill()

class first_attack(pygame.sprite.Sprite):
    def __init__(self, speed, start_pos, target_pos):
        super().__init__()
        self.surf = pygame.image.load("assets/Skills/Z/0.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(center=start_pos)
        self.speed = speed
        self.start_pos_x = start_pos[0]
        self.start_pos_y = start_pos[1]
        self.dx = target_pos[0] - start_pos[0]
        self.dy = target_pos[1] - start_pos[1]
        self.distance = math.hypot(self.dx, self.dy)
        self.time = time
    def update(self):
        # Calculate the new position of the sprite based on the distance and speed
        time = pygame.time.get_ticks()
        
        if self.distance != 0:
            new_x = self.rect.centerx + (self.dx / self.distance) * self.speed * 3
            new_y = self.rect.centery + (self.dy / self.distance) * self.speed * 3
        self.rect.center = (new_x, new_y)
        obj = make_obj([new_x, new_y])
        all_sprites.add(obj)
        obj_1.add(obj)
        if time - self.time > 750:
            self.kill()
            for obj in obj_1:
                obj.kill()

invisible = False
class Z(Player, pygame.sprite.Sprite):
    def __init__(self):
        super().__init__("assets\Ships\Z.png")
        self.speed = 2
        self.dam = 50
        self.init_dam = self.dam
        self.extra_dam_per_level = 18
        self.second_attack_dam = 0.3 * self.dam
        self.dam_after_second_attack = self.dam
        self.hp = 400
        self.extra_hp_per_level = 60
        self.checkpoint = float('inf')
        self.checkpoint_2 = float('inf')
        self.time = -500
        self.time_2 = -2000
        self.time_3 = -20000

    def normal_attack(self):   
        if time - self.time > 500/self.ats:
            self.time = time
            start_pos = self.rect.center
            target_pos = pygame.mouse.get_pos()
            projectile = Projectile(self.speed * 20, start_pos, target_pos)
            all_sprites.add(projectile)
            normal_attack.add(projectile)


    def first_attack(self):
        if time - self.time_2 > 2000:
            self.time_2 = time
            start_pos = self.rect.center
            target_pos = pygame.mouse.get_pos()
            attack = first_attack(self.speed * 5,start_pos, target_pos)
            all_sprites.add(attack)
            one_attack.add(attack)


    def second_attack(self):
        if time - self.time_3 > 20000:
            self.checkpoint = time
            self.checkpoint_2 = time
            self.speed *= 1.2 # 15s
            self.dam *= 1.5


    def update(self, left_click, middle_click, right_click):
        super().update(left_click, middle_click, right_click)
        self.second_attack_dam = self.dam * 0.3
        if time - self.checkpoint > 15000:
            self.speed = self.speed / 1.2
            self.checkpoint = float('inf')
        if time - self.checkpoint_2 > 1000:
            if self.dam / self.init_dam != 3: 
                self.dam += self.second_attack_dam
                self.checkpoint_2 = time
            else:
                if time - self.checkpoint_2 > 10000:
                    self.dam = self.init_dam


Z = Z()

all_sprites = pygame.sprite.Group()
normal_attack = pygame.sprite.Group()
one_attack = pygame.sprite.Group()
obj_1 = pygame.sprite.Group()
all_sprites.add(Z)

running = True
while running:
    time = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_u:
                Z.first_attack()
            if event.key == pygame.K_i:
                Z.second_attack()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Mouse button down")
            print(time)
        elif event.type == pygame.MOUSEBUTTONUP:
            print("Mouse button up")
        elif event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # print(f"Mouse position: ({mouse_x}, {mouse_y})")
            left_click, middle_click, right_click = pygame.mouse.get_pressed()
            if left_click:
                
                print("Left mouse button pressed")
            if right_click:
                Z.normal_attack()
            if middle_click:
                Z.first_attack()
    # Get all the keys currently pressed
    left_click, middle_click, right_click = pygame.mouse.get_pressed()

    # Update the player sprite based on user keypresses
    Z.update(left_click, middle_click, right_click)
    if right_click:
        Z.normal_attack()
    
    screen.fill((0, 0, 0))
    normal_attack.update()
    one_attack.update()
    # Draw all sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    pygame.display.update()

    clock.tick(30)

pygame.quit()