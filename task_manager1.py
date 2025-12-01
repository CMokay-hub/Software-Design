class Task:
    """A class representing a Task with the
    following attributes:
    - task_id: Unique identifier for the task
    - task_title: Title of the task
    - task_description: Description of the task
    """
    def __init__(self, task_id, task_title, task_description):
        self.task_id = task_id
        self.task_title = task_title
        self.task_description = task_description


# Sample objects of Task class
tasks_data = [
    Task(1, "CRUD Matrix", "Create a CRUD matrix for the project."),
    Task(
        2,
        "UML Diagrams",
        "Design UML diagrams for the system architecture.",
    ),
    Task(3, "Class Diagram", "Develop a class diagram for task management.")
]


def display_tasks():
    """Function to display all tasks with their details."""
    print("\n-----Task List-------:\n")
    for task in tasks_data:
        print(
            f"Task ID: {task.task_id}, Title: {task.task_title}, "
            f"Description: {task.task_description}"
        )
    print()


def create_task(new_id, title, description):
    """Function to create a new task and add it to the tasks_data list."""
    new_id = len(tasks_data) + 1
    title = "New Task"
    description = "Description of the new task."
    new_task = Task(new_id, title, description)
    tasks_data.append(new_task)

    print(f"\nTask {new_id} created successfully!\n")
    return


def read_task(task_id):
    """Function to read and display a task based on the task_id."""
    for task in tasks_data:
        if task.task_id == task_id:
            print(
                f"\nTask found - ID: {task.task_id}, Title: "
                f"{task.task_title}, Description: {task.task_description}\n"
            )


def update_task(task_id, new_title, new_description):
    """Function to update an existing task's title and description."""
    for task in tasks_data:
        if task.task_id == task_id:
            task.task_title = new_title
            task.task_description = new_description
            print(f"\nTask {task_id} updated successfully!\n")
            return
    print(f"\nTask with ID {task_id} not found.\n")


def delete_task(task_id):
    """Function to delete a task based on its task ID."""
    for i, task in enumerate(tasks_data):
        if task.task_id == task_id:
            del tasks_data[i]
            print(f"\nTask {task_id} deleted successfully!\n")
            return
    print(f"\nTask with ID {task_id} not found.\n")


# Demonstrate CRUD operations
display_tasks()
create_task(4, "Software Design", "Create software design documents.")
display_tasks()
read_task(2)
update_task(
    3,
    "Updated Class Diagram",
    "Revise the class diagram for accuracy.",
)
display_tasks()
delete_task(1)
display_tasks()
