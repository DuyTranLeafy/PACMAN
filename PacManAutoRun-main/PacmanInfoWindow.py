import pygame
import sys

class PacmanInfoWindow:
    def __init__(self):
        self.WIDTH = 900
        self.HEIGHT = 950

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
        
         # Tạo nút "Back"
        self.back_button = pygame.Rect(240, 760, 250, 50)
        self.back_button_color = pygame.Color("#000000")
        self.back_hover_color = pygame.Color("#333333")

        self.font = pygame.font.Font("Graphics/Font.ttf", 70)

    def run(self):
        running = True
        while running:
            self.timer.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if self.back_button.collidepoint(mouse_pos):
                        background = pygame.image.load('Graphics/Layout.png')
                        background = pygame.transform.scale(background, (self.WIDTH, self.HEIGHT))
                        self.root.blit(background, (0, 0))
                    
                        # You may need to redraw other elements on the screen as well
                    
                        # Update the display
                        pygame.display.flip()
                        return

            # Lấy tọa độ chuột
            mouse_pos = pygame.mouse.get_pos()
                
            # Kiểm tra xem chuột có đang nằm trên nút "Back" hay không
            if self.back_button.collidepoint(mouse_pos):
                back_color = self.back_hover_color
            else:
                back_color = self.back_button_color

            # Vẽ nút "Classic" và "AI Play" với màu hiện tại
           
            pygame.draw.rect(self.root, back_color, self.back_button)

            # Vẽ văn bản "Classic" và "AI Play" giữa nút
        
            back_text = self.font.render("Back", True, "#FFD800")

           
            back_text_rect = back_text.get_rect(center=self.back_button.center)

           
            self.root.blit(back_text, back_text_rect)

            pygame.display.flip()

        pygame.quit()
        sys.exit()
