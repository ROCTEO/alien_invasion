# -*- coding: utf-8 -*-
__author__ = 'zjp'

class Game_stats():
    """跟踪游戏的统计数据"""
    def __init__(self, ai_settings):
        """初始化统计数据"""
        self.ai_settings = ai_settings
        self.reset_stats()
        #游戏刚启动时处于非活动状态
        self.game_active = False

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_life = self.ai_settings.ship_limit