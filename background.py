from entity import Entity


class Background(Entity):
    def __init__(self, name: str, position=(0, 0)):
        super().__init__(name, position)

    def move(self):
        # O mapa não se move, mas você pode colocar lógica de scroll futuramente
        pass