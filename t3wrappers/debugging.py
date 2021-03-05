import functools
import time
import logging
from types import WrapperDescriptorType


# Set Up Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s.%(msecs)03d : %(levelname)s : %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)
# set Debug on during development - Comment out below to reduce log level
logger.setLevel(logging.DEBUG)


def debug_func(print_it: bool=True, log_it: bool=False):
    """Decorator to log or output calling and return values of functions

    This must be run with @debug_func().

    Parameters:
    print_it:   bool        - If True(default) then prints start time and funciton name with calling parameters, and end time return value and type of function that is decorated
    log_it:     bool        - If True(default) then logs start time and funciton name with calling parameters, and end time with  return value and type of function that is decorated
    """
    def decorate_debug_func(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            args_repr = [repr(arg) for arg in args]
            kwargs_repr = [f"{(key)}={value!r}" for key,value in kwargs.items()]
            start_message = f"Beginning Execution of function: {str(func.__name__)}({', '.join(args_repr + kwargs_repr)})"
            start_time = time.time()
            if print_it:
                print(f"{time.ctime(start_time)} - {start_message}")
            if log_it:
                logger.debug(f"{start_message}")
            value = func(*args, **kwargs)
            end_time = time.time()
            execution_time = end_time - start_time
            end_message = f"Execution of {func.__name__} completed and returned '{repr(value)}' of type {type(value)}. Execution Time = {execution_time:4f}s"
            if print_it:
                print(f"{time.ctime(end_time)} - {end_message}")
            if log_it:
                logger.debug(f"{end_message}")
            return value
        return wrapper
    return decorate_debug_func




