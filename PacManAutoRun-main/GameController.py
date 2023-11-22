# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 12:24:54 2023

@author: tranv
"""

import pygame
import sys
import PacMan_BFS
import PacMan_DFS
import PacMan_Greedy

class GameController:
    def __init__(self):
        self.WIDTH = 200
        self.HEIGHT = 400

        pygame.init()
        self.screen = pygame.display.set_mode([self.WIDTH, self.HEIGHT])
        self.timer = pygame.time.Clock()
        self.fps = 60

        # Icon của các cửa sổ
        icon = pygame.image.load('Graphics/Icon_Snake.png')
        pygame.display.set_icon(icon)

        # Màu các nút được sử dụng trong cửa sổ
        self.color = pygame.Color("#000000")

        pygame.display.set_caption("Pacman Game")

        # CỬA SỔ START
        self.root = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        background = pygame.image.load('Graphics/Info.png')
        background = pygame.transform.scale(background, (self.WIDTH, self.HEIGHT))
        self.root.blit(background, (0, 0))
        
        # Tạo nút "Dừng"
        self.pause_button = pygame.Rect(25, 100, 150, 50)
        self.pause_button_color = pygame.Color("#000000")
        self.pause_hover_color = pygame.Color("#333333")

        # Tạo nút "Thoát"
        self.exit_button = pygame.Rect(25, 200, 150, 50)
        self.exit_button_color = pygame.Color("#000000")
        self.exit_hover_color = pygame.Color("#333333")

        self.font = pygame.font.Font("Graphics/Font.ttf", 30)

    def run(self):
        running = True
        while running:
            self.timer.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if self.pause_button.collidepoint(mouse_pos):
                        pacman_game = PacMan_BFS.PacmanGame()
                        pacman_game.stop_game()
                    elif self.exit_button.collidepoint(mouse_pos):
                        pacman_game = PacMan_BFS.PacmanGame()
                        pacman_game.stop_game()
                        background = pygame.image.load('Alogrithm/Layout.png')
                        background = pygame.transform.scale(background, (self.WIDTH, self.HEIGHT))
                        self.root.blit(background, (0, 0))
                    
                        # You may need to redraw other elements on the screen as well
                    
                        # Update the display
                        pygame.display.flip()
                        return

            # Lấy tọa độ chuột
            mouse_pos = pygame.mouse.get_pos()
                
            # Kiểm tra xem chuột có đang nằm trên nút "Dừng" hay không
            if self.pause_button.collidepoint(mouse_pos):
                pause_color = self.pause_hover_color
            else:
                pause_color = self.pause_button_color

            # Kiểm tra xem chuột có đang nằm trên nút "Thoát" hay không
            if self.exit_button.collidepoint(mouse_pos):
                exit_color = self.exit_hover_color
            else:
                exit_color = self.exit_button_color

            # Vẽ nút "Dừng"
            pygame.draw.rect(self.root, pause_color, self.pause_button)
            # Vẽ văn bản "Dừng"
            pause_text = self.font.render("Dừng", True, "#FFD800")
            pause_text_rect = pause_text.get_rect(center=self.pause_button.center)
            self.root.blit(pause_text, pause_text_rect)

            # Vẽ nút "Thoát"
            pygame.draw.rect(self.root, exit_color, self.exit_button)
            # Vẽ văn bản "Thoát"
            exit_text = self.font.render("Thoát", True, "#FFD800")
            exit_text_rect = exit_text.get_rect(center=self.exit_button.center)
            self.root.blit(exit_text, exit_text_rect)

            pygame.display.flip()

        pygame.quit()
        sys.exit()


