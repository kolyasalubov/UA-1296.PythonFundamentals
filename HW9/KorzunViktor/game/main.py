import pygame
from constants import *
import random


done = True
lives = 7

pygame.init()


#Set display parameters
gameDisplay = pygame.display.set_mode((WIDTH_DISPLAY, HEIGHT_DISPLAY))

#Set font parameters
font = pygame.font.Font(None, 36)

#Set game icon
icon = pygame.image.load('HW9/KorzunViktor/game/images/icon.png')
pygame.display.set_icon(icon)

#Set game name
pygame.display.set_caption("Guesser")


#Make user input
input_box = pygame.Rect(150, 150, 300, 50)
color_active = BLUE
color_inactive = GRAY
color = color_inactive
active = False
text = ""

#Restart Button
restart_box = pygame.Rect(10, 350, 100, 30)
restart_text = " Restart"



#Set random game number
game_number = random.randint(1,100)


#Game rules to user
game_rules = "Guess the number from 1 to 100"

#Message to user
user_message = ""







while done:
    #Set background color of game
    gameDisplay.fill(WHITE)

    #Print lives
    lives_message = f"{lives} lives remaining"
    
    
    
    #Main event checker    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos):
                active = not active
            else:
                active = False
            color = color_active if active else color_inactive

        if event.type == pygame.MOUSEBUTTONDOWN:
            if restart_box.collidepoint(event.pos):
                lives = 7
                user_message = ""
                game_number = random.randint(1,100)
                      
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    try:
                        user_number = int(text)                             
                        if 1 <= user_number <= 100:
                            if game_number < user_number:
                                user_message = f"Number is lower then {user_number}"
                                lives -= 1
                            elif game_number > user_number:
                                user_message = f"Number is higher then {user_number}"
                                lives -= 1
                            elif game_number == user_number:
                                user_message = "You win"
                            if lives == 0:
                                done = True
                        else:
                            user_message = "Number is not beetween 1 - 100"
                        
                    except ValueError:
                        user_message = "You enter unncorect number"
                    text = ""
                    
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode
        
        
            
    pygame.draw.rect(gameDisplay, color, input_box, 2)
    pygame.draw.rect(gameDisplay, BLACK, restart_box, 2)

    #Print text in rect
    text_surface = font.render(text, True, BLACK)
    gameDisplay.blit(text_surface, (input_box.x + 5, input_box.y + 10))

    #Print message to user
    user_message_surface = font.render(user_message, True, GREEN)
    gameDisplay.blit(user_message_surface,(125, 100))

    #Print rule to user
    game_rules_surface = font.render(game_rules, True, BLACK)
    gameDisplay.blit(game_rules_surface,(125,20))
                
    #Print lives to user
    lives_surface = font.render(lives_message, True, BLACK)
    gameDisplay.blit(lives_surface,(400,350))

    #Restart Button
    restart_surface = font.render(restart_text, True, BLACK)
    gameDisplay.blit(restart_surface,(12,351))


    


    pygame.display.flip()

   
    

