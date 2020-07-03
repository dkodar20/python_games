import pygame
import random
from Player import Player
from enemy import Enemy
from bullet import Bullet
from score import Score
from pygame import mixer


pygame.init()

screen = pygame.display.set_mode((800, 600))    # this will display a screen

background = pygame.image.load('background.png')
# background sound
mixer.music.load('background.wav')
mixer.music.play(-1)

pygame.display.set_caption("Space Invader")
icon = pygame.image.load('alien.png')
pygame.display.set_icon(icon)

# score
score = Score(10, 10, 32)
final_score = Score(200, 250, 64)

# player
player = Player(370, 480)
player_x_change = 0

# enemy
enemy = []
for i in range(5):
    enemy.append(Enemy(random.randint(0, 736), random.randint(0, 150)))

# bullet
bullet = []
for i in range(5):
    bullet.append(Bullet(370, 480))

# just to make collison function small
def coll(bullet_func, enemy_func):
    return bullet_func.collision(enemy_func.x, enemy_func.y)

temp_player_x = [None, None, None, None, None]
running = True
while running:
    screen.blit(background, (0, 0))
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -5
            if event.key == pygame.K_RIGHT:
                player_x_change = 5
            if event.key == pygame.K_UP:
                for i in range(5):
                    if bullet[i].state == "ready":
                        bullet_sound = mixer.Sound('laser.wav')
                        bullet_sound.play()
                        temp_player_x[i] = player.x
                        bullet[i].state = "fire"
                        bullet[i].fire_bullet(screen, temp_player_x[i])
                        break

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    # player movement
    player.move_player(player_x_change)

    # enemy movement
    for i in range(5):
        enemy[i].move_enemy()
        if enemy[i].y >= 440:
            for j in range(5):
                enemy[j].y = 2000
            final_score.show_score(screen)
            break


    for i in range(5):
        if bullet[i].state == "fire":
            bullet[i].fire_bullet(screen, temp_player_x[i])
        for j in range(5):
            if coll(bullet[i], enemy[j]):
                coll_sound = mixer.Sound('explosion.wav')
                coll_sound.play()
                score.score_val += 10
                final_score.score_val += 10
                bullet[i].x, bullet[i].y = player.x, 480
                enemy[j].x, enemy[j].y = random.randint(0, 736), random.randint(0, 150)
                bullet[i].state = "ready"
        if bullet[i].goes_out():
            bullet[i].x = player.x
            bullet[i].y = 480
            bullet[i].state = "ready"

    # score display
    score.show_score(screen)

    # player display
    player.display_player(screen)

    # enemy display
    for i in range(5):
        enemy[i].display_enemy(screen)

    pygame.display.update()