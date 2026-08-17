expenses = []


def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: ₹"))
    category = input("Enter category: ")

    expense = {
        "name": name,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)
    print("Expense added successfully!\n")


def view_expenses():
    if not expenses:
        print("No expenses recorded yet.\n")
        return

    print("\n--- Your Expenses ---")

    for i, expense in enumerate(expenses, start=1):
        print(
            f"{i}. {expense['name']} | "
            f"₹{expense['amount']:.2f} | "
            f"{expense['category']}"
        )

    print()


def total_expenses():
    total = sum(expense["amount"] for expense in expenses)
    print(f"\nTotal Expenses: ₹{total:.2f}\n")


def main():
    while True:
        print("===== PERSONAL EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Total")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            print("Thank you for using Expense Tracker!")
            break
        else:
            print("Invalid choice. Please try again.\n")


main()