def raise_exception_msg(message=""):
    raise NameError(message)
try:
    name = "C is fun"
except NameError as e:
    print("Error:", e)

raise_exception_msg()