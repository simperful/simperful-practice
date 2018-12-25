import sys

import pygame

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))    # 设置屏幕对象的大小
    pygame.display.set_caption("Alien Invasion")

    # 开始游戏的主循环
    while True:

        # 监视键盘鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # 让最近绘制的屏幕可见
        pygame.display.flip()  # Update the full display Surface to the screen

run_game()

