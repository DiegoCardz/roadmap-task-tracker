#%%
from . classes import Task
from . utils import logger, printv
from .  import config
from datetime import datetime as dt

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
    """
    Module to add a new task.

    ### Examples of usage:
    [ TaskCLI ] >>> add [description]    : --> : adds a new task with the given description
    OR
    [ TaskCLI ] >>> add
    [ TaskCLI / add ] >>> [description]  : --> : prompts for a description and adds a new task
    """
    description = args[0].strip(' "\'') if args else None
    
    while (not description):
        print('A valid description is required.')
        print('[ TaskCLI | add ] >>> ', end='')
        description = input().strip(" \"'").lower()
        if description in ('b', 'q', 'break', 'quit'):
            print("Terminating `add` module without adding a new task!")
            return
    t = Task(description.title())
    Task.export_to_file()


#%%
@logger
def action_manager(action, *args):
    """
    Handles task actions such as update, mark, and delete by managing user input and delegating to the appropriate function.

    Parameters:
        action (str): The action to perform ('update', 'mark', or 'delete').
        *args: Arguments containing the task id and any additional parameters.

    Usage:
        action_manager('update', '1 New description')
        action_manager('mark', '2 done')
        action_manager('delete', '3')
    """
    id, *rest = args[0].split(maxsplit=1) if args else (None, [])
    Task.get_tasks()
    
    # Getting [id] if not present
    if not id:
        print("Type the id of the task you want to modify:")
        print(f"[ TaskCLI / {action} ] >>> ", end ='')
        id = input()
    
    # Checkiing if id is a valid number
    try: int(id)
    except ValueError:
        if id in ('b', 'q', 'break', 'quit'):
            print(f"Terminating `{action}` module without modifying any task!")
            return
        else: 
            print("Invalid task ID. Please enter a number.")
    
    try: 
        Task.tasks[id]
        printv(f"id {id} {type(id)} found in database.")
    except Exception as e:
        printv(f"[Warning] {e}")
        print(f"Coudn't find id {id} {type(id)} in database.")
        print(f"Terminating {action} module without modifying any task!")
        return
    
    match action:
        case 'update':
            description = rest[0].strip(" \"'").title() if rest else None
            update(id, description)
        case 'mark':
            new_status =  rest[0].strip(" \"'").lower() if rest else None
            mark(id, new_status)
        case 'delete':
            delete(id)
    
    Task.export_to_file()


@logger
def update(id, description):
    """
    Module to update existing task descriptions
    
    ### Examples of usage:
    [ TaskCLI ] >>> update [id] [description]       : --> : change description of task [id] as specified
    OR
    [ TaskCLI ] >>> update
    [ TaskCLI / update ] >>> [id]
    [ TaskCLI / update / id[id] ] >>> [description] : --> : change description of task [id] as specified
    """
    t_to_update = Task.tasks[id]
    
    while not description:
        print(f'Type a new valid description for task {id}.')
        print(f'[ TaskCLI / update / id {id} ] >>> ', end='')
        description = input().strip(" \"'").title()
        if not description: continue
        if description in ('b', 'q', 'break', 'quit'):
            print("Terminating `update` module without updating any task!")
            return
    
    t_to_update['description'] = description.title()
    t_to_update['updatedAt'] = str(dt.now())


#%%
def delete(id):
    Task.tasks.pop(id)


#%%
def mark(id, new_status):
    """
    Module to mark tasks and change status.
    
    ### Examples of usage:
    [ TaskCLI ] >>> mark [id] done        : --> : change status of task [id] to 'done' 
    [ TaskCLI ] >>> mark [id] todo        : --> : change status of task [id] to 'todo'
    [ TaskCLI ] >>> mark [id] in-progress : --> : change status of task [id] to 'in-progress'
    OR
    [ TaskCLI ] >>> mark
    [ TaskCLI / mark ] >>> [id]
    [ TaskCLI / mark / id[id] ] >>>: [done, todo, in-progress] : --> : mark task [id] as specified
    """
    t_to_mark = Task.tasks[id]
    if new_status not in ('done', 'todo', 'in-progress'):
        printv(f"status {new_status} invalid!")
        new_status = None
    
    while not new_status:
        print(f'Type a new valid status for task {id}.')
        print(f'[ TaskCLI / mark / id {id} ] >>> ', end='')
        new_status = input().strip(" \"'").lower()
        if new_status in ('done', 'todo', 'in-progress'): break
        if new_status in ('b', 'q', 'break', 'quit'):
            print("Terminating `mark` module without updating any task!")
            return
        printv(f"status {new_status} invalid!")
    
    t_to_mark['status'] = new_status
    t_to_mark['updatedAt'] = str(dt.now())
    


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
    print(f"{'ID':<5} {'Description':<60} {'Status':<15} {'Created At':<20} {'Updated At':<20}")
    for task_id, task_data in Task.tasks.items():
        if condition(task_data):
            print(f"{task_id:<5} {task_data['description'][:60]:<60} {task_data['status']:<15}"
                  f"{task_data['createdAt'][:19]:<20} {task_data['updatedAt'][:19]:<20}")
            counter += 1
    printv(f"Found {counter} tasks with status == {status}")

#%% Test block to be called by: PS .> py -m package.functions 
if __name__ == "__main__":
    mode('verbose')
    
    print("\n"+"-"*50+'\nTesting add("...")')
    for i in range(5):
        n = Task._Task__max_id + 1
        n_str = 'st' if n%100 in (1, 11) else \
            'nd' if n%100 in (2, 12) else \
            'rd' if n%100 in (3, 13) else 'th'
        add(f"This is my {n}{n_str} Task")
    
    print(f"{'Showing tasks:'}")
    print(Task.tasks)
    
    print("\n"+"-"*50+'\nTesting Delete("...")')
    for i in range(n, n-4, -1):
        print(f'Trying to delete task {i}')
        action_manager('delete', f'{i}')
    
    print(f"{'Showing tasks:'}")
    print(Task.tasks)
    
    print("\n"+"-"*50+'\nTesting List()')
    list()
    
    print("\n"+"-"*50+'\nTesting update("...")')
    action_manager('update', '2 this is the second task [!!]')
    print(f"{'Showing tasks:'}")
    print(Task.tasks)
    print("\n"+"-"*50+'\nTesting List()')
    list()
    
    print("\n"+"-"*50+'\nTesting mark("...")')
    action_manager('mark', '2 done')
    print(f"{'Showing tasks:'}")
    print(Task.tasks)
    print("\n"+"-"*50+'\nTesting List("done")')
    list('done')
    
    print(f"\nmax_id: {Task._Task__max_id}")