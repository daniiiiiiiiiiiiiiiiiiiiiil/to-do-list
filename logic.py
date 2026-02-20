from tkinter import messagebox

def add_task(entry, tasks, update_list):
    task = entry.get()
    if task:
        tasks.append(task)
        update_list()
        entry.delete(0, 'end')
    else:
        messagebox.showwarning("Предупреждение", "Введите задачу!")

def delete_task(task_list, tasks, update_list):
    try:
        selected = task_list.curselection()[0]
        del tasks[selected]
        update_list()
    except IndexError:
        messagebox.showwarning("Предупреждение", "Выберите задачу!")

def update_list(task_list, tasks):
    task_list.delete(0, 'end')
    for task in tasks:
        task_list.insert('end', task)