def expense_tracker():
    total = 0
    expenses = {}   

    while True:
        category = input("Enter category (Food, Travel, etc.) or 'done' to finish: ").strip().title()
        
        if category == "Done":
            break

        if category == "":
            print("Category cannot be empty.")
            continue

        try:
            amount = float(input("Enter amount: "))
            
            if amount <= 0:
                print("Amount must be positive.")
                continue

            if category in expenses:
                expenses[category] += amount
            else:
                expenses[category] = amount

            total += amount
            print(f"Added: {category} - ₹{amount:.2f}")
        
        except ValueError:
            print("Invalid amount. Please enter a number.")

    if not expenses:
        print("\nNo expenses entered.")
        return

    print("\n--- Expense Summary ---")
    for i, (category, amount) in enumerate(expenses.items(), start=1):
        print(f"{i}. {category}: ₹{amount:.2f}")

    print(f"\nTotal Spent: ₹{total:.2f}")


if __name__ == "__main__":
    expense_tracker()


