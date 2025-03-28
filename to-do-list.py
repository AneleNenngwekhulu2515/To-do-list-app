import tkinter as tk
from tkinter import messagebox
import os

tasks = []
FILE_NAME = "tasks.txt"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open (FILE_NAME, "r") as file:
            for line in file:
                tasks.append(line.strip())
                listbox.insert(tk.end, line.strip())

def add_tasks():
    task = entry.get()
    if task:
        tasks.append(task)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def delete_task():
    try:
        selected_task = listbox.curselection()[0]
        listbox.delete(selected_task)
        del tasks[selected_task]
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to delete!")

def save_tasks():
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")
    messagebox.showinfo("Saved", "Tasks saved successfully!")

# GUI Setup
root = tk.Tk()
root.title("To-Do List")
root.geometry("300x400")

frame = tk.Frame(root)
frame.pack(pady=10)

listbox = tk.Listbox(frame, width=40, height=10)
listbox.pack()

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

tk.Button(root, text="Add Task", command=add_tasks).pack(pady=2)
tk.Button(root, text="Delete Task", command=delete_task).pack(pady=2)
tk.Button(root, text="Save Tasks", command=save_tasks).pack(pady=2)

load_tasks()
root.mainloop()
