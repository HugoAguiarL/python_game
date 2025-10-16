import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 900
altura = 500

PRETO = (255, 255, 255)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Sprites')


class Sapo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        for i in range(0,7):
            self.sprites.append(pygame.image.load(f'./assets/img_{i}.png'))

        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (45 * 1, 81 * 1))

        self.rect = self.image.get_rect()
        self.rect.topleft = 100, 100

        self.animar = False

    def atacar(self):
        self.animar = True

    def update(self):
        if self.animar == True:
            self.atual = self.atual + 0.35
            if self.atual >= len(self.sprites):
                self.atual = 0
                self.animar = False
            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (45 * 1, 81 * 1))


todas_as_sprites = pygame.sprite.Group()
sapo = Sapo()
todas_as_sprites.add(sapo)

relogio = pygame.time.Clock()

while True:
    relogio.tick(30)
    tela.fill(PRETO)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            sapo.atacar()

    todas_as_sprites.draw(tela)
    todas_as_sprites.update()
    pygame.display.flip()