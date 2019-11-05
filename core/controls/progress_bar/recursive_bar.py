from .progress_bar import ProgressBar


class RecursiveBar(ProgressBar):
    """
    Task 1
    """
    THREAD_NAME = "VKBar"

    def __init__(self, x, y, height, screen, **props):
        super().__init__(x, y, height, screen, **props)

    def update(self, **props):
        """
        len = 4
        0: 0 0 0 0
        1: 1 0 0 0
        2: 1 1 0 0
        3: 1 1 1 0
        4: 1 1 1 1

        5: 0 1 1 1 (-1)
        6: 0 0 1 1 (-2)
        7: 0 0 0 1 (-3)
        8: 0 0 0 0 (-4)
        """
        from core.controls.progress_bar.chunks.progress_chunk import CHUNK_STATE
        is_first_phase = self.current_value <= self.total_value
        if is_first_phase:
            super().update()
        else:
            self.current_value = self.current_value

            _passive_amount = self.current_value % self.total_value
            _active_amount = self.total_value - _passive_amount
            self._chunks_states = [
                *([CHUNK_STATE.PASSIVE] * _passive_amount),
                *([CHUNK_STATE.ACTIVE] * _active_amount),
            ]
        # print(value, self._chunks_states)

    """
    # super().update(
    #     value=self.mod_value(
    #         self.current_value
    #     )
    # )
    # # TODO: Fix
    # print("...")
    # for i in range(self.total_value + 1, self.current_value):
    #     j = self.mod_value(i)
    #     print(j)
    #     self._chunks_states[j] = CHUNK_STATE.PASSIVE
    # print("===")
    """

    # FIXME: DRY
    def next(self):
        from core.modules import console

        if self.current_value == self.total_value * 2 - 1:
            console.log("RESET BAR", thread=self.THREAD_NAME)
            self.current_value = 0
        else:
            self.current_value += 1
        self.update()
