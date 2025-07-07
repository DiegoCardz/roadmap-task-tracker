#%% 
from package.functions \
    import printv, help, add, list, mode, action_manager

#%%
def prompt():
    while True:
        try: 
            cli_in = input("[ TaskCLI ] >>> ").split(maxsplit=1)
            action, *specs = cli_in
            action = action.lower()
        except Exception as e: 
            printv(f"ERROR: {e}.")
            action = '_' 
            specs = None
        
        printv(f"action: {action}")
        if specs: printv(f"specs: {specs}")
        
        match action:
            case 'q' | 'quit':
                print("Good bye!") 
                break
            case 'h' | 'help': help(*specs)
            case 'a' | 'add': add(*specs)
            case 'u' | 'update' | 'up': action_manager('update', *specs)
            case 'd' | 'delete' | 'del': action_manager('delete', *specs)
            case 'm' | 'mark': action_manager('mark', *specs)
            case 'l' | 'list': list(*specs)
            case 'mode': mode(*specs)
            case _: print("Invalid input.\n"
                          "Type 'help' for more information")


#%% Header 
def header():
    print(f"----------TaskCLI----------")
    print('TaskCLI 0.0 (by DiegoCardz | running on Python 3.13.5)\n'
          'Type "help" for more information.')

#%% Main()
header()
prompt()
