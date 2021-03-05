import functools
import time
import logging


# Set Up Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s.%(msecs)03d : %(levelname)s : %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)
# set Debug on during development - Comment out below to reduce log level
logger.setLevel(logging.DEBUG)


def time_func(print_it: bool=True, log_it: bool=False):
    '''Decorator to wrap function and time how long it takes to run - either logs or print or both.

    This must be run with @time_func().

    Parameters:
    print_it:   bool        - If True(default) then prints execution time of function that is decorated
    log_it:     bool        - If True then logs execution time of the function that is decorated as a logging.debug message.
    '''
    def decorator_timefunc(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            value = func(*args, **kwargs)
            end_time = time.perf_counter()
            elapsed_time = end_time - start_time
            if print_it:
                print(f"Execution of function: {func.__name__} took {elapsed_time:4f}")
            if log_it:
                logger.debug(f"Execution of function: {func.__name__} took {elapsed_time:4f}")
            return value
        return wrapper
    return decorator_timefunc
