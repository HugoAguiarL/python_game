import pygame

from background import Background


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name.lower():
            case 'map_2':
                return Background('map_2', position)
