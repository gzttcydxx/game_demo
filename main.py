#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
from game import GlobalGame, Attack
from monster import *


def main():
    global_game = GlobalGame(800, 600)
    
    while True:
        global_game.clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                global_game.game_over()
                return


if __name__ == "__main__":
    main()
