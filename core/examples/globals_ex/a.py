def define_global():
    SOME_GLOBAL_CONSTANT = "Value"
    print("A", globals().get("SOME_GLOBAL_CONSTANT"))
    # globals()["SOME_GLOBAL_CONSTANT"] = SOME_GLOBAL_CONSTANT
    # __built_
    globals().update(SOME_GLOBAL_CONSTANT=SOME_GLOBAL_CONSTANT)
    print("A", globals().get("SOME_GLOBAL_CONSTANT"))
