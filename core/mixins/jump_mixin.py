from core.types.interfaces import IMaterial


class JumpMixin(IMaterial):
    MAX_JUMP_COUNT = 32

    def __init__(self, x, y, width, height, is_jump=False, max_jump_count=None):
        super().__init__(x, y, width, height)
        self.is_jump = is_jump
        self.jump_count = max_jump_count or self.MAX_JUMP_COUNT
        self.MAX_JUMP_COUNT = max_jump_count or self.MAX_JUMP_COUNT

    def jump(self):
        if self.jump_count >= -self.MAX_JUMP_COUNT:
            jump_step = self.jump_count / 2.5
            # jump_step = (self.jump_count ** 2) / 2
            # if self.jump_count < 0:
            #     self.y += jump_step
            # else:
            #     self.y -= jump_step
            self.y -= jump_step
            self.jump_count -= 1
        else:
            self.is_jump = False
            self.jump_count = self.MAX_JUMP_COUNT
