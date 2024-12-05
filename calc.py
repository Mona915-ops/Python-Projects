def calcy():
    print("Welcome Cupcake!")
    print("Select the choice of operator:")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")

    choice=input("Enter the option(1,2,3,4):")

    if choice in ['1','2','3','4']:
        try:
            n1=int(input("Enter the first number:"))
            n2=int(input("Enter the second number:"))
            if choice == '1':
                print(f"The addition of {n1} and {n2} is equal to {n1+n2}")
            elif choice == '2':
                print(f"The subtraction of {n1} and {n2} is equal to {n1-n2}")
            elif choice == '3':
                print(f"The multiplication of {n1} and {n2} is equal to {n1*n2}")
            elif choice == '4':
                if n2 == 0:
                    print("Error: Division by zero is not allowed")
                else:
                    print(f"The division of {n1} and {n2} is equal to {n1/n2}")
        except:
            print("Error: Enter valid input!")
    else:
        print("Error: Invalid choice! please select a valid operation")
calcy()