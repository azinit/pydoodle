def my_decorator(func):
    print("... DECORATOR-HEADER...")
    func()
    print("... DECORATOR-FOOTER...")


@my_decorator
def my_func():
    print("MY FUNC")
