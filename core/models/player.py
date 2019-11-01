from core.consts import Direction
from core.types.entity import Entity

# from core.types.interfaces import Movable

MAX_JUMP_COUNT = 32
_DEFAULT_SPEED = 8


# MAX_JUMP_COUNT = 10
# TODO: Process state (instead of direct properties)
# TODO: Jump,Move functional is Deprecated! Will be moved in the another module!

class Player(Entity):
    DEFAULT_STATE = {
        "is_jump": False,
        "is_move": False,
        "oriented_left": False,
        "oriented_right": False,
    }

    def __init__(self, x, y, width, height, surface, dx=None, dy=None):
        Entity.__init__(self, x, y, width, height, surface, initial_state=self.DEFAULT_STATE)
        # Movable.__init__(self, x, y, 8)

        self.is_jump = False
        self.jump_count = MAX_JUMP_COUNT
        self.dx = dx or _DEFAULT_SPEED
        self.dy = dy or _DEFAULT_SPEED

    def update(self, **props):
        import pygame

        keys = props.get("keys")
        # >>> handle keys
        if keys[pygame.K_SPACE] or keys[pygame.K_w]:
            self.is_jump = True

        # TODO: Switch!
        # >>> Left
        from core.consts import Direction
        if keys[pygame.K_a]:
            self.move(Direction.LEFT)
        if keys[pygame.K_d]:
            self.move(Direction.RIGHT)

        # >>> update
        if self.is_jump:
            self.jump()

    def render(self):
        import pygame

        from core.consts import Colors
        pygame.draw.rect(self.surface, Colors.CYAN, self.rect)
        # print(type(Colors.CYAN))

    # Deprecated! Will be moved in the other class
    def jump(self):
        if self.jump_count >= -MAX_JUMP_COUNT:
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
            self.jump_count = MAX_JUMP_COUNT

    # Deprecated! Will be moved in the other class
    def move(self, *directions):
        for direction in directions:
            self.__move(direction)

    # Deprecated! Will be moved in the other class
    def __move(self, direction: Direction):
        # TODO: Better implementation
        # TODO: Add core/validators?
        if direction == Direction.LEFT:
            self.x -= self.dx
        if direction == Direction.RIGHT:
            self.x += self.dx
        if direction == Direction.UP:
            self.y -= self.dy
        if direction == Direction.DOWN:
            self.y += self.dy
