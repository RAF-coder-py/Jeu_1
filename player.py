import pygame as py

image_player = py.image.load('pictures/NyanCat.webp')

class Player:

    def __init__(self, name:str = 'ghost', velocity:int = 7):
        self.name = name
        self.image = py.transform.scale(image_player, (70, 85))
        self.sol = 445
        self.rect = self.image.get_rect()
        self.rect.y = self.sol
        self.rect.x = 250
        self.jump_height = 15
        self.velocity_x = velocity
        self.velocity_y = self.jump_height
        self.gravity = 1
        self.jumping = False

    def turn(self, rotation:bool = True):
        self.image = py.transform.flip(self.image, rotation, False)

    def jump(self):
        self.rect.y -= self.velocity_y
        self.velocity_y -= self.gravity

        if self.rect.y >= self.sol:
            self.jumping = False
            self.velocity_y = self.jump_height
            self.rect.y = self.sol