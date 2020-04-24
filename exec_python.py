import re, functools, types
from pyperclip import paste, copy

def copy_decorator(func):
    @functools.wraps(func)
    def copy_func(*args, **kwargs):
        result = func(*args, **kwargs)
        if hasattr(result, "__str__"):
            #Kun hvis resultatet kan konverteres til string kan det kopieres
            copy(str(result))
        return result
    return copy_func

#Decorate alle funktioner fra modulerne i listen
DECORATED_MODULES = [re]
for module in DECORATED_MODULES:
    for k,v in vars(module).items():
        if isinstance(v, types.FunctionType):
            vars(module)[k] = copy_decorator(v)

@copy_decorator
def nonewlines(s):
    """
    Replace carriage return- and newline-characters with space charater.
    """
    s = s.replace("\r", " ")
    s = s.replace("\n", " ")

    return s

if __name__ == "__main__":
    s = paste()
    print(s)
