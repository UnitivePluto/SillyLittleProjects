import itertools, os, pygame, random
from general_settings import *
from cards import * 

#Audio Placeholder

class Hand:
    def __init__(self) -> None:
        self.display_surface = pygame.display.get_surface()
        self.winner = None
        self.font = pygame.font.Font(GAME_FONT, 120)
        

    def update(self):
        pass 