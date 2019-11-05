from core.controls import Control
from .chunks.progress_chunk import ProgressChunk, CHUNK_STATE


# _DEFAULT_CHUNKS_GAP = 8
# _DEFAULT_CHUNK_WIDTH = 128


# TODO: Chunks amount?
# TODO: Custom args
# TODO: Default values in class

class ProgressBar(Control):
    """
    Base control implementation
    """

    THREAD_NAME = "ProgressBar"
    DEFAULT_TOTAL_VALUE = 4
    DEFAULT_CHUNKS_WIDTH = 128
    DEFAULT_CHUNKS_GAP = 8
    DEFAULT_CHUNKS_MODEL = ProgressChunk

    def __init__(self, x, y, height, screen, **props):
        super().__init__(x, y, 0, height, screen, **props)
        # >>> init chunks
        self._chunks_model = props.get("chunks_model", self.DEFAULT_CHUNKS_MODEL)
        self._chunks_width = props.get("chunks_width", self.DEFAULT_CHUNKS_WIDTH)
        self._chunks_gap = props.get("chunks_gap", self.DEFAULT_CHUNKS_GAP)
        self._chunks_states = []

        self.current_value = props.get("current_value", 1)
        self.total_value = props.get("total_value", self.DEFAULT_TOTAL_VALUE)
        self.update(value=self.current_value)

    @staticmethod
    def generate_options(chunks_model=None, chunks_width=None, chunks_gap=None, total_value=None, initial_options=None):
        _options = initial_options if initial_options else {}
        # FIXME:
        if chunks_model is not None: _options["chunks_model"] = chunks_model
        if chunks_width is not None: _options["chunks_width"] = chunks_width
        if chunks_gap is not None: _options["chunks_gap"] = chunks_gap
        if total_value is not None: _options["total_value"] = total_value

        return _options

    # @staticmethod
    # def generate_options(initial_options=None, **new_options):
    #
    #     # available_options = [
    #     #     "chunks_model",
    #     #     "chunks_width",
    #     #     "chunks_gap",
    #     #     "total_value",
    #     # ]
    #     _options = initial_options or {}
    #     return {
    #         **_options,
    #         "chunks_model": new_options.get("chunks_model"),
    #         "chunks_width": new_options.get("chunks_width"),
    #         "chunks_gap": new_options.get("chunks_gap"),
    #         "total_value": new_options.get("total_value"),
    #     }

    @property
    def width(self):
        return self.total_value * (self._chunks_width + self._chunks_gap) - self._chunks_gap

    @property
    def passive_amount(self):
        return self.total_value - self.current_value

    @property
    def is_filled(self):
        return self.current_value == self.total_value

    def update(self, **props):
        _chunk_active_state = props.get("active_state", CHUNK_STATE.ACTIVE)
        _chunk_passive_state = props.get("passive_state", CHUNK_STATE.PASSIVE)
        # print(_chunk_active_state, props)

        self._chunks_states = [
            *([_chunk_active_state] * self.current_value),
            *([_chunk_passive_state] * self.passive_amount),
        ]
        # self._chunks_states[0] = CHUNK_STATE.PASSIVE

    def next(self):
        # TODO: pass
        if self.current_value == self.total_value:
            self.current_value = 0
        else:
            self.current_value += 1
        self.update()

    def render(self):
        next_x = self.x
        next_y = self.y

        for chunk_state in self._chunks_states:
            self._chunks_model(
                x=next_x,
                y=next_y,
                width=self._chunks_width,
                height=self.height,
                initial_state=chunk_state,
                screen=self.screen,
            ).render()
            next_x += self._chunks_width + self._chunks_gap
