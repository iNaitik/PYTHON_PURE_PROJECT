import datetime
from datetime import datetime, date
import csv
import os

file_name = 'Expenses.csv'
def initialize_file():
    if not os.path.exists(file_name):
        with open(file_name,'w',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date','Amount','Category','Description'])
def Add_Expense():
    while True:
        expense_date = input("Enter date (YYYY-MM-DD) or leave blank for today: ")
        if not expense_date:
            expense_date = date.today().strftime("%Y-%m-%d")
        else:
            try:
                # Validate the date format but keep it as string
                datetime.strptime(expense_date,'%Y-%m-%d')
            except ValueError:
                print("Invalid date format. Please try again.")
                continue
        while True:
            try:
                Amount = float(input("Enter amount: "))
                if Amount <= 0:
                    print("Amount must be positive. Please try again.")
                else:
                    break
            except ValueError:
                print("Invalid amount. Please enter a number.")
        Category = input("Enter category (e.g., Food, Transport, Utilities): ")
        if not Category:
            Category = "Miscellaneous"
        Discription = input("Enter Description (optional): ")

        initialize_file()
        # Append expense to CSV file automatically creating it if it doesn't exist
        with open(file_name,'a',newline='') as file:
            writer = csv.writer(file)
            writer.writerow([expense_date,Amount,Category,Discription])
        more = input("Add another expense? (y/n): ")
        if more.lower() == 'n':
            break
    
def View_Expenses():
    if not os.path.exists(file_name):
        print("No expenses recorded yet.")
        return
    choice = input("Do you Want to see Last N transaction Enter Number or for All Transaction Enter 'A': ")
    if choice.isdigit(): 
        n = int(choice)
        with open(file_name,'r') as file:
            Expense = []
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                Expense.append(row)

            last = Expense[-n:]   # slice AFTER list is filled
            j = 0

            for row in last:
                print(
                    f"Date: {row[j]} || Amount: {row[j+1]} || "
                    f"Category: {row[j+2]} || Description: {row[j+3]}"
                )

    elif choice.upper() == 'A' :    
        with open(file_name,'r') as file:
            Expense = []
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                Expense.append(row)
            j=0
            for i in range(len(Expense)):
                print(f"Date: {Expense[i][j]} || Amount: {Expense[i][j+1]} || Category: {Expense[i][j+2]} || Description: {Expense[i][j+3]}")
    else:
        print("Invalid Choice!!")

def Filter_Expenses():
    print("Available filter options")
    print("1.Filter by date")
    print("2.Filter by Category")
    opt = int(input("Choose the filter option: "))
    while True:
        if(opt == 1):
            print("Enter Date range (FORMAT: YYYY-MM-DD)")
            From = input("FROM: ")
            to = input("TO: ")
            try:
                From = datetime.strptime(From,'%Y-%m-%d').date()
                to = datetime.strptime(to,'%Y-%m-%d').date()
            except ValueError:
                print("Invalid Date format!!")
                continue
            with open(file_name,'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # Handle both date string formats (with and without time)
                    date_str = row['Date'].split()[0]  # Get only the date part
                    expense_date = datetime.strptime(date_str,'%Y-%m-%d').date()
                    if From <= expense_date <= to:
                        print(f"Date: {row['Date']} || Amount: {row['Amount']} || Category: {row['Category']} || Description: {row['Description']}")
                break
        elif(opt == 2):
            Category = input("Enter your category: ").lower()
            found = 0
            with open(file_name,'r') as file:
                reader = csv.DictReader(file)           #Never call next() on DictReader
                for row in reader:
                    if row['Category'].lower() == Category:
                        print(f"Date: {row['Date']} || Amount: {row['Amount']} || Category: {row['Category']} || Description: {row['Description']}")
                        found = 1
            if found == 0:
                print("No expenses found for this category.")
                break
            elif found == 1:
                break
def Generate_Report():
    initialize_file()
    while True:
        print("---------------------------------------")
        print("1. Total spend in range")
        print("2. Total per Category")
        print("3. Highest single Expense")
        print("4. Average Expense in range")
        print("5. Back to Report Menu")
        print("---------------------------------------")

        choice = input("Choose an option (1-5): ")
        if choice == '1':
            while True:
                print("Enter Date range (FORMAT: YYYY-MM-DD)")
                From = input("FROM: ")
                to = input("TO: ")
                Total =0
                try:
                    From = datetime.strptime(From,'%Y-%m-%d').date()
                    to = datetime.strptime(to,'%Y-%m-%d').date()
                except ValueError:
                    print("Invalid Date format!!")
                    continue
                with open(file_name,'r') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        # Handle both date string formats (with and without time)
                        date_str = row['Date'].split()[0]  # Get only the date part
                        expense_date = datetime.strptime(date_str,'%Y-%m-%d').date()
                        if From <= expense_date <= to:
                            Total += float(row['Amount'])  
                print("-----------------------------------")
                print(f"Total Spending: ₹{Total:.2f}") 
                print("-----------------------------------")
                break
        elif choice == '2':
            x = input("Want to see Overall category wise Spending Enter 'A' or Specific Category Enter 'S': ").upper()
            if x == 'A':
                print("------------------------------------")
                print("Overall Spendings: ")
                overall = {}
                with open(file_name,'r') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        if row['Category'] not in overall:
                            overall[row['Category']] = float(row["Amount"])
                        else:
                            overall[row['Category']] = float(overall[row['Category']]) + float(row['Amount'])
                overall_keys = list(overall.keys())
                overall_values = list(overall.values())
                for i in range(len(overall_keys)):
                    print(f"{overall_keys[i]}: {overall_values[i]:.2f}")
            elif x == 'S':
                print("------------------------------------")
                Category = input("Enter your category: ").lower()
                found = 0
                Total_Category = 0
                with open(file_name,'r') as file:
                    reader = csv.DictReader(file)           #Never call next() on DictReader
                    for row in reader:
                        if row['Category'].lower() == Category:
                            Total_Category += float(row["Amount"])
                            found = 1
                    if found == 0:
                        print("No expenses found for this category.")
                    elif found == 1:
                        print(f"Total Spending on {Category.title()}: {Total_Category}")
                        print("------------------------------------")
        elif choice == '3':
            Highest = 0
            Index = 0
            with open(file_name,'r') as file:
                reader = csv.DictReader(file)
                for index, row in enumerate(reader):
                    Am = float(row["Amount"])
                    if  Am > Highest:
                        Highest = float(row["Amount"])
                        Index = int(index)
                        Highest_row = row
                    else:
                        continue
            print("-------------------------------------------------------")
            print(f"Highest Expense: \n{Highest_row['Date']}\nAmount: {Highest_row['Amount']}\nCategory: {Highest_row['Category']}\nDescription: {Highest_row['Description']}")        
            print("-------------------------------------------------------")
        elif choice == '4':
            while True:
                print("Enter Date range (FORMAT: YYYY-MM-DD)")
                From = input("FROM: ")
                to = input("TO: ")
                Total =0
                i = 0
                try:
                    From = datetime.strptime(From,'%Y-%m-%d').date()
                    to = datetime.strptime(to,'%Y-%m-%d').date()
                except ValueError:
                    print("Invalid Date format!!")
                    continue
                with open(file_name,'r') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        # Handle both date string formats (with and without time)
                        date_str = row['Date'].split()[0]  # Get only the date part
                        expense_date = datetime.strptime(date_str,'%Y-%m-%d').date()
                        if From <= expense_date <= to:
                            Total += float(row['Amount'])
                            i+=1
                try:
                    AVERAGE = Total/i
                    print("-----------------------------------")
                    print(f"Average Spending: ₹{AVERAGE:.2f}") 
                    print("-----------------------------------")
                except ZeroDivisionError:
                    print("No expenses in range")  
                break
        elif choice == '5':
            print("Exiting Report Menu!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Filter Expenses")
        print("4. Generate Report")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")
        if choice == '1':
            Add_Expense()
        elif choice == '2':
            View_Expenses()
        elif choice == '3':
            Filter_Expenses()
        elif choice == '4':
            Generate_Report()
        elif choice == '5':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")