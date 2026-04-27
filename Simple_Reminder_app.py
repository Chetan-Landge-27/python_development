
import time
import datetime
import tkinter as tk
from tkinter import messagebox
import threading

reminders = []

def add_reminder(reminder_time, message):
    reminders.append({"time": reminder_time, "message": message, "done": False})
    print(f" Reminder set for {reminder_time}: {message}")

def view_reminders():
    if not reminders:
        print("\n No reminders yet.\n")
        return
    print("\n Current Reminders:")
    for r in reminders:
        print(f"- {r['time']} → {r['message']}")
    print()

def show_popup(message):
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo(" Reminder Alert", message)
    root.destroy()

def check_reminders():
    while True:
        now = datetime.datetime.now().strftime("%H:%M")

        for r in reminders:
            if r["time"] <= now and not r["done"]:
                print(f"\n Reminder: {r['message']}\n")
                show_popup(r['message'])
                r["done"] = True

        time.sleep(10)  

def run_reminder_app():
    print("🎓 Simple Reminder Application")
    print("Type 'add' to add a reminder, 'view' to see reminders, 'exit' to quit.\n")

    
    threading.Thread(target=check_reminders, daemon=True).start()

    while True:
        command = input("Enter command: ").strip().lower()

        if command == "add":
            reminder_time = input("Enter time (HH:MM): ").strip()
            message = input("Enter reminder message: ").strip()
            add_reminder(reminder_time, message)

        elif command == "view":
            view_reminders()

        elif command == "exit":
            print(" Exiting Reminder App.")
            break

        else:
            print(" Unknown command. Try again.")

if __name__ == "__main__":
    run_reminder_app()
