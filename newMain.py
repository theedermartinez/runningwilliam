import pygame
import os
from player import Player
from asteroid import Asteroid
import random


#enviroment methods
def environment1(screen,player1,gravity,timer,asteroids_list, number_asteroids):
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

    #asteroid make and put in the array with random attributes
    
    
    if len(asteroids_list)< 5:
        
        #create asteroid and add it 
        new_asteroid_object = Asteroid(5, random.randint(800,1000),random.randint(1,400), "Images/Asteroids/asteroid_1_good.png") #create a new asteroid with random location
        #new_asteroid_object = Asteroid(5,100, 100,"Images/Asteroids/asteroid_1.png")
        #new_asteroid_object = Asteroid(5,random.randint(1,400), 200, "Images/Asteroids/asteroid_1.png") #create a new asteroid with random location

        asteroids_list.append(new_asteroid_object)
        

    for x in asteroids_list:
        screen.blit(x.get_surface(), x.get_rectangle())
        x.set_x(-5)
        print("in print asterorid")
        print(x.get_rectangle().x)
        if(x.get_rectangle().right < 0):
            asteroids_list.remove(x)

    ##move asteroid 
        

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



def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((800, 400))

    # Create a Player instance
    player1 = Player(100, 100, 100, 200, "Images/Player/william_movement1.png")
    gravity = 0
    game_time = 300 #60 seconds per plannet 
    game_time_seconds = 0; #helps counter 
    asteroids_list = [] #holds asteroids that will be used 
    life = 100 #start with 100 life

    while True:
        for event in pygame.event.get():
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
            environment1(screen,player1,gravity, game_time,asteroids_list,2)
        
        
        # Update the display
        pygame.display.update()
        clock.tick(60)

main()






    