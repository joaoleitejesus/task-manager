# Task Manager

A command-line task manager built with Python. The application allows users to create, view, complete, and delete tasks, with task data persisted in a JSON file.

## Features

* Add new tasks
* View all tasks
* Mark tasks as completed
* Delete tasks
* Validate empty task descriptions
* Validate user input
* Persist tasks using JSON
* Automatically load saved tasks when the program starts

## Technologies

* Python 3
* JSON
* File handling

## How to Run

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/joaoleitejesus/task-manager.git
cd task-manager
```

Run the application:

```bash
python main.py
```

> The exact command may vary depending on where the main Python file is located in the project.

## Data Persistence

Tasks are stored in a `tasks.json` file. This allows tasks to remain saved even after the program is closed.

Example:

```json
[
    {
        "description": "Study Python",
        "completed": false
    },
    {
        "description": "Finish project",
        "completed": true
    }
]
```

## What I Learned

This project was developed to practice fundamental Python programming concepts, including:

* Functions
* Lists and dictionaries
* Loops and conditionals
* User input and validation
* Exception handling
* File handling
* JSON data persistence
* Basic CRUD operations
* Git and GitHub
