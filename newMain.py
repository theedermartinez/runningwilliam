import pygame
import os
from player import Player
from asteroid import Asteroid
import random
import time


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


def environment2(screen,player1,gravity,timer,asteroids_list, number_asteroids,life):
    ##change path to be in the right place
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    #os.chdir() #change working directory

    ##build background
    background = pygame.image.load('Images/Backgrounds/earth.png')
    screen.blit(background,(0,0)) #will not have collisions

    ##build total time left 
    write_text("white",20,screen, "Time left: " + str(timer), 300,0)

    ##add text to home screen
    write_text("white",20,screen, "Running William",0,0,)

    ##intro text && plannet
    if(timer >220):
        write_text("black",30,screen, "use Space Bar, A and D to move",100,300)
        write_text("black",30,screen, "Welcome to Earth",100,350)

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
 
def environment3(screen,player1,gravity,timer,asteroids_list, number_asteroids,life):
    ##change path to be in the right place
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    #os.chdir() #change working directory

    ##build background
    background = pygame.image.load('Images/Backgrounds/jupiter.png')
    screen.blit(background,(0,0)) #will not have collisions

    ##build total time left 
    write_text("white",20,screen, "Time left: " + str(timer), 300,0)

    ##add text to home screen
    write_text("white",20,screen, "Running William",0,0,)

    ##intro text && plannet
    if(timer >150):
        write_text("white",30,screen, "use Space Bar, A and D to move",100,300)
        write_text("white",30,screen, "Welcome to Jupiter",100,350)

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

def environment4(screen,player1,gravity,timer,asteroids_list, number_asteroids,life):
       ##change path to be in the right place
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    #os.chdir() #change working directory

    ##build background
    background = pygame.image.load('Images/Backgrounds/Uranus.png')
    screen.blit(background,(0,0)) #will not have collisions

    ##build total time left 
    write_text("white",20,screen, "Time left: " + str(timer), 300,0)

    ##add text to home screen
    write_text("white",20,screen, "Running William",0,0,)

    ##intro text && plannet
    if(timer >150):
        write_text("white",30,screen, "use Space Bar, A and D to move",100,300)
        write_text("white",30,screen, "Welcome to Jupiter",100,350)

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
        life = life - 0.6
        return life
    else:
        if life < 100 :
            life += .005
    return life


def check_bounds(mc,life):
    #check up down left and right
    if(mc.get_rectangle().x >900 or mc.get_rectangle().x < -100 or mc.get_rectangle().y >500 or mc.get_rectangle().y < -100):
        life -= 0.5
    return life

def transition(screen,game_time):

    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    initial_alpha = 100
    trans = {"Images/Backgrounds/Lightspeed/lightspeed_1.png","Images/Backgrounds/Lightspeed/lightspeed_2.png","Images/Backgrounds/Lightspeed/lightspeed_3.png","Images/Backgrounds/Lightspeed/lightspeed_4.png"}
    loaded_images = [pygame.image.load(image_path) for image_path in trans]
    for image in loaded_images:
        image.set_alpha(initial_alpha+ 30)
        write_text("Orange",20,screen,"New Planet! Be ready",300,200)
        
        screen.blit(image, (0, 0))
    for image in reversed(loaded_images):
        image.set_alpha(initial_alpha - 30)
        screen.blit(image, (0, 0))
        write_text("Orange",20,screen,"New Planet! Be ready",300,200)

    #game_time -= game_time

    

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
    ##Movement
    move_left = False
    move_right = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            #check events 
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    move_right = True
                if event.key == pygame.K_a:
                    move_left = True
                if event.key == pygame.K_SPACE:
                    gravity = -5
                    player1.set_image("Images/Player/william_movement_jump.png")
                if event.key == pygame.K_RETURN:
                    game_time = 300
                    life_num = 100
                    player1 = Player(100, 100, 100, 200, "Images/Player/william_movement1.png")
                    asteroids_list = [] #resets
                    print("in enter")
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    player1.set_image("Images/Player/william_movement1.png")
                if event.key == pygame.K_d:
                    move_right = False
                if event.key == pygame.K_a:
                    move_left = False
        if (move_right):
            player1.set_x(5)
            number = random.randint(0,3)
            if(number == 0):
                player1.set_image("Images/Player/william_movement2.png")
            if(number ==1):
                player1.set_image("Images/Player/william_movement3.png")
            if(number == 2):
                player1.set_image("Images/Player/william_movement4.png")
        if (move_left):
            player1.set_x(-5)
            number = random.randint(0,3)
            if(number == 0):
                player1.set_image("Images/Player/william_movement2.png")
            if(number ==1):
                player1.set_image("Images/Player/william_movement3.png")
            if(number == 2):
                player1.set_image("Images/Player/william_movement4.png")
                    
        



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

            write_text("white",30,screen, "Game Over, Press enter to continue",100,180)
            write_text("orange",20,screen, "Lead developer & B) - Eder Martinez",100,240)
            write_text("orange",15,screen, "Assistant developer & Sprite Designer - Ella Foxhoven",100,280)
            write_text("orange",15,screen, "Assistant develope & Quality Control - Joshua Burton",100,320)
            write_text("orange",15,screen, "Assistant developer & Art Director - Luke Ferguson ",100,360)
        
        #Scene picker
        print(game_time) 
        if game_time >= 240 and game_time <1000:
            print("env 1") 
            gravity +=0.15
            life_num = environment1(screen,player1,gravity, game_time,asteroids_list,3 ,life_num)

            if game_time <= 245:
                transition(screen,game_time)
                game_time -= 1
            
        elif game_time >= 180 and game_time <1000:
            if(game_time == 239 ):
                print("env 2") 
                asteroids_list = []
                player1 = Player(100, 100, 100, 200, "Images/Player/william_movement1.png")
            gravity +=0.30
            life_num = environment2(screen,player1,gravity, game_time,asteroids_list,4 ,life_num)
            if game_time <= 185:
                transition(screen,game_time)
                print("two transition")
                game_time -= 1

        elif game_time >=120 and game_time <1000:
            if(game_time == 179 ):
                print("env 3") 
                asteroids_list = []
                player1 = Player(100, 100, 100, 200, "Images/Player/william_movement1.png")
            gravity +=0.40
            life_num = environment3(screen,player1,gravity, game_time,asteroids_list,5 ,life_num)
            print("int 3")
            if game_time <= 125:
                transition(screen,game_time)
                game_time -= 1
        
        elif game_time >=60 and game_time <1000:
            if(game_time == 60 ):
                print("env 4") 
                asteroids_list = []
                player1 = Player(100, 100, 100, 200, "Images/Player/william_movement1.png")
            gravity +=0.45
            life_num = environment4(screen,player1,gravity, game_time,asteroids_list,6 ,life_num)
            print("int 22")
            if game_time <= 65:
                print("in 65")
                transition(screen,game_time)
                game_time -= 1
        
        else:
            print("int else hehehehehe")
            life_nums = -1
            game_time = 30000



        
    

        
        
        # Update the display
        pygame.display.update()
        clock.tick(60)

main()






    