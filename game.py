from const import win_height, win_width
from map_1 import MapOne
from menu import Menu

import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((win_width, win_height))


    def run(self):

        while True:
            menu = Menu(self.window)
            return_menu = menu.run()
            if return_menu == 0:
                map1 = MapOne(self.window)
                map1.run()
            elif return_menu == 1:
                pass
            elif return_menu == 2:
                pygame.quit()
                quit()






