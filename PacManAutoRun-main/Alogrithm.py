import pygame
import PacMan_BFS
import PacMan_DFS
import PacMan_Greedy
import sys
from GameController import *

class Alogrithm:
    def __init__(self):
        self.WIDTH = 950
        self.HEIGHT = 900
    

        pygame.init()
        self.screen = pygame.display.set_mode([self.WIDTH, self.HEIGHT])
        self.timer = pygame.time.Clock()
        self.fps = 60

        # Icon của các cửa sổ
        icon = pygame.image.load('Graphics/Icon_Snake.png')
        pygame.display.set_icon(icon)

        pygame.display.set_caption("Pacman Game")

        # CỬA SỔ START
        self.root = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        background = pygame.image.load('Graphics/Alogrithm.png')
        background = pygame.transform.scale(background, (self.WIDTH, self.HEIGHT))
        self.root.blit(background, (0, 0))

        # Tạo nút "BFS"
        self.bfs_button = pygame.Rect(340, 560, 250, 50)
        self.button_color = pygame.Color("#000000")
        self.hover_color = pygame.Color("#333333")

        # Tạo nút "DFS"
        self.dfs_button = pygame.Rect(340, 660, 250, 50)
        self.dfs_button_color = pygame.Color("#000000")
        self.dfs_hover_color = pygame.Color("#333333")

        # Tạo nút "Greedy"
        self.greedy_button = pygame.Rect(340, 760, 250, 50)
        self.greedy_button_color = pygame.Color("#000000")
        self.greedy_hover_color = pygame.Color("#333333")

        # Tạo nút "Back"
        self.back_button = pygame.Rect(140, 760, 250, 50)
        self.back_button_color = pygame.Color("#000000")
        self.back_hover_color = pygame.Color("#333333")

        self.font = pygame.font.Font("Graphics/Font.ttf", 70)


    def run_menu_alogrithm(self):
        running = True
        while running:
            self.timer.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if self.bfs_button.collidepoint(mouse_pos):
                        pacman_game = PacMan_BFS.PacmanGame()
                        pacman_game.run_game()
                        control = GameController()
                        control.run()
                    elif self.dfs_button.collidepoint(mouse_pos):
                        pacman_game = PacMan_DFS.PacmanGame()
                        pacman_game.run_game()
                    elif self.greedy_button.collidepoint(mouse_pos):
                        pacman_game = PacMan_Greedy.PacmanGame()
                        pacman_game.run_game()
                    elif self.back_button.collidepoint(mouse_pos):
                        background = pygame.image.load('Graphics/Mode.png')
                        background = pygame.transform.scale(background, (self.WIDTH, self.HEIGHT))
                        self.root.blit(background, (0, 0))
                    
                        # You may need to redraw other elements on the screen as well
                    
                        # Update the display
                        pygame.display.flip()
                        return

            # Lấy tọa độ chuột
            mouse_pos = pygame.mouse.get_pos()

            # Kiểm tra xem chuột có đang nằm trên nút "BFS" hay không
            if self.bfs_button.collidepoint(mouse_pos):
                bfs_color = self.hover_color
            else:
                bfs_color = self.button_color

            # Kiểm tra xem chuột có đang nằm trên nút "DFS" hay không
            if self.dfs_button.collidepoint(mouse_pos):
                dfs_color = self.dfs_hover_color
            else:
                dfs_color = self.dfs_button_color

            # Kiểm tra xem chuột có đang nằm trên nút "Greedy" hay không
            if self.greedy_button.collidepoint(mouse_pos):
                greedy_color = self.greedy_hover_color
            else:
                greedy_color = self.greedy_button_color

            # Kiểm tra xem chuột có đang nằm trên nút "Back" hay không
            if self.back_button.collidepoint(mouse_pos):
                back_color = self.back_hover_color
            else:
                back_color = self.back_button_color

            # Vẽ nút "BFS", "DFS", "Greedy", và "Back" với màu hiện tại
            pygame.draw.rect(self.root, bfs_color, self.bfs_button)
            pygame.draw.rect(self.root, dfs_color, self.dfs_button)
            pygame.draw.rect(self.root, greedy_color, self.greedy_button)
            pygame.draw.rect(self.root, back_color, self.back_button)

            # Vẽ văn bản "BFS", "DFS", "Greedy", và "Back" giữa nút
            bfs_text = self.font.render("BFS", True, "#FFD800")
            dfs_text = self.font.render("DFS", True, "#FFD800")
            greedy_text = self.font.render("Greedy", True, "#FFD800")
            back_text = self.font.render("Back", True, "#FFD800")

            bfs_text_rect = bfs_text.get_rect(center=self.bfs_button.center)
            dfs_text_rect = dfs_text.get_rect(center=self.dfs_button.center)
            greedy_text_rect = greedy_text.get_rect(center=self.greedy_button.center)
            back_text_rect = back_text.get_rect(center=self.back_button.center)

            self.root.blit(bfs_text, bfs_text_rect)
            self.root.blit(dfs_text, dfs_text_rect)
            self.root.blit(greedy_text, greedy_text_rect)
            self.root.blit(back_text, back_text_rect)

            
            pygame.display.flip()

        pygame.quit()
        sys.exit()

