print("Command line calculator ('type exit to quit')")
while True:
    print("choose an operation")
    print("1. Addition")
    print("2. Subtract ")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    choice = input("Enter your choice : ")
    if choice == '5':
        print("Good Bye")
        break
    if choice in ['1','2','3','4']:
        num1 = float(input("Enter number 1 : "))
        num2 = float(input("Enter number 2 : "))
    if choice=='1':
        print("Result",num1+num2)
    elif choice=='2':
        print("Result",num1-num2)
    elif choice=='3':
        print("Result",num1*num2)
    elif choice=='4':
        if num2!=0:
            print("Result",num1/num2)
    else:
        print("Error")
else:
    print("Invalid choice")


