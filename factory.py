import pygame

from background import Background
from player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'map_2':
                return Background('map_2', position)
            case 'Player':
                return Player('Player', (45,400))
