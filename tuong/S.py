import pygame
import sys
from utils import *
pygame.init()

time = pygame.time.get_ticks()


clock = pygame.time.Clock()
bullets = []
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
class S(Player, pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__(image)
        self.surf_bullet = pygame.image.load("assets/Attacks/S.png").convert()
        self.speed = 2
    def first_skill(enemies, teamates):
        enemies[0].stun(1)
        for teamate in teamates[:3]:
            teamate.temp_health(200, 3)
    def second_skill(enemies):
        for enemy in enemies:
            enemy.stun(3)
            enemy.pushed_away()
    def update(self, left_click, middle_click, right_click):
        super().update(left_click, middle_click, right_click)
        if right_click:
            self.normal_attack("assets/Attacks/S.png", bullets)
        if middle_click:
            pass
S = S('assets\Ships\S.png')
all_sprites = pygame.sprite.Group()
active = True
while active:
    time = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_u:
                S.first_skill()
            if event.key == pygame.K_i:
                S.second_skill()

    left_click, middle_click, right_click = pygame.mouse.get_pressed()
    if not S.is_stunned():
        S.update(left_click, middle_click, right_click)
    for bullet in bullets:
        bullet.update()

    screen.fill((0, 0, 0))
    screen.blit(S.surf, S.rect)
    for bullet in bullets:
        screen.blit(S.surf_bullet, bullet.rect.center)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()