
# 📝 Task Tracker CLI

https://roadmap.sh/projects/task-tracker

> A simple command-line tool to track and manage your tasks.  
> Easily add, update, delete, and list your tasks — all from your terminal.

Task tracker is a project used to track and manage your tasks. In this task, you will build a simple command line interface (CLI) to track what you need to do, what you have done, and what you are currently working on. This project will help you practice your programming skills, including working with the filesystem, handling user inputs, and building a simple CLI application.

## 🚀 Features

The application should run from the command line, accept user actions and inputs as arguments, and store the tasks in a JSON file. The user should be able to:

- Add new tasks with descriptions
- Update existing task descriptions
- Delete tasks
- Mark tasks as:
  - ✅ Done
  - 🔄 In Progress
- List tasks by:
  - All
  - Status (done, todo, in-progress)
- Task data is stored persistently in a local `tasks.json` file

## 🩻 Task Properties

Each task should have the following properties:

- `id:` A unique identifier for the task  
- `description:` A short description of the task  
- `status:` The status of the task (todo, in-progress, done)  
- `createdAt:` The date and time when the task was created  
- `updatedAt:` The date and time when the task was last updated  

These properties are stored in a JSON file in the the same directory as the `.py` file.


## 📦 Example Usage

### Interactive Mode
The application runs in interactive mode where you can enter commands:

```bash
# Start the application
python task_cli.py

# Once started, you can use these commands:
[ TaskCLI ] >>> add "Buy groceries"
OR
[ TaskCLI ] >>> add Buy groceries and cook dinner

# Update a task (you'll be prompted for ID if not provided)
[ TaskCLI ] >>> update 1 "Buy groceries and cook dinner"
OR
[ TaskCLI ] >>> update
[ TaskCLI / update ] >>> 1
[ TaskCLI / update / id 1 ] >>> Buy groceries and cook dinner

# Delete a task
[ TaskCLI ] >>> delete 1
[ TaskCLI ] >>> del 1

# Mark task status
[ TaskCLI ] >>> mark 1 done
[ TaskCLI ] >>> mark 2 in-progress
[ TaskCLI ] >>> m 3 todo

# List all tasks
[ TaskCLI ] >>> list
[ TaskCLI ] >>> l

# List tasks by status
[ TaskCLI ] >>> list done
[ TaskCLI ] >>> list todo
[ TaskCLI ] >>> list in-progress

# Get help
[ TaskCLI ] >>> help
[ TaskCLI ] >>> h

# Exit the application
[ TaskCLI ] >>> quit
[ TaskCLI ] >>> q
```
##### Command Aliases
The CLI supports short aliases for convenience:
- `a` or `add` - Add new task
- `u`, `update`, or `up` - Update existing task
- `d`, `delete`, or `del` - Delete task
- `m` or `mark` - Change task status
- `l` or `list` - List tasks
- `h` or `help` - Show help
- `q` or `quit` - Exit application

##### Verbose Mode
The CLI also has a verbose mode that show more information on command executions
```bash
# Change mode (verbose/normal)
[ TaskCLI ] >>> mode
```
