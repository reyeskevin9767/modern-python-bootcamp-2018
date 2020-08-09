
# * Show Args Exercise
'''
@show_args
def do_nothing(*args, **kwargs):
    pass

do_nothing(1, 2, 3,a="hi",b="bye")

# Should print (on two lines):
# Here are the args: (1, 2, 3)
# Here are the kwargs: {"a": "hi", "b": "bye"}
'''

from functools import wraps


def show_args(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        show_args = (args)
        show_kwargs = dict(kwargs)
        # print(f"Here are the args: {show_args}")
        # print(f"Here are the kwargs: {show_kwargs}")
        print("Here are the args: {}".format(show_args))
        print("Here are the kwargs: {}".format(show_kwargs))
        return fn(*args, **kwargs)
    return wrapper


@show_args
def do_nothing(*args, **kwargs):
    pass


print(do_nothing(1, 2, 3, a="hi", b="bye"))
