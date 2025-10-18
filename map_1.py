import pygame
from pygame import transform

from const import win_width, win_height
from factory import EntityFactory


class MapOne:
    def __init__(self, window):
        self.window = window
        self.entity_background = EntityFactory.get_entity('map_2')

    def run(self):
        while True:

            self.window.blit(self.entity_background.surf, self.entity_background.rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()


            pygame.display.flip()