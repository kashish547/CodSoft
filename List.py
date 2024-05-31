import tkinter as tk
from tkinter import messagebox

# Create the main application window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")
root.configure(bg="#2e2e2e")  # Set background color

# Create a list to store tasks
tasks = []

# Function to update the task list display
def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)
      
# Function to add a new task
def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        update_task_list()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

# Function to delete a selected task
def delete_task():
    try:
        task_index = task_listbox.curselection()[0]
        tasks.pop(task_index)
        update_task_list()
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to delete.")

# Create widgets
task_entry = tk.Entry(root, width=35, font=("Arial", 14), bg="#f0f0f0", fg="#000000")
add_button = tk.Button(root, text="Add Task", command=add_task, bg="#6a5acd", fg="#ffffff", font=("Arial", 12, "bold"))
delete_button = tk.Button(root, text="Delete Task", command=delete_task, bg="#ff4500", fg="#ffffff", font=("Arial", 12, "bold"))
task_listbox = tk.Listbox(root, height=15, width=35, font=("Arial", 12), bg="#ffffff", fg="#000000", selectbackground="#add8e6")

# Layout the widgets
task_entry.pack(pady=10)
add_button.pack(pady=5)
delete_button.pack(pady=5)
task_listbox.pack(pady=10)

# Run the main application loop
root.mainloop()
