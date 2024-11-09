import pygame
import os
from sys import exit

class Player:
    def __init__(self, height, width, xcord, ycord):
        # Initialize instance variables
        self.height = height
        self.width = width
        self.xcord = xcord
        self.ycord = ycord

        # Create surface and rectangle in the correct order
        self.surface = self.make_surface()
        self.rectangle = self.make_rectangle(self.xcord, self.ycord)

    def make_surface(self):
        # Create a Pygame surface using instance width and height
        surface = pygame.Surface((self.width, self.height))  # Set the surface to a new surface
        surface.fill("orange")
        return surface

    # Define where it will spawn in
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
