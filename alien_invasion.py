import pygame

from pygame.sprite import Group
from settings import Settings
from ship import Ship
from game_stats import Game_stats
from button import Button
from scoreboard import Scoreboard
import game_functions as gf


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一个PLAY按钮
    play_button = Button(screen, 'Play')

    # 创建一个用于存储游戏统计信息的实例
    stats = Game_stats(ai_settings)

    # 创建一个显示得分的实例
    sb = Scoreboard(ai_settings, screen, stats)

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    # 创建一个外星人
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 开始游戏的主循环
    while True:
        # 监视鼠标和键盘事件
        gf.check_events(ai_settings, screen, stats, sb, ship, aliens,
                        bullets, play_button)
        if stats.game_active:
            ship.update()
            gf.update_alien(ai_settings, stats, screen, ship, aliens, bullets)
            gf.update_bullet(ai_settings, screen, stats, sb, ship, aliens,
                             bullets)
        # 更新屏幕
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
                         play_button)

run_game()
