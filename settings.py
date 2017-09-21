# -*- coding: utf-8 -*-
__author__ = 'zjp'

class Settings():
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        #屏幕的设置
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (230,230,230)

        #飞船设置
        self.ship_speed_factor = 1.5