import pygame
import os
from sys import exit

class Asteroid:
    def __init__(self, radius, xcord, ycord, frameimg):
        self.radius = radius
        self.xcord = xcord
        self.ycord = ycord
        self.frameimg = frameimg

        self.surface = self.make_surface()
        self.rectangle = self.make_rectangle(self.xcord, self.ycord)
    
    def make_surface(self):
        # Create a Pygame surface using instance width and height
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        self.surface = pygame.image.load(self.frameimg)  # Set the surface to a new surface
        return self.surface

    # the rectangle class to allow positoins 
    def make_rectangle(self, xcord, ycord):
        # Now that self.surface is created, we can use it to create the rectangle
        return self.surface.get_rect(center = (xcord,ycord) )
    
    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height
    
    def get_surface(self):
        return self.surface
    
    def get_rectangle(self):
        return self.rectangle
    
    def set_x(self,mod_num):
        self.rectangle.x += mod_num
    
    def special_x(self, mod_num):
        self.rectangle.x
    
    