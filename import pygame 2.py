import pygame
import random

# Inicializa o Pygame
pygame.init()

# Configurações da tela
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Bait do Quadrado')

# Cores
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# Configurações do quadrado
square_size = 100
font = pygame.font.SysFont(None, 36)

# Função para desenhar o texto fixo
def draw_fixed_text():
    fixed_text = font.render('clique no quadrado : )', True, black)
    screen.blit(fixed_text, (10, 10))

# Função para desenhar o quadrado
def draw_square(x, y, show_message):
    pygame.draw.rect(screen, red, (x, y, square_size, square_size))
    if show_message:
        text = font.render('eu te amo', True, black)
        text_rect = text.get_rect(center=(x + square_size // 2, y + square_size // 2))
        screen.blit(text, text_rect)

# Função para obter nova posição aleatória
def get_random_position():
    x = random.randint(0, width - square_size)
    y = random.randint(0, height - square_size)
    return x, y

# Posição inicial do quadrado
x, y = get_random_position()
click_count = 0
show_message = False

# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if x < mouse_x < x + square_size and y < mouse_y < y + square_size:
                click_count += 1
                if click_count >= 8:
                    show_message = True
                else:
                    x, y = get_random_position()

    screen.fill(white)
    draw_fixed_text()
    draw_square(x, y, show_message)
    pygame.display.flip()

pygame.quit()
