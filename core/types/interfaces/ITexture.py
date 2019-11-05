from core.types.interfaces import IMaterial, IRender


class ITexture(IMaterial, IRender):
    PATH_TO_TEXTURES = "resources/textures/"

    def __init__(self, texture_path, x, y, width, height, screen, **props):
        IMaterial.__init__(self, x, y, width, height)
        IRender.__init__(self, screen)

        self._rel_path = texture_path

        if props.get("auto_load", True):
            self.image = self._load_texture(self.static_path, **props)

    def _load_texture(self, path, **props):
        import pygame
        texture = pygame.image.load(path)
        if props.get("auto_convert", False):
            texture = texture.convert()
        if props.get("auto_scale", True):
            texture = pygame.transform.scale(texture, (self.width, self.height))
        return texture

    def render(self):
        if self.image:
            self.screen.surface.blit(self.image, self.rect)

    @property
    def static_path(self):
        return "{root}/{rel_path}".format(
            root=self.PATH_TO_TEXTURES,
            rel_path=self._rel_path,
        )
