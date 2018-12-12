import time
from datetime import datetime


def timeit(method):
    """
    This decorator print the execution time of a function.

    :param method: Method to mesure.
    :return:
    """

    def timed(*args, **kw):
        print('starting {} at {}'.format(method.__name__, datetime.now().time()))
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts))
        else:
            print('execution of {} took {} sec'.format(method.__name__, (te - ts)))
        return result

    return timed
