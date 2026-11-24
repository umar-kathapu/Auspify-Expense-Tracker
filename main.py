from expense_tracker import ExpenseTracker

tracker = ExpenseTracker()

INCOME_CATEGORIES = [
    "Salary",
    "Freelance",
    "Business",
    "Investment",
    "Gift",
    "Other"
]

EXPENSE_CATEGORIES = [
    "Food",
    "Travel",
    "Shopping",
    "Bills",
    "Education",
    "Health",
    "Entertainment",
    "Other"
]


def select_category(categories):
    print("\nAvailable Categories:")

    for index, category in enumerate(categories, start=1):
        print(f"{index}. {category}")

    while True:
        try:
            choice = int(input("Select category number: "))

            if 1 <= choice <= len(categories):
                return categories[choice - 1]

            print("Invalid category number.")

        except ValueError:
            print("Please enter a valid number.")


def main():
    while True:
        print("\n" + "=" * 40)
        print("       EXPENSE TRACKER SYSTEM")
        print("=" * 40)
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Transactions")
        print("4. Delete Transaction")
        print("5. Balance Summary")
        print("6. Monthly Report")
        print("7. Exit")
        print("=" * 40)

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            add_income()

        elif choice == "2":
            add_expense()

        elif choice == "3":
            view_transactions()

        elif choice == "4":
            delete_transaction()

        elif choice == "5":
            balance_summary()

        elif choice == "6":
            monthly_report()

        elif choice == "7":
            print("\nThank you for using Expense Tracker!")
            break

        else:
            print("\nInvalid choice! Please select between 1 and 7.")

def add_income():
    print("\n--- Add Income ---")

    try:
        amount = float(input("Enter income amount: ₹"))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        category = select_category(INCOME_CATEGORIES)
        description = input("Enter description: ").strip()

        tracker.add_transaction("income", amount, category, description)
        print("\nIncome added successfully!")

    except ValueError:
        print("\nInvalid amount! Please enter a numeric value.")

def add_expense():
    print("\n--- Add Expense ---")

    try:
        amount = float(input("Enter expense amount: ₹"))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        category = select_category(EXPENSE_CATEGORIES)
        description = input("Enter description: ").strip()

        tracker.add_transaction("expense", amount, category, description)
        print("\nExpense added successfully!")

    except ValueError:
        print("\nInvalid amount! Please enter a numeric value.")

def view_transactions():
    transactions = tracker.get_transactions()

    print("\n--- All Transactions ---")

    if not transactions:
        print("No transactions found.")
        return

    for transaction in transactions:
        print("-" * 40)
        print(f"ID          : {transaction['id']}")
        print(f"Type        : {transaction['type'].title()}")
        print(f"Amount      : ₹{transaction['amount']:.2f}")
        print(f"Category    : {transaction['category']}")
        print(f"Description : {transaction['description']}")
        print(f"Date        : {transaction['date']}")


def delete_transaction():
    print("\n--- Delete Transaction ---")

    try:
        transaction_id = int(input("Enter transaction ID to delete: "))
        success = tracker.delete_transaction(transaction_id)

        if success:
            print("Transaction deleted successfully!")
        else:
            print("Transaction ID not found.")

    except ValueError:
        print("Please enter a valid numeric ID.")


def balance_summary():
    summary = tracker.get_summary()

    print("\n" + "=" * 40)
    print("          BALANCE SUMMARY")
    print("=" * 40)
    print(f"Total Income   : ₹{summary['income']:.2f}")
    print(f"Total Expenses : ₹{summary['expenses']:.2f}")
    print("-" * 40)
    print(f"Current Balance: ₹{summary['balance']:.2f}")
    print("=" * 40)

def monthly_report():
    print("\n--- Monthly Report ---")

    try:
        year = int(input("Enter year (e.g., 2026): "))
        month = int(input("Enter month (1-12): "))

        if month < 1 or month > 12:
            print("Invalid month! Enter between 1 and 12.")
            return

        report = tracker.get_monthly_report(year, month)

        print("\n" + "=" * 40)
        print(f"       REPORT: {month:02d}/{year}")
        print("=" * 40)
        print(f"Total Income       : ₹{report['income']:.2f}")
        print(f"Total Expenses     : ₹{report['expenses']:.2f}")
        print(f"Net Savings       : ₹{report['savings']:.2f}")
        print(f"Transactions      : {report['transaction_count']}")
        print("=" * 40)

    except ValueError:
        print("Please enter valid numeric values.")


if __name__ == "__main__":
    main()