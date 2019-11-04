class Some(object):
    def __init__(self, state=None):
        from types import SimpleNamespace
        self.state = SimpleNamespace()
        self.state.a = ">>> A"
        self.state.b = "<<< B"
        print(dir(self.state))

    def foo(self):
        print(self.state.a)
        print(self.state.b)


Some().foo()