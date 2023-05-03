import pygame
import random

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
GRAVITY = 5
JUMP_HEIGHT = 30
PIPE_SPEED = 3
PIPE_GAP = 140
PIPE_FREQUENCY = 200

fondo_pant = pygame.image.load('img/Background/background.png')
fondo_pant = pygame.transform.scale(fondo_pant, (SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

clock = pygame.time.Clock()

bird = pygame.Rect(50, 250, 30, 30)
bird_color = (255, 255, 0)

pipes = []
pipe_color = (0, 255, 0)

class Pipe:
    def __init__(self):
        self.x = SCREEN_WIDTH
        self.y = random.randint(100, SCREEN_HEIGHT - 300)
        self.width = 40
        self.top_height = self.y
        self.bottom_height = SCREEN_HEIGHT - self.y - PIPE_GAP
        self.passed = False

    def update(self):
        self.x -= PIPE_SPEED

    def draw(self):
        pygame.draw.rect(screen, pipe_color, (self.x, 0, self.width, self.top_height))
        pygame.draw.rect(screen, pipe_color, (self.x, SCREEN_HEIGHT - self.bottom_height, self.width, self.bottom_height))

    def collision(self):
        if bird.colliderect((self.x, 0, self.width, self.top_height)) or bird.colliderect((self.x, SCREEN_HEIGHT - self.bottom_height, self.width, self.bottom_height)):
            return True
        return False

def new_pipe():
    if len(pipes) == 0 or SCREEN_WIDTH - pipes[-1].x > PIPE_FREQUENCY:
        pipes.append(Pipe())

def draw_text(text, x, y, font_size):
    font = pygame.font.Font(None, font_size)
    text = font.render(text, True, (255, 255, 255))
    text_rect = text.get_rect(center=(x, y))
    screen.blit(text, text_rect)

score = 0
font = pygame.font.Font(None, 36)
game_over = False
while not game_over:
    bird.y += 1.5

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.y -= JUMP_HEIGHT

    screen.blit(fondo_pant, (0, 0))


    pygame.draw.rect(screen, bird_color, bird)

    for pipe in pipes:
        pipe.update()
        pipe.draw()
        if pipe.x < -pipe.width:
            pipes.remove(pipe)
        if not pipe.passed and pipe.x + pipe.width < bird.x:
            score += 1
            pipe.passed = True
            if (score == 10):
                game_over = True
        if pipe.collision():
            game_over = True
            break
    new_pipe()
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.update()

    clock.tick(60)

pygame.quit()