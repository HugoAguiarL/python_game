from const import win_height, win_width
from menu import Menu

import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((win_width, win_height))


    def run(self):


    
        while True:
            menu = Menu(self.window)
            menu.run()
            pass





