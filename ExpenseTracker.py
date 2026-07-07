# Simple personal finance management tool:
# 1. Add an expense with details like date, category, description, and amount
# 2. View all recorded expenses in a clean format
# 3. Calculate total spending so far
# 4. Exit program gracefully when the user chooses to.

expenses = []   #list of dictionaries
print("\nWelcome to Expense Tracker")

while True:
    print("\n====MENU====")
    print("1. Add Expense")
    print("2. View all Expenses")
    print("3. View Total amount")
    print("4. Exit")

    choice = int(input("Please enter your choice: "))
    if(choice==1):
        # add expense
        date = input("Enter date of your expense (DD-MM-YYYY): ")
        category = input("Enter the category(Food, Travel, Shopping): ")
        description = input("Enter the description: ")
        amount = float(input("Enter the amount: "))
        expense={
            "Date":date,
            "Category":category,
            "Description":description,
            "Amount":amount
        }
        expenses.append(expense)
        print("Expenses Added Successfully!")
# expense=[{"Date":"01-01-2001","Category":"Food","Description":"Pizza","Amount":1000},{item},{item}]
    elif(choice==2):
        # view all expenses
        if(len(expenses)==0):
            print("No Expenses added. Please add your expenses.")
        else:
            print("All Your Expenses:")
            count = 1
            for item in expenses:
                print(f"{count}. Date: {item["Date"]}, Category: {item["Category"]}, Description: {item["Description"]}, Amount: {item["Amount"]}")   
                #print(count,item)
                count+=1 

    elif(choice==3):
        # add total amounts
        sum=0
        for item in expenses:
            sum += item["Amount"]
        print("The Total Spendings:",sum)
    elif(choice==4):
        break
    else:
        print("Please enter correct choice")

