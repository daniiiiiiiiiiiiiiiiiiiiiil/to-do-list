import tkinter as tk
import json
from gui import GUI
from logic import add_task, delete_task, update_list

def main():
    root = tk.Tk()
    tasks = []

    try:
        with open('tasks.json', 'r') as f:
            tasks = json.load(f)
    except FileNotFoundError:
        pass

    def add():
        add_task(gui.entry, tasks, lambda: update_list(gui.task_list, tasks))

    def delete():
        delete_task(gui.task_list, tasks, lambda: update_list(gui.task_list, tasks))

    def update():
        update_list(gui.task_list, tasks)

    gui = GUI(root, add, delete, update)
    update()
    def save_and_close():
        with open('tasks.json', 'w') as f:
            json.dump(tasks, f)
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", save_and_close)
    root.mainloop()

if name == "main":
    main()