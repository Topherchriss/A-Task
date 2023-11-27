import tkinter as tk
from tkinter import messagebox
from datetime import datetime as dt

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


class ToDoListGUI:
    def __init__(self, master):
        self.todo_list = ToDoList() #create an istane of the ToDoList class
        self.master = master
        self.master.title("My To-Do-List App")

        #labels for task
        self.label_title = tk.Label(master, text="Task Title:")
        self.label_description = tk.Label(master, text="Task Description:")
        self.label_due_date = tk.Label(master, text="Task's Due Date:")
        self.label_priority = tk.Label(master, text="Task's priority:")

        #create widgates
        self.entry_title = tk.Entry(master)
        self.entry_description = tk.Entry(master)
        self.entry_due_date = tk.Entry(master)
        self.entry_priority = tk.Entry(master)


        #create Buttons
        self.button_add = tk.Button(master, text="Add Task", command=self.addTask)
        self.button_mark = tk.Button(master, text="Mark Task Complete", command=self.markTaskComplete)
        self.button_display = tk.Button(master, text="All Tasks", command=self.allTasks)


        #Arrange labels and widgets on the grid
        self.label_title.grid(row=0, column=0, sticky=tk.E)
        self.entry_title.grid(row=0, column=1)


        self.label_description.grid(row=1, column=0, sticky=tk.E)
        self.entry_description.grid(row=1, column=1)


        self.label_due_date.grid(row=2, column=0, sticky=tk.E)
        self.entry_due_date.grid(row=2, column=1)


        self.label_priority.grid(row=3, column=0, sticky=tk.E)
        self.entry_priority.grid(row=3, column=1)

        self.button_add.grid(row=4, column=0, columnspan=1)
        self.button_mark.grid(row=4, column=1, columnspan=1)
        self.button_display.grid(row=4, column=2, columnspan=1)

    def addTask(self):
        #retrive values from entry fields

        title = self.entry_title.get()
        description = self.entry_description.get()
        due_date_str = self.entry_due_date.get() #Used a diffrent variable name to store the input string
        priority = self.entry_priority.get()

        #Initialize a list containing valid priority choices
        valid_priority = ["high", "low", "medium"]


        #Validate input
        if not title or not description or not due_date_str or priority.lower() not in valid_priority:
            messagebox.showerror("Incomplete Information or Priority Choice", "Please fill in the title, description, due_date and a valid priority level (High, Medium or Low)!" )
            return

        #Validate due_date_input
        try:
            due_date = dt.strptime(due_date_str, "%d-%m-%Y").date()
        except ValueError:
            messagebox.showerror("Invalid Date Format", "Please enter a valid date in the format DD-MM-YYY")
            return

        #create new task
        new_task = Task(self.entry_title.get(), self.entry_description.get(), self.entry_due_date.get(), self.entry_priority.get())

        #Call the instance method from ToDoList
        self.todo_list.addNewTask(new_task)

        messagebox.showinfo("Task Added", f"Task added succesfully!")

        self.entry_title.delete(0, 'end')
        self.entry_description.delete(0, 'end')
        self.entry_due_date.delete(0, 'end')
        self.entry_priority.delete(0, 'end')



    def markTaskComplete(self):
        task_title = self.entry_title.get()

        #call the instance method from ToDoList
        res = self.todo_list.markComplete(task_title)

        #Validate Input
        if res or task_title != '':
            messagebox.showinfo("Task Completed", f"Task {task_title} marked as completed.")
        else:
            messagebox.showerror("Task Not Found", f"Task not found or empty task title")


    def allTasks(self):

        #used a list comprehension to create a string representation for each task using str(task)

        tasks_info = "\n".join(str(task) for task in self.todo_list.to_do_list)

        if not tasks_info:
            tasks_info = "Your to-do list is empty"

        messagebox.showinfo("All Task", tasks_info)

# Create the main window
root = tk.Tk()
app = ToDoListGUI(root)
root.mainloop()