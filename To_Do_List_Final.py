import tkinter as tk
from tkinter import simpledialog, messagebox

class Class:
    def __init__(self, name):
        """
        Initialize new class for task.

        Parameters:
        self (Class): Class
        name (str): name of class
        """
        self.name = name
        self.tasks = []

    def add_task(self, task):
        """
        Adds a task.

        Parameters:
        self (Class): Class
        task (str): Task being added
        """
        self.tasks.append(task)

    def remove_task(self, task):
        """
        Removes a task.

        Parameters:
        self (Class): Class
        task (str): Task being removed
        """
        self.tasks.remove(task)

    def get_tasks(self):
        """
        Returns tasks.

        Parameters:
        self (Class): Class
        """
        return self.tasks

    def __str__(self):
        """
        Returns string of tasks.

        Parameters:
        self (Class): Class

        Returns:
        str: name
        """
        return self.name

#Store class in list
classes = []

def add_class():
    """
    Add new class
    """
    class_name = simpledialog.askstring("Add Class", "Enter the class name:")
    if class_name:
        class_exists = False
        for c in classes:
            if c.name == class_name:
                class_exists = True
                break
        if not class_exists:
            new_class = Class(class_name)
            classes.append(new_class)
            class_listbox.insert(tk.END, new_class)

def remove_class():
    """
    Remove class
    """
    selected_class_index = class_listbox.curselection()
    if selected_class_index:
        index = selected_class_index[0]
        removed_class = classes.pop(index)
        class_listbox.delete(index)
        update_tasks()
        messagebox.showinfo("Class Removed", f"Class removed: {removed_class}")

def add_task():
    """
    Add task to class
    """
    if selected_class is None:
        messagebox.showwarning("Select Class", "Please select a class first.")
        return

    task = simpledialog.askstring("Add Task", "Enter the task:")
    if task:
        selected_class.add_task(task)
        update_tasks()

def remove_task():
    """
    Remove task from class
    """
    if selected_class is None:
        messagebox.showwarning("Select Class", "Please select a class first.")
        return

    selected_task_index = listbox.curselection()
    if selected_task_index:
        index = selected_task_index[0]
        removed_task = selected_class.get_tasks().pop(index)
        update_tasks()
        messagebox.showinfo("Task Removed", f"Task removed: {removed_task}")

def update_tasks():
    """
    Update current task list
    """
    listbox.delete(0, tk.END)
    if selected_class:
        for task in selected_class.get_tasks():
            listbox.insert(tk.END, task)

def update_class(event):
    """
    Update current class
    """
    selected_index = class_listbox.curselection()
    if selected_index:
        index = selected_index[0]
        global selected_class
        selected_class = classes[index]
        update_tasks()

# Start tkinter window
root = tk.Tk()
root.title("To-Do List")

# Set window size
width = 400
height = 600
root.geometry(f"{width}x{height}")

# Set frame
class_frame = tk.Frame(root)
class_frame.pack(side=tk.LEFT, fill=tk.Y)

# Add class button
add_class_button = tk.Button(class_frame, text="Add Class", command=add_class)
add_class_button.pack()

# Remove class button
remove_class_button = tk.Button(class_frame, text="Remove Class", command=remove_class)
remove_class_button.pack()

# Display list of classes
class_listbox = tk.Listbox(class_frame)
class_listbox.pack(fill=tk.BOTH, expand=True)
class_listbox.bind("<<ListboxSelect>>", update_class)

# Task frame
task_frame = tk.Frame(root)
task_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Add task button
add_task_button = tk.Button(task_frame, text="Add Task", command=add_task)
add_task_button.pack()

# Remove task button
remove_task_button = tk.Button(task_frame, text="Remove Task", command=remove_task)
remove_task_button.pack()

# Display list of tasks
listbox = tk.Listbox(task_frame)
listbox.pack(fill=tk.BOTH, expand=True)

# Initliatize variable for current class
selected_class = None

# Start
root.mainloop()
