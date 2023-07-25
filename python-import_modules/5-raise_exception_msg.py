def raise_exception_msg(message=""):
    try:
        raise_exception_msg("C is fun")
    except NameError as ne:
        print(ne)

raise_exception_msg("")