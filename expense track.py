import csv
from datetime import datetime

def load_expenses():
    try:
        with open('expenses.csv', 'r') as file:
            reader = csv.reader(file)
            return list(reader)
    except FileNotFoundError:
        return []

def save_expenses(expenses):
    with open('expenses.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(expenses)

def add_expense(expenses, category, amount, description):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    expenses.append([timestamp, category, amount, description])
    save_expenses(expenses)
    print("Expense added successfully!")

def view_expenses(expenses):
    if not expenses:
        print("No expenses found.")
    else:
        print("{:<20} {:<15} {:<10} {:<20}".format("Timestamp", "Category", "Amount", "Description"))
        for expense in expenses:
            print("{:<20} {:<15} {:<10} {:<20}".format(expense[0], expense[1], expense[2], expense[3]))

def main():
    expenses = load_expenses()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            category = input("Enter the category: ")
            amount = float(input("Enter the amount: "))
            description = input("Enter the description: ")
            add_expense(expenses, category, amount, description)

        elif choice == '2':
            view_expenses(expenses)

        elif choice == '3':
            print("Exiting Expense Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
