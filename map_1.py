import pygame

from const import win_width, win_height


class MapOne:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/map_1.png').convert()
        self.surf_2 = pygame.image.load('./assets/nuvem_plataform.png').convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (win_width, win_height))
        self.rect = self.surf.get_rect()
        self.rect_plataform = self.surf_2.get_rect()

        self.rect_plataform.x = 300
        self.rect_plataform.y = 400

    def run(self):
        while True:
            self.window.blit(self.surf, self.rect)
            self.window.blit(self.surf_2, (self.rect_plataform.x, self.rect_plataform.y))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            pygame.display.flip()
