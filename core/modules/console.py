PROGRESS_OPTIONS_ITER = {
    "allowed_sys_time": True,
    "allowed_iterator": True,
    "allowed_percent":  False,
    "symb_wait":        "~",
    "symb_finished":    "V",
}


def __sys_time():
    from datetime import datetime
    sys_time = datetime.now().strftime("%H:%M:%S")
    return "[%s] " % sys_time


def write(*values, **kwargs):
    """ Extended print analogue """
    sep         = kwargs.get("sep", " ")
    end         = kwargs.get("end", "\n")
    # file      = kwargs.get("file", None)      # TODO:
    flush       = kwargs.get("flush", False)
    color       = kwargs.get("color", None)     # TODO:
    # TODO: sys_time?

    if flush:
        import sys
        sys.stdout.write("\r" + sep.join(values))
        sys.stdout.flush()
    else:
        print(*values, sep=sep, end=end)

# TODO: As decorator?
def log(message, **kwargs):
    """
    Выводит сообщение с указанием времени
    :param message: Выводимое сообщение
    :param thread: Оповещаемый поток
    :param flush: Нужно ли вывести последующее сообщение на той же строчке
    :return:
    """
    thread = kwargs.get("thread", None)
    flush  = kwargs.get("flush", None)

    from datetime import datetime
    sys_time = datetime.now().strftime("%H:%M:%S")
    write("[{sys_time}]{thread} {message}".format(
        sys_time=sys_time,
        thread="" if thread is None else " [%s]" % thread,
        message=message,
    ), **kwargs)


def process(title, **kwargs):
    """ Print process header with decorators """
    width               = kwargs.get("width", 32)
    symb                = kwargs.get("symb", ".")
    indent              = kwargs.get("indent", True)
    allowed_sys_time    = kwargs.get("allowed_sys_time", False)

    # indent case
    if indent:
        title = " %s " % title
    # init pattern constructor
    pattern = ":{symb}^{width}".format(
        symb=symb,
        width=width,
    )
    pattern = "{%s}" % pattern
    # fill pattern
    msg = "{time}{msg}".format(
        time=allowed_sys_time * __sys_time(),
        msg=pattern.format(title),
    )
    write(msg, **kwargs)


def wait(callback):
    import time
    while not callback():
        steps = ["\\", "|", "/", "-"]
        for s in steps:
            write(s, flush=True)
            time.sleep(0.1)


def result(item, state, available_results, **kwargs):
    thread      = kwargs.get("thread", None)

    are_valid_results = len(available_results) >= 2
    if are_valid_results:
        log(
            message=available_results[state] % item,
            thread=thread,
        )


if __name__ == '__main__':
    def __test__log():
        print(":::::::::::::::::::::log:::::::::::::::::::::")
        log("Hello!")
        log(message="Hello")
        log("Lop", thread="AP")
        log([1, 2, 3])
        log("Message #1", flush=True)
        log("Message #2", flush=True)
        log("Message #3", flush=True)

    def __test__process():
        print(":::::::::::::::::::::process:::::::::::::::::::::")
        # process("L")
        process(
            title="TITLE",
            indent=True,
            width=100,
            symb="/"
        )

        process(
            title="PROCESS",
            indent=True,
            width=64,
            allowed_sys_time=True,
        )

    def __test__write():
        print(":::::::::::::::::::::write:::::::::::::::::::::")
        write("dw", flush=True)
        write("dw", flush=True)
        write("dw", flush=False)
        write("dw", flush=False)
        write("---", "EXCEL", "WRITE", "ROW", "WORK!@#FA%D#$@LF@")


    def __test__wait():
        print(":::::::::::::::::::::wait:::::::::::::::::::::")
        wait(lambda: False)
    # ........................................................................................................
    # __test__log()
    # __test__process()
    # __test__write()
    # __test__progress()
    # __test__ask()
    __test__wait()
