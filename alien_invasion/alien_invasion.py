import sys

import pygame

from settings import Settings

def run_game():
    # 初始化Pygame,设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))    # 设置屏幕对象的大小
    pygame.display.set_caption("Alien Invasion")

    # 开始游戏的主循环
    while True:

        # 监视键盘鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # 每次循环都会重绘屏幕
        screen.fill(ai_settings.bg_color)

        # 让最近绘制的屏幕可见
        pygame.display.flip()  # Update the full display Surface to the screen

run_game()

