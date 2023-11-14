import datetime
import csv

# Initialize an empty list to store expenses
expenses = []

# Function to record an expense
def record_expense(category, amount):
    date = datetime.date.today()
    expenses.append({"Date": date, "Category": category, "Amount": amount})

# Function to generate a monthly report
def generate_monthly_report(year, month):
    monthly_total = 0
    for expense in expenses:
        if expense["Date"].year == year and expense["Date"].month == month:
            print(f"Date: {expense['Date']}")
            print(f"Category: {expense['Category']}")
            print(f"Amount: ${expense['Amount']}")
            print()
            monthly_total += expense["Amount"]
    print(f"Monthly Total: ${monthly_total}")

# Function to save expenses to a CSV file
def save_expenses_to_csv(filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["Date", "Category", "Amount"])
        writer.writeheader()
        writer.writerows(expenses)

# Function to load expenses from a CSV file
def load_expenses_from_csv(filename):
    expenses.clear()
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["Amount"] = float(row["Amount"])
            expenses.append(row)

# Main loop for interacting with the expense tracker
while True:
    print("Expense Tracker Menu:")
    print("1. Record an Expense")
    print("2. Generate Monthly Report")
    print("3. Save Expenses to CSV")
    print("4. Load Expenses from CSV")
    print("5. Exit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == "1":
        category = input("Enter the expense category: ")
        amount = float(input("Enter the expense amount: $"))
        record_expense(category, amount)
        print("Expense recorded successfully.")
    elif choice == "2":
        year = int(input("Enter the year: "))
        month = int(input("Enter the month: "))
        generate_monthly_report(year, month)
    elif choice == "3":
        filename = input("Enter the CSV file name to save expenses: ")
        save_expenses_to_csv(filename)
        print("Expenses saved to CSV file.")
    elif choice == "4":
        filename = input("Enter the CSV file name to load expenses: ")
        load_expenses_from_csv(filename)
        print("Expenses loaded from CSV file.")
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please choose 1, 2, 3, 4, or 5.")

# Optional: Save expenses to a CSV file when exiting
save_expenses_to_csv("expenses.xlsx")

