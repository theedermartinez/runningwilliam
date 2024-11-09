import pygame
from sys import exit
import os
#my own classes
import player


#player object
#global : main character

stat_dic = {} #stat dictionary so we can know his stats


def main():
    pygame.init()
    see = pygame.display.set_mode((800, 400))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Running William")
    
    #main player 
    main_player_surface = player

    game_running = True
    stat_dic["player_gravity"] = 0
    stat_dic["on_platform"] = False

    while game_running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                main_char = player(100,50,0,0)
                player_movement(event, main_char)
        
        scene_1(see)
        see.blit(main_char.make_surface(), main_char.make_rectangle(100,50))#surface and rectangle


    '''do not forget this to update!!!'''
    pygame.display.update()
    clock.tick(60)
            

def player_movement(event, player):
    if game_active:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and player.get_rectangle().bottom >= 300:
                        stat_dic["player_gravity"] = -20
                        print("jump")
                    if event.key == pygame.K_SPACE and stat_dic["on_platform"] == True: #and player_rect.bottom == 300:
                        stat_dic["player_gravity"] = -20
                        print("jumpv2")
                    if event.key == pygame.K_RIGHT:
                        player_right =+ 5
                        print("right")
                    else:
                        player_right = 0 
                    if event.key == pygame.K_LEFT:
                        player_left =- 5
                        print("left")
                    else:
                        player_left = 0
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        player_right = 0
                    elif event.key == pygame.K_LEFT:
                        player_left = 0 
                #Mouse click player jumps
                if event.type == pygame.MOUSEBUTTONDOWN and player.get_rectangle().bottom >= 300:
                    if player.get_rectangle().collidepoint(event.pos):
                        stat_dic["player_gravity"] = -20
    else:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_active = True
            #enemy1_rect.left = 900
            lifes = 100
            player.get_rectangle().x = 20
            player_left = 0
            player_right = 0
            scene = 0
    

def scene_1(viewable):
    """main game scene"""
    viewable.fill(("orange"))
   
    #game_name(viewable) 

main()