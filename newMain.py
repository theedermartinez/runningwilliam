import pygame
import os
from player import Player



#enviroment methods
def environment1(screen,player1,gravity,timer):
    ##change path to be in the right place
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    #os.chdir() #change working directory

    ##build background
    background = pygame.image.load('Images/Backgrounds/Mercury.png')
    screen.blit(background,(0,0)) #will not have collisions

    ##build total time left 
    write_text(screen, "Time left" + str(timer), 300,100 )

    ##add text to home screen
    write_text(screen, "Running William",10,10)

    #set gravity
    gravity +=1
    player1.apply_gravity(gravity)

    #set smooth movement 

    screen.blit(player1.get_surface(), player1.get_rectangle())





#helper methods
def write_text(screen, text,xcord,ycord):
    ##create the font then write on a surface, blits the surface
    font = pygame.font.Font(None, 50) #create the font
    text_surface = font.render(text, False, "orange")
    screen.blit(text_surface, (xcord,ycord))


def make_platform()

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((800, 400))

    # Create a Player instance
    player1 = Player(100, 100, 100, 200, "Images/Player/william_movement1.png")
    gravity = 0
    game_time = 300 #60 seconds per plannet 
    game_time_seconds = 0;

    while True:
        for event in pygame.event.get()
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            #check events 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    #jump
                    player1.set_x(15)
                if event.key == pygame.K_a:
                    player1.set_x(-15)
                if event.key == pygame.K_SPACE:
                    gravity = -5
                    
        




        # Draw the player surface at the rectangle's position
        screen.blit(player1.get_surface(), (0,0))
        #screen.blit(screen)
        ###reduce time resets our internal counter ###
        game_time_seconds+=1

        if game_time_seconds >= 60:
            game_time -=1
            game_time_seconds = 0
        
        print(game_time)
        if game_time >= 240: 
            gravity +=0.15
            environment1(screen,player1,gravity, game_time)
        
        # Update the display
        pygame.display.update()
        clock.tick(60)

main()






    