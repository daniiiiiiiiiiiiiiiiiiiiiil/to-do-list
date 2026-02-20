import tkinter as tk
from tkinter import messagebox

class GUI:
    def init(self, root, add_func, delete_func, update_func):
        self.root = root
        self.root.title("Менеджер задач")

        # Поле ввода
        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=10)

        # Кнопка добавить
        self.add_button = tk.Button(root, text="Добавить задачу", command=add_func)
        self.add_button.pack()

        # Список задач
        self.task_list = tk.Listbox(root, height=10, width=50)
        self.task_list.pack(pady=10)

        # Кнопка удалить
        self.delete_button = tk.Button(root, text="Удалить задачу", command=delete_func)
        self.delete_button.pack()

        self.update_list = update_func  # Для обновления списка