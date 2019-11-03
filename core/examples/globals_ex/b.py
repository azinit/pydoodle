from core.examples.globals_ex.a import define_global

if __name__ == '__main__':
    print(globals())
    print(globals().keys())
    print("B", globals().get("SOME_GLOBAL_CONSTANT"))
    define_global()
    print("B", globals().get("SOME_GLOBAL_CONSTANT"))
    print(globals().keys())

