import csv
from pathlib import Path

FILE = Path(__file__).with_name("expenses.csv")


def read_expenses():
    if not FILE.exists():
        return []
    with FILE.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def save_expenses(rows):
    with FILE.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "category", "amount"])
        writer.writeheader()
        writer.writerows(rows)


def add_expense(category, amount):
    rows = read_expenses()
    new_id = max((int(row["id"]) for row in rows), default=0) + 1
    rows.append({"id": new_id, "category": category, "amount": amount})
    save_expenses(rows)
    print("Expense added.")


def show_expenses():
    rows = read_expenses()
    if not rows:
        print("No expenses yet.")
    for row in rows:
        print(f"{row['id']}. {row['category']} - INR {float(row['amount']):.2f}")


# STUDENT 1: Complete these two functions on feature-member1.
def delete_expense(expense_id):
    rows = read_expenses()
    remaining = [row for row in rows if row["id"] != expense_id]
    if len(remaining) == len(rows):
        print("Expense ID not found.")
    else:
        save_expenses(remaining)
        print("Expense deleted.")


def filter_expenses(category):
    print("Not implemented yet: Student 1 will add filtering.")
