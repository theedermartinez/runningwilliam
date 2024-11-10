import pygame
import os
from player import Player
from asteroid import Asteroid
import random


##text stays up for 10 seconsd: 290, etc e.m
#enviroment methods
def environment1(screen,player1,gravity,timer,asteroids_list, number_asteroids,life):
    ##change path to be in the right place
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    #os.chdir() #change working directory

    ##build background
    background = pygame.image.load('Images/Backgrounds/Mercury.png')
    screen.blit(background,(0,0)) #will not have collisions

    ##build total time left 
    write_text("white",20,screen, "Time left: " + str(timer), 300,0)

    ##add text to home screen
    write_text("white",20,screen, "Running William",0,0,)

    ##intro text && plannet
    if(timer >290):
        write_text("white",30,screen, "use Space Bar, A and D to move",100,300)
        write_text("white",30,screen, "Welcome to Mercury",100,350)

    #asteroid make and put in the array with random attributes
    
    
    if len(asteroids_list)< number_asteroids:
        
        #create asteroid and add it 
        new_asteroid_object = Asteroid(5, random.randint(800,1000),random.randint(1,400), "Images/Asteroids/asteroid_1_good.png") #create a new asteroid with random location
        #new_asteroid_object = Asteroid(5,random.randint(1,400), 200, "Images/Asteroids/asteroid_1.png") #create a new asteroid with random location

        asteroids_list.append(new_asteroid_object)
        

    for x in asteroids_list:
        special_move_counter = random.randint(0,100)
        screen.blit(x.get_surface(), x.get_rectangle())
        x.set_x(-5)

        #print("in print asterorid")
        life = check_col(player1,x,life)

        #check out of bounds 
        
        life = check_bounds(player1,life)
        #print(x.get_rectangle().x)
        if(x.get_rectangle().right < 0):
            asteroids_list.remove(x)

    ##move asteroid 

    #display health
    write_text("white",20,screen, f"Life Remainding: {life:.2f} %",500,0)

    #set gravity
    gravity +=1
    player1.apply_gravity(gravity)

    #set smooth movement 

    screen.blit(player1.get_surface(), player1.get_rectangle())
    return life


    
    
#helper methods
def write_text(color,size,screen, text,xcord,ycord):
    ##create the font then write on a surface, blits the surface
    font = pygame.font.Font("Fonts/speedy-font/SpeedyRegular-7BLoE.ttf", size) #create the font
    text_surface = font.render(text, False, color)
    screen.blit(text_surface, (xcord,ycord))

def check_col(mc, obj,life):
    # print(str(life) + "^^^ ^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    if mc.get_rectangle().colliderect(obj.get_rectangle()):
        print('hit asteroid')
        print(life)
        life = life - 1
        return life
    else:
        if life < 100 :
            life += .0001
    return life


def check_bounds(mc,life):
    #check up down left and right
    if(mc.get_rectangle().x >900 or mc.get_rectangle().x < -100 or mc.get_rectangle().y >500 or mc.get_rectangle().y < -100):
        life -= 0.5
    return life

def transition(screen):
    trans = ""
    screen.blit(background,(0,0)) #will not have collisions

    

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
    life_num = 100 #start with 100 life

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
                    number = random.randint(0,3)
                    if(number == 0):
                        player1.set_image("Images/Player/william_movement2.png")
                    if(number ==1):
                        player1.set_image("Images/Player/william_movement3.png")
                    if(number == 2):
                        player1.set_image("Images/Player/william_movement4.png")
                if event.key == pygame.K_a:
                    player1.set_x(-15)
                    number = random.randint(0,3)
                    if(number == 0):
                        player1.set_image("Images/Player/william_movement2.png")
                    if(number ==1):
                        player1.set_image("Images/Player/william_movement3.png")
                    if(number == 2):
                        player1.set_image("Images/Player/william_movement4.png")
                        
                if event.key == pygame.K_SPACE:
                    gravity = -5
                    player1.set_image("Images/Player/william_movement_jump.png")

                if event.key == pygame.K_RETURN:
                    game_time = 300
                    life_num = 100
                    player1 = Player(100, 100, 100, 200, "Images/Player/william_movement1.png")
                    asteroids_list = [] #resets

                    print("in enter")
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    player1.set_image("Images/Player/william_movement1.png")
                    
        



        # Draw the player surface at the rectangle's position
        screen.blit(player1.get_surface(), (0,0))
        #screen.blit(screen)
        ###reduce time resets our internal counter ###
        game_time_seconds+=1
        print(game_time)
        if game_time_seconds >= 60:
            game_time -=1
            game_time_seconds = 0
        
        #check death && 
        if(life_num <=0):
            game_time =30000
            print("dead")
        if(game_time ==30000):
            dark = pygame.surface.Surface((800,400))
            dark.fill("black")
            screen.blit(dark,(0,0)) #will not have collisions

            write_text("white",30,screen, "You died, Press enter to continue",100,180)
            write_text("orange",20,screen, "Lead developer - Eder Martinez",100,240)
            write_text("orange",20,screen, "Art Director - Luke Ferguson",100,280)
            write_text("orange",20,screen, "Assistant developer - Joshua Burton",100,320)
            write_text("orange",20,screen, "Sprite Designer - Ella Foxhoven",100,360)
        
        #Scene picker 
        if game_time >= 240 and game_time <1000:
            print("env 1") 
            gravity +=0.15
            life_num = environment1(screen,player1,gravity, game_time,asteroids_list,2 ,life_num)

            if game_time <= 245:
                transition(screen)

        
    

        
        
        # Update the display
        pygame.display.update()
        clock.tick(60)

main()






    