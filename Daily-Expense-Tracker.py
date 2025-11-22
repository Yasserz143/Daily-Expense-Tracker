def menu():
    print("Menu:")
    print("1. Add a new expense")
    print("2. View all expenses")
    print("3. Calculate total and average expense")
    print("4. Clear all expenses")
    print("5. Exit")



print("Welcome to the Daily Expense Tracker!\n")
menu()


def program():
    explst = []
    while True:
        choice = int(input())
        if choice == 5:
            print("Exiting the Daily Expense Tracker. Goodbye!")
            break
        elif choice == 1:
            nval1 = float(input())
            explst.append(nval1)
            print("Expense added successfully!")
        elif choice == 2:
            if len(explst) == 0:
                print("No expenses recorded yet.")
            else:
                print("Your expenses:")
                for index, expense in enumerate(explst):
                    print(f"{index + 1}. {expense}")
        elif choice == 3:
            if explst == []:
                print("No expenses recorded yet.")
            else:
                texp = 0
                for index, expense in enumerate(explst):
                    texp += expense
                    aexp = texp / len(explst)
                print(f"Total expense: {texp}")         
                print(f"Average expense: {aexp}")         
        elif choice == 4:
            explst = []
            print("All expenses cleared.")
        else:
            print("Invalid choice. Please try again.")    




        

            

program()            