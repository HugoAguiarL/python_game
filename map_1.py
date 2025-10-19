import pygame
from pygame import transform

from const import win_width, win_height
from factory import EntityFactory


class MapOne:
    def __init__(self, window):
        self.window = window
        self.entity_background = EntityFactory.get_entity('map_2')
        self.entity_background.surf = pygame.transform.scale(self.entity_background.surf, (win_width,win_height))
        self.entity_player = EntityFactory.get_entity('Player')
    def run(self):

        clock = pygame.time.Clock()
        while True:

            self.window.blit(self.entity_background.surf, self.entity_background.rect)
            self.window.blit(self.entity_player.image or self.entity_player.surf, self.entity_player.rect)
            self.entity_player.move()
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:
                        self.entity_player.animate('Attack')

            self.entity_player.update()


            pygame.display.flip()