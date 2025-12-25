import tkinter as tk
from tkinter import messagebox
from classes import Task, TaskManager


class TaskManagerApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Менеджер задач")
        self.manager = TaskManager()
        self.setup_ui()
        self.update_listbox()

    def setup_ui(self):
        tk.Label(self.root, text="Название").grid(row=0, column=0, padx=6, pady=6, sticky="w")
        self.title_entry = tk.Entry(self.root, width=40)
        self.title_entry.grid(row=0, column=1, padx=6, pady=6)

        tk.Label(self.root, text="Описание").grid(row=1, column=0, padx=6, pady=6, sticky="nw")
        self.desc_text = tk.Text(self.root, width=40, height=6)
        self.desc_text.grid(row=1, column=1, padx=6, pady=6)

        tk.Label(self.root, text="Срок (YYYY-MM-DD)").grid(row=2, column=0, padx=6, pady=6, sticky="w")
        self.date_entry = tk.Entry(self.root, width=40)
        self.date_entry.grid(row=2, column=1, padx=6, pady=6)

        tk.Button(self.root, text="Добавить", command=self.add_task).grid(row=3, column=0, padx=6, pady=6, sticky="ew")
        tk.Button(self.root, text="Удалить", command=self.delete_task).grid(row=3, column=1, padx=6, pady=6, sticky="ew")

        self.tasks_listbox = tk.Listbox(self.root, width=60, height=10)
        self.tasks_listbox.grid(row=4, column=0, columnspan=2, padx=6, pady=6)

    def add_task(self):
        title = self.title_entry.get().strip()
        description = self.desc_text.get("1.0", tk.END).strip()
        due_date = self.date_entry.get().strip()

        if not title or not description or not due_date:
            messagebox.showwarning("Ошибка", "Заполните все поля")
            return

        task = Task(title, description, due_date)
        self.manager.add_task(task)
        self.update_listbox()
        self.clear_inputs()

    def delete_task(self):
        selected = self.tasks_listbox.curselection()
        if not selected:
            return
        self.manager.delete_task(selected[0])
        self.update_listbox()

    def update_listbox(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.manager.tasks:
            self.tasks_listbox.insert(tk.END, f"{task.title} (до {task.due_date})")

    def clear_inputs(self):
        self.title_entry.delete(0, tk.END)
        self.desc_text.delete("1.0", tk.END)
        self.date_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
