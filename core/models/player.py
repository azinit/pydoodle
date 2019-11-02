from core.consts import Direction
from core.types.entities import DynamicEntity, Screen
# from core.mixins import SingletoneMixin

MAX_JUMP_COUNT = 32
_DEFAULT_SPEED = 8


# MAX_JUMP_COUNT = 10
# TODO: Process state (instead of direct properties)
# TODO: Jump,Move functional is Deprecated! Will be moved in the another module!

# class Player(DynamicEntity, SingletoneMixin):
class Player(DynamicEntity):
    DEFAULT_STATE = {
        "is_jump": False,
        "is_move": False,
        "oriented_left": False,
        "oriented_right": False,
    }

    DEFAULT_PROPS = {
        "x": 50,
        "y": 425,
        "width": 60,
        "height": 71,
        "screen": Screen.get_global()
    }

    __GLOBAL_INSTANCE = None

    def __init__(self, x, y, width, height, screen, dx=None, dy=None):
        DynamicEntity.__init__(self, x, y, width, height, screen, initial_state=self.DEFAULT_STATE)
        # SingletoneMixin.__init__(self, Player, self.DEFAULT_PROPS)
        # Movable.__init__(self, x, y, 8)

        self.is_jump = False
        self.jump_count = MAX_JUMP_COUNT
        self.dx = dx or _DEFAULT_SPEED
        self.dy = dy or _DEFAULT_SPEED

    def update(self, **props):
        import pygame

        keys = props.get("keys")
        # >>> handle keys

        if keys[pygame.K_SPACE]:
            self.is_jump = True

        # TODO: Switch!
        # >>> Left
        from core.consts import Direction
        # print(self._position_info)
        if keys[pygame.K_a] and not self.left_border_passed:
            self.move(Direction.LEFT)
        if keys[pygame.K_d] and not self.right_border_passed:
            self.move(Direction.RIGHT)
        if keys[pygame.K_w] and not self.top_border_passed:
            self.move(Direction.UP)
        if keys[pygame.K_s] and not self.bottom_border_passed:
            self.move(Direction.DOWN)

        # >>> update
        if self.is_jump:
            self.jump()

    def render(self):
        import pygame

        from core.consts import Colors
        pygame.draw.rect(self.screen.surface, Colors.CYAN, self.rect)
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

    @staticmethod
    def get_global():
        if Player.__GLOBAL_INSTANCE is None:
            from core.types.entities import Screen
            Player.__GLOBAL_INSTANCE = Player(
                x=50,
                y=425,
                width=60,
                height=71,
                screen=Screen.get_global(),
            )

        return Player.__GLOBAL_INSTANCE
