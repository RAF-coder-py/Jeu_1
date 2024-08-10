import pygame as py

image = py.image.load('pictures/NyanCat.webp')

class Player:

    def __init__(self, name:str = 'ghost', velocity:int = 5):
        self.name = name
        self.image = py.transform.scale(image, (50, 60))
        self.sol = 460
        self.rect = self.image.get_rect()
        self.rect.y = self.sol
        self.rect.x = 250
        self.sol = 460
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