import pygame as py

image = py.image.load('pictures/NyanCat.webp')

class Player:

    def __init__(self, name:str = 'ghost', velocity:int = 2):
        self.name = name
        self.velocity = velocity
        self.velocity_y = -4
        self.acceleration_y = 0.5
        self.image = py.transform.scale(image, (50, 60))
        self.rect = self.image.get_rect()
        self.position_y = self.rect.y + 460
        


    def turn(self, rotation:bool = True):
        self.image = py.transform.flip(self.image, rotation, False)

    def jump(self):
        self.rect.y += self.velocity_y
        self.velocity_y += self.acceleration_y
        self.position_y = self.rect.y + 460
