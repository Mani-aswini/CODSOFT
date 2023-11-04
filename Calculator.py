class calculator_menu():
    print("\n*** Calculator Menu ***")
    print("1.Add (+)")
    print("2.Subtract (-)")
    print("3.Multiply (*)")
    print("4.Divide (/)")
    print("5.Exit")
    num1=int(input("Enter first number: "))
    num2=int(input("Enter second number: "))
    option=int(input("Enter operation: "))
    if option == 1:
        print(num1 + num2)
    elif option == 2:
        print(num1 - num2)
    elif option == 3:
        print(num1 * num2)
    elif option == 4:
        if num2 == 0:
            print("Error: Division  by zero")
        else:
            print(num1 / num2)
    elif option == 5:
        print("Exit")
    else:
        print("Invalid Option")



