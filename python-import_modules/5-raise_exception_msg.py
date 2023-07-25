def raise_exception_msg(message=""):
    if not message:
        message = "Name error"

    raise NameError(message)

raise_exception_msg("C is fun")