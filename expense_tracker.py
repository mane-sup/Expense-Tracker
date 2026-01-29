import json
try:
    with open("expenses.json", "r") as file:
        expenses = json.load(file)
except FileNotFoundError:
    expenses=[]
while True:
    print("(1) Add an expense")
    print("(2) View all expenses")
    print("(3) Show total spent")
    print("(4) Exit")
    option_menu=int(input("Choose an action: "))

    if option_menu==1:
        amount=float(input("Enter expense amount: "))
        category=input("Enter expense category (food, transport, etc.): ")
        expense={"amount": amount,"category": category}
        expenses.append(expense)
        print("Expense added!\n")
        with open("expenses.json", "w") as file:
            json.dump(expenses, file)


    elif option_menu==2:
        if len(expenses)==0:
            print("No expenses tracked yet. ")
        else:
            for i, expense in enumerate(expenses, 1):
                print(f"{i}. category: {expense['category']} | amount: {expense['amount']:.2f}\n")

    elif option_menu==3:
        if len(expenses)==0:
            print("No expenses tracked yet. ")
        else:
            total=0
            for expense in expenses:
                expense['amount']
                total+=expense['amount']
            print(f"Total spent: ${total:.2f}")

    elif option_menu==4:
        break
