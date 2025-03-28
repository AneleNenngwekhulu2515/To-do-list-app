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