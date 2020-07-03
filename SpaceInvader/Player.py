import pygame


class Player():

    def __init__(self, player_x, player_y):
        
        self.player_img = pygame.image.load('spaceship.png')
        self.x = player_x
        self.y = player_y


    def move_player(self, x_change):
        self.x += x_change
        if self.x < -64:
            self.x = 800
        elif self.x > 800:
            self.x = -64

    def display_player(self, screen):
        screen.blit(self.player_img, (self.x, self.y))