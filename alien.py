#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'rocteo'

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """创建一个描述外星人的类"""
    def __init__(self,ai_settings,screen):
        """初始化外星人的属性"""
        super(Alien,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #加载外星人的图像，获取rect属性
        self.image = pygame.image.load(r'images\alien.bmp')
        self.rect = self.image.get_rect()

        #将每个外星人放置在左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def blitme(self):
        """绘制外星人"""
        self.screen.blit(self.image,self.rect)