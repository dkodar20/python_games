import pygame


class Enemy():


    def __init__(self, enemy_x, enemy_y):
        
        self.enemy_img = pygame.image.load('alien-monster-1.png')
        self.x = enemy_x
        self.y = enemy_y
        self._x_change = 4

    def move_enemy(self):
        if self.x < -64:
            self._x_change = 4
            self.y += 55
        elif self.x > 800:
            self._x_change = -4
            self.y += 55
        self.x += self._x_change

    def display_enemy(self, screen):
        screen.blit(self.enemy_img, (self.x, self.y))

