from core.types.entities import Entity
from core.types.interfaces import ITexture, IPulse


class Effect(Entity, ITexture, IPulse):
    DEFAULT_TEXTURE = "effect/base_diffuse.png"

    def __init__(self, x, y, width, height, screen):
        Entity.__init__(self, x, y, width, height, screen)
        ITexture.__init__(self, self.DEFAULT_TEXTURE, *self.rect_tuple, self.screen)
        IPulse.__init__(self, *self.rect_tuple)

    def update(self, **props):
        self.activate_bindings()

    def render(self):
        # from core.consts import Colors
        # self.screen.draw.rect(self.surface, Colors.CYAN, self.rect_tuple)
        ITexture.render(self)


class JetPack(Effect):
    DEFAULT_TEXTURE = "jetpack/base_diffuse.png"

    def __init__(self, x, y, width, height, screen):
        super().__init__(x, y, width, height, screen)


class ScoreBoost(Effect):
    DEFAULT_TEXTURE = "score/base_diffuse.png"

    def __init__(self, x, y, width, height, screen):
        super().__init__(x, y, width, height, screen)


"""
Класс буста
@class Effect
@extends Entity
"""
