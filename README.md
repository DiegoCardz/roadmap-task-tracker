
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

> - `id:` A unique identifier for the task
> - `description:` A short description of the task
> - `status:` The status of the task (todo, in-progress, done)
> - `createdAt:` The date and time when the task was created
> - `updatedAt:` The date and time when the task was last updated

These properties are stored in a JSON file in the the same directory as the `.py` file.

## 📦 Example Usage

```sh
# Add a new task
python task_cli.py add "Buy groceries"

# Update a task
python task_cli.py update 1 "Buy groceries and cook dinner"

# Delete a task
python task_cli.py delete 1

# Mark task as in progress
python task_cli.py mark-in-progress 2

# Mark task as done
python task_cli.py mark-done 2

# List all tasks
python task_cli.py list

# List tasks by status
python task_cli.py list done
python task_cli.py list todo
python task_cli.py list in-progress

```
