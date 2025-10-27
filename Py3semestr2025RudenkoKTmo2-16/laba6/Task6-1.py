import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("Менеджер задач")
root.geometry("700x400")

columns = ("Название", "Приоритет", "Статус")
tree = ttk.Treeview(root, columns=columns, show="headings", selectmode="browse")
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=200, anchor="center")
tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

priorities = ["Низкий", "Средний", "Высокий"]
statuses = ["Выполнена", "В процессе", "Отменена"]


def add_task_window():
    add_win = tk.Toplevel(root)
    add_win.title("Добавить задачу")
    add_win.geometry("300x200")
    add_win.grab_set()  # блокировка основного окна

    tk.Label(add_win, text="Название:").pack(pady=5)
    entry_name = tk.Entry(add_win, width=25)
    entry_name.pack()
    entry_name.focus()

    tk.Label(add_win, text="Приоритет:").pack(pady=5)
    combo_priority = ttk.Combobox(add_win, values=priorities, state="readonly")
    combo_priority.current(0)
    combo_priority.pack()

    tk.Label(add_win, text="Статус:").pack(pady=5)
    combo_status = ttk.Combobox(add_win, values=statuses, state="readonly")
    combo_status.current(1)
    combo_status.pack()

    def save_task():
        name = entry_name.get().strip()
        priority = combo_priority.get()
        status = combo_status.get()
        if not name:
            messagebox.showwarning("Ошибка", "Название задачи не может быть пустым!")
            return
        tree.insert("", tk.END, values=(name, priority, status))
        add_win.destroy()

    tk.Button(add_win, text="Добавить задачу", command=save_task).pack(pady=10)


def edit_task_window():
    selected = tree.selection()
    if not selected:
        messagebox.showinfo("Информация", "Выберите задачу для редактирования")
        return

    item = tree.item(selected)
    values = item["values"]

    edit_win = tk.Toplevel(root)
    edit_win.title("Редактировать задачу")
    edit_win.geometry("300x200")
    edit_win.grab_set()

    tk.Label(edit_win, text="Название:").pack(pady=5)
    entry_name = tk.Entry(edit_win, width=25)
    entry_name.insert(0, values[0])
    entry_name.pack()
    entry_name.focus()

    tk.Label(edit_win, text="Приоритет:").pack(pady=5)
    combo_priority = ttk.Combobox(edit_win, values=priorities, state="readonly")
    combo_priority.set(values[1])
    combo_priority.pack()

    tk.Label(edit_win, text="Статус:").pack(pady=5)
    combo_status = ttk.Combobox(edit_win, values=statuses, state="readonly")
    combo_status.set(values[2])
    combo_status.pack()

    def save_changes():
        name = entry_name.get().strip()
        priority = combo_priority.get()
        status = combo_status.get()
        if not name:
            messagebox.showwarning("Ошибка", "Название задачи не может быть пустым!")
            return
        tree.item(selected, values=(name, priority, status))
        edit_win.destroy()

    tk.Button(edit_win, text="Сохранить изменения", command=save_changes).pack(pady=10)


btn_add_main = tk.Button(root, text="Добавить новую задачу", command=add_task_window)
btn_add_main.pack(side=tk.LEFT, padx=10, pady=5)

btn_edit_main = tk.Button(root, text="Редактировать выбранную задачу", command=edit_task_window)
btn_edit_main.pack(side=tk.LEFT, padx=10, pady=5)

root.mainloop()
