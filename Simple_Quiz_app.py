import datetime

def expense_tracker():
    total = 0
    expenses = {}   
    history = []

    budget = input("Set a budget (or press Enter to skip): ").strip()
    budget = float(budget) if budget else None

    while True:
        category = input("\nEnter category (Food, Travel, etc.) or 'done' to finish: ").strip().title()
        
        if category == "Done":
            break

        if category == "":
            print("⚠ Category cannot be empty.")
            continue

        try:
            amount = float(input("Enter amount: "))
            
            if amount <= 0:
                print("⚠ Amount must be positive.")
                continue

            expenses[category] = expenses.get(category, 0) + amount
            total += amount
            history.append((category, amount, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

            print(f" Added: {category} - ₹{amount:.2f}")

            if budget and total > budget:
                print(f"⚠ Budget exceeded! Total = ₹{total:.2f}, Budget = ₹{budget:.2f}")
        
        except ValueError:
            print("⚠ Invalid amount. Please enter a number.")

    if not expenses:
        print("\nNo expenses entered.")
        return

    print("\n--- Expense Summary ---")
    for i, (category, amount) in enumerate(expenses.items(), start=1):
        percent = (amount / total) * 100
        print(f"{i}. {category}: ₹{amount:.2f} ({percent:.1f}%)")

    print(f"\ Total Spent: ₹{total:.2f}")


    max_cat = max(expenses, key=expenses.get)
    min_cat = min(expenses, key=expenses.get)
    print(f" Highest Expense: {max_cat} - ₹{expenses[max_cat]:.2f}")
    print(f"Lowest Expense: {min_cat} - ₹{expenses[min_cat]:.2f}")

    
    print("\n--- Expense History ---")
    for cat, amt, time in history:
        print(f"{time} → {cat}: ₹{amt:.2f}")

if __name__ == "__main__":
    expense_tracker()
