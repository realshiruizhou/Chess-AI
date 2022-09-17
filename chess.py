from constants import *
from game import Game

import pygame
import sys

class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Chess')
        self.game = Game()

    def mainloop(self):
        while True:
            self.game.make_checkerboard(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                pygame.display.update()
        
if __name__ == "__main__":
    main = Main()
    main.mainloop()