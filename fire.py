import pygame as py

image_fire = py.image.load('pictures/fire.png')

class Fire(py.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = py.transform.scale(image_fire, (25, 25))
        self.rect = image_fire.get_rect()
        self.velocity = 15