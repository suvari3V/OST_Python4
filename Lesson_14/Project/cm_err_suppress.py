from contextlib import contextmanager


@contextmanager
def cm_err_suppress():
    try:
        cm = object()
        yield cm
    except ValueError:
        pass
    except Exception as e:
        raise e