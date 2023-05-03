import pygame, sys, subprocess

pygame.init()

def start_game():
    pass

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

fondo_pant = pygame.image.load('img/Background/background.png').convert()
fondo_pant = pygame.transform.scale(fondo_pant, (SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Flappy Bird")

font = pygame.font.Font("fonts/BitfalsFont.otf", 36)

options = ["Teclado", "Mouse", "Salir"]
selected_option = 0

while True:
    screen.blit(fondo_pant, (0, 0))
    
    title = font.render("Flappy Bird", True, ( 155, 255, 213 ))
    title_rect = title.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/8))
    screen.blit(title, title_rect)
    
    for i in range(len(options)):
        text = font.render(options[i], True, BLACK)
        if i == selected_option:
            text = font.render(options[i], True, (255, 0, 0))
        text_rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + i*50))
        screen.blit(text, text_rect)

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                selected_option = (selected_option - 1) % len(options)
            elif event.key == pygame.K_DOWN:
                selected_option = (selected_option + 1) % len(options)
            elif event.key == pygame.K_RETURN:
                if selected_option == 0:
                    pygame.display.flip()
                    subprocess.call(["python", "modes/teclado.py"])
                elif selected_option == 1:
                    subprocess.call(["python", "modes/raton.py"])
                elif selected_option == 2:
                  pygame.quit()
                  sys.exit()
                    
    
   