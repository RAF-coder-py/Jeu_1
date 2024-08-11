import pygame as py


class Rectangle(py.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.color = (54, 238, 54)
        self.length = 70 #length of player
        self.height = 20 #height of player
