class Task:
    def __init__(self, title, description, due_date, priority="low", status=False):

        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.status = status

    def markingComplete(self):
        self.status = True

    def update_details(self, new_title=None, new_description=None, new_due_date=None, new_priority=None):

        if new_title:
            self.title = new_title
        if new_description:
            self.description = new_description
        if new_due_date:
            self.due_date = new_due_date
        if new_priority:
            self.priority = new_priority

        """update_details method takes optional arguments for the new title, new description, and new due date. If any of these arguments are provided, the corresponding attribute of the task is updated."""


    def __str__(self):
        status_str = "Completed" if self.status else "Incomplete"

        return f"Title: {self.title}\nDescription: {self.description}\nDue Date: {self.due_date}\nPriority: {self.priority}\nStatus: {status_str}"

        """This __str__ method returns a formatted string containing the title, description, due date, and status of the task."""


class ToDoList:
    def __init__(self):
        self.to_do_list = []

    #Method to add Tasks
    def addNewTask(self, new_task):
        valid_priorities = ["low", "medium", "high"]
        if new_task.priority.lower() not in valid_priorities:
                print((f"Invalid priority: {new_task.priority}. Priority must be 'low', 'medium', or 'high'. Task not added."))
        else:
            self.to_do_list.append(new_task)
            print(f"Task '{new_task.title}' added successfully.")

    #Method to mark a Task complete
    def markComplete(self, task_title):
        for task in self.to_do_list:

            if task.title == task_title:
                task.markingComplete()
                print(f"Task, {task_title}, marked as Completed.")
                return
        print(f"Task, {task_title}, not found in the To - Do List")

    #Method to display all Tasks
    def display_all_tasks(self):
        if not self.to_do_list:
            print("Your to-do list is empty!")
        for task in self.to_do_list:
            print(task)

