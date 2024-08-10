import pygame as py

image_fire = py.image.load('pictures/fire.png')

class Fire:

    def __init__(self):
        self.image = py.transform.scale(image_fire, (20, 20))