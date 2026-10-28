import tkinter as tk
from tkinter import messagebox
import json
import os

FILE = "tasks.json"

def load_tasks():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks():
    with open(FILE, "w") as f:
        json.dump(tasks, f)

def refresh():
    listbox.delete(0, tk.END)
    for t in tasks:
        listbox.insert(tk.END, t)

def add_task():
    task = entry.get().strip()
    if not task:
        messagebox.showwarning("Warning", "Task empty ah irukku!")
        return
    tasks.append(task)
    save_tasks()
    refresh()
    entry.delete(0, tk.END)

def delete_task():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Warning", "Delete panna oru task select pannunga")
        return
    tasks.pop(selected[0])
    save_tasks()
    refresh()

# ---------- UI ----------
root = tk.Tk()
root.title("My To-Do App")
root.geometry("350x420")

tasks = load_tasks()

entry = tk.Entry(root, font=("Arial", 13))
entry.pack(pady=10, padx=10, fill="x")

tk.Button(root, text="Add Task", command=add_task).pack(pady=3)
tk.Button(root, text="Delete Selected", command=delete_task).pack(pady=3)

listbox = tk.Listbox(root, font=("Arial", 12), height=15)
listbox.pack(padx=10, pady=10, fill="both", expand=True)

refresh()
root.mainloop()