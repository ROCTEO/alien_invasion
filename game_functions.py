# -*- coding: utf-8 -*-
__author__ = 'zjp'

import sys
import pygame

def check_events():
    """响应按键和鼠标的事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

