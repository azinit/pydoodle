from core.types.interfaces import IMaterial, ISpeed, IUpdate, IStateDependent


# TODO: Mixins implements one interface (ISpeed) and __init__ them overwrite properties

# TODO: ? if state.is_some: some()
class GravityMixin(IMaterial, ISpeed, IUpdate, IStateDependent):
    """
    Миксин для возможности прыжка сущности
    @example
    <pre>
        class SomeClass(GravityMixin):
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

    def __init__(self, x, y, width, height, **props):
        IMaterial.__init__(self, x, y, width, height)
        ISpeed.__init__(self, **props)
        IStateDependent.__init__(self)
        self.state.is_jumping = props.get("is_jumping", False)
        self.state.is_falling = props.get("is_falling", False)
        self.state.is_bouncing = props.get("is_bouncing", False)
        self.state.ground = None
        self._gravity_info = None

    def update(self, **props):
        from pygame import K_SPACE

        keys = props.get("keys")
        grounds = props.get("grounds", [])

        # >>> set state
        for potential_ground in grounds:
            if self.is_landed_on(potential_ground):
                if self.state.is_bouncing:
                    self.state.is_jumping = True
                    self.state.is_falling = False
                    self.state.ground = None
                    self.speed.y = self.JUMP_POTENTIAL_VELOCITY * potential_ground.elasticity
                else:
                    self.land(potential_ground)
                break
        else:
            self.state.is_falling = True

        if keys[K_SPACE] and not self.state.is_falling:
            self.state.is_jumping = True
            self.speed.y = self.JUMP_POTENTIAL_VELOCITY

        # # >>> check state
        if self.state.is_jumping:
            self.jump()

        if self.state.is_falling:
            self.fall()

    def jump(self):
        # console.log("^ JUMP", flush=True)
        self.state.is_falling = False
        self.state.ground = None

        self.y -= self.speed.y
        self.speed.y -= self.GRAVITY_ACCELERATION
        if self.speed.y < 0:
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
        # console.log("- LAND", flush=True)
        self.state.is_jumping = False
        self.state.is_falling = False

        self.speed.y = 0
        self.state.ground = ground
        # FIXME:
        self.y = ground.rect.top - self.height + 2

    def fall(self):
        # console.log("V FALL", flush=True)
        self.state.is_jumping = False
        self.state.is_falling = True
        self.state.ground = None

        self.speed.y -= self.GRAVITY_ACCELERATION
        self.y -= self.speed.y

    # @property
    # def JUMP_POTENTIAL_VELOCITY(self):
    #     import math
    #     return math.sqrt(2 * self.GRAVITY_ACCELERATION * self.JUMP_POTENTIAL_HEIGHT)

    @property
    def is_landed(self):
        return self.state.ground is not None

    @property
    def gravity_info(self):
        states = [
            self.state.is_jumping,
            self.is_landed,
            self.state.is_falling,
        ]
        labels = [
            ("T" if state else "F") for state in states
        ]

        if states[0]:
            process = "^"
        elif states[1]:
            process = "-"
        elif states[2]:
            process = "V"
        else:
            process = "?"

        info = "J:{J} | F:{F} | L:{L} | {P}".format(
            J=labels[0],
            L=labels[1],
            F=labels[2],
            P=process,
        )

        IS_UNDEFINED = self._gravity_info is None
        IS_CHANGED = self._gravity_info != info
        if IS_UNDEFINED or IS_CHANGED:
            self._gravity_info = info
            # print(":::", self._position_info)
            return info

        return None
