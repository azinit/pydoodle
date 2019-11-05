from core.types.interfaces import IStateDependent


class IGenerate(IStateDependent):
    def __init__(self):
        super().__init__()

    def generate(self):
        raise NotImplementedError
