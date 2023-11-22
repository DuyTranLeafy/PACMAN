# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 10:22:58 2023

@author: tranv
"""

import pygame
from PacmanInfoWindow import *
from Alogrithm import *
from ChooseMode import *
import sys

class PacmanStartMenu:
    def __init__(self):
        pygame.init()
        self.WIDTH = 900
        self.HEIGHT = 950
        self.screen = pygame.display.set_mode([self.WIDTH, self.HEIGHT])
        self.timer = pygame.time.Clock()
        self.fps = 60

        # Icon của các cửa sổ
        icon = pygame.image.load('Graphics/Icon_Snake.png')
        pygame.display.set_icon(icon)

        pygame.display.set_caption("Pacman Game")

        # CỬA SỔ START
        self.root = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        background = pygame.image.load('Graphics/Layout.png')
        background = pygame.transform.scale(background, (self.WIDTH, self.HEIGHT))
        self.root.blit(background, (0, 0))

        # Tạo nút "Start"
        self.start_button = pygame.Rect(310, 530, 250, 50)
        self.button_color = pygame.Color("#000000")
        self.hover_color = pygame.Color("#333333")

        # Tạo nút "Info"
        self.info_button = pygame.Rect(310, 630, 250, 50)
        self.info_button_color = pygame.Color("#000000")
        self.info_hover_color = pygame.Color("#333333")

        self.font = pygame.font.Font("Graphics/Font.ttf", 70)

    def run_start_menu(self):
        running = True
        while running:
            self.timer.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if self.start_button.collidepoint(mouse_pos):
                        mode = ChooseMode()
                        mode.run_menu()
                    elif self.info_button.collidepoint(mouse_pos):
                        # Xử lý sự kiện khi nút "Info" được nhấn
                        info_window = PacmanInfoWindow()
                        info_window.run()

            # Lấy tọa độ chuột
            mouse_pos = pygame.mouse.get_pos()

            # Kiểm tra xem chuột có đang nằm trên nút "Start" hay không
            if self.start_button.collidepoint(mouse_pos):
                start_color = self.hover_color
            else:
                start_color = self.button_color

            # Kiểm tra xem chuột có đang nằm trên nút "Info" hay không
            if self.info_button.collidepoint(mouse_pos):
                info_color = self.info_hover_color
            else:
                info_color = self.info_button_color

            # Vẽ nút "Start" và "Info" với màu hiện tại
            pygame.draw.rect(self.root, start_color, self.start_button)
            pygame.draw.rect(self.root, info_color, self.info_button)

            # Vẽ văn bản "Start" và "Info" giữa nút
            start_text = self.font.render("Start", True, "#FFD800")
            info_text = self.font.render("Info", True, "#FFD800")

            start_text_rect = start_text.get_rect(center=self.start_button.center)
            info_text_rect = info_text.get_rect(center=self.info_button.center)

            self.root.blit(start_text, start_text_rect)
            self.root.blit(info_text, info_text_rect)

            pygame.display.flip()

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    start_menu = PacmanStartMenu()
    start_menu.run_start_menu()