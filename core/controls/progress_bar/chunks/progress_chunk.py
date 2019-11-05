from core.controls import Control


# @typedef
class CHUNK_STATE:
    PASSIVE = 0
    ACTIVE = 1

    @staticmethod
    def color(state):
        from core.consts import Colors
        if state == CHUNK_STATE.PASSIVE:
            return Colors.GRAY
        if state == CHUNK_STATE.ACTIVE:
            return Colors.SOFT_CYAN


class ProgressChunk(Control):
    CHUNK_STATE_DEFAULT = CHUNK_STATE.PASSIVE

    def __init__(self, x, y, width, height, screen, **props):
        super().__init__(x, y, width, height, screen, **props)
        self._state = props.get("initial_state", self.CHUNK_STATE_DEFAULT)
        self._mapper = props.get("mapper", CHUNK_STATE.color)

    def render(self):
        self.screen.draw.rect(self.surface, self._mapper(self._state), self.rect)

    def update(self, **props):
        state = props.get("state", None)
        if state:
            self._state = state
