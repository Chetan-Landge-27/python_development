import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x500")
root.config(bg="#f0f4f7")  

tasks = []


def add_task(event=None):
    task = task_entry.get()
    if task != "":
        tasks.append(task)
        update_listbox()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def remove_task(event=None):  
    try:
        selected_task_index = task_listbox.curselection()[0]
        tasks.pop(selected_task_index)
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove!")

def update_listbox():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)


title_label = tk.Label(root, text="My To-Do List", font=("Helvetica", 16, "bold"), bg="#f0f4f7", fg="#333")
title_label.pack(pady=10)

task_entry = tk.Entry(root, width=30, font=("Helvetica", 12), bg="#e8eef1", fg="#333")
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task, width=15, bg="#a8dadc", fg="#1d3557")
add_button.pack(pady=5)

remove_button = tk.Button(root, text="Remove Task", command=remove_task, width=15, bg="#f4a261", fg="#fff")
remove_button.pack(pady=5)

task_listbox = tk.Listbox(root, width=40, height=15, font=("Helvetica", 12), bg="#ffffff", fg="#333", selectbackground="#a8dadc")
task_listbox.pack(pady=10)

root.bind('<Return>', add_task)
root.bind('<Delete>', remove_task)  

root.mainloop()