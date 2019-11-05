# https://gist.github.com/lambdalisue/973978/465e7ec8cb34e6bf7842dd2780edc94c171d7905
# https://stackoverflow.com/questions/533631/what-is-a-mixin-and-why-are-they-useful
# https://instructobit.com/tutorial/108/How-to-share-global-variables-between-files-in-Python
# https://www.programiz.com/python-programming/methods/built-in/globals
# https://thepythonguru.com/python-builtin-functions/globals/

# FIXME: Implement better


class SingletonMixin(object):
    """
    Миксин для синглтона
    @remark
    Позволяет создавать глобальный объект для всего класса
    @example
    <pre>
        class SomeClass(SingletonMixin):
            ...

        # получение глобального объекта класса (например общего экрана, игрока, ...)
        SomeClass.get_global()
    </pre>
    @mixin SingletonMixin
    """
    DEFAULT_PROPS = {}
    __GLOBAL_INSTANCE = None

    # def __init__(self, **kwargs):
    #     pass

    @classmethod
    def get_global(cls, **props):
        # >>> if not exist -> create new global instance
        if cls.__GLOBAL_INSTANCE is None or props.get("reset", False):
            cls.__GLOBAL_INSTANCE = cls(**cls.DEFAULT_PROPS)

        return cls.__GLOBAL_INSTANCE
