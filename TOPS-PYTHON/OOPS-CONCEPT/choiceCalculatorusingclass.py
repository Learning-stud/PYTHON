def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Cannot Divide By Zero"


result = True



while(result):
    print(
        """---------User Choice--------
            1.Addition
            2.Substraction
            3.Multiply
            4.Divide
        """
    )

    # user input
    num1 = int(input("Enter First Number : "))
    num2 = int(input("Enter Second Number : "))

    # User choice For Calciulation Of User Choice

    choice = input("Enter Choice (1/2/3/4) : ")

    if choice == "1":
        result = add(num1, num2)

    elif choice == "2":
        result = sub(num1, num2)

    elif choice == "3":
        result = multiply(num1, num2)

    elif choice == "4":
        result = divide(num1, num2)

    else:
        result = "Invalid Choice !"

    print(f"Results => {result}")

    user_choice=input("Do You Want To Continue (Y/N) : ")

    if user_choice == "Y" or user_choice == "y":
        result=True
    else:
        result=False


