import pygame
import os
from sys import exit

class Player:
    #global variables 
    global width
    global height
    global player_type

    def __init__(self, player_type, height, width) :
        # Initialize instance variables
        self.player_type = player_type
        self.height = height
        self.width = width


    def select(self):
        # Define the selection logic based on player type
        if self.player_type == "1":
            # Set attributes or logic for type "1"
            print("Setting player to type one.")
        else:
            # Set attributes or logic for other types
            print("Setting player to type two.")

    def make_surface(width, height):
        # Creating a Pygame surface using instance width and height
        return pygame.Surface(width * height);


    #define player hit box
    def make_rectangle(object,xcord,ycord):
        rect = object.get_rect(midbottom == (xcord,ycord))
        return rect

