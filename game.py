import pygame as py
from player import Player

class Game:



    def __init__(self, width:int = 1080, height:int = 720):
        self.player = Player()
        self.screen = py.display.set_mode((width, height))
        self.screen_rect = self.screen.get_rect()

    def draw_player(self):
        self.screen.blit(self.player.image, (self.player.rect.x, self.player.rect.y))

    def player_move_right(self):
    # if self.player.rect.x < self.screen_rect.x - self.player.rect.x:
        self.player.rect.x += self.player.velocity_x

    def player_move_left(self):
    # if self.player.rect.x > 0:
        self.player.rect.x -= self.player.velocity_x
        

