import pygame
import main

WIDTH = 900
HEIGHT = 950

screen = pygame.display.set_mode([WIDTH, HEIGHT])
timer = pygame.time.Clock()
fps = 60

# Icon của các cửa sổ
icon = pygame.image.load('Graphics/Icon_Snake.png')
pygame.display.set_icon(icon)

# Mau cac nut duoc su dung trong cua so
color = pygame.Color("#000000")

pygame.display.set_caption("Pacman Game")

# CUA SO START
pygame.init()
root = pygame.display.set_mode((WIDTH, HEIGHT))
background = pygame.image.load('Graphics/MainLayout.png')
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
root.blit(background, (0, 0))

# Tạo nút "Start"
start_button = pygame.Rect(310, 500, 250, 50)

pygame.draw.rect(root, color, start_button)

font = pygame.font.Font("Graphics/Font.ttf", 70)

start_text = font.render("Start", True, "#FFD800")

start_text_rect = start_text.get_rect(center=start_button.center)

text_rect = start_text.get_rect()

text_rect.center = (900, 950)
root.blit(start_text, start_text_rect)

running = True
while running:
    timer.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos  # gets mouse position
            if start_button.collidepoint(mouse_pos):
                pacman_game = main.PacmanGame()
                pacman_game.run_game()

    pygame.display.flip()
pygame.quit()
