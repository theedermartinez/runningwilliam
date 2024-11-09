import pygame
from player import Player

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((800, 400))

    # Create a Player instance
    player1 = Player(100, 100, 300, 300)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


        # Draw the player surface at the rectangle's position
        screen.blit(player1.get_surface(), (0,0))
        screen.blit(screen)
        
        # Update the display
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()

def environment1(screen):
    background = pygame.image.load('images/')
    screen.blit()
    