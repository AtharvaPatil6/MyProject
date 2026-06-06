expense=[]
total=0

while True:
    print("--- Welcome to Expense Tracker ---")
    print("1.Add Expense")
    print("2.View All Expense")
    print("3.View Total Spending")
    print("4.To delete a Expense")

    choice=int(input("Enter Your Choice(1/2/3/4): "))

    if choice==1:
        date=input("Enter Date: ") 
        category=input("Enter Expense Category: ") 
        descp=input("More Description: ") 
        amount=float(input("Enter The Amount: "))

        expenses={
            "date":date,
            "category":category,
            "description":descp,
            "amount":amount
        }     

        expense.append(expenses)
    
    elif choice==2:
        count=0
        for exp in expense:
            print(f"Expense: {count} :- Date: {exp["date"]}, Category: {exp["category"]}, Description:{exp["description"]}, amount:{exp["amount"]}")
            count+=1
    
   
    elif choice == 3:
        total = 0

        for i in expense:
            total += i["amount"]

        print("Total Spending =", total)

    elif choice==4:
        delete=input("Enter Expense you want to delete?: ").lower()
        for exp in expense:
            if exp["category"].lower() == delete:
                expense.remove(exp)
                found=True
                print("Expense Removed Succesfully!!")
            
        if not found:
            print("Expense Not found!")
        
    elif choice==5:
        with open("Expensedata.txt","w") as f:
            data=f.write(str(expense))
            print("Data file Created Successfully!!!")
    
    elif choice==6:
        print("Thanks for using the app!!")
        break