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
start_pos = (540,960)
class S(Player, pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__(image)
        self.surf_bullet = pygame.image.load("assets/Attacks/S.png").convert()
        self.speed = 2
    def normal_attack(self, image, bullets):   
        if time - self.time > 500:
            self.time = time
            start_pos = self.rect.center
            target_pos = pygame.mouse.get_pos()
            projectile = Projectile(self.speed * 20, start_pos, target_pos, image)
            bullets.append(projectile)
    def first_skill(self, enemies, teamates):
        closest_enemy = None
        closest_distance = float('inf')
        for enemy in enemies:
            distance = ((enemy.x - self.x) ** 2 + (enemy.y - self.y) ** 2)
            if distance < closest_distance:
                closest_enemy = enemy
                closest_distance = distance
        if closest_enemy is not None:
            closest_enemy.stun(1)
        for teamate in teamates[:3]:
            teamate.temp_health(200, 3)
    def second_skill(self, enemies):
        for enemy in enemies:
            d = ((enemy.x-self.x)**2+(enemy.y-self.y)**2)
            if d <= 10:
                angle = math.atan2(enemy.y - self.y, enemy.x - self.x)
                enemy.x += 20 * math.cos(angle + math.pi / 3)
                enemy.y += 20 * math.sin(angle + math.pi / 3)
                enemy.stun(3)
    def update(self, left_click, middle_click, right_click):
        super().update(left_click, middle_click, right_click)
        if right_click:
            self.move()
        if left_click:
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
    for bullet in bullets:
        screen.blit(S.surf_bullet, bullet.rect.center)

    S.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()