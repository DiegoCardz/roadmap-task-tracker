#%%
from . classes import Task
from . utils import logger, printv
from .  import config


#%%
def help(*args):
    module  = args[0].strip().lower() if args else 'help'

    def print_help():
        print("Available modules:\n"
              "- add (a): add a new task\n"
              "- update (u | up): update an existing task\n"
              "- delete (d | del): delete a task\n"
              "- mark (m): mark a task as done or not done\n"
              "- list (l): list all tasks\n"
              "- mode: change between verbose and normal mode\n"
              "- help (h): show this help message\n"
              "- quit (q): exit the CLI\n"
              "Or type 'help <module>' for more information on a specific module."
              )
    
    match module:
        case 'add': print(add.__doc__)
        case 'update': print(update.__doc__)
        case 'delete': print(delete.__doc__)
        case 'mark': print(mark.__doc__)
        case 'list': print(list.__doc__)
        case 'mode': print(mode.__doc__)
        case 'help': print_help()
        case _:
            print(f"Unknown module '{args[0]}'.")
            print_help()

#%%
@logger
def mode(*args):
    """
    Module to change from verbose to normal mode and vice-versa.
    
    ### Examples of usage:  
    [ TaskCLI ] >>> mode verbose    : --> : changes to verbose mode
    [ TaskCLI ] >>> mode normal     : --> : changes to normal mode
    [ TaskCLI ] >>> mode            : --> : toggles between verbose and normal mode
    """
    new_mode = args[0] if args else ''
    match new_mode:
        case 'verbose': config.verbose = True
        case 'normal': config.verbose = False
        case _: 
            config.verbose = not config.verbose
    printv(f"mode changed to verbose")


#%%
@logger
def add(*args):
    description = args[0].strip(' "\'') if args else None
    
    while (not description):
        print('A valid description is required.')
        print('[ TaskCLI | add ] >>> ', end='')
        description = input().strip(" \"'").lower()
        if description in ('b', 'q', 'break', 'quit'):
            print("Terminating `add` module without adding a new task!")
            return
    t = Task(description.title())
    t.export_to_file()


#%%
def update(*args):
    pass


#%%
def delete(*args):
    pass


#%%
def mark(*args):
    pass


#%%
def list(*args):
    print(Task.tasks)
    pass

#%% Test block
if __name__ == "__main__":
    print('add.__doc__ :', add.__doc__)
    print('mode.__doc__ :', mode.__doc__)