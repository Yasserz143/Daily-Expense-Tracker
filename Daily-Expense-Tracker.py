def exit_program(expenses):
    print("Exiting the Daily Expense Tracker. Goodbye!")
    exit()

def add_expense(expenses):
    amount = float(input("Enter the expense amount: "))
    expenses.append(amount)
    print("Expense added successfully!")

def view_expenses(expenses):
    if len(expenses) == 0:
        print("No expenses recorded yet.")
        return
    print("Your expenses:")
    for index, expense in enumerate(expenses):
        print(f"{index + 1}. {expense}")

def calculate_total_and_average(expenses):
    if len(expenses) == 0:
        print("No expenses recorded yet.")
        return
    total_expense = sum(expenses)
    average_expense = total_expense / len(expenses)
    print(f"Total expense: {total_expense}")
    print(f"Average expense: {average_expense}")

def clear_expenses(expenses):
    expenses.clear()
    print("All expenses cleared.")


program_options = {
    1: add_expense,
    2: view_expenses,
    3: calculate_total_and_average,
    4: clear_expenses,
    5: exit_program
}
program_option_descriptions = {
    1: "Add a new expense",
    2: "View all expenses",
    3: "Calculate total and average expense",
    4: "Clear all expenses",
    5: "Exit"
}


def show_options():
    print("\nPlease choose an option:")
    for key in program_options:
        print(f"{key}. {program_option_descriptions[key]}")


def program():
    expenses = []
    
    print("Welcome to the Daily Expense Tracker!")
    show_options()

    while True:
        choice = int(input("\nEnter your choice: "))
        if choice in program_options:
            program_options[choice](expenses)
        else:
            print("Invalid choice. Please try again.")
            show_options()


program()            