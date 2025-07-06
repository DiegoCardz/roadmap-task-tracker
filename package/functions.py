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
    """
    Module to update existing task descriptions
    """
    id, description = args[0].split(maxsplit=1) if args else (None, [])
    while not id:
        print('A valid task ID is required.')
        print('[ TaskCLI | update ] >>> ', end='')
        try: id = int(input(id))
        except ValueError:
            if id in ('b', 'q', 'break', 'quit'):
                print("Terminating `update` module without updating any task!")
                return
            else: print("Invalid task ID. Please enter a number.")
        # search for id in Task.tasks
        
        
        
    while not description:
        print(f'Type a new valid description for task {id}.')
        print('[ TaskCLI | update ] >>> ', end='')
        description = input().strip(" \"'").lower()
        if description in ('b', 'q', 'break', 'quit'):
            print("Terminating `update` module without updating any task!")
            return
    # Fetch task by ID
    
    pass


#%%
def delete(*args):
    pass


#%%
def mark(*args):
    pass


#%%
@logger
def list(*args):
    """
    Module to list all tasks or filter by status.
    
    ### Examples of usage:
    [ TaskCLI ] >>> list             : --> : lists all tasks
    [ TaskCLI ] >>> list all         : --> : lists all tasks (default)
    [ TaskCLI ] >>> list done        : --> : lists only tasks with status 'done'
    [ TaskCLI ] >>> list todo        : --> : lists only tasks with status 'todo'
    [ TaskCLI ] >>> list in-progress : --> : lists only tasks with status 'in-progress'
    """
    try: status = args[0].lower()
    except IndexError:
        status = 'any'
    
    match status:
        case 'all' | 'any': condition = lambda t: True
        case 'done' | 'todo' | 'in-progress':
            condition = lambda t: t['status'] == status
        case _:
            print(f"Unknown status '{status}'. Showing all tasks.")
            status = 'any'
            condition = lambda t: True
    
    printv(f"{'Showing tasks':-<20}")
    counter = 0
    for t in Task.tasks:
        if condition(t):
            print(t)
            counter += 1
    printv(f"Found {counter} tasks with status == {status}")

#%% Test block
if __name__ == "__main__":
    mode('verbose')
    print(f"Tasks:")
    print('List module-----')
    list()
    list('done')
    list('hadhl')
    list('')
    print(f"max_id: {Task._Task__max_id}")