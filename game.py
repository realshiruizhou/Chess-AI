from constants import *
import pygame

class Game:
    def __init__(self):
        pass

    def make_checkerboard(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                color = DARK if (row + col) % 2 else LIGHT
                rect = (col * SIZE, row * SIZE, SIZE, SIZE)
                pygame.draw.rect(surface, color, rect)