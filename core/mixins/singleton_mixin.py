class SingletonMixin(object):
    DEFAULT_PROPS = {}
    __GLOBAL_INSTANCE = None

    # def __init__(self, **kwargs):
    #     pass

    @classmethod
    def get_global(cls):
        # >>> if not exist -> create new global instance
        if cls.__GLOBAL_INSTANCE is None:
            cls.__GLOBAL_INSTANCE = cls(**cls.DEFAULT_PROPS)

        return cls.__GLOBAL_INSTANCE
