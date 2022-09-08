import time


def timeit(f):
    def timed(*args, **kw):

        ts = time.time()
        result = f(*args, **kw)
        te = time.time()

        print(  # noqa
            f"func:{f.__name__} args:[{args!r}, {kw!r}] took: {te-ts:2.4f} secs"
        )
        return result

    return timed
