import time
import datetime

reminders = []

def add_reminder(reminder_time, message):
    reminders.append({"time": reminder_time, "message": message})
    print(f"✅ Reminder set for {reminder_time}: {message}")

def view_reminders():
    print("\n📋 Current Reminders:")
    for r in reminders:
        print(f"- {r['time']} → {r['message']}")
    print()

def run_reminder_app():
    print("🎓 Simple Reminder Application")
    print("Type 'add' to add a reminder, 'view' to see reminders, 'exit' to quit.\n")
    
    while True:
        command = input("Enter command: ").strip().lower()
        
        if command == "add":
            reminder_time = input("Enter time (HH:MM): ").strip()
            message = input("Enter reminder message: ").strip()
            add_reminder(reminder_time, message)
        
        elif command == "view":
            view_reminders()
        
        elif command == "exit":
            print("👋 Exiting Reminder App.")
            break
        
        else:
            print("⚠️ Unknown command. Try again.")
        
        # Check reminders every loop
        now = datetime.datetime.now().strftime("%H:%M")
        for r in reminders:
            if r["time"] == now:
                print(f"\n🔔 Reminder: {r['message']}\n")
        time.sleep(3)  # check every 3 seconds

if __name__ == "__main__":
    run_reminder_app()