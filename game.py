import pygame as py
from player import Player
from rectangles import White_Rectangle, Green_Rectangle

class Game:


    def __init__(self, width:int = 1080, height:int = 720):
        self.player_1 = Player()
        self.player_2 = Player()
        self.screen = py.display.set_mode((width, height))
        self.screen_rect = self.screen.get_rect()
        self.w_rectangle = White_Rectangle()
        self.g_rectangle = Green_Rectangle()

    def draw_player(self):
        self.screen.blit(self.player_1.image, (self.player_1.rect.x, self.player_1.rect.y))

    def player_move_right(self, player):
        if self.player_1.rect.x <= 1030:
            self.player_1.rect.x += self.player_1.velocity_x

    def player_move_left(self, player):
        if self.player_1.rect.x >= -10:
            self.player_1.rect.x -= self.player_1.velocity_x

    def draw_rectangle(self, player):
        py.draw.rect(self.screen, self.w_rectangle.color, (player.rect.x-3, player.rect.y - 33, self.w_rectangle.length, self.w_rectangle.height))
        py.draw.rect(self.screen, self.g_rectangle.color, (player.rect.x, player.rect.y - 30, int((player.health/player.original_health)*self.g_rectangle.length), self.g_rectangle.height))