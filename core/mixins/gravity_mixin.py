from core.types.interfaces import IMaterial, ISpeed, IUpdate


# TODO: Mixins implements one interface (ISpeed) and __init__ them overwrite properties

# TODO: ? if state.is_some: some()
class GravityMixin(IMaterial, ISpeed, IUpdate):
    """
    Миксин для возможности прыжка сущности
    @example
    <pre>
        class SomeClass(JumpMixin):
            ...
        ...
        some_entity = SomeClass(...)
        ...
        # "Заставляем" сущность прыгать
        some_entity.jump()
    </pre>
    @mixin JumpMixin
    @implements IMaterial
    """
    # JUMP_POTENTIAL_HEIGHT = 200
    JUMP_POTENTIAL_VELOCITY = ISpeed.DEFAULT_SPEED * 2
    GRAVITY_ACCELERATION = 0.5

    # TODO: Realize accelerate?
    # TODO: state dependent

    def __init__(self, x, y, width, height,
                 is_jump=False, is_landed=False, is_falling=True,
                 dx=None, dy=0):
        IMaterial.__init__(self, x, y, width, height)
        ISpeed.__init__(self, dx=dx, dy=dy)
        print(">>>", self.dy)
        self.is_jumping = is_jump
        # self.is_landed = is_landed
        self.is_falling = is_falling
        self.ground = None

    def update(self, **props):
        from pygame import K_SPACE

        keys = props.get("keys")
        grounds = props.get("grounds", [])

        # >>> set state
        for potential_ground in grounds:
            if self.is_landed_on(potential_ground):
                self.land(potential_ground)
                break
        else:
            self.is_falling = True

        if keys[K_SPACE] and not self.is_falling:
            self.is_jumping = True
            self.dy = self.JUMP_POTENTIAL_VELOCITY

        # # >>> check state
        if self.is_jumping:
            self.jump()

        if self.is_falling:
            self.fall()

    def jump(self):
        print("^", "JUMP")
        # self.is_jumping = True
        self.is_falling = False
        self.ground = None

        self.y -= self.dy
        self.dy -= self.GRAVITY_ACCELERATION
        if self.dy < 0:
            self.fall()

        # Deprecated! Old implementation!
        # if self.jump_count >= -self.MAX_JUMP_COUNT:
        #     jump_step = self.jump_count / 2.5
        #     # jump_step = (self.jump_count ** 2) / 2
        #     # if self.jump_count < 0:
        #     #     self.y += jump_step
        #     # else:
        #     #     self.y -= jump_step
        #     self.y -= jump_step
        #     self.jump_count -= 1
        # else:
        #     self.land()

    # TODO: implement landed_ground
    def land(self, ground):
        print("-", "LAND")
        self.is_jumping = False
        self.is_falling = False

        self.dy = 0
        self.ground = ground
        # FIXME:
        self.y = ground.rect.top - self.height + 2

    def fall(self):
        print("V", "FALL")
        self.is_jumping = False
        self.is_falling = True
        self.ground = None

        self.dy -= self.GRAVITY_ACCELERATION
        self.y -= self.dy

    # @property
    # def JUMP_POTENTIAL_VELOCITY(self):
    #     import math
    #     return math.sqrt(2 * self.GRAVITY_ACCELERATION * self.JUMP_POTENTIAL_HEIGHT)

    @property
    def is_landed(self):
        return self.ground is None
