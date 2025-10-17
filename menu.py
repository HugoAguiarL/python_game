import pygame.image
import pygame.display
import pygame.transform
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from const import win_height, win_width, color_blue, menu_option, color_grey


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/menu.png').convert()
        self.surf = pygame.transform.scale(self.surf, (win_width, win_height))
        self.rect = self.surf.get_rect()

    def run(self):
        menu_op = 0
        # pygame.mixer_music.load('./assets/menu_sound.wav')
        # pygame.mixer_music.play(-1)
        while True:
            self.window.blit(self.surf, self.rect)
            self.menu_text(80, "Blue Samurai", color_blue, (win_width / 2, 100))

            for i in range(len(menu_option)):
                if i == menu_op:
                    self.menu_text(25, menu_option[i], color_blue, (win_width / 2, 350 + 30 * i))
                else:
                    self.menu_text(25, menu_option[i], color_grey, (win_width / 2, 350 + 30 * i))

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_op < (len(menu_option) - 1):
                            menu_op = menu_op + 1
                    if event.key == pygame.K_UP:
                        if menu_op > 0:
                            menu_op = menu_op - 1
                    if event.key == pygame.K_RETURN:
                        return menu_op

            pygame.display.flip()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont("Lucida Sans Typewriter", text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)
