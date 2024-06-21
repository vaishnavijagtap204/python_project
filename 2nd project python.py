import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.tasks = []

        # Create UI elements
        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_task_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_task_button.grid(row=0, column=1, padx=10, pady=10)

        self.tasks_listbox = tk.Listbox(root, width=50, height=10, selectmode=tk.SINGLE)
        self.tasks_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.complete_task_button = tk.Button(root, text="Complete Task", command=self.complete_task)
        self.complete_task_button.grid(row=2, column=0, padx=10, pady=10)

        self.delete_task_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_task_button.grid(row=2, column=1, padx=10, pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({'task': task, 'completed': False})
            self.task_entry.delete(0, tk.END)
            self.update_tasks_listbox()
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def update_tasks_listbox(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "Done" if task['completed'] else "Pending"
            self.tasks_listbox.insert(tk.END, f"{task['task']} [{status}]")

    def complete_task(self):
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            self.tasks[index]['completed'] = True
            self.update_tasks_listbox()
        else:
            messagebox.showwarning("Warning", "You must select a task to complete.")

    def delete_task(self):
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            self.tasks.pop(index)
            self.update_tasks_listbox()
        else:
            messagebox.showwarning("Warning", "You must select a task to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()
