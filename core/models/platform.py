from core.types.entities import DynamicEntity


class Platform(DynamicEntity):
    def __init__(self, x, y, width, height, screen, initial_state=None):
        super().__init__(x, y, width, height, screen, initial_state=initial_state)
    
    def update(self, **props):
        pass

    def render(self):
        import pygame
        from core.consts import Colors
        pygame.draw.rect(self.surface, Colors.D_RAVEN, self.rect)


"""
Класс платформы
@class Entity (DynamicEntity?)
"""