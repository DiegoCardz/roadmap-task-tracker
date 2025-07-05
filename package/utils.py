from . import config
import functools

#%% Special print function to show specific messages only in verbose mode
def printv(*args, **kwargs):
    if config.verbose:
        print('----', end='') 
        print(*args, **kwargs)


# %% Decorator to track calls
def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        printv(f"@logger: Calling {func.__name__}")
        if args: printv("----Positional:", args)
        if kwargs: printv("----Keyword:", kwargs)
        return func(*args, **kwargs)
    return wrapper



