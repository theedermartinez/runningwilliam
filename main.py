import pygame
from sys import exit
import os

class Maingame:
    def main():
        pygame.init()
        see = pygame.display.set_mode(1600,800)
        clock = pygame.time.Clock()
        pygame.display.set_caption("Hello")
        game_running = True