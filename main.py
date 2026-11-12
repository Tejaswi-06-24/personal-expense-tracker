from expenses import add_expense, show_expenses, delete_expense, filter_expenses
from reports import total_expenses, export_expenses


def main():
    while True:
        print("\nPERSONAL EXPENSE TRACKER")
        print("1. Add expense")
        print("2. Show expenses")
        print("3. Delete expense")
        print("4. Filter by category")
        print("5. Show total spending")
        print("6. Export to CSV")
        print("0. Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            category = input("Category: ").strip()
            try:
                amount = float(input("Amount (INR): "))
                if not category or amount <= 0:
                    print("Enter a category and a positive amount.")
                else:
                    add_expense(category, amount)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "2":
            show_expenses()
        elif choice == "3":
            delete_expense(input("Expense ID: ").strip())
        elif choice == "4":
            filter_expenses(input("Category: ").strip())
        elif choice == "5":
            total_expenses()
        elif choice == "6":
            export_expenses()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
