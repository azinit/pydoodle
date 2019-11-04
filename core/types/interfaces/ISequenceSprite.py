from core.types.interfaces import IPureSprite


class ISequenceSprite(IPureSprite):
    PATH_TO_SPRITES = "resources/sprites/"

    def __init__(self, texture_path, animation_data, x, y, width, height, screen, **props):
        super().__init__(texture_path, [], x, y, width, height, screen, **props)
        self._frame_pattern = animation_data.get("pattern")
        self.load_frames(animation_data)

    @staticmethod
    def animation_data(amount, pattern):
        return {
            "amount": amount,
            "pattern": pattern
        }

    def load_frames(self, animation_data):
        amount = animation_data.get("amount")
        self._frames = [
            self._load_texture(self.pattern_path.format(i=i))
            for i in range(amount)
        ]

    @property
    def pattern_path(self):
        return "{root}/{rel_path}".format(
            root=self.PATH_TO_SPRITES,
            rel_path=self._frame_pattern
        )
