import pygame


class Score():

    def __init__(self, x_coord, y_coord, font_size):
        
        self._x = x_coord
        self._y = y_coord
        self.score_val = 0
        self._font = pygame.font.Font('freesansbold.ttf', font_size)

    def show_score(self, screen):
        score = self._font.render("Score : {}".format(self.score_val), True, (255, 255, 255))
        screen.blit(score, (self._x, self._y))
