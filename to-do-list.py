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