import pygame as py

image = py.image.load('pictures/NyanCat.webp')

class Player:

    def __init__(self, name:str = 'ghost', velocity:int = 2):
        self.name = name
        self.velocity_x = velocity
        self.image = py.transform.scale(image, (50, 60))
        self.rect = self.image.get_rect()
        self.sol = 460
        self.rect.y = self.sol
        self.rect.x = 250
        self.sol = 460
        self.jump_height = 20
        self.velocity_y = 5
        self.gravity = 1


    def turn(self, rotation:bool = True):
        self.image = py.transform.flip(self.image, rotation, False)

    def jump(self):
        self.rect.y -= self.velocity_y
        self.velocity_y -= self.gravity
        if self.rect.y >= self.sol:
            self.velocity_y = self.jump_height
            self.rect.y = self.sol
            jumping = False
