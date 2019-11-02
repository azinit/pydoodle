class SingletonMixin(object):
    __GLOBAL_INSTANCE = None

    def __init__(self, singleton_class, singleton_props):
        self.__class = singleton_class
        self.props = singleton_props

    @staticmethod
    def get_global():
        if self.__GLOBAL_INSTANCE is None:
            self.__GLOBAL_INSTANCE = self.__class(**self.props)
        return self.__GLOBAL_INSTANCE
