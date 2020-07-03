import pygame
import math


class Bullet():

    def __init__(self, bullet_x, bullet_y):
        
        self.bullet_img = pygame.image.load('bullet-1.png')
        self.x = bullet_x
        self.y = bullet_y
        self.state = "ready"


    def fire_bullet(self, screen, player_x):
        self.y -= 5
        screen.blit(self.bullet_img, (player_x + 16, self.y))

    def collision(self, enemy_x, enemy_y):
        dist = math.sqrt((enemy_x - self.x)**2 + (enemy_y - self.y)**2)
        if dist <= 32:
            return True
        return False

    def goes_out(self):
        if self.y <= 0:
            return True
        return False