import sys
import random
import pygame as pg
from tuong.Z import Z
from tuong.S import S


pg.init()
screen = pg.display.set_mode((1280, 800))
display_width = 1280
display_height = 800

xwingImg = pg.image.load('assets/Ships/A.png').convert()
tieImg= pg.image.load('assets/Ships/Z.png').convert()
space=pg.image.load('space2.jpeg').convert()
xbullet = pg.image.load('assets/Attacks/A.png').convert()
BG_image = pg.image.load('space2.jpeg').convert()

players_team1 = []
players_team2 = []

def main():
    clock = pg.time.Clock()
    player_rect = xwingImg.get_rect()
    player_rect.center = (640, 400)
    change_x = 0
    change_y = 0
    enemies = []
    bullets = []
    spawn_counter = 30

    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    bullets.append(xbullet.get_rect(center=player_rect.midtop))
                if event.key == pg.K_d:
                    change_x = 5
                if event.key == pg.K_w:
                    change_y = -5
                if event.key == pg.K_s:
                    change_y= 5
                if event.key == pg.K_a:
                    change_x = -5
            if event.type == pg.KEYUP:
                if event.key == pg.K_d and change_x > 0:
                    change_x = 0
                if event.key == pg.K_a and change_x < 0:
                    change_x = 0
                if event.key == pg.K_w and change_y<0:
                    change_y=0
                if event.key == pg.K_s and change_y>0:
                    change_y=0

        # Spawn enemies if counter <= 0 then reset it.
        spawn_counter -= 1
        if spawn_counter <= 0:
            # Append an enemy rect. You can pass the position directly as an argument.
            enemies.append(tieImg.get_rect(topleft=(random.randrange(1280), -100)))
            spawn_counter =  30

        # Update player_rect.
        player_rect.x += change_x
        player_rect.y += change_y

        # Update bullets.
        for bullet in bullets:
            bullet.y -= 4

        # Detect collisions and move the enemies.
        hit_enemies = []
        for enemy_rect in enemies:
            enemy_rect.y += 5
            # Collision detection with pygame.Rect.colliderect.
            if player_rect.colliderect(enemy_rect):
                done = True
            # Collision detection with bullets.
            for bullet in bullets:
                if bullet.colliderect(enemy_rect):
                    hit_enemies.append(enemy_rect)

        # Filter the destroyed enemies out.
        survivors = []
        for enemy in enemies:
            if enemy not in hit_enemies:
                survivors.append(enemy)
        enemies = survivors  # Now `enemies` is the list of survivors.

        # Draw everything.
        screen.fill((0,0,0))
        for bullet in bullets:
            screen.blit(xbullet, bullet)

        for enemy_rect in enemies:
            screen.blit(tieImg, enemy_rect)
        screen.blit(xwingImg, player_rect)
        if player_rect.x >display_width:
            player_rect.x = 0
        if player_rect.x < 0:
            player_rect.x= 1280
        if player_rect.y>display_height:
            player_rect.y = 0
        if player_rect.y < 0:
            player_rect.y= 800

        pg.display.flip()
        clock.tick(40)


if __name__ == '__main__':
    main()
    pg.quit()
    sys.exit()