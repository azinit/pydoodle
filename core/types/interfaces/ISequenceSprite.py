from core.types.interfaces import IPureSprite


class ISequenceSprite(IPureSprite):
    """
    @todo Добавить возможность анализировать спрайт из текстурного атласа
    """
    PATH_TO_SPRITES = "resources/sprites/"

    def __init__(self, texture_path, animation_data, x, y, width, height, screen, **props):
        super().__init__(texture_path, [], x, y, width, height, screen, **props)
        self._frame_pattern = animation_data.get("pattern")
        self.__amount = animation_data.get("amount")
        self.load_frames()

    @staticmethod
    def animation_data(amount, pattern):
        return {
            "amount": amount,
            "pattern": pattern
        }

    def load_frames(self, ):
        self._frames = [
            self._load_texture(self.pattern_path.format(i=i))
            for i in range(self.__amount)
        ]

    @property
    def pattern_path(self):
        return "{root}/{rel_path}".format(
            root=self.PATH_TO_SPRITES,
            rel_path=self._frame_pattern
        )
