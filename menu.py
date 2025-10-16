import pygame.image
import pygame.display
import pygame.transform

from const import win_height, win_width


class Menu:
    def __init__(self, window):
        self.window = window
        self.player_img = pygame.image.load("./assets/teste_2.png").convert_alpha()
        self.surf = pygame.image.load('./assets/menu.png').convert()
        self.surf = pygame.transform.scale(self.surf, (win_width, win_height))
        self.rect = self.surf.get_rect()
    def run(self):
        pygame.mixer_music.load('./assets/menu_sound.wav')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(self.surf, self.rect)
            self.window.blit(self.player_img, (40, 420))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
    