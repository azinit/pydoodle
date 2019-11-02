from core.types.interfaces import (
    IRender,
    IUpdate,
    IHandleEvents,
)


# FIXME: Caption "captin | PyDoodl "

class Scene(IRender, IUpdate, IHandleEvents):
    THREAD = "SCENE"

    def __init__(self, caption=None):
        from core.types.entities import Screen
        super().__init__(Screen.get_global())
        self.caption = caption or self.screen.caption
        self.screen.set_caption(self.caption)
        self._controls = []

    def render(self):
        raise NotImplementedError

    def update(self, **props):
        raise NotImplementedError

    def handle_events(self, events):
        raise NotImplementedError

    def _render(self):
        raise NotImplementedError

    def _render__controls(self):
        for _control in self._controls:
            _control.render()
