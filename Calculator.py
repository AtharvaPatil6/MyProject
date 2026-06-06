print("---Welcome to Calculator---")
while True:
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")

    a=int(input("Enter Number 1: "))
    b=int(input("Enter Number 2: "))
    choice=int(input("Enter Your Choice(1/2/3/4): "))
    if choice==1:
        print("Addition: ",a+b)
    elif choice==2:
        print("Subtraction: ",a-b)
    elif choice==3:
        print("Multiplication: ",a*b)
    elif choice=="4":
        print("Division: ",a//b)
    
    elif choice==5:
        print("Thanks for using calculator")
        break