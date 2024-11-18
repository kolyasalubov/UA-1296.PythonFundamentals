import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 450))
pygame.display.set_caption('Guess the number')

PURPLE = (220, 201, 239)
BLACK = (0, 0, 0)

number_to_guess = random.randint(1, 100)
attempts = 10


input_box = pygame.Rect(300, 300, 200, 50)
user_text = ''
guess = None
message = "Try to guess a number between 1 and 100"
attempt_message = f"Attempts left: {attempts}"

def draw_text(text, position):
    font = pygame.font.SysFont(None, 30)
    text_surface = font.render(text, True, BLACK)
    screen.blit(text_surface, position)

running = True
while running:
    screen.fill(PURPLE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if user_text.isdigit():
                    guess = int(user_text)
                    if guess < number_to_guess:
                        message = "Too low!"
                    elif guess > number_to_guess:
                        message = "Too high!"
                    else:
                        message = "Congratulations!"
                    attempts -= 1
                    attempt_message = f"Attempts left: {attempts}"
                    user_text = ''
                    if attempts == 0:
                        message = f"Sorry, no more attempts left. The number was {number_to_guess}"
            elif event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            else:
                user_text += event.unicode

    draw_text(message, (150, 150))
    draw_text(attempt_message, (150, 200))
    pygame.draw.rect(screen, BLACK, input_box, 2)
    draw_text(user_text, (input_box.x + 10, input_box.y + 10))
    
    pygame.display.flip()

pygame.quit()
