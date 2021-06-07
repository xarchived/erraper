__version__ = '0.1.0'

import logging
import time


def error_wrapper(func, pass_exceptions=None, retry_exceptions=None, delays=None, *args, **kwargs):
    if not retry_exceptions:
        retry_exceptions = ()
    if not pass_exceptions:
        pass_exceptions = ()

    delay_times = {}
    for e in retry_exceptions:
        delay = 3
        if delays:
            delay = delays.pop(0)
        delay_times[e] = delay

    while True:
        try:
            return func(*args, **kwargs)
        except pass_exceptions as e:
            logging.info(f'"{type(e).__name__}" raised from "{func.__name__}". Error has been passed')
            break
        except retry_exceptions as e:
            delay = delay_times[type(e)]
            logging.info(f'"{type(e).__name__}" raised from "{func.__name__}". Retry after {delay} seconds')
            time.sleep(delay)
            pass


def error_handler(pass_exceptions=None, retry_exceptions=None, delays=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return error_wrapper(
                func=func,
                pass_exceptions=pass_exceptions,
                retry_exceptions=retry_exceptions,
                delays=delays,
                *args,
                **kwargs,
            )

        return wrapper

    return decorator
