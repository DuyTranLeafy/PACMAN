import pygame
import sys
from PacMan_BFS import PacmanGame

class Content:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)
        self.pacman_game = PacmanGame()

    def draw(self, surface):
        text = self.font.render("Hello from Content class!", True, (255, 255, 255))
        surface.blit(text, (50, 50))

        # Gọi hàm run_game từ PacmanGame để thực thi trò chơi
        self.pacman_game.run_game()

        # Vẽ nút Dừng và Thoát
        pygame.draw.rect(surface, (100, 100, 100), (30, 50, 100, 40))  # Nút Dừng
        pygame.draw.rect(surface, (100, 100, 100), (150, 50, 100, 40))  # Nút Thoát

        text_pause = self.font.render("Dừng", True, (255, 255, 255))
        text_exit = self.font.render("Thoát", True, (255, 255, 255))

        surface.blit(text_pause, (40, 60))
        surface.blit(text_exit, (160, 60))

pygame.init()

# Kích thước màn hình chính
screen_size = (1050, 1500)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Pygame Window")

# Kích thước cửa sổ
window_size = (950, 900)
window = pygame.Surface(window_size)
window_rect = window.get_rect()

# Vị trí cửa sổ trên màn hình chính
window_position = ((screen_size[0] - window_size[0]) // 2, (screen_size[1] - window_size[1]) // 2)

# Màu sắc
white = (255, 255, 255)
black = (0, 0, 0)

# Tạo đối tượng từ class Content
content = Content()

# Biến để kiểm soát việc kéo di chuyển cửa sổ
dragging = False
offset = [0, 0]

# Bước lặp chính
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Kiểm tra xem chuột có ở trong cửa sổ không
            if window_rect.collidepoint(event.pos):
                dragging = True
                offset = [event.pos[0] - window_position[0], event.pos[1] - window_position[1]]
        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = False
        elif event.type == pygame.MOUSEMOTION:
            # Di chuyển cửa sổ nếu đang kéo
            if dragging:
                window_position = [event.pos[0] - offset[0], event.pos[1] - offset[1]]

    # Xóa màn hình
    screen.fill(white)

    # Vẽ cửa sổ
    pygame.draw.rect(screen, black, (window_position[0] - 5, window_position[1] - 5, window_size[0] + 10, window_size[1] + 10))
    window.fill(black)  # Xóa nền cũ của cửa sổ

    # Gọi hàm draw từ đối tượng content để vẽ nội dung vào cửa sổ
    content.draw(window)

    # Hiển thị cửa sổ lên màn hình chính
    screen.blit(window, window_position)

    # Hiển thị lên màn hình
    pygame.display.flip()

pygame.quit()
sys.exit()
