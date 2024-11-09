import pygame
import os
from sys import exit

class Player:
   
    def __init__(self, height, width,xcord,ycord):
        # Initialize instance variables
        self.height = height
        self.width = width
        self.surface = None  # Initialize surface variable
        self.rectangle = None # to be returned 
        self.xcord = xcord
        self.ycord = ycord

        self.make_rectangle(self.xcord,self.ycord)
        self.make_surface()
    

    def make_surface(self):
        # Create a Pygame surface using instance width and height
        self.surface = pygame.Surface((self.width, self.height))  # Set the surface to a new surface
        self.surface.fill("orange")
        return self.surface

    # Define where it will spawn in
    def make_rectangle(self, xcord, ycord):
       rectangle = self.surface.get_rect(midbottom = (xcord,ycord))

    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height
    
    def get_surface(self):
       return self.surface
    
    def get_rectangle(self):
        return self.rectangle
