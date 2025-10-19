import pygame

from const import win_height, win_width
from entity import Entity

class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name,position)
        self.speed = 2
        self.spritesheets = self.load_frames()
        self.image = None
        self.current_animation = None
        self.frame_index = 0
        self.animation_speed = 0.2
        self.is_animating = False

    def load_frames(self):
        run_spritesheet = pygame.image.load('assets/Run.png')
        attack_spritesheet = pygame.image.load('assets/Attack_3.png')
        spritesheets = {}

        run_frames = []
        attack_frames = []
        for i in range (3):
            frame = attack_spritesheet.subsurface(pygame.Rect(i*120,0,120,80))
            attack_frames.append(frame)
        spritesheets['Attack'] = attack_frames

        for i in range (8):
            frame = run_spritesheet.subsurface(pygame.Rect(i*80, 0, 80, 80))
            run_frames.append(frame)
        spritesheets['Run'] = run_frames

        return spritesheets

    def animate(self, attack_type):
        if self.current_animation != self.spritesheets[attack_type]:
            self.current_animation = self.spritesheets[attack_type]
            self.frame_index = 0
        self.is_animating = True

    def update(self):
        if self.is_animating:
            self.frame_index += self.animation_speed
            if self.frame_index >= len(self.current_animation):
                self.frame_index = 0
                self.is_animating = False


            self.image = self.current_animation[int(self.frame_index)]

        else:
            self.frame_index = 0
            self.image = pygame.image.load('assets/Player.png')




    def move(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_UP] and self.rect.top > 0:
            self.rect.centery -= self.speed
        if pressed_key[pygame.K_DOWN] and self.rect.bottom < win_height:
            self.rect.centery += self.speed
        if pressed_key[pygame.K_RIGHT] and self.rect.right < win_width:
                self.rect.centerx += self.speed
                self.animate('Run')

        if pressed_key[pygame.K_LEFT] and self.rect.left > 0:
                self.rect.centerx -= self.speed

