def raise_exception_msg(message=""):
    raise NameError()

try:
    raise_exception_msg("C is fun")
except NameError as ne:
    print(ne)