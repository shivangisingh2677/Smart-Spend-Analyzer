import csv
import os
import datetime

# File to store data
filename = "expense_data.csv"
my_limit = 3000  # Changing budget to 3000

def setup_file():
    # Check if file exists, if not create it
    if not os.path.exists(filename):
        with open(filename, 'w', newline='') as f:
            w = csv.writer(f)
            # Header row
            w.writerow(["Date", "Type", "Cost", "Details"])
        print("Database created.")

def add_new():
    print("\n--- Add New Expense ---")
    
    # Get today's date
    d = datetime.date.today()
    
    # Taking inputs
    cat = input("Enter Category (Food/Travel/etc): ")
    note = input("Short Note: ")
    
    try:
        cost = float(input("Enter Amount: "))
    except:
        print("Error: Please enter a valid number.")
        return

    # Saving to csv file
    with open(filename, 'a', newline='') as f:
        w = csv.writer(f)
        w.writerow([d, cat, cost, note])
    
    print("Entry saved!")

def view_all():
    print("\n--- All Expenses ---")
    
    if not os.path.exists(filename):
        print("No data found.")
        return

    total = 0
    
    with open(filename, 'r') as f:
        r = csv.reader(f)
        
        # simple printing
        for row in r:
            # Skip the header line purely by checking if it says "Date"
            if row[0] == "Date":
                continue
                
            # row[0]=Date, row[1]=Type, row[2]=Cost
            print(f"{row[0]} | {row[1]} | {row[2]}")
            
            # Add to total
            total = total + float(row[2])

    print("-" * 20)
    print("Total Spent:", total)
    
    rem = my_limit - total
    print("Money Left:", rem)

# Main code starts here
setup_file()

while True:
    print("\n1. Add Expense")
    print("2. View Summary")
    print("3. Exit")
    
    opt = input("Select option: ")
    
    if opt == '1':
        add_new()
    elif opt == '2':
        view_all()
    elif opt == '3':
        print("Bye!")
        break
    else:
        print("Wrong choice.")