from functools import wraps


def addarg(arg):
    """Returns a decorator that add argument to list of another arguments."""
    def addarg_decorator(f):
        """Decorator function that apply wrapper on each call."""
        @wraps(f)
        def addarg_wrapper(*args, **kwargs):
            """Adds argument as the first argument to all calls to
            decorated functions."""
            return f(arg, *args, **kwargs)
        return addarg_wrapper
    return addarg_decorator

