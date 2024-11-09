import pygame
import os
from sys import exit

class Player:
    def __init__(self, height, width, xcord, ycord, frameimg):
        # Initialize instance variables
        self.height = height
        self.width = width
        self.xcord = xcord
        self.ycord = ycord
        self.frameimg = frameimg
        # Create surface and rectangle in the correct order
        self.surface = self.make_surface()
        self.rectangle = self.make_rectangle(self.xcord, self.ycord)

        os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # the image itself
    def make_surface(self):
        # Create a Pygame surface using instance width and height
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        surface = pygame.image.load(self.frameimg)  # Set the surface to a new surface
        
        return surface

    # the rectangle class to allow positoins 
    def make_rectangle(self, xcord, ycord):
        # Now that self.surface is created, we can use it to create the rectangle
        return self.surface.get_rect(midbottom=(xcord, ycord))

    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height
    
    def get_surface(self):
        return self.surface
    
    def get_rectangle(self):
        return self.rectangle
    
    def set_x(self,mod_num):
        num = 0
        self.rectangle.x += mod_num

    def set_y(self, mod_num):
        self.rectangle.y += mod_num
    
    def apply_gravity(self, gravity):
       
        self.rectangle.y += gravity
